---
url: 'https://docs.gitlab.com/ee/administration/raketasks/maintenance.html'
tags:
  - gitlab
  - admin
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.946Z'
id: 918b55cc-dabf-4f5f-a450-74d0b1179349
validated: true
submitted: true
---
# gitlab-rake

**Status**: Unverified

## Overview

gitlab-rake is GitLab's wrapper around Ruby's Rake tool for running maintenance, diagnostic, and info tasks on a GitLab instance, used post-RCE for environment reconnaissance.

## Description

It executes predefined tasks like gitlab:env:info to output versions, configs, and system details, aiding in verifying exploitation success and planning further actions.

## Features

- Feature 1: Environment info gathering
- Feature 2: Maintenance tasks (backup, migrate)
- Feature 3: Diagnostic outputs for troubleshooting

## Installation

### Requirements

- Installed as part of GitLab (Ruby/Rake dependency)
- Run from GitLab server shell

### Install Commands

```bash
# Part of GitLab installation
gitlab-ctl reconfigure
```

## Basic Usage

```bash
gitlab-rake --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--trace` | Detailed error tracing |
| `-T` | List available tasks |

## Examples

### Example 1: Basic Usage

```bash
gitlab-rake gitlab:env:info
```

### Example 2: Advanced Usage

```bash
gitlab-rake gitlab:check
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[System Information Discovery]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Logs of rake task executions
- Unusual admin task runs by 'git' user
- File system changes from maintenance tasks

## Related Procedures


## Related Tools

- [[tools/rake]]
- [[tools/git]]

## References

- Official documentation: https://docs.gitlab.com/ee/administration/raketasks/
- Related resources: GitLab troubleshooting guides
