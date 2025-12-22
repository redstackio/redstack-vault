---
id: procedure-trigger-xss-discount-creation
tags:
  - xss
  - execution
  - shopify
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:31.973Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Reflected-XSS-in-Discount-Creation

## Summary

This procedure activates the reflected XSS by interacting with the app's discount creation feature, causing unsanitized product/collection data to be displayed and execute JavaScript.

## Description

The Bulk Discount App fetches and renders store data without proper escaping during discount setup, reflecting the injected payload. This executes in the shopifyapps.com context, allowing client-side attacks like cookie theft. Requires prior payload injection and app access.

## Requirements

1. Payload-injected product/collection in the store.
2. Installed and accessible Bulk Discount App.
3. Authenticated session on shopifyapps.com.

## Defense

Defensive measures and detection strategies:

- Apply output encoding (e.g., HTML entity escaping) when rendering user inputs in app views.
- Deploy Web Application Firewall (WAF) rules to block common XSS payloads.
- Monitor JavaScript errors and unexpected prompts in browser consoles via client-side logging.

## Objectives

1. Reflect and execute the injected payload.
2. Demonstrate domain takeover via JS.
3. Enable potential data exfiltration.

## Instructions

### Step 1: Initiate Discount Creation

**Context**: Trigger data fetch and render.

In the app dashboard, click "Create One now" or "New Discount Set".

> This loads forms or lists including products/collections.

### Step 2: Observe Execution

**Context**: Confirm XSS trigger.

As the interface renders the reflected name/title, the payload executes, showing a prompt with the domain.

> Use browser dev tools to inspect the DOM for injection points and verify execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]
- [[shopify]]
