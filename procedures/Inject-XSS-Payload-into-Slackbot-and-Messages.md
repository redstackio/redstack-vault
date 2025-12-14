---
id: proc-uuid-1
tags:
  - xss
  - injection
  - slackbot
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
updated_at: '2025-12-14T03:15:47.443Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject XSS Payload into Slackbot and Messages

## Summary

This procedure injects a malicious SVG payload with an onload JavaScript handler into Slackbot messages to test storage without proper sanitization enabling stored XSS.

## Description

In Slack's messaging system user-supplied content in slackbot interactions is not adequately sanitized allowing SVG elements with onload attributes to execute JavaScript when rendered. This step focuses on direct message injection to establish persistence. Prerequisites include an authenticated Slack session. Expected outcome is payload storage visible in message history ready for triggering.

## Requirements

1. Authenticated access to a Slack workspace with messaging permissions
2. Web browser for manual input
3. Knowledge of basic HTML/SVG syntax for payload crafting

## Defense

Defensive measures and detection strategies:

- Implement strict Content Security Policy (CSP) to block inline JavaScript execution
- Sanitize all user inputs by parsing and stripping dangerous attributes like onload in SVG
- Monitor for anomalous JavaScript prompts or alerts in browser consoles

## Objectives

1. Store malicious payload in slackbot conversation
2. Verify non-sanitized reflection in message rendering
3. Prepare for cross-context execution on page refresh

## Instructions

### Step 1: Craft and Enter Payload in Slackbot

**Context**: Open a direct message with slackbot and input the payload to simulate user interaction.

No specific command as this is browser-based; manually enter:

```html
<img class="emoji" alt="😯" src="x" /><svg onload=prompt(document.domain)>
```

> This payload uses a benign emoji image to mask the SVG which executes prompt(document.domain) on load revealing the domain if successful.

### Step 2: Submit and Observe Storage

**Context**: Send the message and check if it persists without errors.

Manually submit the message in the chat input.

> Expected output: Message appears in history with payload intact no immediate execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[injection]]
