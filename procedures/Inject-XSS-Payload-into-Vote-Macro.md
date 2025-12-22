---
tags:
  - xss-injection
  - payload-craft
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
updated_at: '2025-12-14T03:46:26.685Z'
sub_techniques: []
id: 65b37f6f-5ab6-4b62-95d7-3e706e254ebd
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Vote-Macro

## Summary

This procedure details crafting and inserting a malicious JavaScript payload into the TopCoder wiki's vote macro to exploit insufficient sanitization, enabling stored XSS execution.

## Description

The vote macro processes user input without proper escaping, allowing closure of HTML tags and injection of script elements. In a browser-based attack scenario, the attacker uses the rich text editor to embed the payload, which remains dormant until triggered. Prerequisites include edit access; outcomes involve storing executable code that can steal cookies or perform other client-side actions when another user edits the page.

## Requirements

1. Access to wiki editor in rich text mode
2. Knowledge of payload syntax to break out of macro context
3. Browser compatibility (works in Firefox; may be disabled in Chrome)

## Defense

Defensive measures and detection strategies:

- Sanitize macro parameters with HTML entity encoding
- Validate input against whitelists for allowed characters
- Implement content security policy (CSP) to block inline scripts

## Objectives

1. Bypass macro sanitization using tag closure
2. Embed functional JavaScript without immediate detection
3. Ensure payload persistence in page content

## Instructions

### Step 1: Craft Payload

**Context**: Design the payload to close the macro and inject an onload script.

No specific command; construct manually:

Payload: {vote:What is your favorite vulnerability?} RCE SSRF XSS"><img src=X onerror=alert(document.domain)> {vote}

> This closes the attribute with ">, injects an img tag with onerror handler. Expected output: Payload ready for insertion.

### Step 2: Insert into Editor

**Context**: Place the payload in the page content via the rich text tab.

No specific command; paste into the editor field.

> Verify it appears as text without executing. Success if editor accepts it.

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
