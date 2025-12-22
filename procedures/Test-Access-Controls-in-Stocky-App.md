---
id: proc-uuid-001
tags:
  - access-control
  - testing
  - shopify
  - stocky
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:29:44.384Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Test-Access-Controls-in-Stocky-App

## Summary

This procedure tests for missing permission checks in the Shopify Stocky application's draft orders and purchase orders features, identifying potential IDOR vulnerabilities by attempting unauthorized access with a low-privilege user account.

## Description

In the Shopify Stocky app, an inventory management tool, users without draft order permissions should be restricted from viewing or interacting with draft orders. This procedure simulates access attempts to uncover absent authorization logic, allowing progression to data exfiltration. It targets the web-based admin interface and relies on manual testing via browser interactions. Prerequisites include a Shopify account with limited roles; expected outcomes are successful unauthorized views, confirming the vulnerability.

## Requirements

1. Shopify user account without draft order permissions
2. Access to the Stocky app via Shopify admin panel
3. Web browser with developer tools enabled

## Defense

Defensive measures and detection strategies:

- Implement role-based access control (RBAC) checks on all draft order endpoints
- Log and monitor access attempts to sensitive features, alerting on permission mismatches
- Use Shopify's app bridge for secure API calls with token validation

## Objectives

1. Verify if permission checks are enforced for draft order access
2. Identify exploitable endpoints for further IDOR testing
3. Confirm unauthorized access without triggering alerts

## Instructions

### Step 1: Log In and Navigate to Stocky

**Context**: Establish a session with a low-privilege account to test baseline access.

Log in to your Shopify admin at admin.shopify.com with the restricted user account. From the apps section, launch the Stocky app and attempt to access the "Draft Orders" menu.

> No specific command; perform via UI. Expected: UI loads without errors, allowing navigation despite lacking permissions.

### Step 2: Inspect Draft Orders Functionality

**Context**: Probe for missing checks by interacting with draft order elements.

In the Stocky dashboard, click on draft orders or use the search to view existing ones. Open browser developer tools (F12), go to the Network tab, and refresh or interact to capture requests (e.g., GET /draft_orders).

> Expected: Requests succeed with 200 OK responses, no 403 Forbidden, revealing missing auth checks.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[access-control]]
- [[testing]]
- [[shopify]]
- [[stocky]]
