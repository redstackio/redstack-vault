---
type: command
executor: bash
data: nmap --script-updatedb
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - nmap
  - update
verified: true
validated: true
---

# nmap-update-scripts

## Command

```bash
nmap --script-updatedb
```

## Description

Updates the Nmap Scripting Engine (NSE) database by downloading the latest scripts from the official repository. Use this before running script-based scans to ensure access to current NSE scripts like hostmap-crtsh.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --script-updatedb | Fetches and installs updated NSE scripts | Yes |

## Examples

### Basic Usage

```bash
nmap --script-updatedb
```

### Advanced Usage

Run in a specific directory if custom scripts are used:
```bash
nmap --script-updatedb --script-path /custom/scripts
```

## Expected Output

Nmap scan report for localhost (127.0.0.1)
Host is up.
NSE: Script Pre-scanning.
NSE: Script Post-scanning.
Initiating NSE at ... (successful update messages or list of new scripts).

## Related

- [[procedures/Subdomain-Enumeration-using-Nmap-CRTsh-Script]]
- [[tools/Nmap]]
