---
tags:
  - access-control-bypass
  - otp-bypass
  - improper-authentication
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-direct-endpoint-access]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: cd063025-4701-4d77-a2bd-ac7191daa7e6
created_at: '2025-12-14T17:29:57.339Z'
updated_at: '2025-12-14T17:29:57.339Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-OTP-Verification-for-Admin-Log-Download

## Summary

This procedure exploits improper access control in the Lark Technologies web application to bypass one-time password (OTP) verification, allowing any authenticated organization user to directly download sensitive admin logs without additional identity checks.

## Description

In the Lark system, downloading admin logs normally requires an OTP sent to the user's email for verification. However, the admin log download endpoint lacks proper checks for this OTP when accessed directly, enabling bypass. This vulnerability allows unauthorized exposure of confidential information such as user activities, system configurations, and internal events. The attack targets web-based SaaS platforms with flawed authentication flows and is effective against any user within the organization, potentially leading to data leakage or further compromise.

## Requirements

1. Valid user credentials for the target organization in Lark Technologies
2. Network access to the Lark web application (HTTPS)
3. Web browser or command-line tool like curl for direct endpoint access
4. Ability to extract session tokens (e.g., JWT from cookies)

## Defense

Defensive measures and detection strategies:

- Implement server-side checks for OTP verification on all sensitive endpoints, regardless of access path
- Use rate limiting and logging on admin endpoints to detect anomalous direct accesses
- Enforce role-based access control (RBAC) to restrict log downloads to admins only
- Monitor for unexpected file downloads in application logs

## Objectives

1. Access sensitive admin logs without OTP verification
2. Exfiltrate confidential organization data
3. Demonstrate impact of improper access controls

## Instructions

### Step 1: Authenticate as Organization User

**Context**: Gain initial access to the application to obtain a session token, which will be used for the bypass.

Log in to the Lark web interface using standard user credentials. Use browser developer tools (F12) to inspect network requests and extract the Authorization Bearer token from cookies or headers.

### Step 2: Identify the Admin Log Download Endpoint

**Context**: Locate the direct endpoint URL, typically revealed through application source code, API documentation, or trial-and-error navigation.

In the browser, navigate to the admin logs section (if visible) and monitor network tab for the download request URL, e.g., `https://lark.example.com/admin/logs/download`. Note any required headers like Authorization.

### Step 3: Directly Access the Endpoint

**Context**: Send a direct request to the endpoint using the session token, bypassing the UI flow that triggers OTP.

**Command** ([[commands/curl-direct-endpoint-access]]):
```bash
curl -X GET 'https://lark.example.com/admin/logs/download' -H 'Authorization: Bearer YOUR_JWT_TOKEN' -H 'Content-Type: application/json' -o admin_logs.zip
```

> This command fetches the logs directly. Expected output is a ZIP file or JSON response with log data. If successful, no OTP is prompted, confirming the bypass. Replace placeholders with actual values from Step 1 and 2.

### Step 4: Validate and Exfiltrate

**Context**: Confirm the downloaded content contains sensitive data and secure it for analysis.

Open the downloaded file to verify it includes admin-level logs. If needed, transfer the file securely to avoid detection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-direct-endpoint-access]]

## Tools Used


## Tags

- access-control-bypass
- otp-bypass
- web-vulnerability
