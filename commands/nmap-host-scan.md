---
id: cmd-nmap-host
data: nmap -sV -O 52.77.124.190
tags:
  - scanning
type: command
output: |-
  PORT    STATE SERVICE VERSION
  443/tcp open  https Apache Tomcat
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:32.244Z'
verified: false
validated: true
submitted: true
---
# nmap-host-scan

## Command

```bash
nmap -sV -O 52.77.124.190
```

## Description

Scans host for services and OS, detecting versions for vuln assessment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -sV | Service version detection | Yes |
| -O | OS detection | Yes |
| IP | Target IP | Yes |

## Examples

### Basic Usage

```bash
nmap -sV -O 52.77.124.190
```

## Expected Output

Open ports, services like Tomcat on 443.

## Related

- [[commands/nmap-port-scan]]
