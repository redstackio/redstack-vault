---
type: command
executor: bash
data: nmap -p- --initial-rtt-timeout 50ms $_TARGET_IP
tags:
  - Enumeration
  - Network
platforms:
  - Linux
  - Windows
verified: true
validated: true
---

# nmap-scan-with-initial-rtt-timeout-template

## Command

```bash
nmap -p- --initial-rtt-timeout 50ms $_TARGET_IP
```

## Description

Sets the initial round-trip timeout to 50ms for the first probes, allowing quick assessment of host responsiveness.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address or hostname of the target | Yes |
| -p- | Scan all 65535 TCP ports | Built-in |
| --initial-rtt-timeout 50ms | Initial RTT wait time | Built-in |

## Examples

### Basic Usage

```bash
nmap -p- --initial-rtt-timeout 50ms 192.168.1.100
```

### Advanced Usage

```bash
nmap -p- --initial-rtt-timeout 100ms --min-rtt-timeout 20ms 192.168.1.100
```

## Expected Output

```
Starting Nmap 7.80 ( https://nmap.org ) at 2023-01-01 12:00 UTC
Nmap scan report for 192.168.1.100
Host is up (0.0500s latency).
Not shown: 65528 closed ports
PORT     STATE SERVICE
22/tcp   open  ssh
443/tcp  open  https
Nmap done: 1 IP address (1 host up) scanned in 120.75 seconds
```

## Related

- [[procedures/Scan-Problematic-Hosts-with-Nmap-Timing-Templates]]
- [[tools/Nmap]]
