---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - path-traversal
  - file-read
  - expressionengine
  - php
  - web
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Exploit-Path-Traversal-in-ExpressionEngine]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:21.856Z'
description: >-
  A non-authenticated attacker exploits a path traversal vulnerability in
  ExpressionEngine to read arbitrary files, leading to sensitive information
  disclosure.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Non-Authenticated Path Traversal in ExpressionEngine for Arbitrary File Read

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Path Traversal] --> B[Arbitrary File Read]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP client like curl)

### Target Environment

- Web platform running ExpressionEngine (PHP-based CMS)
- Vulnerable version affected by CVE-2021-44534
- No authentication required

### Initial Access Requirements

- Network access to the ExpressionEngine instance
- No credentials needed
- Public-facing web application

## Detailed Attack Procedures

### Step 1: Exploit Path Traversal for File Disclosure
procedure: [[procedures/Exploit-Path-Traversal-in-ExpressionEngine]]

**Objective**: Send a crafted request to the vulnerable endpoint to traverse directories and read sensitive files like configuration or system files.

**Instructions**: Identify the vulnerable endpoint in ExpressionEngine (typically an unspecified upload or file handling route). Use [[commands/curl-path-traversal]] to send a GET request with path traversal payloads such as multiple '../' sequences to access files outside the web root, e.g., /etc/passwd or application configs.

```bash
curl -X GET "http://target.com/vulnerable-endpoint/../../etc/passwd" -v
```

Verify the response contains file contents. Adjust the payload depth (e.g., ../../../) based on the directory structure.

**Expected Output**: HTTP response body displaying the contents of the targeted file, such as user accounts from /etc/passwd.

**Success Indicators**:
- Response includes arbitrary file contents
- No authentication prompt or error indicating access denial
- File path traversal confirmed by reading known sensitive files
