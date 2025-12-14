---
id: proc-uuid-6
name: Verify-Product-Status-Change
tags:
  - verification
  - web
  - csrf
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Search Open Websites-Domains]]'
updated_at: '2025-12-14T17:27:15.649Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Search Open Websites-Domains]]'
---
# Verify-Product-Status-Change

## Summary

This procedure checks the victim's product management page to confirm the CSRF attack successfully hid the targeted product.

## Description

After the victim visits the malicious page, the POST request changes the status. Verification involves accessing the authenticated products dashboard to observe the change, confirming the exploit's success and potential sales diversion.

## Requirements

1. Access to victim's account or proxy to check
2. Knowledge of the targeted product ID
3. Browser for navigation

## Defense

Defensive measures and detection strategies:

- Audit logs for status changes without user intent
- Alerts on bulk or unauthorized product updates

## Objectives

1. Confirm product is now hidden/disabled
2. Validate the attack impact
3. Assess for further exploitation

## Instructions

### Step 1: Access Products Page

**Context**: Log in as victim or use shared access to the dashboard.

No command; navigate to `https://www.digitalsellz.com/user/#/products`.

> Refresh the page to load current statuses.

### Step 2: Check Status

**Context**: Locate the targeted product and inspect its visibility.

No command; look for status indicator.

> Expected: Product marked as hidden or disabled, no longer visible to customers.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Search Open Websites-Domains]] Search Open Technical Databases

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
- [[web]]
- [[csrf]]
