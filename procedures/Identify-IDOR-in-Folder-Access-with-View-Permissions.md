---
tags:
  - idor
  - web
  - discovery
  - access-control
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-delete-lark-folder]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:29.103Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 4e5ccfe4-ddcd-4267-bdd4-d9ef8a5e6d43
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Identify-IDOR-in-Folder-Access-with-View-Permissions

## Summary

This procedure tests for an Insecure Direct Object Reference (IDOR) vulnerability in web applications like Lark Technologies' platform, where a user with view-only permissions can access and manipulate (e.g., delete) folders by directly referencing their alphanumeric tokens, bypassing standard authorization checks.

## Description

In the attack scenario, an authenticated user with limited view permissions discovers that the platform's folder management API allows direct object references via tokens without validating the user's ownership or admin rights. This is identified by submitting a delete request to the folder endpoint using the token obtained from legitimate viewing. The target environment is a web-based collaborative platform handling file storage and bins. Expected outcomes include confirmation of the vulnerability through successful unauthorized actions, highlighting improper access controls that could lead to broader resource manipulation.

## Requirements

1. Authenticated session with view-only user permissions on the target platform
2. Knowledge of a target folder's alphanumeric token (e.g., extracted from URLs or API responses during normal browsing)
3. Network access to the web application API (HTTPS)

## Defense

Defensive measures and detection strategies:

- Implement server-side authorization checks to validate user permissions on referenced objects, not just authentication
- Use indirect object references (e.g., hashed IDs or session-bound tokens) instead of predictable alphanumeric tokens
- Log and monitor API requests for anomalous delete actions from low-privilege accounts; use WAF rules to flag direct token usage

## Objectives

1. Confirm the presence of IDOR by successfully attempting a privileged action (delete) with insufficient permissions
2. Map the vulnerable endpoint for further exploitation
3. Assess the scope of accessible objects via token enumeration

## Instructions

### Step 1: Prepare Authentication and Token

**Context**: Establish a session and obtain the folder token to test direct reference.

Log in to the platform with view-only credentials to get an access token (e.g., from browser cookies or API login response). Identify a target admin folder token via legitimate view access (e.g., inspect network requests in browser dev tools).

No specific command; use platform login interface.

### Step 2: Test Delete Access with Token

**Context**: Submit a delete request using the token to identify if authorization is bypassed.

**Command** ([[commands/curl-delete-lark-folder]]):
```bash
curl -X DELETE -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" https://app.lark.com/api/v1/folders/{folder_token}
```

> This command sends a DELETE request to the folder endpoint. Expected output: A successful response (e.g., {"status": "deleted"}) indicates IDOR, as view-only users should be denied. If it fails with permission error, no vulnerability.

### Step 3: Verify Pre-Deletion Access

**Context**: Confirm token validity by reading folder details before attempting delete.

Use a GET request (adapt from delete command):
```bash
curl -H "Authorization: Bearer $ACCESS_TOKEN" https://app.lark.com/api/v1/folders/{folder_token}
```

> Expected: Folder metadata returned, confirming direct reference works for reads.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques

-

## Commands Used

- [[commands/curl-delete-lark-folder]]

## Tools Used

-

## Tags

- [[idor]]
- [[web]]
- [[Discovery]]
