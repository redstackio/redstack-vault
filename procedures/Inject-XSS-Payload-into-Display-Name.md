---
tags:
  - xss
  - payload-injection
  - stored-xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-05T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.108Z'
sub_techniques: []
id: 3508d2de-7570-43d1-b925-431938ac87f1
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Display-Name

## Summary

This procedure involves enabling the custom profile field in Bridge CMS and inserting a stored XSS payload into the display name, exploiting the lack of server-side sanitization to store malicious JavaScript.

## Description

Bridge CMS fails to properly escape user input in the display name field when the custom profile option is enabled. The payload, such as `p<script>alert('xss')</script>`, is stored in the database and later rendered in Twig templates using `user_display_name()|e('html')` concatenated with other content followed by `|raw`, which can bypass escaping. This step assumes account access from the prior procedure and targets self-XSS scenarios, with potential for broader impact in IE11.

## Requirements

1. Access to the /my/account page with editing permissions
2. Knowledge of XSS payloads compatible with the rendering context
3. No client-side blockers (though server-side is the key flaw)

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs server-side using strict escaping (e.g., htmlspecialchars in PHP)
- Implement Content-Security-Policy (CSP) headers to block inline scripts
- Log and validate unusual input patterns in profile fields

## Objectives

1. Enable custom profile to expose the vulnerable field
2. Insert executable JavaScript without immediate rejection
3. Store the payload for later rendering

## Instructions

### Step 1: Enable Custom Profile

**Context**: Activate the option that allows custom display name input.

Check the 'Custom Profile field option' checkbox on the account page.

> This unlocks the display name field for custom entry.

### Step 2: Enter XSS Payload

**Context**: Input the malicious script into the display name field.

Enter `p<script>alert('xss')</script>` in the display name input.

> The form accepts the input without sanitization; preview may show it benignly.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- injection
- twig
