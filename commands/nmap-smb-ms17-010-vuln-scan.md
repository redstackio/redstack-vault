---
type: command
executor: bash
data: >-
  nmap -Pn -p445 --open --max-hostgroup 3 --script smb-vuln-ms17-010
  <ip_netblock>
tags:
  - scanning
  - smb
  - vulnerability
platforms:
  - Linux
  - Windows
  - macOS
verified: true
validated: true
---

# nmap-smb-ms17-010-vuln-scan

## Command

```bash
nmap -Pn -p445 --open --max-hostgroup 3 --script smb-vuln-ms17-010 <ip_netblock>
```

## Description

This command uses Nmap to scan a network range for hosts vulnerable to the MS17-010 EternalBlue SMB flaw, focusing on port 445. It is ideal for initial reconnaissance in penetration testing to identify exploitable Windows systems.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| <ip_netblock> | IP range to scan (e.g., 192.168.1.0/24) | Yes |
| -Pn | Skip host discovery, treat all as online | No |
| -p445 | Scan only SMB port 445 | No |
| --open | Show only open ports | No |
| --max-hostgroup 3 | Limit parallel host groups to 3 for stability | No |
| --script smb-vuln-ms17-010 | Run the EternalBlue vulnerability NSE script | Yes |

## Examples

### Basic Usage

```bash
nmap -Pn -p445 --open --max-hostgroup 3 --script smb-vuln-ms17-010 192.168.1.0/24
```

### Advanced Usage

```bash
nmap -Pn -p445 --open -T4 --script smb-vuln-ms17-010,vuln 10.0.0.0/16
```

## Expected Output

```
Nmap scan report for 192.168.1.10
Host is up (0.005s latency).
PORT    STATE SERVICE
445/tcp open  microsoft-ds
| smb-vuln-ms17-010:
|   VULNERABLE:
|   Remote Code Execution vulnerability in Microsoft SMBv1 servers (ms17-010)
|     State: VULNERABLE
|     IDs:  CVE:CVE-2017-0144
|     Description:
|       The RCE vulnerability is in the SMBv1 server in Microsoft Windows.
|     Disclosure date: 2017-03-14
|     References:
|       https://nvd.nist.gov/vuln/detail/CVE-2017-0144
|_      https://technet.microsoft.com/library/security/MS17-010

Nmap done: 256 IP addresses (1 host up) scanned in 45.23 seconds
```

## Related

- [[procedures/EternalBlue-SMB-Exploitation]]
- [[tools/Nmap]]
