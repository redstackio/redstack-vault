---
id: 2a6f9a7f-9ec6-4314-9f84-62dfbbd20698
name: apt-install-tcpdump
type: command
executor: bash
data: sudo apt-get install tcpdump
output: null
created_at: '2023-04-06T03:56:23.097374+00:00'
updated_at: '2023-04-10T20:25:12.038720+00:00'
platforms:
  - Linux
tags:
  - installation
  - tcpdump
verified: true
validated: true
---

# apt-install-tcpdump

## Command

```bash
sudo apt-get install $_PACKAGE
```

## Description

Installs tcpdump on Debian/Ubuntu systems for network packet capture capabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| sudo | Elevate privileges | Yes |
| apt-get install $_PACKAGE | Package name (tcpdump) | Yes |

## Examples

### Basic Usage

```bash
sudo apt-get install tcpdump
```

### Update First

```bash
sudo apt-get update && sudo apt-get install tcpdump
```

## Expected Output

Installation progress and confirmation: "tcpdump is already the newest version."

## Related

- [[procedures/Network-Trace-Capture]]
- [[commands/tcpdump-write-to-file]]
