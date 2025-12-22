---
id: fc2e0c0c-7263-4709-90ce-ee6fc08cbede
type: command
executor: bash
data: nmap -sV $_TARGET_IP
output: >-
  root@kali:~# nmap -sV 10.10.10.10

  Starting Nmap 7.80 ( https://nmap.org ) at 2019-09-12 14:23 EDT

  Nmap scan report for 10.10.10.10

  Host is up (0.0000050s latency).

  Not shown: 999 closed ports

  PORT    STATE SERVICE VERSION

  80/tcp  open  http     Apache httpd 2.4.29 ((Ubuntu))

  443/tcp open  https    Apache httpd 2.4.29 ((Ubuntu))


  Service detection performed. Please report any incorrect results at
  https://nmap.org/submit/ .

  Nmap done: 1 IP address (1 host up) scanned in 6.41 seconds
created_at: '2019-09-12T18:24:17.551382+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - recon
  - enumeration
verified: true
validated: true
---

# nmap-port-scan-with-service-version-detection

## Command

```bash
nmap -sV $_TARGET_IP
```

## Description

Scans the target IP for open TCP ports and detects service versions/banners, useful for identifying web servers in reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -sV | Enable service version detection | Yes |
| $_TARGET_IP | IP address or hostname to scan | Yes |

## Examples

### Basic Usage

```bash
nmap -sV 10.10.10.10
```

### With Port Specification

```bash
nmap -sV -p 80,443 10.10.10.10
```

## Expected Output

Description of open ports and services, e.g., 80/tcp open http Apache httpd 2.4.29.

## Related

- [[procedures/Basic-Port-Scan-with-Service-Enumeration]]
- [[tools/Nmap]]
