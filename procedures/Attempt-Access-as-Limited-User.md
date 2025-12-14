---
id: proc-uuid-3
tags:
  - shopify
  - access-denied
type: procedure
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:28:52.132Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Attempt-Access-as-Limited-User

## Summary

Test access to the Activity Feed as a limited user to confirm enforcement of permissions on the main endpoint.

## Description

Log in with limited credentials and attempt to access /admin/activity, expecting a block due to missing 'Home' permission. This validates the control before attempting bypass.

## Requirements

1. Limited user credentials (User Y)
2. Web browser
3. Active Shopify session

## Defense

Defensive measures and detection strategies:

- Audit failed access attempts
- Rate-limit unauthorized endpoint calls

## Objectives

1. Confirm permission restrictions
2. Identify blocked features
3. Set up for bypass testing

## Instructions

### Step 1: Log In as Limited User

**Context**: Switch to restricted session.

Log in with User Y credentials at https://yourshop.myshopify.com/admin.

> Expected: Limited dashboard loads.

### Step 2: Attempt Activity Access

**Context**: Try direct navigation to restricted page.

Navigate to https://yourshop.myshopify.com/admin/activity.

> Expected: Access blocked with permission error.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- shopify
- permission-check
