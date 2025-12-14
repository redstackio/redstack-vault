---
data: apt update && apt install -y python3-scapy openssh-client
tags:
  - installation
type: command
output: null
executor: bash
platforms:
  - Linux
  - Ubuntu
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.885Z'
id: b4c34f49-b08f-4e94-a500-d90adc68d4b4
verified: false
validated: true
submitted: true
---
# apt-install-scapy-openssh

## Command

```bash
apt update && apt install -y python3-scapy openssh-client
```

## Description

Updates package index and installs Scapy and OpenSSH client without prompts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -y | Auto-confirm install | Yes |
| package | Packages to install | Yes |

## Examples

### Basic Usage

```bash
apt install -y python3
```

## Expected Output

Reading package lists... Done
Building dependency tree... Done
... (install complete)

## Related

- [[procedures/Install-Dependencies-and-Generate-SSH-Key]]
