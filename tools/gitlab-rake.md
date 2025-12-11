---
url: ''
tags:
  - recon
  - gitlab
type: tool
platforms:
  - Linux
description: 'Tool for running Rake tasks in GitLab, used to gather environment information.'
id: f61dadef-c570-42a9-8525-517735b9354f
created_at: '2025-12-11T03:47:39.839Z'
updated_at: '2025-12-11T03:47:39.839Z'
verified: false
validated: true
submitted: true
---
# gitlab-rake

**Status**: Unverified

## Overview

Gitlab-rake is a wrapper for running Rake tasks in GitLab, here used for environment reconnaissance post-exploitation.

## Description

Provides administrative tasks for GitLab; in security, useful for gathering internal config after access.

## Features

- Task execution (e.g., env:info)
- GitLab management

## Installation

### Requirements

- GitLab installed

### Install Commands

(Part of GitLab)

## Basic Usage

```bash
gitlab-rake --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--help` | Show help |

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

- Monitor rake task executions

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #gitlab-rake

## References

- GitLab docs
