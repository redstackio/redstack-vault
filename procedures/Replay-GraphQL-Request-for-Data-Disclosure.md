---
id: proc-uuid-3
tags:
  - session-replay
  - graphql-replay
  - data-disclosure
  - burp-repeater
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:25:53.654Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[T1539.001]]'
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Replay-GraphQL-Request-for-Data-Disclosure

## Summary

This procedure replays a captured GraphQL request in Burp Repeater after session revocation to demonstrate insufficient expiration, resulting in unauthorized disclosure of sensitive HackerOne user data.

## Description

Exploiting the gap in HackerOne's session revocation where GraphQL sessions are not invalidated, this procedure sends a previously captured query post-logout. The target is the GraphQL endpoint at https://hackerone.com/graphql. Prerequisites include a captured request from an authenticated session and Burp Suite. Expected outcomes: Successful response with sensitive data like bounties, reports, and payment info, confirming the vulnerability.

## Requirements

1. Captured GraphQL POST request with session token
2. Burp Suite Repeater module active
3. Revoked session (post-logout state)
4. Network access to https://hackerone.com/graphql

## Defense

Defensive measures and detection strategies:

- Synchronize session revocation across all endpoints, including GraphQL
- Use stateless tokens with revocation lists or short expiration times
- Monitor for replayed requests with revoked tokens via anomaly detection in API logs
- Rate-limit GraphQL queries and validate token freshness

## Objectives

1. Replay the GraphQL query using revoked session token
2. Verify successful execution and data access
3. Disclose sensitive information to assess impact

## Instructions

### Step 1: Send Captured Request to Repeater

**Context**: Prepare the intercepted request for replay in an isolated module.

In Burp Proxy, right-click the captured GraphQL POST and select 'Send to Repeater'.

> Expected output: Request loaded in Repeater tab with original headers, body, and token.

### Step 2: Replay the Request

**Context**: Execute the request post-revocation to test persistence.

In Repeater, click 'Send' to POST the request to https://hackerone.com/graphql.

**Technical Details**: Include the original Authorization header and body: {"query":"query User_bounty_settings_page..."}, variables {"first_0":100,"currency_1":"USD","currency_2":"XLA"}.

> Expected output: 200 OK response with JSON data.

### Step 3: Analyze Response for Disclosure

**Context**: Inspect the response to confirm sensitive data access.

Review the JSON response in Repeater for fields like bounties, awarded amounts, report titles, teams, payment methods.

> Expected output: Detailed user data returned, e.g., {"data":{"me":{"bounties":[{"amount":1000,"title":"Report XYZ"}],"paymentPreferences":["Wire"]} }}.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Steal Web Session Cookie]]

### Sub-Techniques

- [[T1539.001]]

## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- session-replay
- graphql
- info-disclosure
