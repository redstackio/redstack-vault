---
type: command
executor: bash
data: nmap -p- --min-hostgroup 3 --max-hostgroup 4 $_TARGET_IP
tags:
  - Enumeration
  - Network
platforms:
  - Linux
  - Windows
verified: true
validated: true
---

# nmap-scan-with-hostgroup-template

## Command

```bash
nmap -p- --min-hostgroup 3 --max-hostgroup 4 $_TARGET_IP
```

## Description

Scans all ports while limiting parallel host probes to 3-4, reducing load on the scanner and network for stealthier multi-host scans.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address or hostname of the target | Yes |
| -p- | Scan all 65535 TCP ports | Built-in |
| --min-hostgroup 3 | Minimum hosts scanned in parallel | Built-in |
| --max-hostgroup 4 | Maximum hosts scanned in parallel | Built-in |

## Examples

### Basic Usage

```bash
nmap -p- --min-hostgroup 3 --max-hostgroup 4 192.168.1.100
```

### Advanced Usage

```bash
nmap -p- --min-hostgroup 1 --max-hostgroup 2 -iL targets.txt
```

## Expected Output

```
Starting Nmap 7.80 ( https://nmap.org ) at 2023-01-01 12:00 UTC
Nmap scan report for 192.168.1.100
Host is up (0.0010s latency).
Not shown: 65530 closed ports
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
Nmap done: 1 IP address (1 host up) scanned in 120.45 seconds
```

## Related

- [[procedures/Scan-Problematic-Hosts-with-Nmap-Timing-Templates]]
- [[tools/Nmap]]
