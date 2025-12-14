---
tags:
  - xss
  - admin-exploitation
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
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
updated_at: '2025-12-13T23:52:33.592Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: c0c4fd23-f47a-4944-bc43-aa4908815b77
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-in-Admin-Order-Details

## Summary

This procedure logs in as a Shopify admin, views the targeted order, and clicks the malicious link to execute the stored JavaScript payload in the privileged context, potentially stealing CSRF tokens for further actions.

## Description

In the Shopify admin panel, order details include a 'conversion details' section with a clickable link labeled 'The first page they visited' sourced from the stored _landing_page value. Clicking it executes the javascript: URI directly. This elevates from customer to admin context, enabling token theft or session hijacking. Requires admin credentials; outcomes include arbitrary JS execution.

## Requirements

1. Order ID from previous checkout
2. Valid admin login credentials
3. Access to the admin panel URL

## Defense

Defensive measures and detection strategies:

- Sanitize reflected links in admin UI, converting to plain text or safe URLs
- Implement JS URI blocking via CSP or URL validation
- Log and alert on JS execution attempts in admin sessions

## Objectives

1. Execute payload in admin browser
2. Steal sensitive data like CSRF tokens
3. Enable follow-on actions like adding attacker as admin

## Instructions

### Step 1: Login to Admin Panel

**Context**: Gain privileged access to view orders.

Navigate to `[shop].myshopify.com/admin` and log in with admin credentials.

> Expected: Dashboard loads; no issues.

### Step 2: View Order Details

**Context**: Locate and open the order containing the payload.

Go to Orders, search or select the recent guest order by ID (e.g., from confirmation email).

> Expected: Order details page loads with sections like customer info and conversion details.

### Step 3: Click Malicious Link

**Context**: Trigger execution by interacting with the reflected value.

Scroll to 'Conversion details' or similar section, locate 'The first page they visited' link, and click it.

> Expected: Payload executes (e.g., alert(1) or network exfil to attacker server); check console for JS errors or successes.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[xss]]
- [[admin-exploitation]]
