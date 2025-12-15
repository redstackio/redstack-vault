---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - account-takeover
  - credential-reuse
  - authentication-bypass
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/curl-login-with-stolen-creds]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:33:12.411Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Unsecured Credentials]]'
---
# Utilize-Exposed-Credentials-for-Account-Takeover

## Summary

This procedure uses credentials extracted from cleartext storage to authenticate to target services, achieving account takeover. It applies to scenarios like the IBM vulnerability where employee credentials are exposed, allowing impersonation and access to internal resources.

## Description

Following credential retrieval, this procedure involves testing and using the stolen credentials against IBM authentication endpoints or associated applications. The attack assumes the credentials are active and targets web-based login forms. Outcomes include session hijacking and potential lateral movement. Prerequisites: Valid credentials from prior exposure and knowledge of target login URLs.

## Requirements

1. Extracted credentials (username/password pairs)
2. Target authentication endpoint (e.g., IBM login portal)
3. HTTP client for POST requests

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA) on all accounts
- Rotate credentials immediately upon exposure detection
- Implement anomaly detection in auth logs for unusual login patterns
- Use credential monitoring tools to alert on leaked secrets

## Objectives

1. Authenticate using exposed credentials
2. Gain control of compromised employee accounts
3. Access sensitive data or perform unauthorized actions

## Instructions

### Step 1: Test Credential Validity on Target Service

**Context**: Attempt login with stolen credentials to verify they are active and usable for takeover.

**Command** ([[commands/curl-login-with-stolen-creds]]):
```bash
curl -X POST -d 'username=stolen_username&password=stolen_password' https://auth.ibm.com/login
```

> This simulates a login POST request. Replace placeholders with actual values from extraction. Successful output includes a token or success message; failure returns 401/403.

### Step 2: Establish Persistent Access

**Context**: Upon successful auth, capture session cookies or tokens for ongoing access to the account.

**Command** (Follow-up with cookie extraction):
```bash
curl -X POST -d 'username=stolen_username&password=stolen_password' -c cookies.txt https://auth.ibm.com/login
```

> Saves session cookies to file. Use these in subsequent requests to maintain access, e.g., curl -b cookies.txt https://ibm.com/dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Valid Accounts]]
- [[Unsecured Credentials]]

### Sub-Techniques


## Commands Used

- [[commands/curl-login-with-stolen-creds]]

## Tools Used


## Tags

- [[account-takeover]]
- [[credential-reuse]]
- [[authentication-bypass]]
