---
type: command
executor: bash
data: nmap -p- --host-timeout 100ms $_TARGET_IP
tags:
  - Enumeration
  - Network
platforms:
  - Linux
  - Windows
verified: true
validated: true
---

# nmap-scan-with-host-timeout-template

## Command

```bash
nmap -p- --host-timeout 100ms $_TARGET_IP
```

## Description

Scans all ports but aborts after 100ms if the host is unresponsive, speeding up scans on dead or heavily filtered targets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address or hostname of the target | Yes |
| -p- | Scan all 65535 TCP ports | Built-in |
| --host-timeout 100ms | Maximum time per host before timeout | Built-in |

## Examples

### Basic Usage

```bash
nmap -p- --host-timeout 100ms 192.168.1.100
```

### Advanced Usage

```bash
nmap -p- --host-timeout 500ms -iL targets.txt
```

## Expected Output

```
Starting Nmap 7.80 ( https://nmap.org ) at 2023-01-01 12:00 UTC
Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn
Nmap done: 1 IP address (0 hosts up) scanned in 0.10 seconds
```

## Related

- [[procedures/Scan-Problematic-Hosts-with-Nmap-Timing-Templates]]
- [[tools/Nmap]]
