---
type: command
executor: bash
data: nmap -sn -n --disable-arp-ping $_IP_RANGE | grep -v "Host down"
output: null
created_at: '2023-04-06T03:56:21.904156+00:00'
updated_at: '2023-04-10T20:25:09.485621+00:00'
platforms:
  - Linux
tags:
  - recon
  - network-discovery
verified: true
validated: true
---

# nmap-host-discovery-scan

## Command

```bash
nmap -sn -n --disable-arp-ping $_IP_RANGE | grep -v "Host down"
```

## Description

This command uses Nmap to discover live hosts on a network by sending lightweight probes (ICMP echo, TCP SYN/ACK) without performing port scans. It disables DNS resolution and ARP ping for faster, stealthier remote scans, then filters output to show only up hosts. Use this during initial reconnaissance to map active systems in a subnet.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_IP_RANGE | Target IP range or CIDR (e.g., 192.168.1.1-254 or 10.0.0.0/24) | Yes |
| -sn | Perform host discovery only, no port scan | Built-in |
| -n | Skip DNS resolution to avoid delays and logs | Built-in |
| --disable-arp-ping | Disable ARP for non-local networks | Built-in |
| grep -v "Host down" | Filter out non-responsive hosts from output | Built-in |

## Examples

### Basic Usage

```bash
nmap -sn -n --disable-arp-ping 192.168.1.1-254 | grep -v "Host down"
```

### Advanced Usage

```bash
nmap -sn -n --disable-arp-ping -T4 10.0.0.0/24 | grep -v "Host down" > live_hosts.txt
```

> Adds timing template (-T4) for faster scans and outputs to file.

## Expected Output

Nmap scan report for 192.168.1.10
Host is up (0.0012s latency).
MAC Address: 00:11:22:33:44:55 (Vendor)

Nmap scan report for 192.168.1.100
Host is up (0.00045s latency).

> Lists only live hosts with latency and MAC if local; no port details.
