---
id: cmd-nmap-port-927413
data: nmap -sV -p- 52.77.124.190
tags:
  - scanning
type: command
output: |
  PORT    STATE SERVICE VERSION
  443/tcp open  https Apache Tomcat
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:35.632Z'
verified: false
validated: true
submitted: true
---
# nmap-port-scan

## Command

```bash
nmap -sV -p- 52.77.124.190
```

## Description

Scans all ports on the target IP for services and versions, used to enumerate Zomato's exposed ports like 443.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-sV` | Version detection | No |
| `-p-` | Scan all 65535 ports | No |
| `52.77.124.190` | Target IP | Yes |

## Examples

### Basic Usage

```bash
nmap 52.77.124.190
```

### Advanced Usage

```bash
nmap -sV -A 52.77.124.190
```

## Expected Output

List of open ports, e.g., 443/tcp open https, with service details.

## Related

- [[Related Procedure: Network-Service-Scanning-with-Nmap]]
