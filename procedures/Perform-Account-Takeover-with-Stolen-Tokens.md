---
tags:
  - account-takeover
  - session-hijacking
  - pii-leakage
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/get-tabbed-home]]'
  - '[[commands/get-userdetails]]'
  - '[[commands/post-auth]]'
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
  - '[[Use Alternate Authentication Material]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 5ddee77e-3e4f-47f0-8ff2-ddf31c66b029
created_at: '2025-12-13T09:01:26.160Z'
updated_at: '2025-12-13T09:01:26.160Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Use Alternate Authentication Material]]'
---
# Perform Account Takeover with Stolen Tokens

## Summary

This procedure uses stolen X-Access-Tokens to query user endpoints, extract PII, and impersonate victims for full account takeover on Zomato.

## Description

Stolen tokens allow access to user details without authentication, enabling extraction of UserID, names, phones, emails, and session swapping during login for persistent access.

## Requirements

1. Stolen X-Access-Token from previous steps
2. Burp Suite for request interception and modification
3. Target API endpoints

## Defense

Defensive measures and detection strategies:

- Implement token binding and short expiration
- Monitor for anomalous API access patterns

## Objectives

1. Extract victim UserID and PII
2. Impersonate user sessions
3. Achieve mass takeovers

## Instructions

### Step 1: Extract UserID

**Context**: Query home endpoint with token.

**Command** ([[commands/get-tabbed-home]]):
```http
GET /v2/tabbed/home HTTP/1.1
```

> Parse response for UserID.

### Step 2: Leak PII

**Context**: Fetch user details.

**Command** ([[commands/get-userdetails]]):
```http
GET /v2/userdetails.json/<USERID> HTTP/1.1
```

> Replace <USERID> with extracted value; obtain name, phone, email.

### Step 3: Session Takeover

**Context**: Intercept and swap during login.

**Command** ([[commands/post-auth]]):
```http
POST /v2/auth HTTP/1.1
```

> Modify request with victim's token/UserID for impersonation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Valid Accounts]]
- [[Use Alternate Authentication Material]]

### Sub-Techniques



## Commands Used

- [[commands/get-tabbed-home]]
- [[commands/get-userdetails]]
- [[commands/post-auth]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[account-takeover]]
- [[session-hijacking]]
- [[pii-leakage]]
