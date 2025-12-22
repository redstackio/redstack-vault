---
id: ede28152-8003-4c7e-b2e4-6947d34a6bd5
name: proxychains-proxy-list-configuration
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:22.517186+00:00'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Linux
tags:
  - configuration
  - pivoting
validated: true
---

# proxychains-proxy-list-configuration

## Code

```bash
[ProxyList]
socks4 localhost 8080
```

## Description

This code snippet configures the [ProxyList] section in Proxychains' /etc/proxychains.conf file, specifying a SOCKS4 proxy for routing traffic. It is used to chain connections through a compromised host for network pivoting, enabling access to internal resources.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| IP (replace 'localhost') | IP address of the proxy server (compromised host) | 192.168.1.100 |
| PORT (replace '8080') | Port on which the SOCKS proxy is listening | 1080 |

## Usage

Append or replace the [ProxyList] section in /etc/proxychains.conf with this snippet, substituting the IP and port as needed. Then, prefix any command with 'proxychains' (e.g., proxychains nmap target). This is typically used after establishing a proxy on a pivoted host via SSH -D.

## Detection

- File integrity monitoring on /etc/proxychains.conf for unauthorized edits.
- Process monitoring for proxychains-ng executions or unusual SOCKS traffic from internal hosts.
- Log analysis for dynamic port forwarding in SSH logs.

## Related

- [[procedures/Network-Pivoting-with-Proxychains]]
- [[tools/Proxychains]]
