---
tags:
  - privilege-escalation
  - shopify
  - api
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:58.893Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 16484b32-26bd-407a-87d0-73883132b4d9
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Identify-Privilege-Verification-Flaw-in-Shopify-Apps

## Summary

This procedure identifies flaws in Shopify apps that use offline API access mode, where user privileges are not verified, enabling unauthorized data access.

## Description

In Shopify's app ecosystem, apps can operate in offline mode, generating long-lived tokens for store access without tying requests to specific user sessions. This procedure involves testing such apps to confirm they do not check the requesting user's permissions, allowing low-privilege accounts to access restricted resources. The target environment is a Shopify store with installed apps like Order Printer. Prerequisites include a valid Shopify account and basic API knowledge. Expected outcomes include confirmation of the bypass, leading to potential data exposure.

## Requirements

1. Authenticated access to a Shopify store as any user role
2. Installed third-party app using offline API mode (e.g., Order Printer)
3. Browser or API testing tool for making requests

## Defense

Defensive measures and detection strategies:

- Enforce online access mode for apps to tie permissions to user sessions
- Implement app-level privilege checks before proxying API calls
- Monitor API usage logs for anomalous access patterns from low-privilege accounts

## Objectives

1. Verify absence of privilege verification in offline API apps
2. Document the flaw for exploitation or reporting
3. Assess potential data exposure risks

## Instructions

### Step 1: Review App Configuration

**Context**: Examine the app's API mode and documentation to understand access patterns.

Access the Shopify app settings and confirm offline mode is enabled, which uses store-level tokens without user context.

### Step 2: Test API Requests

**Context**: Send test requests as a low-privilege user to check for permission enforcement.

Use the app's interface or direct API calls to request restricted data, observing if responses succeed without errors.

**Expected Output**: Successful data retrieval without privilege denial.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[privilege-escalation]]
- [[shopify]]
- [[api]]
