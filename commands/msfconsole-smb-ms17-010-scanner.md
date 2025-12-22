---
type: command
executor: bash
data: >-
  msfconsole -q -x "use auxiliary/scanner/smb/smb_ms17_010; set RHOSTS
  <ip_netblock>; run"
tags:
  - scanning
  - metasploit
platforms:
  - Linux
  - Windows
verified: true
validated: true
---

# msfconsole-smb-ms17-010-scanner

## Command

```bash
msfconsole -q -x "use auxiliary/scanner/smb/smb_ms17_010; set RHOSTS <ip_netblock>; run"
```

## Description

Metasploit auxiliary module to detect MS17-010 across a range, reporting vulnerable hosts for follow-up exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| <ip_netblock> | IP range (RHOSTS) | Yes |

## Examples

### Basic Usage

```bash
msfconsole -q -x "use auxiliary/scanner/smb/smb_ms17_010; set RHOSTS 192.168.1.0/24; run"
```

## Expected Output

```
[*] 192.168.1.10:445    - 192.168.1.10:445 - MS17-010 Confirmed Vulnerable (Product:Microsoft Windows 7)
[*] Scanned 256 hosts in 120.45 seconds
```

## Related

- [[procedures/EternalBlue-SMB-Exploitation]]
- [[tools/Metasploit-Framework]]
