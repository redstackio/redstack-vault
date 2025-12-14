---
tags:
  - phishing
  - email-delivery
  - electron
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1566.001]]'
updated_at: '2025-12-14T17:23:41.279Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: fcf682d0-7014-4f03-91de-7b4184f443d7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.001]]'
---
# Send-Malicious-Email-Attachment-via-HEY

## Summary

This procedure delivers a malicious .terminal file as an email attachment using the HEY macOS client, exploiting its failure to quarantine downloads for Gatekeeper bypass.

## Description

The Electron-based HEY app handles file uploads to the inbox without setting the com.apple.quarantine attribute, allowing attachments like .terminal files to execute without developer verification warnings. This targets victims using the HEY client, leading to RCE upon opening. Prerequisites: Access to a HEY-compatible email account and the crafted payload. Outcome: Victim receives and can download the file silently.

## Requirements

1. HEY macOS app installed and logged in
2. Malicious .terminal file prepared
3. Victim's email address

## Defense

Defensive measures and detection strategies:

- Train users to avoid opening unsolicited attachments
- Implement email gateway scanning for executable files
- Monitor app downloads for missing quarantine attributes using xattr commands

## Objectives

1. Deliver payload via trusted email channel
2. Exploit app-specific handling flaws
3. Ensure no immediate security alerts

## Instructions

### Step 1: Compose Email in HEY

**Context**: Use the HEY inbox to attach the file, leveraging the app's upload mechanism.

**Command** (App UI action; no CLI):

In HEY, create a new email, attach 'exploit.terminal', and send to victim.

> The upload bypasses quarantine; verify by checking xattr -l on downloaded file (should be empty).

### Step 2: Verify Delivery

**Context**: Confirm the attachment arrives intact in victim's HEY inbox.

**Command** (Optional check on victim side for testing):

```bash
xattr -l exploit.terminal
```

> Expected: No com.apple.quarantine output, confirming bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1566.001]] Phishing: Spearphishing Attachment

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[Phishing]]
- [[email-delivery]]
