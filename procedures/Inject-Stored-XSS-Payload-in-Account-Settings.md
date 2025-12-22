---
tags:
  - xss
  - stored-xss
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 07f461d7-f7c7-4fe9-b68d-9deaacda2a03
created_at: '2025-12-14T03:16:25.389Z'
updated_at: '2025-12-14T03:16:25.389Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-Payload-in-Account-Settings

## Summary

This procedure demonstrates how to inject a stored XSS payload into editable fields within Moneybird's account settings, exploiting insufficient input sanitization to persist malicious JavaScript for later execution.

## Description

In the Moneybird application, certain account settings fields (e.g., company name or address) do not properly escape user input, allowing attackers with account access to store JavaScript code. This stored payload can then execute when the settings are rendered in other parts of the application, such as the Bank tab, potentially leading to session hijacking or data theft. The attack requires an authenticated session but can affect other users viewing the affected account's data. Prerequisites include a valid Moneybird account and basic knowledge of JavaScript payloads.

## Requirements

1. Authenticated access to Moneybird account settings
2. Browser with developer tools for testing payloads
3. Attacker-controlled server for exfiltration (optional for advanced payloads)

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output escaping (e.g., using libraries like DOMPurify)
- Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous JavaScript network requests from the application

## Objectives

1. Persist malicious JavaScript in account settings
2. Verify payload storage without immediate execution
3. Set up for cross-context execution in sensitive areas like the Bank tab

## Instructions

### Step 1: Access Account Settings

**Context**: Log in to the Moneybird dashboard and navigate to the account settings section to identify injectable fields.

No specific command; use the web interface to reach `/account/settings` or equivalent.

> Expected: Editable text fields visible for input.

### Step 2: Craft and Inject Payload

**Context**: Create a simple test payload to confirm vulnerability, then escalate to a functional one for exfiltration.

Use browser interface to input: `<script>alert('XSS Test');</script>` in a field like company description.

> Submit the form. Expected: Payload saves without errors; refresh to see it unescaped in HTML source.

### Step 3: Verify Storage

**Context**: Check if the payload persists by viewing the settings page source.

Inspect element in browser dev tools to confirm script tag is present.

> Expected: Raw script in DOM, no auto-execution here.

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
