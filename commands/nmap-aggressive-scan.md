---
id: 146ef251-3807-4bba-8d64-30a531b0ed9e
name: nmap-aggressive-scan
type: command
executor: bash
data: nmap -A -T4 $_TARGET
output: null
created_at: '2023-04-06T03:56:21.986079+00:00'
updated_at: '2023-04-10T20:25:08.731691+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - recon
  - scanning
verified: true
validated: true
---

# nmap-aggressive-scan

## Command

```bash
nmap -A -T4 $_TARGET
```

## Description

This command performs an aggressive Nmap scan on a target host or network, enabling OS detection, service version identification, default NSE script execution, and traceroute. Use it for thorough reconnaissance to map services and potential vulnerabilities during initial discovery phases.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET | Target IP address, hostname, or range (e.g., 192.168.1.1, scanme.nmap.org, 10.0.0.0/24) | Yes |
| -A | Enables OS detection, version detection, script scanning, and traceroute | Built-in |
| -T4 | Aggressive timing template (0-5; 4 is fast for most networks) | Built-in |

## Examples

### Basic Usage

```bash
nmap -A -T4 scanme.nmap.org
```

### Advanced Usage

```bash
nmap -A -T4 -oN results.txt 192.168.1.0/24
```

Saves output to a file for later analysis.

## Expected Output

Sample output for a single host:

Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.10s latency).
Not shown: 996 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 4.4p1 Debian 5ubuntu1 (Ubuntu Linux; protocol 2.0)
25/tcp   open  smtp    Postfix smtpd
80/tcp   open  http    Apache httpd 2.2.8 ((Ubuntu) DAV/2)
OS details: Linux 2.6.24 - 2.6.28
Network Distance: 12 hops

TRACEROUTE
HOP RTT     ADDRESS
1   10.00 ms 192.168.1.1
...

## Related

- [[commands/nmap-host-discovery]]
- [[procedures/Network-Discovery-with-Nmap-Full-Scan]]
