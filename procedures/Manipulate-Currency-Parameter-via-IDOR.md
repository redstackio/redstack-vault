---
tags:
  - idor
  - parameter-tampering
  - web
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:23.581Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 5161671e-1f80-463f-af24-0755e6ee6647
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Manipulate-Currency-Parameter-via-IDOR

## Summary

This procedure exploits an Insecure Direct Object Reference (IDOR) in the MailPoet order endpoint by appending an unauthorized 'cur' parameter to the URL, switching the currency from EUR to USD without server-side validation.

## Description

The MailPoet order creation process at /orders/new lacks proper authorization checks on the 'cur' parameter, allowing authenticated users to arbitrarily change the currency via URL manipulation. Starting from the default order URL (e.g., https://account.mailpoet.com/orders/new?p=214), appending '&cur=usd' forces the system to process the order in USD while keeping the numerical amount unchanged (e.g., 33600). This results in a lower real-world payment value due to favorable exchange rates, directly impacting revenue. The attack assumes an active session and targets the web application layer.

## Requirements

1. Loaded order page from prior navigation (e.g., with plan ID)
2. Web browser address bar access
3. Authenticated session in MailPoet

## Defense

Defensive measures and detection strategies:

- Validate 'cur' parameter server-side against user locale or plan defaults
- Implement parameter whitelisting and authorization checks
- Log and alert on unexpected currency changes in order requests

## Objectives

1. Bypass currency restrictions via IDOR
2. Switch to a weaker currency (USD) for numerical equivalence
3. Prepare order for processing with reduced effective cost

## Instructions

### Step 1: Identify Order URL

**Context**: Locate the base URL after loading the plan order page.

Copy the current URL from the browser, e.g., https://account.mailpoet.com/orders/new?p=214.

> Ensures the starting point for modification.

### Step 2: Append Currency Parameter

**Context**: Exploit IDOR by directly altering the URL parameter.

Edit the address bar to add '&cur=usd', resulting in https://account.mailpoet.com/orders/new?p=214&cur=usd, then press Enter to reload.

> The page updates to display USD pricing without errors.

### Step 3: Verify Change

**Context**: Confirm the manipulation succeeded.

Check the displayed price for 33600$ in USD.

> Validates the IDOR exploitation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- idor
- parameter-tampering
- web
