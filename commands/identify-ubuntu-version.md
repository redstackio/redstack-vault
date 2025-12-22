---
id: cmd-lsb-release-001
data: lsb_release -a
tags:
  - recon
  - env
type: command
output: >-
  Distributor ID: Ubuntu\nDescription: Ubuntu 20.04.6 LTS\nRelease:
  20.04\nCodename: focal
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.531Z'
verified: false
validated: true
submitted: true
---
# identify-ubuntu-version

## Command

```bash
lsb_release -a
```

## Description

Displays detailed information about the Linux distribution using LSB (Linux Standard Base) tools, useful for confirming the testing environment in vulnerability assessments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-a` | Show all information about the distribution | Yes |

## Examples

### Basic Usage

```bash
lsb_release -a
```

### Advanced Usage

```bash
lsb_release -d  # Short description only
```

## Expected Output

Distributor ID: Ubuntu, Description: Ubuntu 20.04.6 LTS, Release: 20.04, Codename: focal

## Related

- [[commands/compile-libcurl-test]]
