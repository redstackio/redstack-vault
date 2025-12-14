---
tags:
  - social-engineering
  - phishing
  - slack
  - android
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Android
  - Web
techniques:
  - '[[T1566.001]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 4b8ae071-dcaa-4a71-9a67-9dbf2a782315
created_at: '2025-12-14T17:31:42.984Z'
updated_at: '2025-12-14T17:31:42.984Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.001]]'
---
# Induce Victim to Open File on Android Device

## Summary

This procedure uses social engineering within a Slack workspace to convince the victim to download and open a malicious file using the Slack Android app, activating the directory traversal vulnerability.

## Description

Reported in HackerOne #1378889, the vulnerability requires user interaction: the victim must open the uploaded file (>1MB) on Android, where the app's file handling lacks path validation, allowing OS-level traversal. Attacker leverages workspace trust to prompt opening, ensuring the exploit chain proceeds without technical exploits beyond the upload.

## Requirements

1. Shared Slack workspace with victim
2. Uploaded crafted file from prior step
3. Victim using vulnerable Slack Android app version

## Defense

Defensive measures and detection strategies:

- Implement user training on verifying file sources in collaboration tools
- Use Slack's DLP features to flag suspicious interactions
- Monitor for unusual file open patterns in mobile app logs

## Objectives

1. Obtain victim interaction to trigger download/open
2. Confirm execution on Android platform
3. Minimize suspicion to ensure completion

## Instructions

### Step 1: Craft Enticing Message

**Context**: Use workspace context to socially engineer the open without raising alarms.

- Send the file link in a relevant conversation, e.g., "Hey, open this report on your phone for the charts"
- Target during work hours for higher engagement

### Step 2: Verify Interaction

**Context**: Prompt or follow up to ensure the victim opens the file on Android.

- Ask: "Did you see the file? Open it in the app"
- If needed, resend or escalate in group chat

**Expected Output**: Victim reports opening or no error; exploit triggers silently.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.001]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[social-engineering]]
- [[Phishing]]
- [[slack]]
- [[android]]
