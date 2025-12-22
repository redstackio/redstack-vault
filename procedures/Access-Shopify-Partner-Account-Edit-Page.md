---
id: proc-uuid-2
tags:
  - navigation
  - shopify
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T03:15:52.968Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Shopify-Partner-Account-Edit-Page

## Summary

This procedure details navigating to the Shopify partner account edit page, exposing the vulnerable 'Website (optional)' field for payload injection.

## Description

After logging in, attackers directly access the edit endpoint at https://app.shopify.com/services/partners/account/edit. This page renders a form without proper input validation on URL fields, allowing storage of malicious schemes. The target environment is the authenticated Shopify partner web app, with outcomes including form accessibility for exploitation.

## Requirements

1. Active Shopify partner account
2. Logged-in session
3. Web browser

## Defense

Defensive measures and detection strategies:

- Log access to admin edit pages and alert on unusual patterns
- Enforce session timeouts to limit exposure

## Objectives

1. Reach the vulnerable form endpoint
2. Prepare for payload entry
3. Confirm edit permissions

## Instructions

### Step 1: Log In and Navigate

**Context**: Ensure authenticated state and direct to edit URL.

No specific command; from dashboard, enter or visit https://app.shopify.com/services/partners/account/edit in browser.

> The page should load with editable fields including 'Website (optional)'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[navigation]]
- [[shopify]]
