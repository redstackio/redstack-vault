---
id: cd3ad18e-4b15-49d9-a72d-9eedfdd1d24f
name: nmap-service-version-scan-with-scripts
type: command
executor: bash
data: nmap -sV -sC -oA ~/nmap-initial $_TARGET_IP
output: null
created_at: '2023-04-06T03:56:21.959439+00:00'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Linux
tags:
  - recon
  - scanning
verified: true
validated: true
---

# nmap-service-version-scan-with-scripts

## Command

```bash
nmap -sV -sC -oA ~/nmap-initial $_TARGET_IP
```

## Description

This command performs a TCP SYN scan with service version detection, default NSE script execution, and multi-format output saving. It is used for initial network mapping to identify exploitable services during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | Target IP address, hostname, or CIDR range (e.g., 192.168.1.1 or 10.0.0.0/24) | Yes |
| -sV | Enables service version detection by probing open ports with banners and probes | Built-in |
| -sC | Invokes the 100+ default NSE scripts for common service enumeration and vulnerability checks | Built-in |
| -oA | Saves scan results in normal, XML, and grepable formats with the prefix "nmap-initial" in the current directory | Built-in |
| ~/nmap-initial | Output file prefix and path; customizable to any directory (e.g., /tmp/scan-results) | Yes |

## Examples

### Basic Usage

Scan a single host:
```bash
nmap -sV -sC -oA ~/nmap-initial 192.168.1.1
```

### Advanced Usage

Scan a subnet with rate limiting to reduce detection:
```bash
nmap -sV -sC -oA ~/nmap-initial --min-rate 500 192.168.1.0/24
```

## Expected Output

The command outputs real-time scan progress and results to the terminal, with files saved separately. Sample successful output:

Starting Nmap 7.80 ( https://nmap.org ) at 2024-01-01 12:00 UTC
Nmap scan report for 192.168.1.1
Host is up (0.0012s latency).
Not shown: 997 closed ports
PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 96:f9:... (RSA)
80/tcp  open  http     Apache httpd 2.4.29 ((Ubuntu))
| http-title: Example Web Site
|_Requested resource was http://192.168.1.1/

Nmap done: 1 IP address (1 host up) scanned in 4.56 seconds

Files generated: ~/nmap-initial.nmap, ~/nmap-initial.xml, ~/nmap-initial.gnmap.

## Related

- [[procedures/Basic-Nmap-Service-Version-Scan]]
- [[tools/Nmap]]
