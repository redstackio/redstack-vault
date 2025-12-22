---
id: b6625a02-8416-464b-8fef-b42490e590f8
name: nmap-service-scan-without-host-discovery
type: command
executor: bash
data: nmap -sV -Pn $_TARGET_IP
output: >-
  root@kali:~# nmap -sV -Pn 10.10.10.10

  Starting Nmap 7.80 ( https://nmap.org ) at 2019-09-12 14:52 EDT

  Nmap scan report for 10.10.10.10

  Host is up (0.0017s latency).

  Not shown: 999 closed ports

  PORT     STATE SERVICE     VERSION

  21/tcp   open  ftp         vsftpd 2.3.4

  MAC Address: 00:0C:29:66:97:CB (VMware)

  Service Info: Hosts:  host.localdomain, irc.host.LAN; OSs: Unix, Linux; CPE:
  cpe:/o:linux:linux_kernel


  Service detection performed. Please report any incorrect results at
  https://nmap.org/submit/ .

  Nmap done: 1 IP address (1 host up) scanned in 11.72 seconds
created_at: '2019-09-12T18:53:18.085226+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
  - scanning
verified: true
validated: true
---

# Nmap Service Scan Without Host Discovery

## Command

```bash
nmap -sV -Pn $_TARGET_IP
```

## Description

This command performs a TCP port scan with service version detection on the specified target IP, skipping the host discovery phase. It is ideal for targets that block or ignore ICMP pings, ensuring the scan proceeds by treating the host as online. Use this during initial reconnaissance to map services without alerting basic detection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address or hostname of the target to scan (e.g., 10.10.10.10 or example.com) | Yes |
| -sV | Probe open ports to determine service/version info; sends additional probes like banner grabs | Built-in |
| -Pn | Never perform host discovery (ping scan); treat all hosts as online to skip ICMP/DNS checks | Built-in |

## Examples

### Basic Usage

Scan the default top 1000 ports on a single IP:

```bash
nmap -sV -Pn 10.10.10.10
```

### Advanced Usage

Scan specific ports (e.g., common web services) with verbose output:

```bash
nmap -sV -Pn -p 80,443,8080 -v $_TARGET_IP
```

## Expected Output

A detailed report of scanned ports, open services, and versions. Successful output indicates the host was probed and services enumerated:

```
root@kali:~# nmap -sV -Pn 10.10.10.10
Starting Nmap 7.80 ( https://nmap.org ) at 2019-09-12 14:52 EDT
Nmap scan report for 10.10.10.10
Host is up (0.0017s latency).
Not shown: 999 closed ports
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 2.3.4
MAC Address: 00:0C:29:66:97:CB (VMware)
Service Info: Hosts:  host.localdomain, irc.host.LAN; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 11.72 seconds
```

Look for 'open' ports with version details; closed/filtered ports are summarized.

## Related

- [[procedures/scan-ports-for-services-without-host-discovery]]
- [[tools/Nmap]]
