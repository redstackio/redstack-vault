---
tags:
  - xss
  - javascript-execution
  - reply-trigger
type: procedure
tools:
  - '[[tools/Chrome]]'
  - '[[tools/Chromium]]'
  - '[[tools/Opera]]'
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
updated_at: '2025-12-14T03:16:30.682Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 8f65dd34-9bda-4e77-ac04-202e6614977f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Victim-Reply

## Summary

This procedure simulates the victim accessing the malicious message and replying, causing the unsanitized original content to be quoted into the reply form, executing the injected JavaScript in the victim's browser.

## Description

The victim logs into Concrete CMS, views the inbox at `index.php/account/messages`, opens the malicious PM (sanitized, no execution), and selects 'Reply' from the dropdown. The reply form at `index.php/account/messages/write/{sender_id}` auto-quotes the original under '------- Original Message -------' without escaping, allowing the payload's `</textarea><script>...</script>` to close the form element and run the JS, which creates an img tag to exfiltrate cookies to the attacker's server.

## Requirements

1. Target user credentials (for simulation)
2. Malicious message in target's inbox
3. Browser supporting JS (e.g., Chrome v59)

## Defense

Defensive measures and detection strategies:

- Implement HTML entity encoding for all quoted content in forms
- Add client-side validation to detect tag mismatches in textareas
- Use browser dev tools or WAF to block unexpected script injections

## Objectives

1. Load the reply form with unsanitized quote
2. Execute payload for client-side compromise
3. Initiate data exfiltration

## Instructions

### Step 1: Authenticate as Victim

**Context**: Log in as the target user to access messages.

Use [[tools/Chrome]] or [[tools/Chromium]] to login and go to `index.php/account/messages`.

**Expected Output**: Inbox loads with malicious message listed.

### Step 2: View Malicious Message

**Context**: Open the message; confirm sanitization.

Click to view; payload displays as text, no JS runs.

**Expected Output**: Safe view of content.

### Step 3: Initiate Reply

**Context**: Trigger the vulnerable quoting.

Select 'Reply' from dropdown; form loads with quoted original.

**Expected Output**: JS executes; network tab shows request to attacker's URL with cookies.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome]]
- [[tools/Chromium]]
- [[tools/Opera]]

## Tags

- xss
- javascript-execution
- reply-trigger
