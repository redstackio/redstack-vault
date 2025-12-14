---
id: cmd-lsb-release
data: lsb_release -a
tags:
  - recon
  - environment
type: command
output: |-
  Distributor ID: Ubuntu
  Description: Ubuntu 20.04.6 LTS
  Release: 20.04
  Codename: focal
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.065Z'
verified: false
validated: true
submitted: true
---
# lsb-release-identify-environment

## Command

```bash
lsb_release -a
```

## Description

Displays Linux Standard Base (LSB) information to identify the distribution, useful for confirming the testing environment like Ubuntu 20.04 for libcurl vulnerability assessment.

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
lsb_release -d
```

> Shows only the description.

## Expected Output

Distributor ID: Ubuntu
Description: Ubuntu 20.04.6 LTS
Release: 20.04
Codename: focal

## Related

- [[commands/compile-parserbatch-test]]
