---
id: proc-uuid-003
tags:
  - phishing
  - social-engineering
  - electron
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - macOS
  - Desktop
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:28.094Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Lure-Victim-to-View-or-Edit-Page-in-WordPress-Desktop

## Summary

This procedure involves social engineering to trick a WordPress.com user into opening a malicious page in the desktop app, triggering the iframe exploit and subsequent RCE via the NFS-hosted app.

## Description

The attacker invites the victim to collaborate on the malicious page or sends a lure link. When the victim uses WordPress Desktop to view or edit, the app loads the iframe, executes JS, and calls shell.openExternal on the file:// URL, launching the remote .app. Prerequisites: Victim's WordPress.com access and desktop app usage. Expected outcome: Arbitrary code execution on victim's macOS system.

## Requirements

1. Target's WordPress.com username/email for invitation
2. Malicious page already published
3. NFS app hosted and accessible

## Defense

Defensive measures and detection strategies:

- User training on phishing and unexpected invites
- App sandboxing to prevent external executions
- Logging of URL opens in desktop applications

## Objectives

1. Gain victim interaction with malicious content
2. Trigger exploitation in client-side app
3. Achieve full RCE on endpoint

## Instructions

### Step 1: Send Invitation or Lure

**Context**: Use WordPress.com features to involve the victim.

In WordPress.com, invite the user to edit the page via their email. Alternatively, send a phishing email with the page link, urging use of the desktop app.

> Example invite message: "Please review and edit this page in WordPress Desktop."

### Step 2: Monitor Execution

**Context**: Confirm the exploit triggers on victim side.

Once victim opens the page in desktop app, the payload executes automatically. Verify via backdoor in .app (e.g., exfil data) or observed effects like Calculator opening.

> Success if commands from .app run, e.g., /etc/hosts contents accessible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[Phishing]]
- [[lure]]
- [[client-execution]]
