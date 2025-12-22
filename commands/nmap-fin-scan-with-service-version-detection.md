---
id: 0d4b53ca-8aa9-4eed-9182-13d3d32e00ec
name: nmap-fin-scan-with-service-version-detection
type: command
executor: bash
data: nmap -sV -sF -p- $_TARGET_IP
output: >
  root@kali:~# nmap -sV -sF 10.10.10.10

  Starting Nmap 7.80 ( https://nmap.org ) at 2019-09-12 14:55 EDT

  Nmap scan report for 10.10.10.10

  Host is up (0.0026s latency).

  Not shown: 998 closed ports

  PORT     STATE SERVICE     VERSION

  21/tcp   open  ftp         vsftpd 2.3.4

  22/tcp   open  ssh         OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)

  MAC Address: 00:0C:29:66:97:CB (VMware)


  Service detection performed. Please report any incorrect results at
  https://nmap.org/submit/ .

  Nmap done: 1 IP address (1 host up) scanned in 13.03 seconds
created_at: '2019-09-12T19:01:25.583612+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
  - scanning
verified: true
validated: true
---

# nmap-fin-scan-with-service-version-detection

## Command

```bash
nmap -sV -sF -p- $_TARGET_IP
```

## Description

This command executes a FIN scan (-sF) on all TCP ports (-p-) of the specified target IP, while also performing service version detection (-sV). It is designed for stealthy port discovery in environments where SYN scans may be blocked by firewalls, as FIN packets can sometimes elicit responses from open ports without a full connection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | The IP address or hostname of the target to scan (e.g., 10.10.10.10 or example.com) | Yes |
| -sV | Enables service version detection on open ports, probing for software names and versions | Yes |
| -sF | Performs a FIN scan, sending TCP FIN packets to ports | Yes |
| -p- | Scans all 65535 TCP ports (1-65535) | Yes |

## Examples

### Basic Usage

Scan a single host for all TCP ports using FIN method with service info:

```bash
nmap -sV -sF -p- 10.10.10.10
```

### Advanced Usage

Add output to file and increase verbosity for a target range:

```bash
nmap -sV -sF -p- -oN scan_results.txt -v 192.168.1.0/24
```

## Expected Output

The output lists the target's open ports, services, and versions. For example:

```
root@kali:~# nmap -sV -sF 10.10.10.10
Starting Nmap 7.80 ( https://nmap.org ) at 2019-09-12 14:55 EDT
Nmap scan report for 10.10.10.10
Host is up (0.0026s latency).
Not shown: 998 closed ports
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 2.3.4
22/tcp   open  ssh         OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)
MAC Address: 00:0C:29:66:97:CB (VMware)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.03 seconds
```

Success is indicated by the "Host is up" message and any listed open ports with service details. Closed ports are summarized as "Not shown: X closed ports".

## Related

- [[procedures/Port-Scan-All-TCP-Ports-with-FIN-Scan]]
- [[tools/Nmap]]
