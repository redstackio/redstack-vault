---
tags:
  - xss
  - sharing
  - nextcloud
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:20.810Z'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
id: 9190d134-3b8e-4cc4-89ff-53e2c5438c16
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Share-Malicious-Folder-with-Victim

## Summary

This procedure shares the folder containing the stored XSS payload with a target victim using Nextcloud's built-in sharing feature, delivering the exploit without raising suspicion.

## Description

Nextcloud's sharing mechanism allows authenticated users to share folders with others, preserving the malicious directory name. This step propagates the stored payload to the victim's account, setting up the conditions for execution in their browser session.

## Requirements

1. Ownership of the malicious folder
2. Knowledge of victim's Nextcloud username or email
3. Authenticated session

## Defense

Defensive measures and detection strategies:

- Review shared folders for suspicious names before accepting
- Implement sharing audits and notifications for admins
- Block shares from untrusted users

## Objectives

1. Deliver the malicious folder to victim
2. Maintain payload integrity during share
3. Enable victim access without alerting

## Instructions

### Step 1: Select the Malicious Folder

**Context**: Locate the folder in your file manager.

Navigate to Files and find the folder named `<img src=x onerror=alert(1)>`.

### Step 2: Initiate Sharing

**Context**: Use the Share UI to target the victim.

Click the Share icon (person silhouette) on the folder. In the dialog, enter the victim's username or email and select view permissions.

### Step 3: Confirm and Notify

**Context**: Finalize the share to notify the victim.

Click Share; the victim will receive an invitation or see it in their shared items.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- nextcloud
- folder-sharing
