---
id: 5e5b9a80-b278-4447-98d3-79ab9d9def4f
name: nmap-full-port-scan-with-service-enumeration
type: command
executor: bash
data: nmap -sV -p- $_TARGET_IP -oN $_OUTPUT
output: |-
  root@kali:~# nmap -sV -p- 10.10.10.10 -oN allports
  Starting Nmap 7.70 ... 
  Nmap scan report for 10.10.10.10
  ... PORT      STATE SERVICE VERSION
  80/tcp    open  http    Apache httpd 2.4.29
  ... Nmap done: 1 IP ... in 106.06 seconds
created_at: '2019-10-11T19:37:17.062629+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - Network
tags:
  - recon
  - full-scan
verified: true
validated: true
---

# nmap-full-port-scan-with-service-enumeration

## Command

```bash
nmap -sV -p- $_TARGET_IP -oN $_OUTPUT
```

## Description

Full scan of all 65535 TCP ports with version detection for complete coverage.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -sV | Version detection | Yes |
| -p- | All ports (1-65535) | Yes |
| $_TARGET_IP | Target | Yes |
| -oN $_OUTPUT | Output file | Yes |

## Examples

### Full Scan

```bash
nmap -sV -p- 10.10.10.10 -oN full.txt
```

## Expected Output

All open ports listed with services.

## Related

- [[procedures/thorough-port-scan-with-service-enumeration]]
