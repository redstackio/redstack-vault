---
id: 69e68fc6-1a8f-458f-adc1-80d7d687bbc4
name: proxychains-nmap-tcp-connect-scan
type: command
executor: bash
data: proxychains nmap -sT $_TARGET_IP
output: null
created_at: '2023-04-06T03:56:22.517397+00:00'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Linux
tags:
  - pivoting
  - scanning
verified: true
validated: true
---

# proxychains-nmap-tcp-connect-scan

## Command

```bash
proxychains nmap -sT $_TARGET_IP
```

## Description

This command routes an Nmap TCP connect scan through Proxychains to a target IP, allowing pivoting from an external attacker machine via an internal proxy to scan hosts behind firewalls.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address of the internal target to scan (e.g., 192.168.5.6) | Yes |
| -sT | Perform TCP connect scan (full handshake) | Built-in |

## Examples

### Basic Usage

```bash
proxychains nmap -sT 192.168.5.6
```

### Advanced Usage

```bash
proxychains nmap -sT -p 1-1000 -O 10.0.0.50
```

## Expected Output

```
[ProxyChains] DLL init: proxychains-ng 4.14
[ProxyChains] Strict chain ... 127.0.0.1:1080 ... 127.0.0.1:1080 ... OK
Starting Nmap 7.80 ( https://nmap.org ) at 2023-04-06 10:00 UTC
Nmap scan report for 192.168.5.6
Host is up (0.15s latency).
Not shown: 997 closed ports
PORT    STATE SERVICE
22/tcp  open  ssh
80/tcp  open  http
443/tcp open  https

Nmap done: 1 IP address (1 host up) scanned in 5.23 seconds
```

## Related

- [[procedures/Network-Pivoting-with-Proxychains]]
- [[tools/Proxychains]]
