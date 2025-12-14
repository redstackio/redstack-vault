---
id: proc-uuid-2
tags:
  - dns-spoofing
  - hosts-file
  - cross-origin
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/add-hosts-entry]]'
verified: false
platforms:
  - Linux
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T17:30:26.621Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Configure-Local-DNS-Resolution-for-Cross-Origin-Simulation

## Summary

This procedure modifies the local /etc/hosts file to map a domain like a.com to 127.0.0.1, enabling simulation of cross-origin redirects in a controlled local environment for vulnerability testing.

## Description

To mimic a cross-origin redirect without relying on real DNS, this adds an entry to /etc/hosts, ensuring that the redirect target resolves locally. This is crucial for PoCs involving HTTP clients like undici, where origin differences trigger security checks. Requires sudo access; reversible by removing the entry.

## Requirements

1. Sudo privileges for editing /etc/hosts
2. Unix-like system (Linux/macOS)
3. Basic text editor or echo command access

## Defense

Defensive measures and detection strategies:

- Regularly audit /etc/hosts for unauthorized changes
- Use DNSSEC to prevent local overrides in production
- Monitor system logs for hosts file modifications

## Objectives

1. Force local resolution of external-looking domains
2. Enable isolated testing of cross-origin behaviors
3. Validate setup before executing client requests

## Instructions

### Step 1: Add Hosts Entry

**Context**: Append the mapping to /etc/hosts to simulate cross-origin.

**Command** ([[commands/add-hosts-entry]]):
```bash
echo "127.0.0.1 a.com" | sudo tee -a /etc/hosts
```

> Adds the line to /etc/hosts. Expected output: The echoed line, confirming addition.

### Step 2: Verify Resolution

**Context**: Test that the domain now resolves to localhost.

**Command** (ping test):
```bash
ping -c 1 a.com
```

> Should resolve to 127.0.0.1 and ping successfully.

### Step 3: Clean Up (Optional)

**Context**: Remove the entry after testing to restore normal resolution.

**Command** (remove line):
```bash
sudo sed -i '/a.com/d' /etc/hosts
```

> Deletes the line. Expected output: No output if successful.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[System Information Discovery]] System Information Discovery

### Sub-Techniques


## Commands Used

- [[commands/add-hosts-entry]]

## Tools Used


## Tags

- dns-spoofing
- hosts-file
- cross-origin
