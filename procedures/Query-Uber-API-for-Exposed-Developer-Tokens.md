---
tags:
  - information-disclosure
  - api-vulnerability
  - token-exposure
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/curl-api-query-with-auth]]'
platforms:
  - Web
techniques:
  - '[[Unsecured Credentials]]'
skill_level: basic
impact_level: high
detection_risk: low
sub_techniques: []
id: f1977292-8200-4bcc-96a4-518bf9ce32b7
created_at: '2025-12-14T17:32:48.434Z'
updated_at: '2025-12-14T17:32:48.434Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Query Uber API for Exposed Developer Tokens

## Summary

This procedure exploits an information disclosure vulnerability in Uber's internal API endpoint on riders.uber.com, which returns sensitive client secrets and server tokens for third-party developer applications authorized to access the user's Uber account without proper access controls or data filtering.

## Description

The vulnerability allows any authenticated user to query the API and receive unredacted sensitive data, such as client_secret and server_token, for developer apps linked to their account. An attacker with user-level access can use this to extract tokens, potentially enabling impersonation of authorized applications, data exfiltration from the user's Uber account, or further abuse of third-party integrations. The attack requires only standard user authentication and a simple API request; no advanced exploitation is needed. Uber mitigated this by restricting the endpoint's response to exclude sensitive fields.

## Requirements

1. Valid Uber user account and authentication token (e.g., Bearer token from login)
2. Network access to https://riders.uber.com/
3. Tool for making HTTP requests (e.g., curl or browser developer tools)

## Defense

Defensive measures and detection strategies:

- Implement data filtering on API responses to exclude sensitive fields like client_secret and server_token
- Enforce least-privilege access controls on internal endpoints, ensuring only necessary data is returned
- Monitor API logs for anomalous queries to developer app endpoints and rate-limit requests
- Use token scoping to limit exposure of third-party credentials in user-facing APIs

## Objectives

1. Retrieve exposed client secrets and server tokens from the Uber API
2. Enable potential misuse of tokens for unauthorized access to user-linked applications
3. Demonstrate information disclosure impact on third-party integrations

## Instructions

### Step 1: Obtain Authentication Token

**Context**: Authenticate as a user to gain a session token required for API access.

Log in to the Uber riders portal via web or app to capture the auth token from network requests (e.g., using browser dev tools).

### Step 2: Query the Vulnerable Endpoint

**Context**: Send an authenticated GET request to the internal API endpoint that handles developer applications, exploiting the lack of filtering to disclose secrets.

**Command** ([[commands/curl-api-query-with-auth]]):
```bash
curl -H "Authorization: Bearer YOUR_AUTH_TOKEN" \
     -H "Content-Type: application/json" \
     https://riders.uber.com/api/v1/developer-apps \
     -X GET
```

> This command sends a GET request to the vulnerable endpoint with the user's auth token. The response will include JSON data with fields like client_secret and server_token for each authorized developer app. Replace YOUR_AUTH_TOKEN with the actual Bearer token obtained from login. Successful execution returns sensitive token data, confirming the disclosure.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques


## Commands Used

- [[commands/curl-api-query-with-auth]]

## Tools Used


## Tags

- information-disclosure
- api-vulnerability
- token-exposure
