---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567894
tags:
  - shopify
  - verification
  - api
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:32:20.579Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Verify-CSRF-Action-Execution

## Summary

This procedure checks the Shopify admin dashboard to confirm the success of the CSRF attack by inspecting the affected resource.

## Description

After the malicious form submission, the API action (e.g., product creation) persists in the store. Navigating to the relevant admin page verifies the unauthorized change, such as a new product with attacker-controlled data. This step validates exploit success and assesses impact, like stored XSS in descriptions.

## Requirements

1. Active Shopify admin session
2. Knowledge of the targeted endpoint and expected change
3. Web browser to access the dashboard

## Defense

Defensive measures and detection strategies:

- Regularly review admin logs for anomalous API actions (e.g., unexpected product creations)
- Set up alerts for API endpoint access outside normal patterns
- Use immutable audit trails to trace unauthorized changes

## Objectives

1. Confirm the CSRF payload executed successfully
2. Identify any persistent impacts like new resources
3. Evaluate potential for further exploitation

## Instructions

### Step 1: Navigate to Affected Resource

**Context**: Access the admin section corresponding to the API endpoint.

Log in to the dashboard if needed, then go to https://[shop].myshopify.com/admin/products (for products.json example).

> The page lists all products; scan for the newly added one with title "API CSRF TEST".

### Step 2: Inspect and Validate

**Context**: Examine details to ensure attacker control.

Click on the suspicious product to view details, checking vendor, description (for XSS), and creation timestamp.

> Success: Product exists with exact payload values; if XSS in body_html, it may execute in admin view.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[verification]]
- [[api]]
