---
id: proc-uuid-001
tags:
  - mitm
  - hosts-file
  - simulation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/edit-hosts-file]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Adversary-in-the-Middle]]'
updated_at: '2025-12-14T17:28:12.475Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Simulate-MitM-via-Hosts-File-Modification

## Summary

This procedure simulates a Man-in-the-Middle (MitM) attack by modifying the Windows hosts file to redirect a legitimate domain like www.google.com to a controlled IP address, triggering certificate mismatches when accessed over HTTPS. It sets up the environment for exploiting UI vulnerabilities in security software like Kaspersky.

## Description

In a real attack on public WiFi, an attacker poisons DNS or ARP to redirect traffic. Here, local hosts file editing mimics this to force a certificate error on legitimate sites, allowing demonstration of clickjacking on warning pages. Requires admin privileges; tested on Windows with Kaspersky Internet Security.

## Requirements

1. Windows OS with administrative access
2. Text editor (e.g., Notepad) run as administrator
3. Target domain (e.g., www.google.com) and alternate IP (e.g., 93.184.216.34 for example.com)

## Defense

Defensive measures and detection strategies:

- Monitor hosts file changes via file integrity monitoring (e.g., Sysmon)
- Use DNSSEC to prevent poisoning in real MitM scenarios
- Educate users on certificate warnings and avoid public WiFi for sensitive sites

## Objectives

1. Redirect domain resolution to trigger SSL errors
2. Simulate network-level attack without external tools
3. Prepare for UI exploitation in security prompts

## Instructions

### Step 1: Open Hosts File as Administrator

**Context**: Gain elevated access to modify system DNS resolution.

**Command** ([[commands/edit-hosts-file]]):
```bash
# Run Notepad as administrator and open %WINDIR%\sysnative\drivers\etc\hosts
```

> Opens the file for editing; ensure no syntax errors to avoid resolution issues.

### Step 2: Add Redirection Entry

**Context**: Append the line to map the target domain to the attacker-controlled IP.

**Command** ([[commands/edit-hosts-file]]):
```bash
# Add: 93.184.216.34 www.google.com
```

> Saves the file; flush DNS cache if needed with `ipconfig /flushdns` for immediate effect.

### Step 3: Verify Redirection

**Context**: Confirm the simulation works before proceeding.

**Command**:
```bash
ping www.google.com
```

> Expected output: Pings resolve to 93.184.216.34 instead of Google's IP.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### Sub-Techniques


## Commands Used

- [[commands/edit-hosts-file]]

## Tools Used


## Tags

- mitm
- hosts-file
- simulation
