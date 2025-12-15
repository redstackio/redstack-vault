---
id: proc-shopify-initiate-dev-store
tags:
  - shopify
  - store-creation
  - initiation
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
  - '[[T1078.004]]'
updated_at: '2025-12-14T17:30:35.778Z'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1078.004]]'
---
# Initiate-Development-Store-Creation

## Summary

This procedure describes how a staff member starts the development store creation process in the Shopify Partner Dashboard, establishing the necessary session and UI state for subsequent bypass steps.

## Description

The staff member logs into the dashboard and navigates to the store creation page, selecting the development store option. This action triggers the initial signup flow without full validation, allowing continuation even after permission changes. The procedure targets the web-based Partner Dashboard and assumes temporary permissions are in place. Outcomes include an active creation session that can be completed post-revocation.

## Requirements

1. Staff account with temporary development store permissions
2. Access to https://partners.shopify.com
3. Web browser (e.g., Chrome, Firefox)

## Defense

Defensive measures and detection strategies:

- Validate permissions at every stage of multi-step processes
- Log and monitor initiation of resource creation events
- Use session-based permission enforcement to prevent stale access

## Objectives

1. Start the development store signup workflow
2. Obtain UI/API tokens or state for continuation
3. Position for permission revocation test

## Instructions

### Step 1: Staff Login

**Context**: Authenticate the staff member to access the dashboard.

**Command** (Browser Navigation):
```bash
# No CLI; browser action
# URL: https://partners.shopify.com/sign_in
# Enter staff credentials (e.g., Doe)
```

> Successful login. Expected output: Redirect to dashboard.

### Step 2: Navigate to Store Creation

**Context**: Access the new stores page and select development option.

**Command** (Browser UI):
```bash
# UI steps:
# 1. Visit: https://partners.shopify.com/organizationID/stores/new
# 2. Select 'Development store' option
# 3. Proceed to signup form
```

> Initiate creation. Expected output: Signup form or token request visible; no errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1078.004]] Cloud Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[store-creation]]
- [[initiation]]
