---
url: ''
tags:
  - discovery
type: tool
platforms:
  - Linux
description: Rake task runner for GitLab administration.
id: 90849171-ddfa-4f57-9a5d-c45ece0eeed2
created_at: '2025-12-11T06:10:22.571Z'
updated_at: '2025-12-11T06:10:22.571Z'
verified: false
validated: true
submitted: true
---
# gitlab-rake

**Status**: Unverified

## Overview

GitLab-rake runs administrative tasks, used here for environment info gathering.

## Description

Part of GitLab, allows querying system details post-compromise.

## Features

- Environment info
- Database tasks

## Installation

### Requirements

- GitLab installed

### Install Commands

Included with GitLab.

## Basic Usage

```bash
gitlab-rake --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `gitlab:env:info` | Show env info |

## Examples

### Example 1: Basic Usage

```bash
gitlab-rake gitlab:env:info
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[System Information Discovery]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Rake task logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[rake]]

## References

- GitLab docs
