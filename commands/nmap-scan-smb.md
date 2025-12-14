---
id: cmd-uuid-001
data: nmap -p 445 --script smb-security-mode 192.168.1.0/24
tags:
  - scanning
  - smb
type: command
output: null
executor: bash
platforms:
  - Linux
  - Network
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.662Z'
verified: false
validated: true
submitted: true
---
# nmap-scan-smb

## Command

```bash
nmap -p 445 --script smb-security-mode 192.168.1.0/24
```

## Description

Scans a network range for open SMB ports (445) and assesses security mode, identifying potential anonymous access points.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-p 445` | Specify port 445 for SMB | Yes |
| `--script smb-security-mode` | Run NSE script to check SMB signing and guest access | Yes |
| `192.168.1.0/24` | Target IP range | Yes |

## Examples

### Basic Usage

```bash
nmap -p 445 --script smb-security-mode 10.0.0.0/24
```

### Advanced Usage

```bash
nmap -p 445 --script smb-security-mode,banner 192.168.1.0/24 -oN scan-results.txt
```

## Expected Output

Host details with SMB version, signing required (yes/no), and guest access allowed.

## Related

- [[Related Procedure: Discover-Exposed-SMB-Servers]]
