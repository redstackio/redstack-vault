---
id: proc-create-malicious-collection
tags:
  - xss
  - injection
  - shopify
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
updated_at: '2025-12-14T03:15:52.843Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Collection-for-Shopify-XSS

## Summary

This procedure creates a product collection in Shopify's admin with a name containing an XSS payload, exploiting insufficient input validation to store malicious JavaScript for later execution.

## Description

In Shopify's myshopify.com Admin, the collection creation form accepts arbitrary input for the title without HTML escaping or sanitization. By injecting a payload like an onerror image tag, an attacker with admin access can prepare for reflected XSS in downstream features like tax overrides. This targets the admin browser context, potentially leading to session hijacking or data theft. Prerequisites include admin privileges; no tools beyond a browser are needed.

## Requirements

1. Valid Shopify admin account with collection management access
2. Web browser (e.g., Chrome) for UI interaction
3. Knowledge of basic XSS payloads

## Defense

Defensive measures and detection strategies:

- Implement client-side and server-side input sanitization using libraries like DOMPurify
- Monitor for anomalous collection names via audit logs
- Enable Content Security Policy (CSP) to restrict inline script execution

## Objectives

1. Store unsanitized XSS payload in a collection object
2. Prepare payload for reflection in admin UI
3. Enable subsequent JS execution without direct input

## Instructions

### Step 1: Access Collection Management

**Context**: Log in and navigate to the collections interface to begin creation.

Log in to myshopify.com/admin. Click Products > Collections > Create collection.

### Step 2: Inject Payload

**Context**: Enter the malicious name to bypass validation.

In the 'Title' field, input: `<img src=x onerror=prompt(7)>`. Optionally add a description. Click 'Save'.

> This stores the payload as-is; verify by viewing the collection list where the name renders raw HTML.

### Step 3: Verify Storage

**Context**: Confirm the payload is retained without alteration.

Refresh the collections page. The malicious name should display, potentially breaking layout if rendered insecurely.

**Expected Output**: Collection listed with payload visible.

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
- [[shopify]]
- [[injection]]
