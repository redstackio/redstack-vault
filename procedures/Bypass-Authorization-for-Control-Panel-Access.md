---
id: proc-bypass-auth-choice-av-ru
tags:
  - authorization-bypass
  - missing-auth
  - web-vuln
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-access-endpoint]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:59.117Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass Authorization for Control Panel Access

## Summary

This procedure exploits missing authorization checks in the choice.av.ru web application to allow unauthenticated users to access the administrative control panel, potentially enabling sensitive data exposure or unauthorized modifications.

## Description

The vulnerability stems from a lack of proper authorization enforcement on administrative endpoints. During a security assessment, attackers can directly access URLs like `/admin` or similar paths without authentication tokens or sessions. This leads to medium-severity impact, as unauthorized users can view or interact with admin functions such as user management or system configurations. The target environment is a web platform, requiring only public internet access.

## Requirements

1. Network access to choice.av.ru over HTTP/HTTPS
2. A web browser or command-line tool like curl for testing
3. No authentication credentials or prior session needed

## Defense

Defensive measures and detection strategies:

- Implement server-side authorization checks on all admin endpoints using role-based access control (RBAC)
- Use web application firewalls (WAF) to block unauthenticated access to sensitive paths
- Monitor access logs for anomalous requests to admin URLs from unauthenticated IPs

## Objectives

1. Gain unauthorized access to the control panel
2. Identify and potentially exploit exposed administrative features
3. Demonstrate the impact of broken access controls

## Instructions

### Step 1: Identify and Access Admin Endpoint

**Context**: Locate the control panel URL through common administrative paths and attempt direct access to verify missing authorization.

**Command** ([[commands/curl-access-endpoint]]):
```bash
curl -v https://choice.av.ru/admin
```

> This command sends a GET request to the admin endpoint with verbose output to inspect headers and response. Expected output includes a 200 OK status and HTML content rendering the control panel, confirming the bypass. If redirected or denied, try variations like `/control-panel` or `/admin/dashboard`.

### Step 2: Interact with Panel Features

**Context**: Once access is confirmed, explore the panel to assess exposed functionalities, such as viewing user data or modifying settings.

**Command** ([[commands/curl-access-endpoint]]):
```bash
curl -v https://choice.av.ru/admin/users
```

> This fetches a specific admin subsection, like user management. Successful output reveals sensitive data listings. Use browser developer tools to interact further if needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-endpoint]]

## Tools Used


## Tags

- authorization-bypass
- missing-auth
- web-vuln
