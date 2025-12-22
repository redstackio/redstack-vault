---
id: proc-inject-xss-redirect-001
tags:
  - xss
  - payload-injection
  - javascript-uri
  - data-uri
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
updated_at: '2025-12-14T03:15:52.892Z'
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
# Inject-XSS-Payload-into-Redirect

## Summary

This procedure details the creation of a malicious URL redirect in Shopify's admin panel by injecting XSS payloads via javascript: or data: URI schemes, exploiting the absence of input sanitization.

## Description

The Shopify admin's 'Add URL Redirect' form at https://[shop-name].myshopify.com/admin/redirects fails to validate or whitelist redirect URL schemes, allowing injection of executable JavaScript. An attacker specifies an old path (e.g., /test) and sets the redirect to a payload like javascript:alert(document.domain) for proof-of-concept or a base64-encoded data: URI for cookie theft and redirection. Upon saving, a redirect link is generated, setting up execution. This requires admin access and targets the browser context for high-impact attacks like session hijacking.

## Requirements

1. Access to the redirects admin page (from prior procedure)
2. Knowledge of XSS payload encoding (e.g., base64 for data: URIs)
3. Target old path that doesn't conflict with existing redirects

## Defense

Defensive measures and detection strategies:

- Enforce strict URL scheme whitelisting (e.g., only http/https)
- Sanitize and validate all redirect inputs server-side
- Log and alert on suspicious redirect creations (e.g., non-standard schemes)
- Use Content Security Policy (CSP) to block inline JavaScript execution

## Objectives

1. Bypass URL validation to embed executable code
2. Generate a functional malicious redirect link
3. Prepare for payload execution without immediate detection

## Instructions

### Step 1: Initiate Redirect Creation

**Context**: Open the form to input redirect details.

Click 'Add URL Redirect' on the admin page.

> Form fields for 'Old path' and 'Redirect to' appear.

### Step 2: Enter Malicious Payload

**Context**: Inject the XSS scheme into the redirect URL.

Set 'Old path' to /malicious-test. For the 'Redirect to' field, enter `javascript:alert(document.domain)` or the advanced payload `data:text/html;base64,PHNjcmlwdD5hbGVydCgiY29va2llIHN0ZWFsOiAiK2RvY3VtZW50LmNvb2tpZSk7d2luZG93LmxvY2F0aW9uLmhyZWY9J2h0dHA6Ly93d3cuZ29vZ2xlLmNvbSc7PC9zY3JpcHQ+`.

> No errors occur if validation is bypassed.

### Step 3: Save Redirect

**Context**: Persist the injection to generate the link.

Click 'Save' to create the redirect.

> A new entry appears in the list with the full redirect URL (e.g., https://[shop].myshopify.com/malicious-test).

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
- [[payload-injection]]
