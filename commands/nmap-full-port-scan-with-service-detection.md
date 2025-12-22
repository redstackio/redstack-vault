---
id: aa8cd2f5-f391-48e7-ad54-553f4d18317b
name: nmap-full-port-scan-with-service-detection
type: command
executor: bash
data: nmap -p- -sV -oX a.xml $_TARGET_IP
output: null
created_at: '2023-04-06T03:56:22.011537+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - network-discovery
  - port-scanning
  - service-detection
verified: true
validated: true
---

# nmap-full-port-scan-with-service-detection

## Command

```bash
nmap -p- -sV -oX a.xml $_TARGET_IP
```

## Description

This command performs a comprehensive scan of all ports on the target IP, detects service versions on open ports, and outputs results in XML format for further analysis or tool integration. Use it during initial reconnaissance to map the target's network exposure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | The IP address or hostname of the target to scan (e.g., 192.168.1.100) | Yes |
| -p- | Scan all 65,535 TCP ports | Built-in |
| -sV | Enable service version detection | Built-in |
| -oX | Output scan results in XML format to the specified file | Built-in |
| a.xml | Filename for XML output (overwrites if exists) | Yes |

## Examples

### Basic Usage

```bash
nmap -p- -sV -oX a.xml 192.168.1.100
```

### Advanced Usage

```bash
nmap -p- -sV -O -oX a.xml 192.168.1.0/24
```
(Adds OS detection with -O and scans a subnet)

## Expected Output

Nmap scan report for 192.168.1.100
Host is up (0.005s latency).
Not shown: 65532 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http    Apache httpd 2.4.29 ((Ubuntu))

Nmap done: 1 IP address (1 host up) scanned in 45.23 seconds

(The XML file 'a.xml' will contain structured data like <port id="22" state="open"><service name="ssh" version="OpenSSH 7.6p1"/></port>)

## Related

- [[Related Procedure|procedures/Network-Discovery-and-Vulnerability-Search-with-Nmap-and-Searchsploit]]
- [[Related Tool|tools/Nmap]]
