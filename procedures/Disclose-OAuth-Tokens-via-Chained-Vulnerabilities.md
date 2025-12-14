---
tags:
  - information-disclosure
  - oauth-token-theft
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/curl-chained-disclosure]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:24:35.440Z'
sub_techniques: []
id: 5eb1823a-c376-48bb-ab5a-3a42ef14c5f3
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Disclose OAuth Tokens via Chained Vulnerabilities

## Summary

This procedure chains an image injection vulnerability with unspecified weaknesses to disclose sensitive OAuth tokens, potentially allowing unauthorized access to authenticated services.

## Description

Following image injection on the Bully Anniversary Edition endpoint, attackers can leverage additional flaws (e.g., improper token handling or internal endpoint exposure) to force disclosure of OAuth tokens. This occurs under conditions where the injected image triggers requests to internal OAuth services, leaking tokens in responses. The procedure assumes a web environment with OAuth integration and focuses on high-impact credential theft.

## Requirements

1. Successful image injection from prior step
2. Knowledge of internal OAuth endpoints (inferred from chaining)
3. HTTP interception tools to capture leaked tokens

## Defense

Defensive measures and detection strategies:

- Scope OAuth tokens tightly and avoid exposure in public responses
- Implement rate limiting and anomaly detection on image processing endpoints
- Log and alert on requests to internal resources from public paths

## Objectives

1. Trigger disclosure of OAuth tokens via chained exploit
2. Capture and validate stolen tokens
3. Enable follow-on access to protected resources

## Instructions

### Step 1: Craft Chained Payload

**Context**: Modify the image injection to target internal OAuth resources.

**Command** ([[commands/curl-chained-disclosure]]):
```bash
curl -X GET "https://www.rockstargames.com/bully/anniversaryedition?image=http://internal.oauth.service/token" -v
```

> This injects an internal URL into the image parameter. Expected output reveals token in response headers or body if chaining succeeds.

### Step 2: Intercept and Extract Token

**Context**: Use a proxy to capture any disclosed tokens during the request.

**Command** ([[commands/curl-chained-disclosure]]):
```bash
curl -X GET "https://www.rockstargames.com/bully/anniversaryedition?image=http://internal.oauth.service/token" -D - -o response.html
```

> The -D flag dumps headers. Search for 'Authorization: Bearer <token>' or similar in output to extract the OAuth token.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques


## Commands Used

- [[commands/curl-chained-disclosure]]

## Tools Used


## Tags

- [[information-disclosure]]
- [[oauth-token-theft]]
