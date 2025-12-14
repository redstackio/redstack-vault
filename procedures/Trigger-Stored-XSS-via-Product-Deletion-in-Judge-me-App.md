---
id: proc-trigger-xss-deletion
tags:
  - xss
  - trigger
  - judge-me
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
updated_at: '2025-12-14T03:46:38.092Z'
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
# Trigger-Stored-XSS-via-Product-Deletion-in-Judge-me-App

## Summary

This procedure triggers the execution of a stored XSS payload by deleting a malicious product through the Judge.me app's AliExpress Review Importer interface, where the product name is rendered without proper output encoding.

## Description

The Judge.me app fails to escape product names during the deletion process in its importer UI, allowing the stored payload to execute in the admin's browser context. An attacker navigates to the app's Products section, selects the tainted product, and deletes it, causing the name to be injected into the DOM unsafely. This leads to arbitrary JavaScript execution, such as alerts or data exfiltration. Prerequisites are the malicious product already created and admin access. Outcomes include payload activation, confirmed by JavaScript events firing.

## Requirements

1. Malicious product with XSS payload already created in Shopify
2. Judge.me app access via Shopify admin
3. Admin session active in the browser

## Defense

Defensive measures and detection strategies:

- Apply output encoding (e.g., HTML entity encoding) when rendering user input in admin interfaces
- Use strict CSP headers to block unsafe inline scripts
- Log and alert on XSS payload executions via browser console monitoring or WAF rules

## Objectives

1. Render the unsanitized product name during deletion
2. Execute JavaScript in the admin's session context
3. Validate vulnerability by observing payload effects

## Instructions

### Step 1: Navigate and Delete

**Context**: Access the importer interface and perform the deletion action to force rendering of the payload.

No specific command; perform via UI:

1. In Shopify Admin, open the Judge.me app.
2. Go to AliExpress Review Importer > Products.
3. Find the malicious product, select it, and click Delete.
4. Confirm the deletion.

> Upon confirmation, the product name is displayed without escaping, triggering the onerror handler and executing the script (e.g., prompt with domain).

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
- [[trigger]]
- [[judge-me]]
