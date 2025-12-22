---
id: proc-pulse-auth-2019
tags:
  - pulse-secure
  - authentication
  - credential-reuse
  - cve-2019-11510
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:26:17.753Z'
skill_level: basic
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Credentials In Files]]'
---
# Authenticate to Pulse Secure SSL VPN Using Stolen Credentials

## Summary

This procedure uses credentials stolen via pre-auth file reading to authenticate to the Pulse Secure SSL VPN, gaining access to protected resources and enabling post-auth exploits.

## Description

After extracting plaintext credentials from system files, log in to the VPN portal. This step bridges initial access to authenticated operations, targeting the /dana-na/auth/welcome.html endpoint. Prerequisites: valid creds from prior exploitation. Expected outcomes: session establishment for further attacks like RCE.

## Requirements

1. Stolen username and password from file read
2. Network access to VPN login portal
3. Browser or HTTP client for login

## Defense

Defensive measures and detection strategies:

- Rotate credentials regularly and use MFA
- Monitor authentication logs for unusual IP origins
- Implement rate limiting on login attempts
- Audit for weak or default credential storage

## Objectives

1. Gain authenticated session to VPN
2. Access post-auth endpoints
3. Prepare for command injection

## Instructions

### Step 1: Access Login Portal

**Context**: Navigate to the authentication page.

**Command** (Browser or curl):
```bash
curl -k https://target-vpn.com/dana-na/auth/welcome.html
```

> This fetches the login form. Expected output: HTML login page.

### Step 2: Submit Credentials

**Context**: Post the stolen creds to authenticate.

**Command** (Using curl for POST):
```bash
curl -k -d "username=stolen_user&password=stolen_pass" https://target-vpn.com/dana-na/auth/url_default/welcome.cgi
```

> Replace with actual creds. Expected output: Redirect to dashboard or success message.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]
- [[Credentials In Files]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[pulse-secure]]
- [[authentication]]
- [[credential-reuse]]
- [[cve-2019-11510]]
