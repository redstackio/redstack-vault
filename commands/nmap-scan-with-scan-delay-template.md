---
type: command
executor: bash
data: nmap -p- --scan-delay 10s $_TARGET_IP
tags:
  - Enumeration
  - Network
platforms:
  - Linux
  - Windows
verified: true
validated: true
---

# nmap-scan-with-scan-delay-template

## Command

```bash
nmap -p- --scan-delay 10s $_TARGET_IP
```

## Description

Inserts a 10-second delay between probes to bypass time-based firewall rules or IDS thresholds.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address or hostname of the target | Yes |
| -p- | Scan all 65535 TCP ports | Built-in |
| --scan-delay 10s | Delay between probes | Built-in |

## Examples

### Basic Usage

```bash
nmap -p- --scan-delay 10s 192.168.1.100
```

### Advanced Usage

```bash
nmap -p- --scan-delay 5s -T0 192.168.1.100
```

## Expected Output

```
Starting Nmap 7.80 ( https://nmap.org ) at 2023-01-01 12:00 UTC
Nmap scan report for 192.168.1.100
Host is up (0.0100s latency).
Not shown: 65534 closed ports
PORT    STATE SERVICE
80/tcp  open  http
Nmap done: 1 IP address (1 host up) scanned in 655350.00 seconds
```

## Related

- [[procedures/Scan-Problematic-Hosts-with-Nmap-Timing-Templates]]
- [[tools/Nmap]]
