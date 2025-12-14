---
data: nmap -p- -sV TARGET_IP
tags:
  - port-scan
  - recon
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: f5dfd2d6-5b6d-4037-8581-937b9d5d75a9
created_at: '2025-12-14T03:15:05.030Z'
updated_at: '2025-12-14T03:15:05.030Z'
verified: false
validated: true
submitted: true
---
# nmap-port-scan-on-ip

## Command

```bash
nmap -p- -sV TARGET_IP
```

## Description

This Nmap command performs a full port scan (-p-) with service version detection (-sV) on a target IP to identify open ports and running services on exposed cloud instances.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-p-` | Scan all 65535 ports | Yes |
| `-sV` | Detect service versions | Yes |
| `TARGET_IP` | IP address to scan (e.g., 35.241.6.32) | Yes |

## Examples

### Basic Usage

```bash
nmap -p- 35.241.6.32
```

### Advanced Usage

```bash
nmap -p 80,443,5432 -sV -O 35.241.6.32
```

## Expected Output

PORT     STATE SERVICE VERSION
80/tcp   open  http    nginx
443/tcp  open  https   Apache
5432/tcp open  postgres PostgreSQL DB 12.5

## Related

- [[Related Procedure: Port-Scan-Exposed-Origin-IPs]]
