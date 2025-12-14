---
tags:
  - xss
  - payload-injection
  - slack
type: procedure
tools:
  - '[[tools/Slack-Self-XSS-Demonstration-Video]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:31.796Z'
sub_techniques: []
id: 3db56527-5335-4477-a893-b05b95c25507
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Enter-XSS-Payload-in-Slack-Post

## Summary

This procedure involves typing a malicious HTML/JavaScript payload into the Slack post editor to set up for self-XSS execution.

## Description

The payload `<svg onload=alert(domain)>` is entered directly into the text area. This step targets the post editor in Slack's web interface, where initial input is not sanitized. The expected outcome is the payload being accepted without execution until formatting and rendering occur. This is part of a self-XSS chain affecting only the user's browser.

## Requirements

1. Open Slack post creation editor
2. Keyboard or copy-paste capability
3. No special permissions needed

## Defense

Defensive measures and detection strategies:

- Client-side input validation to flag suspicious HTML tags
- Content security policy (CSP) to restrict script execution

## Objectives

1. Inject the exact XSS payload into the editor
2. Ensure payload integrity for later execution
3. Avoid premature triggering

## Instructions

### Step 1: Input the Payload

**Context**: Place the malicious code in the editor text area.

No command required; perform the following UI interaction:

Type `<svg onload=alert(domain)>` into the post creation text area.

> The text appears in the editor as plain input, ready for formatting. Verify by checking the text matches exactly.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Slack-Self-XSS-Demonstration-Video]]

## Tags

- [[xss]]
- [[payload-injection]]
