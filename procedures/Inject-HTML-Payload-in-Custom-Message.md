---
tags:
  - xss
  - html-injection
  - payload
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.002]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 72f3deec-269e-4df8-8b65-f7b0c6db55f9
created_at: '2025-12-14T17:33:24.145Z'
updated_at: '2025-12-14T17:33:24.145Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.002]]'
---
# Inject-HTML-Payload-in-Custom-Message

## Summary

This procedure exploits the lack of HTML sanitization in Mattermost's custom invitation message field to insert malicious payloads that render in emails, facilitating phishing.

## Description

The vulnerability stems from insufficient escaping in the guest invite custom message, allowing arbitrary HTML like links and inputs to be injected and executed in the recipient's email client. This can trick users into clicking phishing links or submitting credentials via injected forms, potentially leading to account takeover. Prerequisites include the prepared invite form from prior setup.

## Requirements

1. Access to the guest invite form with custom message field visible
2. Knowledge of target phishing domain (e.g., evil.com)
3. Web browser for input

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs in email templates using HTML entity encoding
- Use content security policies or email-safe rendering
- Log and alert on invites with script-like content

## Objectives

1. Insert executable HTML without rejection
2. Craft payload for phishing or XSS
3. Enable malicious interaction in emails

## Instructions

### Step 1: Access Custom Message Field

**Context**: Locate the vulnerable input area in the invite form.

Scroll to the "Set a custom message" section in the UI.

> Field is editable and accepts multi-line input.

### Step 2: Enter Malicious Payload

**Context**: Input HTML that will render unsafely in the email.

Enter the following in the field: `<a href=evil.com>click</a><input type=x>`.

> The payload is stored without sanitization; no errors occur.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[T1566.002]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[html-injection]]
- [[payload]]
