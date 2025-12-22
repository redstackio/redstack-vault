---
id: proc-uuid-002
name: Bypass-Broken-Access-Controls-in-Admin-Panel
tags:
  - broken-access-control
  - privilege-escalation
  - admin-bypass
  - web
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T03:46:26.391Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Bypass-Broken-Access-Controls-in-Admin-Panel

## Summary

This procedure exploits insufficient access controls in the IBM access control panel's admin interface, allowing unauthorized users to perform administrative operations by directly accessing restricted endpoints without proper authentication or role checks.

## Description

Broken access control in the admin panel enables attackers to infer and access admin functions, such as user management or system configuration, by manipulating URLs, parameters, or session data obtained from prior exploits like SQL injection. The target environment is a web-based admin panel with flawed authorization logic. Prerequisites include initial access to the application and any elevated data from database queries. This vulnerability was identified alongside SQLi in a HackerOne report, leading to unauthorized admin access.

## Requirements

1. Access to the web application and admin panel URLs
2. Elevated privileges or data (e.g., admin IDs) from prior SQLi exploitation
3. Web proxy tool for request manipulation

## Defense

Defensive measures and detection strategies:

- Enforce role-based access control (RBAC) with server-side enforcement
- Implement proper session management and token validation
- Log and monitor access to admin endpoints for anomalies
- Use multi-factor authentication (MFA) for admin functions

## Objectives

1. Gain unauthorized entry to the admin panel
2. Execute administrative operations like data modification
3. Achieve persistent or escalated control over the system

## Instructions

### Step 1: Identify Admin Endpoints

**Context**: From application reconnaissance or SQLi dumps, locate admin panel URLs (e.g., /admin/users). Attempt direct access without authentication.

**Instructions**: Navigate to the suspected admin URL in a browser or via curl. If accessible, the broken control is confirmed.

```bash
curl -X GET "https://target.ibm.com/admin/dashboard" -v
```

> Expected output: HTTP 200 response with admin page content, instead of 403 Forbidden.

### Step 2: Manipulate Parameters for Access

**Context**: Use obtained data (e.g., admin user_id) to bypass checks by altering request parameters.

**Instructions**: Intercept a user request with a proxy, change role= user to role=admin or user_id=1 (admin ID), and forward to the admin endpoint.

For example:

```bash
curl -X POST "https://target.ibm.com/admin/users" -d "user_id=1&action=delete" -H "Cookie: session=abc123" -v
```

> Expected output: Successful admin action, such as user deletion confirmation, indicating bypass success.

### Step 3: Validate and Execute Admin Operations

**Context**: Perform test operations to confirm full access and scope.

**Instructions**: Execute a low-impact admin function, like viewing logs, then escalate to modifications.

**Expected Output**: Admin dashboard loads with full functionality.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- broken-access-control
- admin-bypass
- web
