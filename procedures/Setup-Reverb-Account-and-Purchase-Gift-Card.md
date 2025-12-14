---
tags:
  - setup
  - authentication
  - purchase
type: procedure
tools:
  - '[[tools/Burp-Suite-Pro]]'
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
updated_at: '2025-12-14T17:24:22.988Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 5bd8a41a-ca95-4994-8e37-91048d59ee6b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-Reverb-Account-and-Purchase-Gift-Card

## Summary

This procedure establishes an authenticated session on the Reverb.com sandbox environment and purchases a gift card to obtain a redeemable token, setting up the preconditions for exploiting the race condition.

## Description

In the context of testing the gift card redemption vulnerability, this step involves logging into a Reverb account and navigating the purchase flow to acquire a gift card token. The sandbox environment (https://sandbox.reverb.com) is used to avoid impacting production. Expected outcomes include a valid session and a fresh gift card token valued at e.g., $25, which will be used in subsequent redemption attempts. Prerequisites include valid credentials and browser access.

## Requirements

1. Valid Reverb.com account credentials
2. Access to https://sandbox.reverb.com
3. Web browser with proxy support for Burp Suite

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on account actions to detect anomalous logins
- Monitor for unusual gift card purchases from sandbox environments

## Objectives

1. Gain authenticated access to the platform
2. Acquire a gift card token for redemption testing
3. Prepare for request interception

## Instructions

### Step 1: Login to Reverb Account

**Context**: Authenticate to establish a session for subsequent actions.

Navigate to https://sandbox.reverb.com and enter credentials to log in.

**Expected Output**: Redirect to account dashboard with session cookies set.

### Step 2: Purchase Gift Card

**Context**: Complete the gift card purchase to generate a token.

Follow the platform's purchase flow to buy a $25 gift card.

**Expected Output**: Receipt with gift card token (e.g., a alphanumeric code).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Pro]]

## Tags

- setup
- authentication
