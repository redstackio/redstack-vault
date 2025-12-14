---
id: proc-inject-xss-store-name
tags:
  - xss
  - payload-injection
  - shopify
type: procedure
tools: []
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
updated_at: '2025-12-13T23:52:49.961Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-in-Store-Name

## Summary

This procedure injects a JavaScript payload into the Shopify Email app's store name field, exploiting lack of sanitization to store malicious code for later execution.

## Description

The stored XSS vulnerability arises from improper escaping of the store name when rendered in email templates. By entering a payload like an img tag with onerror, the attacker persists JavaScript that executes in the admin context upon template rendering. This targets Shopify web platforms and requires prior app configuration. Outcomes include payload storage without immediate execution.

## Requirements

1. Access to the template branding page (your-store.myshopify.com/admin/apps/shopify-email/template-branding)
2. Admin privileges on the Shopify store
3. Knowledge of basic XSS payloads

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user inputs in template rendering (e.g., use HTML entity encoding)
- Implement Content Security Policy (CSP) to restrict script execution in admin panels
- Log and monitor unusual inputs in configuration fields

## Objectives

1. Bypass input validation on store name field
2. Persist XSS payload in backend storage
3. Set up for triggered execution in admin context

## Instructions

### Step 1: Locate the Vulnerable Field

**Context**: Identify the store name input on the branding page.

No command required; use the UI:

- Ensure the template branding page is open
- Focus on the store name text input field

> Field should accept arbitrary text without immediate rejection.

### Step 2: Enter and Save Payload

**Context**: Craft and submit the XSS payload to store it unsanitized.

No command required; use the UI:

- Input: `'><img src=xx onerror=alert(document.domain)>`
- Click the Save button

> Save succeeds, storing the payload; no visible changes in UI but payload is persisted.

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
- [[stored-xss]]
