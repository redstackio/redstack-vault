---
id: uuid-configure-hosts
tags:
  - domain-spoofing
  - hosts-file
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Linux
  - Windows
  - macOS
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:52:21.052Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Configure-Hosts-File-for-Domain-Mapping

## Summary

This procedure modifies the system's hosts file to map a malicious domain like roolee.co to localhost, enabling local simulation of a subdomain that tricks Shopify's origin check via substring matching.

## Description

Shopify's vulnerability relies on indexOf checks failing for origins without trailing slashes, allowing 'https://roolee.co' to partially match 'https://roolee.com'. By editing /etc/hosts (Linux/macOS) or %Windir%\System32\drivers\etc\hosts (Windows), the attacker redirects the domain to 127.0.0.1. This requires admin privileges and affects only the local machine.

## Requirements

1. Administrator or root access to edit hosts file
2. Text editor like nano or notepad
3. Knowledge of target domain (e.g., roolee.co for roolee.com shop)

## Defense

Defensive measures and detection strategies:

- Regularly audit hosts file changes via integrity monitoring (e.g., Tripwire)
- Use endpoint protection to alert on hosts file modifications

## Objectives

1. Redirect malicious domain to local attacker-controlled server
2. Enable HTTPS access without external hosting
3. Validate resolution before server start

## Instructions

### Step 1: Edit Hosts File

**Context**: Add the mapping entry.

On Linux/macOS:

```bash
sudo nano /etc/hosts
```

Add line: 127.0.0.1 roolee.co

On Windows: Open as admin and add the line.

> Expected: File saves without errors.

### Step 2: Verify Mapping

**Context**: Test domain resolution.

```bash
ping roolee.co
```

> Expected: Pings 127.0.0.1; success if local loopback responds.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- domain-spoofing
- hosts-file
