---
type: command
executor: bash
data: nmap -p- --max-rate 2 $_TARGET_IP
tags:
  - Enumeration
  - Network
platforms:
  - Linux
  - Windows
verified: true
validated: true
---

# nmap-scan-with-max-rate-template

## Command

```bash
nmap -p- --max-rate 2 $_TARGET_IP
```

## Description

Limits the scan to 2 packets per second to evade rate-limiting defenses while scanning all ports.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address or hostname of the target | Yes |
| -p- | Scan all 65535 TCP ports | Built-in |
| --max-rate 2 | Maximum packets per second | Built-in |

## Examples

### Basic Usage

```bash
nmap -p- --max-rate 2 192.168.1.100
```

### Advanced Usage

```bash
nmap -p- --max-rate 5 -T1 192.168.1.100
```

## Expected Output

```
Starting Nmap 7.80 ( https://nmap.org ) at 2023-01-01 12:00 UTC
Nmap scan report for 192.168.1.100
Host is up (0.0012s latency).
Not shown: 65533 closed ports
PORT    STATE SERVICE
22/tcp  open  ssh
Nmap done: 1 IP address (1 host up) scanned in 3000.00 seconds
```

## Related

- [[procedures/Scan-Problematic-Hosts-with-Nmap-Timing-Templates]]
- [[tools/Nmap]]
