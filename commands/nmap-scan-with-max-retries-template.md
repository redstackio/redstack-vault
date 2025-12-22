---
type: command
executor: bash
data: nmap -p- --max-retries 5 $_TARGET_IP
tags:
  - Enumeration
  - Network
platforms:
  - Linux
  - Windows
verified: true
validated: true
---

# nmap-scan-with-max-retries-template

## Command

```bash
nmap -p- --max-retries 5 $_TARGET_IP
```

## Description

Retries up to 5 times per probe to handle packet loss in unreliable networks during full port scans.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address or hostname of the target | Yes |
| -p- | Scan all 65535 TCP ports | Built-in |
| --max-retries 5 | Maximum retries per probe | Built-in |

## Examples

### Basic Usage

```bash
nmap -p- --max-retries 5 192.168.1.100
```

### Advanced Usage

```bash
nmap -p- --max-retries 10 -T3 192.168.1.100
```

## Expected Output

```
Starting Nmap 7.80 ( https://nmap.org ) at 2023-01-01 12:00 UTC
Nmap scan report for 192.168.1.100
Host is up (0.0015s latency).
Not shown: 65530 closed ports
PORT     STATE SERVICE
80/tcp   open  http
Nmap done: 1 IP address (1 host up) scanned in 180.20 seconds
```

## Related

- [[procedures/Scan-Problematic-Hosts-with-Nmap-Timing-Templates]]
- [[tools/Nmap]]
