---
id: proc-uuid-001
tags:
  - authorization-bypass
  - web-exploit
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-access-findusers]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:44.936Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Findusers-Script-Without-Authentication

## Summary

This procedure tests direct access to the ImpressCMS /include/findusers.php script without authentication to confirm initial access restrictions before attempting bypass.

## Description

In ImpressCMS, the /include/findusers.php script is intended for authenticated users to search for other users, but lacks proper auth checks. This step verifies the endpoint exists and is protected, providing baseline for the token bypass. It targets PHP-based web apps vulnerable to authorization flaws, leading to potential information disclosure if bypassed.

## Requirements

1. Network access to the ImpressCMS instance
2. Web browser or curl tool
3. Target URL known (e.g., http://target.com)

## Defense

Defensive measures and detection strategies:

- Implement proper session-based authentication checks in all endpoints
- Log unauthorized access attempts to /include/findusers.php
- Use web application firewalls (WAF) to block direct script access

## Objectives

1. Confirm endpoint accessibility and initial denial
2. Identify the target for subsequent exploitation
3. Gather response details for analysis

## Instructions

### Step 1: Direct Browser Access

**Context**: Manually navigate to the script to observe restrictions without tools.

No command required; use browser to visit http://target.com/include/findusers.php.

> Expect an error or blank page indicating access denied.

### Step 2: Scripted Access Verification

**Context**: Use curl to probe the endpoint and capture HTTP status/response.

**Command** ([[commands/curl-access-findusers]]):
```bash
curl -i "http://target.com/include/findusers.php"
```

> This sends a GET request and displays headers/body. Look for 200 OK but no data, or 403/401 errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-findusers]]

## Tools Used


## Tags

- [[authorization-bypass]]
- [[web-exploit]]
