---
tags:
  - url-bypass
  - access-control
  - rockset
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:51.651Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: a417fac0-c956-476a-abe6-187dec0454af
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Directly-Access-Rockset-Billing-Page

## Summary

This procedure exploits broken access controls by directly navigating to the Rockset billing URL in a member session, loading admin-only sensitive information despite UI hiding.

## Description

With a member account logged in, manually enter the billing endpoint URL (https://console.rockset.com/billing?tab=payment) in the browser. Due to missing server-side authorization, the page renders fully, exposing payment methods, invoices, and other financial data. This targets the web console's routing system and highlights the risk of client-side-only protections in cloud management interfaces.

## Requirements

1. Active member browser session
2. Knowledge of the internal billing URL
3. Browser developer tools optional for inspection

## Defense

Defensive measures and detection strategies:

- Implement server-side RBAC checks on all endpoints, rejecting unauthorized requests with 403
- Log direct URL accesses and alert on anomalies from non-admin sessions
- Use URL obfuscation or parameterized routes to prevent guessable paths

## Objectives

1. Bypass UI restrictions to access hidden admin page
2. Expose sensitive billing and payment data
3. Demonstrate impact of improper authorization

## Instructions

### Step 1: Prepare Browser Session

**Context**: Ensure member login is active.

Verify you're on the member dashboard; do not log out.

> Session cookies must be present for authenticated access.

### Step 2: Enter Direct URL

**Context**: Navigate bypassing the menu.

In the address bar, type https://console.rockset.com/billing?tab=payment and press Enter.

> The page loads, showing tabs like 'Payment' with details such as credit card info and billing history.

### Step 3: Inspect Exposed Data

**Context**: Validate vulnerability success.

Scroll through the page to view and screenshot sensitive sections.

> Confirm admin-only elements like payment methods are visible without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- url-bypass
- access-control
- rockset
