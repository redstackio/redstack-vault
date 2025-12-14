---
id: cmd-nmap-exim-detect
data: nmap -p 25 --script smtp-commands target.example.com
tags:
  - recon
  - smtp
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:28.355Z'
verified: false
validated: true
submitted: true
---
# nmap-exim-detect

## Command

```bash
nmap -p 25 --script smtp-commands target.example.com
```

## Description

Scans port 25 on the target to detect SMTP service and enumerate supported commands, helping identify Exim MTA installations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-p 25` | Specifies port 25 (SMTP) | Yes |
| `--script smtp-commands` | Runs NSE script to list SMTP commands | Yes |
| `target.example.com` | Target hostname or IP | Yes |

## Examples

### Basic Usage

```bash
nmap -p 25 --script smtp-commands 192.168.1.1
```

### Advanced Usage

```bash
nmap -p 25 --script smtp-commands,banner -oN scan.txt target.example.com
```

## Expected Output

PORT   STATE SERVICE
25/tcp open  smtp
| smtp-commands: 
|   helo
|   ehlo
|   starttls
|_  Supported: ... (indicates Exim if commands match)

## Related

- [[Related Procedure: Detect-Exim-Vulnerability]]
