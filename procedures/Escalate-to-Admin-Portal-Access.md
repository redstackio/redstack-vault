---
id: proc-uuid-003
name: Escalate-to-Admin-Portal-Access
tags:
  - privilege-escalation
  - admin-access
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
commands:
  - '[[commands/curl-admin-login]]'
  - '[[commands/httpx-probe]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:20.505Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Escalate-to-Admin-Portal-Access

## Summary

Using data extracted from SQLi, this procedure attempts to authenticate to the administrator portal, escalating from data access to full control over the application.

## Description

After dumping credentials via SQLi in forgot_password.jsp, this targets related admin endpoints (e.g., /admin/login.jsp) on platforms like gmmovinparts.com. It leverages valid accounts obtained from the database. Prerequisites: Extracted credentials. Outcomes: Session hijack or admin dashboard access.

## Requirements

1. Extracted credentials from prior SQLi
2. Target admin URL and login parameters
3. Cookie handling for session persistence

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication for admin portals
- Rate-limit login attempts and monitor for credential stuffing
- Use session tokens with short expiration

## Objectives

1. Authenticate using leaked admin credentials
2. Verify access to privileged features
3. Explore for further persistence

## Instructions

### Step 1: Attempt Admin Login

**Context**: Submit extracted credentials to the admin login endpoint.

**Command** ([[commands/curl-admin-login]]):
```bash
curl -X POST https://gmmovinparts.com/admin/login.jsp -d "username=admin&password=extracted_hash" -c cookies.txt -v
```

> Successful login returns a session cookie. Expected output: HTTP 302 redirect to dashboard.

### Step 2: Probe Admin Endpoints

**Context**: Validate and enumerate accessible admin paths.

**Command** ([[commands/httpx-probe]]):
```bash
httpx -l admin-endpoints.txt -status-code
```

> Probes a list of potential admin URLs. Output shows live endpoints with 200 status.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Lateral Movement]]

### Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-admin-login]]
- [[commands/httpx-probe]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[privilege-escalation]]
- [[admin-access]]
- [[web]]
