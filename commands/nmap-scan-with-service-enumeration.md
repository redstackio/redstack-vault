---
id: b8f280a3-8838-4a76-9a1e-4d7cf8cb3ed4
name: nmap-scan-with-service-enumeration
type: command
executor: bash
data: nmap -sV $_TARGET_IP -oN $_OUTPUT
output: >-
  root@kali:~# nmap -sV 10.10.10.10 -oN default

  Starting Nmap 7.70 ( https://nmap.org ) at 2019-10-11 14:56 EDT

  Nmap scan report for 10.10.10.10

  Host is up (0.00025s latency).

  Not shown: 990 closed ports

  PORT      STATE SERVICE      VERSION

  80/tcp    open  http         Apache httpd 2.4.29 ((Ubuntu))

  ... (additional ports)

  Service detection performed. Please report any incorrect results at
  https://nmap.org/submit/ .

  Nmap done: 1 IP address (1 host up) scanned in 60.51 seconds
created_at: '2019-10-11T19:37:17.057364+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - Network
tags:
  - recon
  - port-scan
verified: true
validated: true
---

# nmap-scan-with-service-enumeration

## Command

```bash
nmap -sV $_TARGET_IP -oN $_OUTPUT
```

## Description

Performs a SYN scan on the top 1000 TCP ports with service version detection, outputting to a file for review. Use for initial target mapping.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -sV | Enable service version detection | Yes |
| $_TARGET_IP | IP address or hostname to scan | Yes |
| -oN | Normal output to specified file | Yes |
| $_OUTPUT | Filename for results (e.g., scan.txt) | Yes |

## Examples

### Basic Usage

```bash
nmap -sV 10.10.10.10 -oN initial.txt
```

### With Port Specification

```bash
nmap -sV -p 80,443 10.10.10.10 -oN web.txt
```

## Expected Output

Description of open ports and services, e.g., 80/tcp open http Apache httpd.

## Related

- [[procedures/thorough-port-scan-with-service-enumeration]]
- [[tools/Nmap]]
