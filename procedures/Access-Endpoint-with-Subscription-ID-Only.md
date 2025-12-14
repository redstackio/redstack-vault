---
id: proc-uuid-003
name: Access-Endpoint-with-Subscription-ID-Only
tags:
  - idor
  - parameter-omission
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-subscription-id-only]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:29.698Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Access-Endpoint-with-Subscription-ID-Only

## Summary

This procedure removes the user_id parameter from the request to the Zomato Gold payment success endpoint, confirming that subscription details are accessible solely via subscription_id due to missing validation.

## Description

The endpoint ties details directly to the provided subscription_id without requiring or validating the user_id, allowing anyone to view membership information by omitting the user_id parameter.

## Requirements

1. Valid subscription_id from prior steps
2. HTTP request tool

## Defense

Defensive measures and detection strategies:

- Require both parameters and cross-validate them
- Implement session-based access controls
- Monitor for requests missing expected parameters

## Objectives

1. Verify access without user_id
2. Expose subscription details independently
3. Highlight validation gaps

## Instructions

### Step 1: Omit User ID

**Context**: Send request with only subscription_id to test isolation.

**Command** ([[commands/curl-subscription-id-only]]):
```bash
curl -X GET "https://www.zomato.com/gold/payment-success?subscription_id=███████" -i
```

> Expected output: Subscription details revealed, tied to membership ID.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-subscription-id-only]]

## Tools Used


## Tags

- idor
- parameter-omission
