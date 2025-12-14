---
id: proc-coinbase-create-confirm-001
tags:
  - auth
  - 2fa
  - coinbase
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:31.048Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-and-Confirm-Coinbase-Recurring-Payment

## Summary

This procedure outlines creating a recurring payment on Coinbase's beta platform with 2FA enabled and capturing the confirmation request, serving as the initial setup for replay attacks.

## Description

In the context of testing for replay vulnerabilities, a user authenticates to beta.coinbase.com, sets up a recurring payment (e.g., scheduled transfers), triggers 2FA verification via an authenticator app or SMS, and submits the code. This generates a POST request to the confirmation endpoint. The procedure assumes a valid account and focuses on request capture for subsequent steps. Expected outcome: A confirmed payment with capturable HTTP details, highlighting the need for secure request handling.

## Requirements

1. Valid Coinbase beta account with 2FA enabled
2. Browser with developer tools (e.g., Firefox/Chrome) or proxy for request interception
3. Access to 2FA codes

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on payment creation endpoints
- Log all 2FA verifications with timestamps for anomaly detection
- Use client-side fingerprinting to detect session anomalies

## Objectives

1. Establish a baseline confirmed payment state
2. Capture exact request details for replay testing
3. Verify 2FA integration in payment workflows

## Instructions

### Step 1: Initiate Recurring Payment Creation

**Context**: Log in and navigate to create a new recurring payment to trigger the workflow.

No specific command; use the web UI to select payment amount, recipient, and schedule.

> Enter details and proceed to confirmation, which requires 2FA.

### Step 2: Verify with 2FA and Capture Request

**Context**: Enter the 2FA code to confirm, intercepting the POST request sent to the server.

Use browser dev tools (Network tab) or a proxy to capture the request.

> The request includes POST /recurring_payments/{id}/confirm with body utf8=✓ and _method=patch. Save headers (e.g., CSRF-Token, Cookies), URL, and payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- auth
- 2fa
- coinbase
