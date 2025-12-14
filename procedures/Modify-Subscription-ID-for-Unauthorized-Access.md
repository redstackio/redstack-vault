---
id: proc-uuid-002
name: Modify-Subscription-ID-for-Unauthorized-Access
tags:
  - idor
  - parameter-manipulation
  - unauthorized-access
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-modify-subscription-id]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:29.702Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Modify-Subscription-ID-for-Unauthorized-Access

## Summary

This procedure modifies the subscription_id parameter in the Zomato Gold payment success endpoint to retrieve details of other users' memberships, exploiting the lack of ownership validation.

## Description

By changing the subscription_id to arbitrary values while keeping the user_id, the endpoint returns sensitive details like start/end dates and plan duration without checking if the requester owns the subscription. This IDOR allows privacy violations by exposing other users' data directly.

## Requirements

1. Baseline access from previous step
2. Arbitrary subscription_id values (e.g., sequential integers)
3. HTTP client for parameter alteration

## Defense

Defensive measures and detection strategies:

- Validate subscription ownership against session user_id
- Sanitize and log parameter changes
- Use indirect references (e.g., hashes) instead of direct IDs

## Objectives

1. Access unauthorized subscription details
2. Confirm IDOR vulnerability
3. Extract validity periods and plans

## Instructions

### Step 1: Alter Subscription ID

**Context**: Replace the original subscription_id with a guessed or fuzzed value to test access.

**Command** ([[commands/curl-modify-subscription-id]]):
```bash
curl -X GET "https://www.zomato.com/gold/payment-success?subscription_id=123456&user_id=█████████" -i
```

> Expected output: Details like "Start: 22 Dec 2017, End: 22 Jun 2018, Plan: 6 month plan" without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-modify-subscription-id]]

## Tools Used


## Tags

- idor
- unauthorized-access
