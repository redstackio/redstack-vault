---
data: nmap ci.nextcloud.com
tags:
  - recon
  - scanning
type: command
output: null
executor: bash
platforms:
  - Linux
id: c2526a5b-8267-431b-b37b-8aa17c258f4c
created_at: '2025-12-14T17:26:36.885Z'
updated_at: '2025-12-14T17:26:36.885Z'
verified: false
validated: true
submitted: true
---
# nmap-scan-host

## Command

```bash
nmap ci.nextcloud.com
```

## Description

Performs a default TCP SYN port scan on the specified host to discover open ports and services, useful for identifying exposed DNS on port 53 during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Target (positional) | Hostname or IP to scan (e.g., ci.nextcloud.com) | Yes |

## Examples

### Basic Usage

```bash
nmap ci.nextcloud.com
```

### Advanced Usage

```bash
nmap -sV -p 53 ci.nextcloud.com
```

## Expected Output

Nmap scan report for ci.nextcloud.com
Host is up (0.XXs latency).
Not shown: 996 closed ports
PORT    STATE SERVICE
22/tcp  open  ssh
53/tcp  open  domain
80/tcp  open  http
443/tcp open  https

## Related

- [[Related Procedure: Scan-Target-for-Open-DNS-Port]]
