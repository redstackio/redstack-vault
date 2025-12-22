---
id: p-trick-victim-click
tags:
  - social-engineering
  - csrf
  - phishing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.001]]'
updated_at: '2025-12-14T17:27:15.577Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.001]]'
---
# Trick Victim into Clicking Link to Trigger Action

## Summary

This procedure uses social engineering to deliver the crafted malicious URL to an authenticated victim on m.ok.ru, triggering the CSRF-bypassed action (e.g., photo deletion) upon interaction like clicking 'cancel' in the repost dialog.

## Description

The attack relies on the victim's session to authenticate the request. Share the URL via email, chat, or social media, disguising it as a benign repost link. When opened on m.ok.ru, it presents a dialog; any click (e.g., cancel) executes the st.rtu payload. This leads to unauthorized data modification without direct access to victim credentials.

## Requirements

1. Crafted malicious URL from prior procedure
2. Communication channel to victim (e.g., email, messaging app)
3. Victim authenticated on m.ok.ru

## Defense

Defensive measures and detection strategies:

- Educate users on suspicious links and dialog interactions
- Implement referrer checks and same-site cookies
- Monitor for rapid unauthorized actions post-link clicks

## Objectives

1. Induce victim to open and interact with the URL
2. Execute the embedded action silently
3. Confirm impact (e.g., photo deleted)

## Instructions

### Step 1: Distribute the Link

**Context**: Share the URL in a convincing context, e.g., "Check out this repost about your photo."

Embed in HTML: <a href="MALICIOUS_URL">Click here</a>

> Send via email or message; ensure victim is logged in.

### Step 2: Verify Execution

**Context**: Monitor for success by checking if the photo is deleted (if observable) or via victim reports.

No command; observe account changes or use a test account.

> Success: Action completes on 'cancel' click without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[T1566.001]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[social-engineering]]
- [[Phishing]]
