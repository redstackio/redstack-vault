---
type: command
executor: bash
data: nmap -p- --min-rtt-timeout 5ms --max-rtt-timeout 100ms $_TARGET_IP
tags:
  - Enumeration
  - Network
platforms:
  - Linux
  - Windows
verified: true
validated: true
---

# nmap-scan-with-min-max-rtt-timeout-template

## Command

```bash
nmap -p- --min-rtt-timeout 5ms --max-rtt-timeout 100ms $_TARGET_IP
```

## Description

Sets RTT timeouts between 5ms and 100ms to adapt to network latency variations during port scanning.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address or hostname of the target | Yes |
| -p- | Scan all 65535 TCP ports | Built-in |
| --min-rtt-timeout 5ms | Minimum RTT timeout | Built-in |
| --max-rtt-timeout 100ms | Maximum RTT timeout | Built-in |

## Examples

### Basic Usage

```bash
nmap -p- --min-rtt-timeout 5ms --max-rtt-timeout 100ms 192.168.1.100
```

### Advanced Usage

```bash
nmap -p- --min-rtt-timeout 10ms --max-rtt-timeout 200ms -T1 192.168.1.100
```

## Expected Output

```
Starting Nmap 7.80 ( https://nmap.org ) at 2023-01-01 12:00 UTC
Nmap scan report for 192.168.1.100
Host is up (0.0050s latency).
Not shown: 65531 closed ports
PORT     STATE SERVICE
22/tcp   open  ssh
Nmap done: 1 IP address (1 host up) scanned in 90.15 seconds
```

## Related

- [[procedures/Scan-Problematic-Hosts-with-Nmap-Timing-Templates]]
- [[tools/Nmap]]
