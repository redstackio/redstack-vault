---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
data: nmap -sV --script vuln target-confluence.dod.mil
tags:
  - recon
  - scanning
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:25:13.107Z'
verified: false
validated: true
submitted: true
---
# nmap-vuln-scan

## Command

```bash
nmap -sV --script vuln target-confluence.dod.mil
```

## Description

Performs service version detection and runs vulnerability scripts on the target to identify exposures like CVE-2017-9506 in Confluence.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-sV` | Version detection | Yes |
| `--script vuln` | Run vulnerability NSE scripts | Yes |
| Target | Hostname or IP | Yes |

## Examples

### Basic Usage

```bash
nmap -sV --script vuln example.com
```

### Advanced Usage

```bash
nmap -sV -p 80,443 --script ssrf,vuln target.dod.mil
```

## Expected Output

Port listings with versions and vuln matches, e.g., "80/tcp open http Atlassian Confluence 5.x (vulnerable to CVE-2017-9506)".

## Related

- [[Related Procedure]]
