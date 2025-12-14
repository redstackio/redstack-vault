---
url: 'https://www.sudo.ws/'
tags:
  - privilege
  - user
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:56.930Z'
id: 75ac49b6-13b9-497d-83c9-11412b5425d3
validated: true
submitted: true
---
# sudo

**Status**: Unverified

## Overview

Sudo allows users to run commands as another user, here used to switch to the 'git' user for exploiting writable log permissions.

## Description

Provides controlled privilege escalation for administrative tasks, but misconfigurations can enable lateral movement to system users like 'git' in GitLab.

## Features

- Feature 1: User specification with -u
- Feature 2: Logging of commands
- Feature 3: Timeout and policy enforcement

## Installation

### Requirements

- Standard on Linux

### Install Commands

```bash
apt-get install sudo
```

## Basic Usage

```bash
sudo --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -u | Run as specified user |
| -i | Interactive shell |

## Examples

### Example 1: Basic Usage

```bash
sudo -u git /bin/bash
```

### Example 2: Advanced Usage

```bash
sudo -u git whoami
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Valid Accounts]] Valid Accounts

### Tactics

- [[Privilege Escalation]] Privilege Escalation

## Detection

Indicators and methods for detecting this tool's usage:

- Sudo logs (/var/log/auth.log) showing switches to 'git'
- Unusual user impersonations
- Audit sudoers for over-permissions

## Related Procedures

- [[procedures/Prepare-Environment-as-Git-User]]

## Related Tools

- [[tools/su]]

## References

- Official site: https://www.sudo.ws/
