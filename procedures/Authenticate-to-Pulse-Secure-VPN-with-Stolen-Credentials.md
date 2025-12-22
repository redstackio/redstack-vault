---
tags:
  - vpn-auth
  - valid-accounts
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:26:22.443Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques:
  - '[[Default Accounts]]'
id: f6743872-82db-42be-836d-40735f507819
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-to-Pulse-Secure-VPN-with-Stolen-Credentials

## Summary

This procedure uses extracted plaintext credentials to authenticate to the Pulse Secure SSL VPN, gaining post-auth access for further exploitation.

## Description

With creds from prior steps, submit a login to the /dana-na/auth endpoint. This transitions from unauthenticated to authenticated context, enabling RCE. Prerequisites: Valid creds and session handling.

## Requirements

1. Extracted username/password
2. Network access to VPN
3. Cookie jar for session persistence

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA)
- Monitor for unusual login attempts from external IPs
- Rate-limit login endpoints
- Alert on credential use patterns

## Objectives

1. Establish authenticated session
2. Access protected VPN resources
3. Set up for post-auth exploits

## Instructions

### Step 1: Submit Login Request

**Context**: POST creds to the auth endpoint using curl.

**Command**:
```bash
curl -k -c cookies.txt -d "username=stolen_user&password=stolen_pass" https://target-vpn/dana-na/auth/url_default/welcome.cgi
```

> Saves session cookies; expected output: Redirect to dashboard.

### Step 2: Verify Authentication

**Context**: Request a protected page to confirm session.

**Command**:
```bash
curl -k -b cookies.txt https://target-vpn/dana-na/home.cgi
```

> Expected output: Authenticated content, not login page.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

- [[Default Accounts]]

## Commands Used

## Tools Used

- [[tools/curl]]

## Tags

- authentication
- stolen-creds
