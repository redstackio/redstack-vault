---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - xss
  - stored-xss
  - shopify
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:18.470Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-in-Shopify-Team-Invite

## Summary

This procedure exploits a stored XSS vulnerability in Shopify's partner dashboard by injecting a malicious JavaScript payload into the email field during team member invitations, allowing arbitrary code execution when any authorized user views the resulting invitation page.

## Description

The vulnerability stems from insufficient input validation and output encoding in the 'Invite owner' feature. The email parameter accepts arbitrary HTML and JavaScript, stores it without sanitization, and renders it unsafely on the invitation page (e.g., /invitations/{id}). This enables attackers with 'manage members' permissions to target other team members, including owners, potentially stealing session cookies or performing other client-side attacks. The exploit requires authenticated access but has medium impact due to permission gating.

## Requirements

1. Authenticated Shopify partner account with 'manage members' permissions.
2. Access to a web browser for manual interaction and payload testing.
3. Target Shopify partner organization ID (e.g., via URL: partners.shopify.com/{id}).

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and validation for email fields, rejecting non-email formats.
- Use output encoding (e.g., HTML entity encoding) when rendering user inputs on pages.
- Employ Content Security Policy (CSP) to restrict inline script execution.
- Monitor for anomalous JavaScript alerts or cookie access in browser logs.
- Audit invitation logs for suspicious email patterns containing HTML tags.

## Objectives

1. Store a malicious XSS payload in the invitation email field.
2. Trigger JavaScript execution on the invitation page to demonstrate impact like cookie theft.
3. Highlight the need for better input/output handling in web applications.

## Instructions

### Step 1: Authenticate and Access Dashboard

**Context**: Establish a session with necessary permissions to reach the vulnerable feature.

No specific command; manually log in at partners.shopify.com using valid credentials.

> Successful login grants access to team management.

### Step 2: Initiate Invitation and Inject Payload

**Context**: Open the invite form and insert the payload to bypass sanitization.

Enter the following payload in the email field: `<svg/onload=alert(document.cookie)>abcdef@test.com`.

> The payload uses an SVG onload handler to execute JavaScript upon rendering.

### Step 3: Submit and View Invitation

**Context**: Store the payload and trigger it by accessing the generated invitation page.

Submit the form, ignore any connection warnings, then navigate to the invitation URL (e.g., https://partners.shopify.com/{id}/invitations/{invitation_id}).

> Upon loading, the alert should fire, confirming execution and displaying cookies.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[shopify]]
- [[web]]
