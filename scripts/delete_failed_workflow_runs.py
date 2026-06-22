#!/usr/bin/env python3
"""Delete failed GitHub Actions workflow runs from a repository.

By default this script performs a dry run and only reports the runs that would
be deleted. Pass ``--apply`` to issue delete requests.

Authentication:
- ``--github-token`` argument, or
- ``GITHUB_TOKEN`` / ``GH_TOKEN`` environment variables

The token must be able to read workflow runs and delete them.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).resolve().parent))

from platform_config import REPO_NAME  # noqa: E402

DEFAULT_OWNER = "bdousa"
DEFAULT_REPO = REPO_NAME
API_VERSION = "2022-11-28"


def github_headers(token: str) -> dict[str, str]:
    return {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "User-Agent": "pythonFeedLinux workflow cleanup",
        "X-GitHub-Api-Version": API_VERSION,
    }


def github_request(
    method: str,
    url: str,
    token: str,
    data: bytes | None = None,
) -> tuple[int, object, dict[str, str]]:
    request = urllib.request.Request(url, data=data, method=method, headers=github_headers(token))
    try:
        with urllib.request.urlopen(request) as response:
            body = response.read().decode("utf-8") if response.length != 0 else ""
            payload = json.loads(body) if body else None
            headers = {key: value for key, value in response.headers.items()}
            return response.status, payload, headers
    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="replace")
        detail = error_body.strip()
        raise RuntimeError(f"GitHub API {method} {url} failed ({exc.code}): {detail}") from exc


def extract_next_link(link_header: str) -> str:
    if not link_header:
        return ""
    for part in link_header.split(","):
        section = part.strip()
        if 'rel="next"' not in section:
            continue
        if section.startswith("<") and ">" in section:
            return section[1 : section.index(">")]
    return ""


def list_failed_runs(owner: str, repo: str, token: str, branch: str, event: str) -> list[dict]:
    params = {"per_page": "100", "status": "completed"}
    if branch:
        params["branch"] = branch
    if event:
        params["event"] = event
    next_url = (
        f"https://api.github.com/repos/{owner}/{repo}/actions/runs?"
        f"{urllib.parse.urlencode(params)}"
    )

    runs: list[dict] = []
    while next_url:
        _, payload, headers = github_request("GET", next_url, token)
        workflow_runs = payload.get("workflow_runs", []) if isinstance(payload, dict) else []
        for run in workflow_runs:
            if run.get("conclusion") == "failure":
                runs.append(run)
        next_url = extract_next_link(headers.get("Link", ""))
    return runs


def delete_run(owner: str, repo: str, run_id: int, token: str) -> None:
    url = f"https://api.github.com/repos/{owner}/{repo}/actions/runs/{run_id}"
    status, _, _ = github_request("DELETE", url, token)
    if status != 204:
        raise RuntimeError(f"Expected 204 deleting workflow run {run_id}, got {status}.")


def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Delete failed GitHub Actions workflow runs.")
    parser.add_argument("--owner", default=DEFAULT_OWNER)
    parser.add_argument("--repo", default=DEFAULT_REPO)
    parser.add_argument("--branch", default="")
    parser.add_argument("--event", default="")
    parser.add_argument("--limit", type=int, default=0, help="Optional max number of failed runs to delete.")
    parser.add_argument("--github-token", default="")
    parser.add_argument("--apply", action="store_true", help="Actually delete the failed runs.")
    return parser.parse_args(argv)


def main(argv: Optional[list[str]] = None) -> int:
    args = parse_args(argv)
    token = args.github_token or os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or ""
    if not token:
        print("Missing GitHub token. Provide --github-token or set GITHUB_TOKEN / GH_TOKEN.", file=sys.stderr)
        return 1

    runs = list_failed_runs(args.owner, args.repo, token, args.branch, args.event)
    if args.limit > 0:
        runs = runs[: args.limit]

    if not runs:
        print(f"No failed workflow runs found for {args.owner}/{args.repo}.")
        return 0

    print(f"Failed workflow runs found: {len(runs)}")
    for run in runs:
        print(
            f"- id={run.get('id')} workflow={run.get('name') or 'unknown'} "
            f"run_number={run.get('run_number')} branch={run.get('head_branch') or 'unknown'} "
            f"created_at={run.get('created_at') or 'unknown'} url={run.get('html_url') or ''}"
        )

    if not args.apply:
        print("Dry run complete. Re-run with --apply to delete these workflow runs.")
        return 0

    for run in runs:
        run_id = int(run["id"])
        delete_run(args.owner, args.repo, run_id, token)
        print(f"Deleted workflow run {run_id}.")

    print(f"Deleted {len(runs)} failed workflow runs from {args.owner}/{args.repo}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
