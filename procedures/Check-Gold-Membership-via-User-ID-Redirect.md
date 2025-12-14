---
id: proc-uuid-004
name: Check-Gold-Membership-via-User-ID-Redirect
tags:
  - idor
  - redirect-enumeration
  - membership-check
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-user-id-only]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:29.695Z'
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
# Check-Gold-Membership-via-User-ID-Redirect

## Summary

This procedure uses only the user_id parameter to check for Gold membership by observing a 301 redirect that reveals the associated subscription_id if the user is a member.

## Description

Supplying a user_id alone triggers a redirect for Gold members to the full endpoint with subscription_id, enabling discovery of membership status and IDs without direct access checks.

## Requirements

1. Target user_id (guessed or known)
2. HTTP client supporting redirects (-L flag in curl)

## Defense

Defensive measures and detection strategies:

- Avoid redirects that leak IDs; use 404 for non-members
- Rate-limit user_id probes
- Log redirect patterns for anomaly detection

## Objectives

1. Detect Gold membership via redirect
2. Extract subscription_id from redirect URL
3. Enable further enumeration

## Instructions

### Step 1: Request with User ID Only

**Context**: Follow redirects to capture leaked subscription_id.

**Command** ([[commands/curl-user-id-only]]):
```bash
curl -X GET "https://www.zomato.com/gold/payment-success?user_id=███████" -i -L
```

> Expected output: 301 to ?subscription_id=212504 for members; no redirect otherwise.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-user-id-only]]

## Tools Used


## Tags

- redirect-enumeration
- membership-check
