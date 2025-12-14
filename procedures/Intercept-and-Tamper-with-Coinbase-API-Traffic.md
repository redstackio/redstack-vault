---
tags:
  - api-interception
  - replay-attack
  - tampering
  - oauthtoken-theft
  - android
type: procedure
tools:
  - '[[tools/Charles-Proxy]]'
tactics:
  - '[[Collection]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Android
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Local Accounts]]'
updated_at: '2025-12-14T17:24:40.192Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 40669c38-1854-42ff-8277-9400137a4252
validated: true
mitre_tactics:
  - '[[Collection]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Local Accounts]]'
---
# Intercept-and-Tamper-with-Coinbase-API-Traffic

## Summary

This procedure uses the configured MITM proxy to monitor, decrypt, and manipulate Coinbase API requests from the Android app, exploiting insecure API design to view hardcoded credentials and OAuth tokens in plaintext, replay transactions (e.g., repeated bitcoin purchases), and modify requests (e.g., alter transfer amounts or recipients), leading to potential financial loss or account hijacking.

## Description

With SSL bypassed, Charles Proxy decrypts HTTPS requests to endpoints like buy/sell/send bitcoin, revealing plaintext consumer ID/secret and access tokens for full API control. The API lacks HMAC signing, nonces, or other protections, relying only on SSL (now compromised) for integrity, allowing easy tampering and replays under MITM conditions. The target environment is the proxied Android device running the Coinbase app on a controlled network. Prerequisites: Completed proxy setup with CA installed. Expected outcomes: Stolen tokens for external API abuse, demonstrated transaction modifications, and replay attacks draining accounts.

## Requirements

1. Charles Proxy configured and traffic routed (from prior procedure)
2. Android device with Coinbase app logged in
3. Knowledge of API endpoints (e.g., /api/v1/transactions/buy)

## Defense

Defensive measures and detection strategies:

- Add application-level signing (e.g., HMAC with nonces) to API requests to prevent tampering/replays
- Implement token binding or short-lived JWTs to limit intercepted token utility
- Monitor for anomalous API patterns like repeated transactions from single IPs

## Objectives

1. Intercept and view sensitive API data including tokens and credentials
2. Modify request parameters to alter transactions
3. Replay requests to execute unauthorized actions

## Instructions

### Step 1: Monitor App Interactions

**Context**: Launch the app and perform actions to generate API traffic for interception.

No specific command; open Coinbase app, login, and initiate a transaction (e.g., buy $10 bitcoin).

> In Charles, filter for coinbase.com; requests/responses appear in plaintext, showing consumer ID/secret and OAuth access_token.

### Step 2: View and Extract Sensitive Data

**Context**: Inspect decrypted requests to steal credentials and tokens.

No specific command; select a request in Charles Overview, view Structure or Raw tabs.

> Extract access_token from Authorization header for external use; note lack of pinning allowed this decryption.

### Step 3: Modify and Replay Requests

**Context**: Tamper with transaction details and replay to demonstrate impact.

No specific command; right-click a request in Charles > Edit > modify JSON (e.g., change "amount": "10" to "100", or "recipient": "attacker_wallet"), then Repeat.

> For replay: Select buy request > Repeat Advanced > execute multiple times. API accepts without nonce checks, potentially draining linked bank.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection
- [[Execution]] Execution

### Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie
- [[Local Accounts]] Application Layer Protocol

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Charles-Proxy]]

## Tags

- api-interception
- replay-attack
