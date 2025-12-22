---
tags:
  - pii-leak
  - token-usage
type: procedure
tools:
  - '[[tools/Custom-HTTP-Smuggling-Tools]]'
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/smuggle-request-basic]]'
  - '[[commands/smuggle-request-token-theft]]'
  - '[[commands/smuggle-request-triage]]'
  - '[[commands/get-userid]]'
  - '[[commands/get-userdetails]]'
  - '[[commands/post-auth]]'
platforms:
  - Web
techniques:
  - '[[Use Alternate Authentication Material]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: c3fa046c-d01c-4a74-8543-27655a71849e
created_at: '2025-12-11T06:10:24.513Z'
updated_at: '2025-12-11T06:10:24.513Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1550]]'
---
# Retrieve UserID and PII with Stolen Token

## Summary

This procedure uses a stolen access token to query API endpoints for UserID and personal identifiable information (PII).

## Description

After obtaining a victim's X-Access-Token, send authenticated GET requests to retrieve UserID and then detailed PII, enabling data exfiltration in compromised API environments.

## Requirements

1. Stolen X-Access-Token
2. Access to Zomato API endpoints
3. HTTP client for sending requests

## Defense

Defensive measures and detection strategies:

- Implement token validation and rate limiting
- Monitor API access for unusual patterns

## Objectives

1. Obtain UserID from token
2. Leak PII details
3. Support further compromise

## Instructions

### Step 1: Get UserID

**Context**: Query home endpoint.

Execute [[commands/get-userid]]:

```bash
GET /v2/tabbed/home HTTP/1.1
```

> Response includes UserID.

### Step 2: Get PII

**Context**: Query user details.

Execute [[commands/get-userdetails]]:

```bash
GET /v2/userdetails.json/<USERID> HTTP/1.1
```

> Returns name, phone, email.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Use Alternate Authentication Material]]

### Sub-Techniques



## Commands Used

- [[commands/get-userid]]
- [[commands/get-userdetails]]

## Tools Used



## Tags

- [[pii-leak]]
- [[token-usage]]
