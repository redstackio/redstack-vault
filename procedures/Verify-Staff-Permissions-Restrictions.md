---
id: proc-shopify-verify-staff-restrictions
tags:
  - shopify
  - permissions-check
  - access-denied
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
updated_at: '2025-12-14T17:30:26.794Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Verify-Staff-Permissions-Restrictions

## Summary

This procedure tests the boundaries of a low-privilege staff account in Shopify by attempting access to restricted features like subscriptions and billing, confirming denials to establish that the account lacks intended privileges before exploiting gaps.

## Description

Shopify's permission model restricts staff based on assigned roles. Using a 'report'-only account, this procedure simulates access attempts to protected areas. The scenario targets the admin panel during trial setup. Prerequisites: Active staff session. Outcomes include error confirmations, validating the setup for access control bypass testing.

## Requirements

1. Active staff login session
2. Web browser for navigation
3. Knowledge of restricted paths (e.g., /admin/settings/billing)

## Defense

Defensive measures and detection strategies:

- Log all access denial events and review for patterns
- Use Shopify's permission audit tools to ensure no over-privileging
- Implement client-side checks alongside server-side enforcement

## Objectives

1. Confirm lack of access to subscription features
2. Document denial indicators for baseline
3. Ensure no unintended privileges

## Instructions

### Step 1: Attempt Subscription Access

**Context**: Test navigation to plan-related sections.

**Instructions**: From staff dashboard, click Settings > Plan or Billing. Observe response.

> Expected output: 'Access denied' or redirect to dashboard.

### Step 2: Check Trial Status Visibility

**Context**: Verify inability to view or modify trial details.

**Instructions**: Search for 'trial' or navigate to any subscription overview.

> Expected output: No access or permission error message.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- shopify
- permission-verification
- restrictions
