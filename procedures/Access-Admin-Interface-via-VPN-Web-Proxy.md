---
id: proc-uuid-5
tags:
  - web-proxy
  - admin-access
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands:
  - '[[commands/access-vpn-admin-proxy]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Protocol Tunneling]]'
updated_at: '2025-12-14T17:31:52.993Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Protocol Tunneling]]'
---
# Access Admin Interface via VPN Web Proxy

## Summary

Use the VPN's web proxy to reach the internal admin panel at https://0/admin/ post-login.

## Description

After VPN login, the proxy allows forwarding to localhost services, exposing the post-auth admin interface for further exploitation.

## Requirements

1. Active VPN session
2. Proxy enabled in VPN config

## Defense

Defensive measures and detection strategies:

- Restrict proxy to non-admin paths
- Authenticate proxy requests
- Monitor internal URL access

## Objectives

1. Load admin panel
2. Prepare for credential capture
3. Chain to injection

## Instructions

### Step 1: Navigate to Admin URL

**Context**: Use proxy to access internal admin.

Execute [[commands/access-vpn-admin-proxy]]:

```bash
curl -b "vpn_session=active" https://vpn.example.com/proxy/https/0/admin/
```

> Loads admin login page.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]]

### Techniques

- [[Protocol Tunneling]]

### Sub-Techniques


## Commands Used

- [[commands/access-vpn-admin-proxy]]

## Tools Used


## Tags

- web-proxy
- admin-access
