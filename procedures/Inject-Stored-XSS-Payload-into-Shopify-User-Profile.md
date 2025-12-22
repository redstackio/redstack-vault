---
id: proc-inject-shopify-xss-profile
name: Inject-Stored-XSS-Payload-into-Shopify-User-Profile
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:37.560Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - stored-xss
  - injection
platforms:
  - Web
commands: []
tools: []
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Inject-Stored-XSS-Payload-into-Shopify-User-Profile

## Summary

This procedure involves injecting a malicious JavaScript payload into the First Name and Last Name fields of a Shopify account profile, exploiting insufficient input sanitization to store the payload for later reflection as stored XSS.

## Description

In the Shopify ecosystem, user profile fields on the accounts page are not properly sanitized, allowing attackers with account access to insert XSS payloads. These payloads are then reflected without encoding on partner-related pages, enabling arbitrary JavaScript execution in the victim's browser context. This is particularly dangerous in authenticated sessions, potentially leading to session hijacking or data exfiltration. The procedure requires a valid Shopify account and targets the web-based account settings interface.

## Requirements

1. Valid authenticated session to https://accounts.shopify.com/account
2. Browser access to modify form fields
3. Knowledge of effective XSS payloads (e.g., for testing or exploitation)

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization on all user profile fields using libraries like DOMPurify
- Enforce Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous JavaScript execution in browser logs or via WAF rules targeting common XSS patterns

## Objectives

1. Persist malicious payload in user profile without triggering immediate errors
2. Set up for reflection in downstream pages like partners dashboard
3. Achieve stored XSS for cross-user impact

## Instructions

### Step 1: Access Account Settings

**Context**: Log in to the Shopify account and navigate to the profile editing section to prepare for payload injection.

Navigate to https://accounts.shopify.com/account in your browser and ensure you are authenticated.

### Step 2: Inject XSS Payload

**Context**: Modify the First Name and Last Name fields with a payload that evades basic filters, such as an onerror-based script or simple alert for testing.

Enter the following payload in both fields: `<img src=x onerror=alert('XSS Triggered')>` or `<script>alert(document.domain)</script>`. Click save to persist the changes.

> This step stores the payload server-side without execution, as the fields accept HTML-like input.

### Step 3: Verify Storage

**Context**: Confirm the payload is saved by reloading the profile page and checking if the fields retain the injected content.

Reload https://accounts.shopify.com/account and inspect the displayed names; the payload should appear unescaped.

> Expected output: Profile shows the injected script tags or attributes without sanitization.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[injection]]
