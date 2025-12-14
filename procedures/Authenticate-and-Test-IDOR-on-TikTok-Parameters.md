---
id: proc-tiktok-idor-test-1
tags:
  - idor
  - authentication
  - parameter-manipulation
  - tiktok
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-modify-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:27.065Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Authenticate-and-Test-IDOR-on-TikTok-Parameters

## Summary

This procedure authenticates a user as an Analyst on TikTok Business and tests for IDOR by manipulating org_id and account_id parameters in API requests to access unauthorized resources.

## Description

In the context of TikTok Business, Analyst users can escalate privileges via IDOR in endpoints handling ads management. The procedure involves logging in, capturing requests, and altering object references to probe for access control bypasses, potentially revealing data from other organizations. Prerequisites include valid Analyst credentials and tools for request interception.

## Requirements

1. Valid Analyst credentials for TikTok Business account
2. Access to Business.TikTok.com over HTTPS
3. Burp Suite or similar proxy for request manipulation

## Defense

Defensive measures and detection strategies:

- Implement proper server-side authorization checks on org_id and account_id
- Log and monitor parameter manipulations in API requests
- Use session-based access tokens tied to specific org/account scopes

## Objectives

1. Confirm authenticated access to the platform
2. Identify IDOR by accessing unauthorized resources
3. Gather evidence of insufficient access controls

## Instructions

### Step 1: Authenticate as Analyst

**Context**: Log in to establish a session for testing.

**Command** ([[commands/curl-modify-request]]):
```bash
# Not directly applicable; use browser or API client to login
# Example: curl -X POST 'https://business.tiktok.com/api/login' -d 'username=analyst&password=pass'
```

> Successful login returns an Authorization Bearer token. Store this for subsequent requests.

### Step 2: Capture and Modify Request Parameters

**Context**: Intercept a legitimate API request and alter org_id/account_id to test access.

**Command** ([[commands/curl-modify-request]]):
```bash
curl -X GET 'https://business.tiktok.com/api/ads?org_id=YOUR_ORG&account_id=YOUR_ACC' \
  -H 'Authorization: Bearer TOKEN' \
  -d 'org_id=TARGET_ORG_ID&account_id=TARGET_ACCOUNT_ID'
```

> If IDOR exists, the response will include data from the target org/account without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-modify-request]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- idor
- tiktok
- web
