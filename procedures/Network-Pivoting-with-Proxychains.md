---
id: 2c0cd4a8-3c6a-4bba-a212-f568988eab8e
name: Network-Pivoting-with-Proxychains
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:22.522993+00:00'
updated_at: '2024-01-01T00:00:00Z'
tactics:
  - '[[Command and Control]]'
techniques:
  - '[[Connection Proxy]]'
sub_techniques: []
tags:
  - '[[tags/Network-Pivoting-Techniques]]'
  - '[[tags/Proxychains]]'
commands:
  - '[[commands/proxychains-nmap-tcp-connect-scan]]'
platforms:
  - Linux
tools:
  - '[[tools/Proxychains]]'
  - '[[tools/Nmap]]'
validated: true
---

# Network-Pivoting-with-Proxychains

## Summary

Network pivoting with Proxychains enables attackers to route traffic through a compromised proxy host to reach internal network segments that are not directly accessible, effectively bypassing firewalls, network segmentation, and access controls to perform reconnaissance or exploitation on hidden targets.

## Description

In a typical attack scenario, an attacker has gained initial access to a system within the target network (e.g., via phishing or exploiting a public-facing service) and sets up a SOCKS proxy on that host. Proxychains then forces subsequent tools like Nmap to tunnel their connections through this proxy, allowing the attacker to pivot laterally or access isolated subnets from their external position. This technique is particularly effective in segmented environments like corporate intranets or cloud VPCs where direct inbound connections are blocked. The target environment is usually Linux-based Kali or similar attacker machines connecting to Windows/Linux proxies in enterprise networks. Expected outcomes include successful port scans or connections to internal hosts without direct exposure of the attacker's IP, though it may introduce latency and requires a stable proxy connection.

## Requirements

1. Compromised host in the target network with a SOCKS4/5 proxy server running (e.g., via SSH dynamic forwarding on port 8080).
2. Proxychains installed on the attacker's machine.
3. Nmap installed for scanning through the pivot.
4. Root or sudo access on the attacker machine to edit /etc/proxychains.conf.
5. Knowledge of the proxy's IP and port.

## Defense

- Implement strict network segmentation with micro-segmentation to limit east-west traffic between hosts.
- Monitor for anomalous outbound connections from internal hosts (e.g., unexpected SOCKS proxy traffic) using tools like Zeek or Suricata.
- Enforce least-privilege access and disable unnecessary dynamic port forwarding on bastion hosts.
- Use application-layer proxies or next-gen firewalls to inspect and block proxied tunneling attempts.

## Objectives

1. Route attacker traffic through a compromised internal host to access restricted network segments.
2. Bypass firewall rules and segmentation to perform internal reconnaissance.
3. Maintain operational security by masking the attacker's external IP during lateral movement.

## Instructions

### Step 1: Configure Proxychains Proxy List

**Context**: Edit the Proxychains configuration file to specify the proxy server details, ensuring all subsequent proxied commands route through the compromised host. This step sets up the chain for SOCKS4 proxies; save changes to /etc/proxychains.conf and test connectivity.

**Code** ([[codes/proxychains-proxy-list-configuration]]):

```bash
[ProxyList]
socks4 localhost 8080
```

> This configuration adds a SOCKS4 proxy entry. Replace 'localhost' with the IP of your compromised proxy host if running remotely. After editing, verify the config by running a simple proxied command like 'proxychains curl ifconfig.me' to confirm IP masking. If the proxy is unreachable, the command will fail with connection errors.

### Step 2: Scan Target via Proxied Nmap

**Context**: Use Proxychains to execute an Nmap TCP connect scan on an internal target IP, routing through the configured proxy to discover open ports and services without direct exposure. This verifies the pivot and gathers intel on the target.

**Command** ([[commands/proxychains-nmap-tcp-connect-scan]]):

```bash
proxychains nmap -sT $_TARGET_IP
```

> The -sT flag performs a full TCP handshake scan, which is reliable but detectable. Proxychains will prepend proxy routing, potentially showing [ProxyChains] logs for each connection attempt. If successful, Nmap will report ports as if scanning from the proxy's perspective; failures may indicate proxy instability or firewall blocks on the target.
