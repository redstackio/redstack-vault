---
id: tool-uuid-1
url: 'https://git-scm.com/'
tags:
  - version-control
  - git
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:23.301Z'
validated: true
submitted: true
---
---

# git

**Status**: Unverified

## Overview

Git is a distributed version control system used for cloning, committing, and pushing repository changes, critical for setting up and exploiting git-based vulnerabilities like submodule URL abuse in GitLab.

## Description

In offensive security, Git facilitates repository manipulation, such as adding submodules and injecting payloads into configuration files like .gitmodules. It supports SSH/HTTPS remotes and is essential for workflows involving GitLab or GitHub exploits.

## Features

- Feature 1: Distributed version control with branching
- Feature 2: Submodule support for nested repositories
- Feature 3: SSH integration for authenticated pushes

## Installation

### Requirements

- POSIX-compliant OS or Windows with Git Bash

### Install Commands

```bash
# Linux (Ubuntu)
apt update && apt install git

# macOS
brew install git

# Windows
# Download from https://git-scm.com/download/win
```

## Basic Usage

```bash
git --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --version` | Display version |

## Examples

### Example 1: Basic Usage

```bash
git clone https://example.com/repo
```

### Example 2: Advanced Usage

```bash
git submodule add remote/path subdir
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor git process executions in logs
- Track SSH connections to git hosts
- Scan for .gitmodules with suspicious URLs

## Related Procedures

- [[procedures/Initialize-GitLab-Project-and-Wiki-Repositories]]
- [[procedures/Add-Wiki-as-Relative-Git-Submodule]]

## Related Tools

- [[tools/gitlab-cli]]

## References

- Official documentation: https://git-scm.com/doc
- GitLab security: https://docs.gitlab.com/ee/user/project/modules.html
