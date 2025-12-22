---
tags:
  - social-engineering
  - slack
type: procedure
tools:
  - '[[tools/HTTP-Proxy]]'
  - '[[tools/HTTPS-Enabled-Server]]'
  - '[[tools/Developer-Tools]]'
  - '[[tools/Email-Client]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/open-calculator-macos]]'
  - '[[commands/open-calculator-windows]]'
  - '[[commands/exec-shell-command-nodejs]]'
  - '[[commands/alert-localstorage]]'
platforms:
  - Desktop
  - Electron
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 48adc966-0a35-4521-8fa1-eb79bd4259ca
created_at: '2025-12-11T06:10:22.517Z'
updated_at: '2025-12-11T06:10:22.517Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Share Injected Slack Post with Victim

## Summary

This procedure shares the malicious Slack Post to trick the victim into clicking and triggering the redirect.

## Description

Share in a channel or directly; the injected image redirects to the attacker site in _top frame.

## Requirements

1. Access to shared Slack channel or DM.
2. Injected Post ready.
3. Enticing content to prompt click.

## Defense

Defensive measures and detection strategies:

- Educate users on suspicious links.
- Validate redirects in app.

## Objectives

1. Deliver payload to victim.
2. Initiate interaction.
3. Lead to RCE trigger.

## Instructions

### Step 1: Share Post

**Context**: Use Slack UI to share.

No command; perform via interface.

> Expected: Victim views Post and clicks image.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[social-engineering]]
- [[slack]]
