---
id: proc-uuid-001
tags:
  - brute-force
  - throttling
  - graphql
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-invalid-login]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:32:28.903Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Trigger-Login-Throttle-with-Invalid-Passwords

## Summary

This procedure simulates multiple failed login attempts to Shopify's customerAccessTokenCreate mutation using invalid passwords, activating the API's throttling mechanism which limits further invalid submissions but does not affect valid ones.

## Description

In the context of testing Shopify StoreFront API vulnerabilities, this step exhausts the authentication attempt limit by repeatedly submitting incorrect credentials via GraphQL mutation. The root cause is that throttling is only enforced for invalid passwords, setting up a bypass for subsequent valid attempts. Prerequisites include access to the StoreFront API endpoint and a target customer email. Expected outcome is an error response indicating the limit has been exceeded, confirming the throttle is active.

## Requirements

1. Network access to the Shopify StoreFront API (e.g., https://store.myshopify.com/api/2023-01/graphql.json)
2. Valid storefront access token for API calls
3. Target customer email address
4. curl or similar HTTP client

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on all authentication attempts, regardless of validity
- Monitor for spikes in failed login attempts from single IPs
- Use CAPTCHA or multi-factor authentication post-failed attempts

## Objectives

1. Activate throttling to test bypass potential
2. Confirm vulnerability by observing error responses
3. Prepare for valid credential testing

## Instructions

### Step 1: Prepare GraphQL Mutation for Invalid Login

**Context**: Craft a GraphQL mutation payload with an invalid password to trigger failed authentication.

**Command** ([[commands/curl-invalid-login]]):
```bash
curl -X POST https://target-store.myshopify.com/api/2023-01/graphql.json \
  -H 'Content-Type: application/json' \
  -H 'X-Shopify-Storefront-Access-Token: your_token_here' \
  -d '{"query": "mutation customerAccessTokenCreate($input: CustomerAccessTokenCreateInput!) { customerAccessTokenCreate(input: $input) { customerAccessToken { accessToken } userErrors { field message } } }", "variables": {"input": {"email": "target@example.com", "password": "wrongpass123"}}}'
```

> This sends a POST request with the mutation. On first runs, expect a standard invalid credential error. Repeat 5-10 times to hit the limit.

### Step 2: Repeat Until Throttle Activates

**Context**: Automate or manually repeat the command until the 'Login attempt limit exceeded' error appears.

**Command** ([[commands/curl-invalid-login]]):
```bash
# Run in a loop: for i in {1..10}; do curl ... (as above); sleep 1; done
```

> Expected output after limit: JSON with userErrors message 'Login attempt limit exceeded'. This confirms success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-invalid-login]]

## Tools Used

- None

## Tags

- [[brute-force]]
- [[throttling]]
- [[graphql]]
