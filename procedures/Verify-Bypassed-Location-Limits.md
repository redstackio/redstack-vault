---
id: proc-verify-shopify-location-bypass
tags:
  - race-condition
  - verification
  - shopify
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-query-locations]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:22.599Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Bypassed-Location-Limits

## Summary

This procedure checks the Shopify dashboard or API to confirm that more locations have been created than allowed by the billing plan, validating the race condition exploit.

## Description

After sending concurrent requests, query the locations list to observe the inflated count. This confirms the bypass, as the system failed to enforce limits due to the race. Applicable to web-based Shopify admin interfaces.

## Requirements

1. Successful execution of prior concurrent request procedure
2. Access to Shopify API or dashboard
3. Knowledge of the plan's location limit (e.g., 4 for basic plans)

## Defense

Defensive measures and detection strategies:

- Real-time limit enforcement with atomic transactions
- Audit logs for location creation events and correlate with billing
- Dashboard alerts for limit exceedances

## Objectives

1. Retrieve and count current locations
2. Compare against billing plan allowance
3. Document proof of bypass for reporting

## Instructions

### Step 1: Query API for Locations

**Context**: Use API to list all locations and check count.

**Command** ([[commands/curl-query-locations]]):
```bash
curl -X GET 'https://yourstore.myshopify.com/admin/api/2023-10/locations.json' -H 'Authorization: Bearer your-access-token'
```

> Parse the JSON response for the locations array length. Expected output: {"locations":[ ... ]} with array size > plan limit (e.g., 12 items).

### Step 2: Check Dashboard

**Context**: Visually verify in the UI.

**Command** ([[commands/refresh-shopify-dashboard]]):
```bash
# Browser action: Log in to Shopify admin > Settings > Locations
```

> Refresh the page and count listed locations. Expected output: Dashboard shows excess locations, all active.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-query-locations]]
- [[commands/refresh-shopify-dashboard]]

## Tools Used


## Tags

- race-condition
- verification
- shopify
