---
tags:
  - kaspersky
  - setup
  - hosts-file
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/edit-windows-hosts]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Disable or Modify Tools]]'
updated_at: '2025-12-14T17:28:58.620Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 3d613929-9f9a-4624-b340-039d74ccc599
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Disable or Modify Tools]]'
---
# Setup-Kaspersky-Test-Environment

## Summary

This procedure configures the target environment by enabling specific Kaspersky features, modifying the Windows hosts file to simulate a trigger domain for URL Advisor, and verifying the browser extension is active, preparing for the postMessage exploitation.

## Description

In the attack scenario, the target runs Windows with Kaspersky Internet Security 19.0.0.1088 installed. The procedure ensures Anti-Banner and Private Browsing are enabled to demonstrate disablement later. The hosts file is edited to map 'www.google.example.com' to localhost, as URL Advisor activates only for hostnames starting with 'www.google.'. The Kaspersky Protect extension must be enabled in Firefox or Chrome. This setup isolates the exploit to a controlled local environment and requires administrator privileges for the hosts edit. Expected outcomes include a ready-to-trigger setup where navigation to the fake domain invokes the vulnerable URL Advisor frame.

## Requirements

1. Windows OS with administrator access
2. Kaspersky Internet Security 19.0.0.1088 installed
3. Firefox 64+ or Chrome 71+ browser
4. Local network access to localhost

## Defense

Defensive measures and detection strategies:

- Monitor hosts file modifications via file integrity monitoring tools like Sysmon
- Restrict extension installations and enable browser sandboxing
- Use endpoint detection to alert on AV configuration changes

## Objectives

1. Enable testable Kaspersky features for exploitation verification
2. Simulate a legitimate URL Advisor trigger domain
3. Confirm extension readiness without alerting defenses

## Instructions

### Step 1: Enable Kaspersky Features

**Context**: Turn on Anti-Banner and Private Browsing to establish a baseline for later disablement.

Access Kaspersky settings via the system tray icon or application interface and toggle the features on.

**Expected Output**: Features listed as enabled in the settings panel.

### Step 2: Modify Hosts File

**Context**: Map a fake domain to localhost to trick URL Advisor into activating on the malicious page.

**Command** ([[commands/edit-windows-hosts]]):

Manual edit (run as administrator):

```bash
echo "127.0.0.1 www.google.example.com" >> %WINDIR%\sysnative\drivers\etc\hosts
```

> This appends the mapping to the hosts file. Verify with `ping www.google.example.com` resolving to 127.0.0.1. Expected output: Domain resolves locally without DNS query.

### Step 3: Verify Extension

**Context**: Ensure the Kaspersky Protect extension is active in the browser.

Navigate to browser extensions settings (chrome://extensions/ or about:addons in Firefox) and confirm the extension is enabled.

**Expected Output**: Extension toggle set to 'On'.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Disable or Modify Tools]] Disable or Modify Tools

### Sub-Techniques

-

## Commands Used

- [[commands/edit-windows-hosts]]

## Tools Used

-

## Tags

- [[kaspersky]]
- [[setup]]
- [[hosts-file]]
