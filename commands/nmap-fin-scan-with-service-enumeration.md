---
type: command
executor: bash
data: nmap -sV -sF -p- $_TARGET_IP
tags:
  - Enumeration
  - Network
platforms:
  - Linux
  - Windows
verified: true
validated: true
---

# nmap-fin-scan-with-service-enumeration

## Command

```bash
nmap -sV -sF -p- $_TARGET_IP
```

## Description

Performs a FIN scan (-sF) to evade some firewalls by sending FIN packets, combined with service version detection (-sV) across all ports (-p-). Use when SYN scans fail to detect open ports due to firewall rules.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address or hostname of the target | Yes |
| -sV | Enable service version detection | Built-in |
| -sF | Use FIN scan (TCP FIN packets) | Built-in |
| -p- | Scan all 65535 TCP ports | Built-in |

## Examples

### Basic Usage

```bash
nmap -sV -sF -p- 192.168.1.100
```

### Advanced Usage

```bash
nmap -sV -sF -p- -T2 192.168.1.100
```

## Expected Output

```
root@kali:~# nmap -sV -sF 10.10.10.10
Starting Nmap 7.80 ( https://nmap.org ) at 2019-09-12 14:55 EDT
Nmap scan report for 10.10.10.10
Host is up (0.0026s latency).
Not shown: 998 closed ports
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 2.3.4
22/tcp   open  ssh         OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)
MAC Address: 00:0C:29:66:97:CB (VMware)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.03 seconds
```

## Related

- [[procedures/Scan-Problematic-Hosts-with-Nmap-Timing-Templates]]
- [[tools/Nmap]]
