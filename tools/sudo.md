---
url: 'https://www.sudo.ws/'
tags:
  - privilege-escalation
type: tool
platforms:
  - Linux
  - macOS
description: Execute commands with elevated privileges
id: 57996d83-b257-4c95-a7ec-b28c61cef543
created_at: '2025-12-11T03:47:39.390Z'
updated_at: '2025-12-11T03:47:39.390Z'
verified: false
validated: true
submitted: true
---
# sudo

**Status**: Unverified

## Overview

sudo allows running commands as another user, often root, used in exploits for changing file permissions.

## Description

Essential for administrative tasks in testing environments, like chown in GitLab exploit setups.

## Features
- User switching
- Password caching
- Configuration via sudoers

## Installation

### Requirements
- Standard on Unix-like systems

### Install Commands

```bash
sudo apt install sudo
```

## Basic Usage

```bash
sudo --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-u` | Specify user |
| `-g` | Specify group |

## Examples

### Example 1: Basic Usage

```bash
sudo chown root file
```

### Example 2: Advanced Usage

```bash
sudo -u git chown git:git file
```

## MITRE ATT&CK Mapping

### Techniques
- [[Abuse Elevation Control Mechanism]]

### Tactics
- [[Privilege Escalation]]

## Detection

- Audit sudo logs
- Privilege change monitoring

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools
- #su
- #pkexec

## References
- https://www.sudo.ws/man.html
