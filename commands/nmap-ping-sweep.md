---
id: 7b5609ae-c4fc-482e-a93f-2be00490d107
name: nmap-ping-sweep
type: command
executor: bash
data: nmap -sn $_TARGET_SUBNET/$_CIDR
output: |-
  root@kali:~# nmap -sn 10.10.10.0/24
  Starting Nmap 7.70 ( https://nmap.org ) at 2019-09-11 16:44 EDT
  Nmap scan report for 10.10.10.1
  Host is up (0.016s latency).
  Nmap scan report for 10.10.10.2
  Host is up (0.005s latency).
  Nmap done: 256 IP addresses (2 hosts up) scanned in 2.03 seconds
created_at: '2019-09-11T20:46:03.382284+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
  - host-discovery
verified: true
validated: true
---

# nmap-ping-sweep

## Command

```bash
nmap -sn $_TARGET_SUBNET/$_CIDR
```

## Description

This command performs a ping sweep using Nmap to discover live hosts on a subnet without scanning ports. It uses ICMP echo requests, ARP requests (on local networks), and probes to common TCP/UDP ports to determine host availability. Ideal for initial network mapping in reconnaissance phases.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_SUBNET | Base IP address of the subnet (e.g., 10.10.10.0) | Yes |
| $_CIDR | CIDR mask for the subnet (e.g., 24 for /24) | Yes |
| -sn | Disable port scanning; perform host discovery only | Built-in |

## Examples

### Basic Usage

```bash
nmap -sn 192.168.1.0/24
```

### Advanced Usage

```bash
nmap -sn --min-parallelism 100 10.0.0.0/16
```

This increases parallelism for faster scans on larger subnets.

## Expected Output

Description of what output to expect when the command runs successfully.

```
root@kali:~# nmap -sn 10.10.10.0/24
Starting Nmap 7.70 ( https://nmap.org ) at 2019-09-11 16:44 EDT
Nmap scan report for 10.10.10.1
Host is up (0.016s latency).
Nmap scan report for 10.10.10.2
Host is up (0.005s latency).
Nmap done: 256 IP addresses (2 hosts up) scanned in 2.03 seconds
```

The output lists live hosts with latency; unresponsive hosts are omitted.

## Related

- [[procedures/Ping-Sweep-a-Subnet-for-Online-Hosts]]
- [[tools/Nmap]]
