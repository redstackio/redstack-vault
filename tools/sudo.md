---
url: 'https://www.sudo.ws/'
tags:
  - privilege
  - admin
type: tool
platforms:
  - Linux
  - macOS
description: 'Execute commands as another user, typically root'
id: 4ddb7ae6-a8e0-4df7-8623-7e2b10c25ea6
created_at: '2025-12-11T06:10:15.378Z'
updated_at: '2025-12-11T06:10:15.378Z'
verified: false
validated: true
submitted: true
---
# sudo

**Status**: Unverified

## Overview

sudo allows running commands with elevated privileges, used in testing for changing file ownership in exploit setups.

## Description

Essential for administrative tasks like chown in controlled environments to simulate permission scenarios.

## Features

- Feature 1: User switching
- Feature 2: Command execution
- Feature 3: Configuration via sudoers

## Installation

### Requirements

- Installed on most Unix-like systems

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
| `-k` | Invalidate timestamp |

## Examples

### Example 1: Basic Usage

```bash
sudo chown user:group file
```

### Example 2: Advanced Usage

```bash
sudo -u git chown git:git /tmp/ggg
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Abuse Elevation Control Mechanism]]

### Tactics

- [[Privilege Escalation]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Audit sudo logs
- Detection method 2: Monitor privilege escalations

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[su]]
- [[pkexec]]

## References

- Official documentation: https://www.sudo.ws/docs/
