---
tags:
  - auth
  - cookie
  - login
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-login-starbucks]]'
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 1da139d3-12a7-4378-80b3-22fb09c8b444
created_at: '2025-12-14T17:31:52.945Z'
updated_at: '2025-12-14T17:31:52.945Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Obtain-Starbucks-Auth-Cookie

## Summary

This procedure authenticates a user to the Starbucks web application at app.starbucks.com to obtain a valid session cookie, which can later be misused in combination with path traversal attacks to access restricted areas.

## Description

The Starbucks app requires user authentication to establish a session. By performing a standard login, an attacker can capture the authentication cookie (typically a session ID or JWT token) from the response. This cookie grants legitimate access but, due to poor path validation elsewhere, allows traversal beyond intended boundaries. Prerequisites include valid credentials, which could be obtained via phishing or purchased. The procedure targets the login endpoint and assumes form-based authentication.

## Requirements

1. Valid username and password for a Starbucks account.
2. Network access to https://app.starbucks.com.
3. Tools like curl or a browser for capturing cookies.

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) to prevent credential misuse.
- Monitor login attempts for anomalies, such as unusual IP locations.
- Use cookie flags like HttpOnly and Secure to limit exposure.

## Objectives

1. Establish a valid session with the target application.
2. Capture the authentication cookie for reuse.
3. Enable subsequent exploitation without re-authentication.

## Instructions

### Step 1: Prepare Login Request

**Context**: Set up the HTTP client to handle cookies and submit credentials to the login endpoint.

**Command** ([[commands/curl-login-starbucks]]):
```bash
curl -c cookies.txt -d "username=validuser&password=validpass" -X POST https://app.starbucks.com/login
```

> This command sends a POST request with credentials and saves cookies to a file. Expected output: HTTP 200/302 with Set-Cookie header in response.

### Step 2: Verify and Extract Cookie

**Context**: Inspect the cookie file to confirm the session token is captured and valid.

**Command** ([[commands/curl-login-starbucks]]):
```bash
cat cookies.txt
```

> Look for entries like #HttpOnly_app.starbucks.com	TRUE	/	FALSE	0	session_id	abc123. Use this token in headers for authenticated requests.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-login-starbucks]]

## Tools Used

- None

## Tags

- [[auth]]
- [[cookie]]
- [[web]]
