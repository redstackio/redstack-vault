---
tags:
  - dns-mapping
  - hosts-file
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/add-hosts-entry]]'
verified: false
platforms:
  - Linux
  - macOS
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:29:09.545Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: ad0ece20-a2c8-48c0-9759-f1aa1fc1f21f
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Configure-DNS-Mapping

## Summary

This procedure configures local DNS resolution by adding an entry to the /etc/hosts file, mapping a custom domain to localhost for simulating cross-origin redirects in vulnerability testing.

## Description

To test the undici redirect behavior without relying on external DNS, map 'a.com' to 127.0.0.1. This ensures the redirect target is local, allowing traffic capture on a specific port. Requires sudo access for hosts file modification.

## Requirements

1. Administrative (sudo) privileges
2. Access to /etc/hosts file
3. Basic text editor or echo command

## Defense

Defensive measures and detection strategies:

- Monitor /etc/hosts for unauthorized modifications
- Use endpoint detection tools to alert on hosts file changes
- Implement DNSSEC for production environments to prevent spoofing

## Objectives

1. Redirect traffic to local listener for controlled testing
2. Simulate cross-origin without external network access
3. Verify domain resolution post-configuration

## Instructions

### Step 1: Add Hosts Entry

**Context**: Append the mapping to /etc/hosts to resolve a.com locally.

**Command** ([[commands/add-hosts-entry]]):
```bash
sudo echo "127.0.0.1 a.com" >> /etc/hosts
```

> Adds the line to the hosts file. Expected output: No output if successful; verify with cat /etc/hosts.

### Step 2: Verify Mapping

**Context**: Test resolution to confirm the change.

**Command** (ping test):
```bash
ping -c 1 a.com
```

> Pings the domain. Expected output: PING a.com (127.0.0.1) with local responses.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques


## Commands Used

- [[commands/add-hosts-entry]]

## Tools Used


## Tags

- dns-mapping
- hosts-file
