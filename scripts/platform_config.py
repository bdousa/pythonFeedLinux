#!/usr/bin/env python3

import re

REPO_NAME = "pythonFeedLinux"
LEGACY_SOURCE_REPO_NAME = "pythonFeedWindows"
COMPATIBILITY_LABEL = "Ubuntu x64 only. Python 3.13.x required."
TARGET_RUNTIME_LABEL = "Python 3.13.x on Ubuntu x64"
TARGET_PLATFORM_LABEL = "Ubuntu x64"
TARGET_OS_CLASSIFIER_TOKENS = ("POSIX", "Linux", "Unix")
NON_TARGET_OS_CLASSIFIER_TOKENS = ("Microsoft :: Windows", "MacOS", "Mac OS", "iOS", "Android")
USER_AGENT_PREFIX = "pythonFeedLinux"
EXAMPLE_RELEASE_OWNER = "bdousa"
EXAMPLE_RELEASE_REPO = REPO_NAME
EXAMPLE_UNIVERSAL_URL = f"https://github.com/{EXAMPLE_RELEASE_OWNER}/{EXAMPLE_RELEASE_REPO}/releases/download/requests-v2.34.2/requests-2.34.2-py3-none-any.whl"
EXAMPLE_PLATFORM_URL = f"https://github.com/{EXAMPLE_RELEASE_OWNER}/{EXAMPLE_RELEASE_REPO}/releases/download/azure-ai-projects-v1.0.0/azure_ai_projects-1.0.0-py3-none-any.whl"
PREFERRED_WHEEL_PATTERNS = (
    re.compile(r"cp313-[^-]*-manylinux[^/]*x86_64\.whl$"),
    re.compile(r"cp313-[^-]*-musllinux[^/]*x86_64\.whl$"),
    re.compile(r"cp313-[^-]*-linux_x86_64\.whl$"),
)
UNIVERSAL_WHEEL_PATTERNS = (
    re.compile(r"py3-none-any\.whl$"),
    re.compile(r"py2\.py3-none-any\.whl$"),
)


def user_agent(component: str) -> str:
    return f"{USER_AGENT_PREFIX} {component}"


def is_target_linux_wheel(file_name: str) -> bool:
    return any(pattern.search(file_name) for pattern in PREFERRED_WHEEL_PATTERNS)


def is_universal_wheel(file_name: str) -> bool:
    return any(pattern.search(file_name) for pattern in UNIVERSAL_WHEEL_PATTERNS)
