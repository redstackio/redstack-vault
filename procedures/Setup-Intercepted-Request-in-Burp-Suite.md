---
id: proc-burp-setup-001
tags:
  - graphql
  - api-abuse
  - burp-suite
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:57.228Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup Intercepted Request in Burp Suite

## Summary

This procedure intercepts and customizes an HTTP request to HackerOne's GraphQL endpoint in Burp Suite, preparing it for batched report submission by replacing authentication and target placeholders.

## Description

In the context of exploiting GraphQL batching, this step involves capturing a POST request to /graphql, updating it with user credentials (Cookie and X-CSRF-Token), and setting the target team_handle. The request includes a JSON payload with operationName 'CreateReport', variables for product_area and product_feature, and a placeholder for the batched query. This sets up the foundation for rate limit bypass without triggering single-request protections.

## Requirements

1. Burp Suite installed and running with proxy interception enabled
2. Valid HackerOne session (cookie and CSRF token obtained via browser login)
3. Target team handle (e.g., from HackerOne URL)
4. Network access to hackerone.com

## Defense

Defensive measures and detection strategies:

- Implement request inspection proxies to detect unusual GraphQL payloads
- Enforce CSRF token validation and monitor for rapid request patterns from Burp-like user agents

## Objectives

1. Prepare authenticated request for GraphQL mutation
2. Avoid early detection by using legitimate session tokens
3. Enable forwarding to automation tools like Turbo Intruder

## Instructions

### Step 1: Intercept Base Request

**Context**: Start by pasting or intercepting a sample POST request to /graphql in Burp Suite's Repeater or Proxy.

No specific command; manually edit the request headers and body to include:

- Host: hackerone.com
- Cookie: {your-h1-cookie}
- X-CSRF-Token: {your-csrf-token}
- Content-Type: application/json
- X-Product-Feature: inbox
- X-Product-Area: reports

JSON payload:

```json
{
  "operationName": "CreateReport",
  "variables": {
    "team_handle": "{target-team-handle}",
    "product_area": "reports",
    "product_feature": "inbox"
  },
  "query": "{your-generated-query}"
}
```

> This creates a modifiable request template. Expected output: Valid HTTP/2 POST request with placeholders intact.

### Step 2: Replace Placeholders

**Context**: Substitute personal values to authenticate and target the program.

Manually update in Burp:

- Replace {your-h1-cookie} with actual session cookie (e.g., from browser dev tools)
- Replace {your-csrf-token} with token from HackerOne headers
- Replace {target-team-handle} with desired program (e.g., "example-team")

> Ensures the request is authenticated and directed. Expected output: No 401/403 errors on test send.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- graphql
- api-abuse
- burp-suite
