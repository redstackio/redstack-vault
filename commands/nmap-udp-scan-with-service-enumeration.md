---
id: da2d00e4-9966-403e-8ab0-10c2c7ba14b8
name: nmap-udp-scan-with-service-enumeration
type: command
executor: bash
data: nmap -sU -sV $_TARGET_IP -oN $_OUTPUT
output: |-
  root@kali:~# nmap -sU -sV 10.10.10.10 -oN udpports
  Starting Nmap 7.70 ... 
  Nmap scan report for 10.10.10.10
  ... PORT     STATE         SERVICE      VERSION
  161/udp  open          snmp         SNMPv1 server (public)
  ... Nmap done: 1 IP address ... scanned in 852.73 seconds
created_at: '2019-10-11T19:37:17.022538+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - Network
tags:
  - recon
  - udp-scan
verified: true
validated: true
---

# nmap-udp-scan-with-service-enumeration

## Command

```bash
nmap -sU -sV $_TARGET_IP -oN $_OUTPUT
```

## Description

Scans UDP ports with version detection to find non-TCP services like SNMP.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -sU | UDP scan type | Yes |
| -sV | Service version detection | Yes |
| $_TARGET_IP | Target IP | Yes |
| -oN $_OUTPUT | Output file | Yes |

## Examples

### Basic UDP Scan

```bash
nmap -sU -sV 10.10.10.10 -oN udp.txt
```

## Expected Output

UDP ports with states like open|filtered and service info.

## Related

- [[procedures/thorough-port-scan-with-service-enumeration]]
