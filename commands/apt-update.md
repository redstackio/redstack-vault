---
type: command
executor: bash
data: sudo apt-get update
output: null
created_at: '2023-04-06T03:56:16.220578+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - installation
  - debian
verified: true
validated: true
---

# apt-update

## Command

```bash
sudo apt-get update
```

## Description

Updates the local package index from the configured repositories on Debian-based systems, ensuring access to the latest package versions during installations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `update` | Refreshes package lists | Yes |

## Examples

### Basic Usage

```bash
sudo apt-get update
```

## Expected Output

Hit:1 http://archive.ubuntu.com/ubuntu focal InRelease
Reading package lists... Done
Building dependency tree
Reading state information... Done
All packages are up to date.

## Related

- [[commands/install-openjdk-11-jdk]]
- [[procedures/Cobalt-Strike-Team-Server-Installation-and-Execution]]
