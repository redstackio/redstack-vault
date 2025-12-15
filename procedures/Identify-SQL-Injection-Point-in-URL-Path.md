---
id: proc-uuid-001
tags:
  - sqli
  - injection-point
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-http-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:22.299Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify SQL Injection Point in URL Path

## Summary

This procedure identifies a SQL injection vulnerability in URL path processing by inserting a single quote immediately after the leading slash, observing server response anomalies on targets like www.ibm.com.

## Description

In vulnerable web applications, URL paths are directly concatenated into SQL queries without sanitization, allowing injection via special characters like single quotes. This step focuses on pinpointing the injection point in any path, leading to syntax errors that reveal the vulnerability. It applies to public-facing sites with dynamic path handling and SQL backends, enabling further blind exploitation.

## Requirements

1. Public access to the target website (e.g., www.ibm.com)
2. Browser or HTTP client like curl for request crafting
3. Basic knowledge of URL structure and SQL syntax

## Defense

Defensive measures and detection strategies:

- Use parameterized queries or prepared statements in backend code
- Implement web application firewalls (WAF) to block anomalous path inputs
- Log and monitor URL access for single quotes or SQL keywords

## Objectives

1. Confirm injectable point in URL path
2. Validate without disrupting site functionality
3. Prepare for advanced payload testing

## Instructions

### Step 1: Craft Basic Injection Test

**Context**: Insert a single quote after the leading slash to break SQL syntax in path processing.

**Command** ([[commands/curl-http-request]]):
```bash
curl -i "https://www.ibm.com/'/some/existing/path"
```

> This sends a request to a modified path like /'/some/existing/path. Expected output: A 500 error or unexpected response differing from normal /some/existing/path (200 OK), indicating unescaped quote injection into SQL.

### Step 2: Validate Response Anomaly

**Context**: Compare against a clean request to isolate injection effects.

**Command** ([[commands/curl-http-request]]):
```bash
curl -i "https://www.ibm.com/some/existing/path"
```

> Normal response should be a standard page load. Any deviation (e.g., error page) confirms the injection point.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-http-request]]

## Tools Used


## Tags

- [[sqli]]
- [[web]]
