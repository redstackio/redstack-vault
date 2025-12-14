---
id: proc-003
tags:
  - hosts-file
  - dns-spoofing
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/edit-windows-hosts-file]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Dynamic Linker Hijacking]]'
updated_at: '2025-12-14T17:29:36.216Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Dynamic Linker Hijacking]]'
---
# Modify Windows Hosts File for Domain Redirect

## Summary

This procedure edits the Windows hosts file to map a fake Google domain to localhost, enabling the malicious page to load under a hostname that triggers Kaspersky's Web protection script injection.

## Description

By adding an entry for www.google.example.com to point to 127.0.0.1, navigation to this domain resolves locally to the HTTPS server. This tricks Kaspersky into injecting its protection script, which then becomes vulnerable to the interception exploit in the same JS context.

## Requirements

1. Administrator privileges on Windows
2. Text editor like Notepad
3. Local server running on port 5000

## Defense

Defensive measures and detection strategies:

- Protect hosts file with integrity monitoring
- Audit file changes via Windows Event Logs (ID 4656)
- Use DNS over HTTPS to bypass local hosts overrides

## Objectives

1. Redirect domain to local exploit server
2. Trigger Kaspersky script on Google-like hostname
3. Enable seamless payload delivery

## Instructions

### Step 1: Open Hosts File as Admin

**Context**: Gain elevated access to edit system file.

Run Notepad as administrator, then open %WINDIR%\sysnative\drivers\etc\hosts.

> Expected: File opens in editable mode without permission denial.

### Step 2: Add Entry and Save

**Context**: Insert the redirect mapping.

Execute [[commands/edit-windows-hosts-file]] by appending the line `127.0.0.1 www.google.example.com` to the file end. Save and close.

```bash
echo 127.0.0.1 www.google.example.com >> %WINDIR%\sysnative\drivers\etc\hosts
```

> Expected: File updated; verify with `ping www.google.example.com` showing 127.0.0.1.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Dynamic Linker Hijacking]] Hijack Execution Flow: Network Provider DLL Hijacking (adapted for DNS)

### Sub-Techniques


## Commands Used

- [[commands/edit-windows-hosts-file]]

## Tools Used


## Tags

- [[hosts-file]]
- [[dns-spoofing]]
