---
type: command
executor: bash
data: nmap -p- --min-rate 2 $_TARGET_IP
tags:
  - Enumeration
  - Network
platforms:
  - Linux
  - Windows
verified: true
validated: true
---

# nmap-scan-with-min-rate-template

## Command

```bash
nmap -p- --min-rate 2 $_TARGET_IP
```

## Description

Ensures at least 2 packets per second are sent, preventing overly slow scans in low-bandwidth scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address or hostname of the target | Yes |
| -p- | Scan all 65535 TCP ports | Built-in |
| --min-rate 2 | Minimum packets per second | Built-in |

## Examples

### Basic Usage

```bash
nmap -p- --min-rate 2 192.168.1.100
```

### Advanced Usage

```bash
nmap -p- --min-rate 1 --max-rate 10 192.168.1.100
```

## Expected Output

```
Starting Nmap 7.80 ( https://nmap.org ) at 2023-01-01 12:00 UTC
Nmap scan report for 192.168.1.100
Host is up (0.0020s latency).
Not shown: 65529 closed ports
PORT      STATE SERVICE
21/tcp    open  ftp
Nmap done: 1 IP address (1 host up) scanned in 600.50 seconds
```

## Related

- [[procedures/Scan-Problematic-Hosts-with-Nmap-Timing-Templates]]
- [[tools/Nmap]]
