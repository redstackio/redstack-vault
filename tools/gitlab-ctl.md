---
id: tool-gitlab-ctl
url: 'https://docs.gitlab.com/omnibus/maintenance/'
tags:
  - gitlab
  - service-management
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.746Z'
validated: true
submitted: true
---
# gitlab-ctl

**Status**: Unverified

## Overview

gitlab-ctl is GitLab's control tool for managing Omnibus services, used here to restart Unicorn for persistence.

## Description

Handles reconfigure, restart, status for components like Unicorn, Sidekiq; integral to GitLab administration and exploitation persistence.

## Features

- Feature 1: Service start/stop/restart
- Feature 2: Status checks
- Feature 3: Reconfiguration

## Installation

### Requirements

- GitLab Omnibus package

### Install Commands

```bash
# Part of GitLab install
apt install gitlab-ee
```
(Or CE equivalent.)

## Basic Usage

```bash
gitlab-ctl --help
```

### Common Options

| Option | Description |
|--------|-------------|
| restart | Restart a service |
| status | Check service status |

## Examples

### Example 1: Basic Usage

```bash
gitlab-ctl status
```

### Example 2: Advanced Usage

```bash
gitlab-ctl restart unicorn
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Shortcut Modification]]

### Tactics

- [[Privilege Escalation]]

## Detection

Indicators and methods for detecting this tool's usage:

- Logs of service restarts
- Unauthorized admin access

## Related Procedures

- [[procedures/Restart-Unicorn-to-Persist-Overwrites]]

## Related Tools

- [[tools/systemctl]]

## References

- Official documentation: https://docs.gitlab.com/omnibus/maintenance/
