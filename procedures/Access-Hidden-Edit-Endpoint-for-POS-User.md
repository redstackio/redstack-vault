---
tags:
  - idor
  - access-bypass
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:59.134Z'
skill_level: intermediate
impact_level: medium
sub_techniques: []
id: 67ffc880-69f5-48b1-ade4-f2c0fdb0eed3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Hidden-Edit-Endpoint-for-POS-User

## Summary

This procedure constructs and accesses an undocumented edit URL for a POS User in the Stocky app, bypassing standard UI restrictions.

## Description

Using the extracted user_id, build the URL https://stocky.shopifyapps.com/users/{user_id}/edit and load it directly. This hidden endpoint lacks UI controls but allows form-based edits. In the Shopify Stocky environment, this exploits missing authorization checks for POS users. Expected: Edit form loads without errors.

## Requirements

1. Extracted user_id from prior step
2. Admin session active
3. Direct URL access capability

## Defense

Defensive measures and detection strategies:

- Restrict direct endpoint access via authorization middleware
- Log all direct URL requests to hidden paths
- Validate user type before serving edit forms

## Objectives

1. Load POS User edit form
2. Confirm endpoint accessibility
3. Prepare for payload modifications

## Instructions

### Step 1: Construct URL

**Context**: Replace placeholder with actual ID.

Form the URL: https://stocky.shopifyapps.com/users/12345/edit (use real ID).

> Copy to address bar.

### Step 2: Load and Verify

**Context**: Ensure form is editable.

Navigate to the URL and check if user details load.

> Expected: Form fields populated with POS User data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[idor]]
- [[access-bypass]]
