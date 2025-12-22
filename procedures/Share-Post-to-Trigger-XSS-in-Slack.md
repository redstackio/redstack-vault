---
id: uuid-for-proc3
tags:
  - xss
  - stored-xss
  - slack
  - sharing
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
updated_at: '2025-12-14T03:16:31.253Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Share-Post-to-Trigger-XSS-in-Slack

## Summary

This procedure shares a created post via direct message or team share to a victim with a malicious user name, triggering the stored XSS payload execution in the recipient's browser during menu rendering.

## Description

The share post menu in Slack renders user names in HTML without proper output encoding, allowing the stored payload to execute JavaScript in the victim's authenticated session. This leads to arbitrary code execution, potentially enabling session theft or data exfiltration. Requires the prior setup of a malicious name and post. The attack relies on the victim's interaction with the share interface.

## Requirements

1. Existing post from previous procedure
2. Victim user with malicious name configured
3. Authenticated session to initiate sharing

## Defense

Defensive measures and detection strategies:

- Sanitize and encode all user names in UI rendering, especially in dynamic menus
- Implement XSS filters and strict CSP headers
- Monitor for JavaScript errors or unexpected alerts in browser consoles via logging

## Objectives

1. Deliver the XSS payload via sharing interface
2. Achieve JavaScript execution in victim context
3. Enable follow-on attacks like session hijacking

## Instructions

### Step 1: Open Share Menu

**Context**: Access the sharing options for the created post.

In Slack, right-click or select the post and choose "Share" or navigate to the share interface.

### Step 2: Select Recipient

**Context**: Choose the direct message or team share option including the maliciously named user.

Search for and select the victim user or team; the name renders in the menu HTML.

> This triggers the `<img src=x onerror=alert(1)>` payload, executing alert(1) or custom JS.

### Step 3: Confirm Execution

**Context**: Verify the payload fires in the victim's view.

Have the victim open the shared post or menu; check for alert or console execution.

**Expected Output**: JavaScript alert or logged execution in browser dev tools.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss-trigger
- slack-share
- execution
