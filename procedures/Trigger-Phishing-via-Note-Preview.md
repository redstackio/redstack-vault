---
tags:
  - phishing
  - social-engineering
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Android
techniques:
  - '[[Phishing]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: a44bc75d-d8f9-4bb1-a774-4f6f0027d68b
created_at: '2025-12-14T17:24:42.442Z'
updated_at: '2025-12-14T17:24:42.442Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Trigger-Phishing-via-Note-Preview

## Summary

This procedure involves sharing the malicious note and inducing the victim to interact with the rendered form in Simplenote's preview mode, leading to credential submission.

## Description

Once shared, the victim opens the note on Android, switches to preview, and the unsanitized HTML form renders. Submission sends data to the attacker, exploiting trust in shared notes for phishing.

## Requirements

1. Obfuscated malicious note ready
2. Sharing method (email, chat, link)
3. Victim with vulnerable Simplenote app

## Defense

Defensive measures and detection strategies:

- Verify note sources before preview
- Use network proxies to block external form submissions
- Log app network activity for anomalies

## Objectives

1. Deliver note to victim
2. Induce preview and form interaction
3. Capture submitted credentials

## Instructions

### Step 1: Share Note

**Context**: Distribute via social engineering.

Export or link the note and send: "Check this important note: [link]"

> Expected: Victim receives and opens in app.

### Step 2: Monitor Victim Action

**Context**: Wait for preview trigger.

Victim switches to preview; form appears.

> Expected: No warnings; form interactive.

### Step 3: Receive Data

**Context**: Collect exfiltrated info.

Check server logs for POST data.

> Expected: Email/password pairs logged.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Phishing]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[social-engineering]]
