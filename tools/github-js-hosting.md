---
url: 'https://github.com'
tags:
  - hosting
  - js-payload
type: tool
verified: false
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.996Z'
id: 8c6cf696-2322-48e6-be7c-0745f7915ea0
validated: true
submitted: true
---
# github-js-hosting

**Status**: Unverified

## Overview

GitHub serves as a platform for hosting static JavaScript files in public repositories, often abused in attacks to bypass CSP restrictions via URL manipulation for loading malicious payloads in XSS exploits.

## Description

Public GitHub repos allow raw file access via raw.githubusercontent.com or githack.com proxies. In this context, it's used to host final.js for CSP bypass by path backtracking in allowed domains, enabling external JS execution without direct hosting costs.

## Features

- Feature 1: Free public static file hosting
- Feature 2: Raw URL access for scripts
- Feature 3: Version control for payloads

## Installation

### Requirements

- GitHub account

### Install Commands

N/A; use web UI or git.

```bash
# Clone and push
mkdir repo
cd repo
git init
git remote add origin https://github.com/user/repo.git
git add final.js
git commit -m "add payload"
git push
```

## Basic Usage

```bash
github raw url: https://raw.githubusercontent.com/user/repo/master/final.js
```

### Common Options

N/A

## Examples

### Example 1: Basic Usage

Upload final.js to https://github.com/Ajay-Aj-00/Test/master/final.js

### Example 2: Advanced Usage

Use githack proxy for CORS: https://raw.githack.com/user/repo/master/file.js

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Script loads from raw.githubusercontent.com
- Unusual GitHub repo accesses in logs

## Related Procedures


## Related Tools

- [[tools/jsdelivr]]
- [[tools/unpkg]]

## References

- GitHub Docs: https://docs.github.com/en/repositories
