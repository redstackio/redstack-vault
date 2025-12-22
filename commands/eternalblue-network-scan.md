---
type: command
executor: bash
data: python eternal_scanner.py -t <ip_netblock>
tags:
  - scanning
  - eternalblue
platforms:
  - Linux
verified: true
validated: true
---

# eternalblue-network-scan

## Command

```bash
python eternal_scanner.py -t <ip_netblock>
```

## Description

Scans a network range for EternalBlue-vulnerable hosts using the dedicated scanner script, outputting architecture and vulnerability status for efficient targeting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -t <ip_netblock> | Target IP range (e.g., 192.168.1.0/24) | Yes |

## Examples

### Basic Usage

```bash
python eternal_scanner.py -t 192.168.1.0/24
```

### Advanced Usage

```bash
python eternal_scanner.py -t 10.0.0.0/16 -p 445
```

## Expected Output

```
[*] Scanning 192.168.1.0/24
[+] 192.168.1.10:445 => x86 VULNERABLE
[-] 192.168.1.11:445 => PATCHED
```

## Related

- [[procedures/EternalBlue-SMB-Exploitation]]
- [[tools/MS17-010-EternalBlue-Tools]]
