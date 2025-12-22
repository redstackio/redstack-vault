---
id: 4509bd7b-a62e-4dd0-899e-49661bcccf24
name: p0f-passive-fingerprinting
type: command
executor: bash
data: p0f -i $_INTERFACE -p -o $_OUTPUT.log
output: >-
  root@kali:~# p0f -i eth0 -p -o output.log\n--- p0f 3.09b by Michal Zalewski
  <lcamtuf@coredump.cx> ---\n\n[+] Closed 1 file descriptor.\n[+] Loaded 322
  signatures from '/etc/p0f/p0f.fp'.\n[+] Intercepting traffic on interface
  'eth0'.\n[+] Default packet filtering configured [+VLAN].\n[+] Log file
  'output.log' opened for writing.\n[+] Entered main event loop.\n\n.-[
  10.10.10.11/57962 -> 10.10.10.10/199 (syn) ]-\n|\n| client   =
  10.10.10.10/57962\n| app      = NMap SYN scan\n| dist     = <= 16\n| params  
  = random_ttl\n| raw_sig  = 4:48+16:0:1460:1024,0:mss::0\n...
created_at: '2019-09-12T18:07:35.196374+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - Windows
tags:
  - network
  - fingerprinting
  - sniffing
verified: true
validated: true
---

# p0f-passive-fingerprinting

## Command

```bash
p0f -i $_INTERFACE -p -o $_OUTPUT.log
```

## Description

This command runs p0f to passively fingerprint network traffic on the specified interface, capturing details like OS and application types without generating probes. Use it during stealthy reconnaissance to map network hosts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i $_INTERFACE | Network interface to monitor (e.g., eth0) | Yes |
| -p | Enable promiscuous mode for full traffic capture | Yes |
| -o $_OUTPUT.log | Output log file for fingerprints (e.g., output.log) | Yes |

## Examples

### Basic Usage

```bash
p0f -i eth0 -p -o fingerprints.log
```

### With Additional Filtering

```bash
p0f -i eth0 -p -o output.log -f /etc/p0f/p0f.fp
```

## Expected Output

root@kali:~# p0f -i eth0 -p -o output.log\n--- p0f 3.09b by Michal Zalewski <lcamtuf@coredump.cx> ---\n\n[+] Closed 1 file descriptor.\n[+] Loaded 322 signatures from '/etc/p0f/p0f.fp'.\n[+] Intercepting traffic on interface 'eth0'.\n[+] Default packet filtering configured [+VLAN].\n[+] Log file 'output.log' opened for writing.\n[+] Entered main event loop.\n\n.-[ 10.10.10.11/57962 -> 10.10.10.10/199 (syn) ]-\n|\n| client   = 10.10.10.10/57962\n| app      = NMap SYN scan\n| dist     = <= 16\n| params   = random_ttl\n| raw_sig  = 4:48+16:0:1460:1024,0:mss::0\n...

## Related

- [[procedures/Passive-Network-Traffic-Fingerprinting]]
- [[tools/p0f]]
