---
id: proc-uuid-001
name: Trigger-Rate-Limiting-on-GraphQL-Login
tags:
  - rate-limit
  - graphql
  - login
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/curl-invalid-login]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:33:24.275Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Trigger-Rate-Limiting-on-GraphQL-Login

## Summary

This procedure sends invalid login credentials to a GraphQL endpoint to trigger the server's rate limiting mechanism, revealing improper enforcement that allows subsequent valid attempts to bypass the wait period.

## Description

In scenarios targeting web applications with GraphQL APIs, such as login systems, rate limiting is intended to prevent brute-force attacks by throttling excessive failed attempts. However, if the implementation fails to block all subsequent requests during the cool-down, attackers can chain failed logins to trigger the limit and then immediately attempt valid credentials for account access. This procedure focuses on the initial triggering step using tools like Burp Suite to simulate failed attempts on endpoints like /graphql with LogInUserMutation.

## Requirements

1. Network access to the target web application (HTTPS)
2. Burp Suite or equivalent proxy for request interception
3. Known login endpoint URL (e.g., https://target.com/graphql)
4. Invalid test credentials (e.g., fake email and password)

## Defense

Defensive measures and detection strategies:

- Implement strict rate limiting that blocks all requests from the IP/session during the throttle period, regardless of credential validity
- Monitor for patterns of rapid failed logins followed by successes
- Enforce CAPTCHA or secondary factors after throttle triggers

## Objectives

1. Activate rate limiting to test enforcement flaws
2. Confirm 429 responses with wait periods
3. Set up conditions for bypass testing

## Instructions

### Step 1: Intercept and Modify Login Request

**Context**: Use Burp Suite to capture the initial login POST request and alter credentials to invalid values, simulating a failed attempt.

**Command** ([[commands/curl-invalid-login]]):
```bash
curl -X POST https://dubsmash.com/graphql \
  -H "Content-Type: application/json" \
  -d '{"query":"mutation LogInUser($input: LogInUserInput!) { logInUser(input: $input) { ... on LogInUserSuccess { token } } }","variables":{"input":{"email":"wrongcredentials@gmail.com","password":"password","client_id":"client_id","client_secret":"client_secret"}}}' -c cookies.txt -v
```

> This sends a GraphQL mutation with invalid credentials, expecting a failure response. Repeat 5-10 times to approach the rate limit threshold. Output includes error details or 200 with auth failure.

### Step 2: Verify Initial Responses

**Context**: Check responses to ensure failed logins are processed without immediate throttling.

**Command** ([[commands/curl-invalid-login]]):
```bash
curl -X POST https://dubsmash.com/graphql \
  -H "Content-Type: application/json" \
  -d '{"query":"mutation LogInUser($input: LogInUserInput!) { logInUser(input: $input) { ... on LogInUserSuccess { token } } }","variables":{"input":{"email":"wrongcredentials@gmail.com","password":"password","client_id":"client_id","client_secret":"client_secret"}}}' -c cookies.txt -s | jq .
```

> Use jq for JSON parsing if available; expect auth error messages in the response body.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques


## Commands Used

- [[commands/curl-invalid-login]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- rate-limit
- graphql
- brute-force
