---
tags:
  - xss
  - trigger
  - judgeme
  - shopify
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
  - Shopify
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 8c865f38-1727-4f9d-ad0d-1dc8488c94b7
created_at: '2025-12-13T23:52:25.675Z'
updated_at: '2025-12-13T23:52:25.675Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger XSS via Judge.me Filters

## Summary

This procedure triggers the stored XSS payload by interacting with the Judge.me app's TYPE filter dropdown, causing the unsanitized product type to render and execute JavaScript in the admin's browser.

## Description

The Judge.me app fetches product types from Shopify without proper escaping when populating the filter dropdown. Selecting the malicious type inserts the payload into the DOM, executing the onerror handler. This occurs in the authenticated admin context, enabling potential theft of session data or impersonation.

## Requirements

1. Installed Judge.me app
2. Product with injected payload existing in the store
3. Victim admin access to the Judge.me products page

## Defense

Defensive measures and detection strategies:

- Sanitize all output from Shopify data in app filters (e.g., escape HTML)
- Implement browser-based XSS auditors or CSP
- Log filter interactions and monitor for anomalous JavaScript prompts

## Objectives

1. Render the stored payload in the filter UI
2. Execute arbitrary JavaScript
3. Demonstrate impact like domain alerting or session access

## Instructions

### Step 1: Navigate to Judge.me Products Page

**Context**: Access the vulnerable interface.

Log in as an admin and go to https://xxx.myshopify.com/admin/apps/judgeme/products.

### Step 2: Interact with TYPE Filter

**Context**: Select the malicious option to trigger execution.

Click the TYPE filter dropdown. Locate and select the entry containing the payload (e.g., the injected product type).

**Expected Output**: JavaScript alert showing the document domain; potential for further payload expansion.

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
- [[judgeme]]
- [[shopify]]
