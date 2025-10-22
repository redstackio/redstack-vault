---
id: 0d401f82-835e-40f0-aa20-8183d8cfe1b5
name: Dynamic Port Forwarding with an SSH SOCKS Proxy
type: procedure
verified: false
submitted: false
created_at: '2019-10-19T03:53:12.563527+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Connection Proxy|T1090 - Connection Proxy]]'
platforms:
- Linux
- Windows
tags:
- '[[Network]]'
- '[[Pivot]]'
- '[[tunnel]]'
commands:
- '[[Proxychains Redirect an Application''s Network Traffic Through a SOCKS Proxy]]'
- '[[SSH Dynamic Port Forwarding Through a Remote Host]]'
---

# Dynamic Port Forwarding with an SSH SOCKS Proxy

## Summary

OpenSSH is typically configured to allow TCP port forwarding. This allows authenticated SSH users to forward local ports on the target to the user's local machine, potentially bypassing the system's firewall and exposing services which are only set to listen on other interfaces, for example the loo

## Description

# Description

OpenSSH is typically configured to allow TCP port forwarding. This allows authenticated SSH users to forward local ports on the target to the user's local machine, potentially bypassing the system's firewall and exposing services which are only set to listen on other interfaces, for example the loopback (127.0.0.1). SSH dynamic port forwarding can also be used, potentially exposing not only the local ports of the target, but also local networks. This vulnerability exists even if OpenSSH is configured to only allow restrictive shells, such as SFTP or Python interactive shell.

# Instructions

1. Connect to the target SSH server using dynamic port forwarding. If using dynamic port forwarding with proxychains, use port 9050 as that is the default SOCKS4 port set in /etc/proxychains.conf.

**Command** ([[SSH Dynamic Port Forwarding Through a Remote Host]]):

```bash
ssh -f -N -D $_PORT $_USERNAME@$_TARGET_IP
```

2. a) Use proxychains to open a program (Firefox, curl, Nmap, etc), and forward the traffic through a SOCKS5 proxy.

**Command** ([[Proxychains Redirect an Application's Network Traffic Through a SOCKS Proxy]]):

```bash
proxychains $_PROGRAM
```

2. b) Burp Suite can also be configured to connect to a SOCKS proxy instead of using proxychains. Simply enter the proxy information in Burp under `User Options > SOCKS Proxy`

- SOCKS Proxy Host: 127.0.0.1

- SOCKS Proxy Port: 9050

## Platforms

- Linux
- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Connection Proxy|T1090 - Connection Proxy]]

## Commands Used

- [[Proxychains Redirect an Application's Network Traffic Through a SOCKS Proxy]]
- [[SSH Dynamic Port Forwarding Through a Remote Host]]

## Tags

- [[Network]]
- [[Pivot]]
- [[tunnel]]
