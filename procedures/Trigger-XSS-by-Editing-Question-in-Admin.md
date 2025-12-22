---
tags:
  - xss
  - execution
  - session-hijacking
  - admin
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
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
id: 00123614-8e78-4add-b616-07d5f14faf5f
created_at: '2025-12-14T03:46:32.047Z'
updated_at: '2025-12-14T03:46:32.047Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-by-Editing-Question-in-Admin

## Summary

This procedure executes the stored XSS payload by editing the associated question in the Shopify admin, leading to JavaScript execution and potential session theft.

## Description

In the Judge.me admin interface, editing a question for an out-of-stock product displays the product name without sanitization, triggering the XSS. The payload executes in the admin's browser context, allowing actions like prompting the domain or exfiltrating cookies. This bypasses the fix from report #1416672. Expected outcome: Arbitrary JS execution, e.g., alert confirming control.

## Requirements

1. Shopify admin credentials (targeted victim)
2. Question with malicious association exists
3. Browser with JS enabled

## Defense

Defensive measures and detection strategies:

- Enforce output encoding (e.g., escape HTML) for all displayed fields in admin
- Implement XSS auditors or WAF rules for admin endpoints
- Monitor admin actions for unexpected JS errors or alerts

## Objectives

1. Execute payload in privileged context
2. Steal admin session data
3. Achieve account takeover

## Instructions

### Step 1: Access Judge.me Admin

**Context**: Log in as admin to the questions section.

Go to Apps > Judge.me Product Reviews > Questions.

### Step 2: Locate and Edit Question

**Context**: Select the question tied to the deleted product.

Find the relevant question and click 'Edit'. The product name field will render the payload.

> Upon loading the edit form, the XSS should trigger (e.g., `prompt(document.domain)` alert showing 'shopify.myshopify.com').

### Step 3: Exploit Execution

**Context**: Extend payload for impact.

In a real attack, replace prompt with code to exfiltrate document.cookie to an attacker server.

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
