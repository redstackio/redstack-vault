---
type: command
executor: bash
data: nmap -p- --min-parallelism 2 --max-parallelism 2 $_TARGET_IP
tags:
  - Enumeration
  - Network
platforms:
  - Linux
  - Windows
verified: true
validated: true
---

# nmap-scan-with-min-max-parallelism-template

## Command

```bash
nmap -p- --min-parallelism 2 --max-parallelism 2 $_TARGET_IP
```

## Description

Maintains exactly 2 parallel probes to control scan intensity and avoid detection in sensitive environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address or hostname of the target | Yes |
| -p- | Scan all 65535 TCP ports | Built-in |
| --min-parallelism 2 | Minimum parallel probes | Built-in |
| --max-parallelism 2 | Maximum parallel probes | Built-in |

## Examples

### Basic Usage

```bash
nmap -p- --min-parallelism 2 --max-parallelism 2 192.168.1.100
```

### Advanced Usage

```bash
nmap -p- --min-parallelism 1 --max-parallelism 5 -T2 192.168.1.100
```

## Expected Output

```
Starting Nmap 7.80 ( https://nmap.org ) at 2023-01-01 12:00 UTC
Nmap scan report for 192.168.1.100
Host is up (0.0010s latency).
Not shown: 65532 closed ports
PORT    STATE SERVICE
443/tcp open  https
Nmap done: 1 IP address (1 host up) scanned in 150.30 seconds
```

## Related

- [[procedures/Scan-Problematic-Hosts-with-Nmap-Timing-Templates]]
- [[tools/Nmap]]
