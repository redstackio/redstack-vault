---
tags:
  - shopify
  - access-verification
  - permission-check
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:30:47.377Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: eaf50356-a5ae-4e6a-ac5a-c14eb8258d1a
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Verify-Access-Restrictions-for-Limited-User

## Summary

This procedure tests and confirms that a limited-privilege user in Shopify's Partner Portal is denied access to the referrals functionality through the standard user interface, highlighting frontend permission enforcement.

## Description

After creating the limited user, log in with those credentials and attempt to access the restricted referrals page. This step validates that UI-level checks are in place, setting the stage for backend bypass. The target URL is https://partners.shopify.com/[partner_id]/referrals/, where insufficient privileges should block access.

## Requirements

1. Active limited-privilege user account credentials.
2. Web browser for navigation and login.
3. Knowledge of the partner ID for URL construction.

## Defense

Defensive measures and detection strategies:

- Enforce consistent frontend and backend permission checks.
- Log all access attempts to restricted pages for anomaly detection.
- Use session-based permission validation on every page load.

## Objectives

1. Confirm UI restrictions prevent unauthorized referrals access.
2. Document the exact error message for reproduction.
3. Ensure no unintended access paths in the frontend.

## Instructions

### Step 1: Log In and Attempt Restricted Access

**Context**: Use limited user credentials to test UI permission enforcement.

Log in to https://partners.shopify.com with limited user credentials. Navigate directly to https://partners.shopify.com/[partner_id]/referrals/ and observe the denial.

> Expected output: Permission error or redirect; access blocked.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[access-verification]]
