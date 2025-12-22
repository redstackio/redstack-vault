---
id: d0791778-87b6-4fca-adb1-694c98e2c994
name: Nmap OS Detection and Service Scan
type: command
executor: bash
data: nmap -O -sV $_TARGET_IP
output: >-
  root@kali:~# nmap -O -sV 10.10.10.10

  Starting Nmap 7.70 ( https://nmap.org ) at 2019-09-13 17:41 EDT

  Nmap scan report for 10.10.10.10

  Host is up (0.00059s latency).

  Not shown: 998 closed ports

  PORT     STATE SERVICE     VERSION

  22/tcp open  ssh           OpenSSH 7.2p2 Ubuntu 4ubuntu2.6 (Ubuntu Linux;
  protocol 2.0)

  80/tcp   open  http        Apache httpd 2.4.18 ((Ubuntu))

  MAC Address: 08:00:27:31:27:7A (Oracle VirtualBox virtual NIC)

  Device type: general purpose

  Running: Linux 2.6.X

  OS CPE: cpe:/o:linux:linux_kernel:2.6

  OS details: Linux 2.6.9 - 2.6.33

  Network Distance: 1 hop

  Service Info: Hosts:  host.localdomain, localhost, irc.host.LAN; OSs: Unix,
  Linux; CPE: cpe:/o:linux:linux_kernel


  OS and Service detection performed. Please report any incorrect results at
  https://nmap.org/submit/ .

  Nmap done: 1 IP address (1 host up) scanned in 13.72 seconds
created_at: '2019-09-13T22:29:10.923723+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
  - discovery
verified: true
validated: true
---

# Nmap OS Detection and Service Scan

## Command

```bash
nmap -O -sV $_TARGET_IP
```

## Description

This command performs remote OS detection and service version scanning on a target IP using Nmap. The -O flag enables OS fingerprinting by analyzing TCP/IP stack behaviors, while -sV probes open ports for service and version details via banners. Use this during reconnaissance to identify the target's OS family and version for exploit selection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address or hostname of the target to scan | Yes |
| -O | Enable OS detection (sends additional probes) | Built-in |
| -sV | Enable service version detection (banner grabbing) | Built-in |

## Examples

### Basic Usage

```bash
nmap -O -sV 192.168.1.100
```

Scans a single host for OS and services.

### Advanced Usage

```bash
nmap -O -sV -p 22,80,443 $_TARGET_IP
```

Limits scan to specific ports (e.g., SSH, HTTP, HTTPS) for faster execution.

## Expected Output

Starting Nmap 7.70 ( https://nmap.org ) at 2019-09-13 17:41 EDT
Nmap scan report for 10.10.10.10
Host is up (0.00059s latency).
Not shown: 998 closed ports
PORT     STATE SERVICE     VERSION
22/tcp open  ssh           OpenSSH 7.2p2 Ubuntu 4ubuntu2.6 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http        Apache httpd 2.4.18 ((Ubuntu))
MAC Address: 08:00:27:31:27:7A (Oracle VirtualBox virtual NIC)
Device type: general purpose
Running: Linux 2.6.X
OS CPE: cpe:/o:linux:linux_kernel:2.6
OS details: Linux 2.6.9 - 2.6.33
Network Distance: 1 hop
Service Info: Hosts:  host.localdomain, localhost, irc.host.LAN; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.72 seconds

Look for "Running:" and "OS details:" for OS info, and "VERSION" column for service banners.

## Related

- [[procedures/Identify-Operating-System-and-Version]]
- [[tools/Nmap]]
