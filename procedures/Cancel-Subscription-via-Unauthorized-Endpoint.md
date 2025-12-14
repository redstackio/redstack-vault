---
id: proc-taxjar-cancel-subscription
name: Cancel-Subscription-via-Unauthorized-Endpoint
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.482Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
tags:
  - access-control
  - authorization-bypass
  - web
platforms:
  - Web
commands: []
tools: []
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Cancel-Subscription-via-Unauthorized-Endpoint

## Summary

This procedure exploits an improper access control flaw in TaxJar by directly accessing the subscription cancellation endpoint with member permissions, allowing unauthorized disruption of account services.

## Description

The procedure targets the TaxJar web application's subscription management, where the endpoint https://app.taxjar.com/account/subscription/cancel lacks proper admin permission checks. In the attack scenario, a logged-in member user can trigger cancellation, impacting service availability. Outcomes include successful unsubscribe without elevated access, demonstrating the vulnerability's severity.

## Requirements

1. Active session as a TaxJar member user
2. Web browser capable of navigating to specific URLs
3. Target subscription active in the account

## Defense

Defensive measures and detection strategies:

- Validate user roles on all sensitive endpoints with server-side checks
- Log and alert on subscription changes from non-admin accounts
- Use CAPTCHA or secondary verification for destructive actions like cancellations

## Objectives

1. Bypass admin-only restrictions to access cancellation functionality
2. Execute subscription cancellation to disrupt the target account
3. Confirm impact without requiring victim interaction

## Instructions

### Step 1: Locate Cancellation Endpoint

**Context**: Identify and request the vulnerable URL from within the authenticated session.

From the dashboard, directly enter or navigate to https://app.taxjar.com/account/subscription/cancel in the browser address bar.

### Step 2: Initiate Cancellation

**Context**: Submit the cancellation request, exploiting the lack of permission enforcement.

If a confirmation dialog appears, proceed with the action; the endpoint processes the request as if admin-authorized.

### Step 3: Verify Cancellation

**Context**: Check the account status to confirm the disruption.

Return to the account or subscription page to observe the updated status indicating cancellation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[access-control]]
- [[authorization-bypass]]
- [[web]]
