---
data: nmap owncloud.com
tags:
  - recon
  - scanning
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.386Z'
id: 79f45096-58b5-4c4c-97a9-df3fb3a75f30
verified: false
validated: true
submitted: true
---
# nmap-scan-target

## Command

```bash
nmap owncloud.com
```

## Description

Scans the target host owncloud.com (resolves to 50.30.33.235) for open ports, services, and versions, useful for discovering vulnerable DNS servers like BIND9 on port 53.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| owncloud.com | Target hostname or IP | Yes |

## Examples

### Basic Usage

```bash
nmap owncloud.com
```

### Advanced Usage

```bash
nmap -sV -p 53 owncloud.com
```

## Expected Output

Host is up (0.XXs latency).
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 5.8
53/tcp open  domain  BIND 9.9.4-rpz2.13269.14-P2

## Related

- [[Related Procedure: Scan-Target-with-Nmap-for-Vulnerable-BIND9-Services]]
