# Security Validated Python Packages

This repository contains Python packages validated through automated security scanning and manual approval.

> ⚠️ **Compatibility:** Ubuntu x64 only. Python 3.13.x required.

> The canonical package index is [`packages.json`](./packages.json). This README is generated from that manifest and should not be edited by hand.

## 📊 Quick Stats
- **Active packages:** 3
- **Deprecated packages:** 0
- **Most recent validation:** 2026-06-22 (`azure-ai-projects`)
- **Target runtime:** Python 3.13.x on Ubuntu x64

## ✅ Requirements
- **Python 3.13.x** (required for compatibility)
- **Ubuntu x64** environment

## 🔎 Quick Jump

[A](#a) · [R](#r)

## 🆕 Recently Validated

| Package | Version | Validated |
|---------|---------|-----------|
| [`requests`](#requests) | `2.34.2` | 2026-06-22 |
| [`azure-ai-transcription`](#azure-ai-transcription) | `1.0.0` | 2026-06-22 |
| [`azure-ai-projects`](#azure-ai-projects) | `1.0.0` | 2026-06-22 |

## 📦 Available Packages

### A

#### `azure-ai-projects`
- **Latest version:** `1.0.0`
- **Validated:** 2026-06-22
- **Package type:** Universal wheel (Python 3+)
- **Download wheel:** [download](https://github.com/bdousa/pythonFeedLinux/releases/download/azure-ai-projects-v1.0.0/azure_ai_projects-1.0.0-py3-none-any.whl)
- **Release notes:** [release](https://github.com/bdousa/pythonFeedLinux/releases/tag/azure-ai-projects-v1.0.0)
- **Validation run:** [build #27967291855](https://github.com/bdousa/pythonFeedLinux/actions/runs/27967291855)
- **Quick command:**
```text
python -m pip install -r https://raw.githubusercontent.com/bdousa/pythonFeedLinux/main/bundles/azure-ai-projects-v1.0.0.txt
```

#### `azure-ai-transcription`
- **Latest version:** `1.0.0`
- **Validated:** 2026-06-22
- **Package type:** Universal wheel (Python 3+)
- **Download wheel:** [download](https://github.com/bdousa/pythonFeedLinux/releases/download/azure-ai-transcription-v1.0.0/azure_ai_transcription-1.0.0-py3-none-any.whl)
- **Release notes:** [release](https://github.com/bdousa/pythonFeedLinux/releases/tag/azure-ai-transcription-v1.0.0)
- **Validation run:** [build #27970233148](https://github.com/bdousa/pythonFeedLinux/actions/runs/27970233148)
- **Quick command:**
```text
python -m pip install -r https://raw.githubusercontent.com/bdousa/pythonFeedLinux/main/bundles/azure-ai-transcription-v1.0.0.txt
```

### R

#### `requests`
- **Latest version:** `2.34.2`
- **Validated:** 2026-06-22
- **Package type:** Universal wheel (Python 3+)
- **Download wheel:** [download](https://github.com/bdousa/pythonFeedLinux/releases/download/requests-v2.34.2/requests-2.34.2-py3-none-any.whl)
- **Release notes:** [release](https://github.com/bdousa/pythonFeedLinux/releases/tag/requests-v2.34.2)
- **Validation run:** [build #27967793908](https://github.com/bdousa/pythonFeedLinux/actions/runs/27967793908)
- **Quick command:**
```text
python -m pip install -r https://raw.githubusercontent.com/bdousa/pythonFeedLinux/main/bundles/requests-v2.34.2.txt
```


## 🚀 Usage Instructions

### 🐍 Python 3.13.x Installation Requirements
All packages in this repository require Python 3.13.x on Ubuntu x64 for compatibility.

### Linux Installation

Currently these are all x86_64 packages, not x86 (32-bit).

#### Ubuntu Packages

Install or activate Python 3.13.x on Ubuntu before installing packages from this feed.

```bash
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

### Package Installation Instructions
#### Option 1: Direct Install
Use the quick install commands from the package sections above.

#### Option 2: Requirements File

Create a requirements.txt with direct GitHub URLs:
```
https://github.com/bdousa/pythonFeedLinux/releases/download/requests-v2.34.2/requests-2.34.2-py3-none-any.whl
https://github.com/bdousa/pythonFeedLinux/releases/download/azure-ai-projects-v1.0.0/azure_ai_projects-1.0.0-py3-none-any.whl
```

## 🔍 Security Validation Process
All packages in this repository have been validated through our comprehensive security pipeline:
- ✅ **Vulnerability Scanning** - Scanned with Snyk for known CVEs
- ✅ **Source Code Analysis** - Static analysis for security issues
- ✅ **Dependency Analysis** - All dependencies scanned for vulnerabilities
- ✅ **License Compliance** - License compatibility verified
- ✅ **Manual Review** - Security team approval required
- ✅ **Package Integrity** - Cryptographic verification of packages

## 📋 Request New Package Review
To request validation of a new package:
1. **Azure DevOps Request**: Go to [ServiceNow Request Portal](https://bdous.service-now.com/sp?id=sc_cat_item&sys_id=c746dd861b3e6910182c63d07e4bcbac)
2. **Select Category**: Choose '3rd party library approval'
3. **Approval Process**: Packages typically validated within 3 business days

*Last updated: 2026-06-22 18:13 UTC*

*Powered by Azure DevOps Security Pipeline*
