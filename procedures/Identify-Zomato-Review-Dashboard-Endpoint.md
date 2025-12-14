---
tags:
  - reconnaissance
  - endpoint-discovery
  - web-vulnerability
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:29:28.836Z'
sub_techniques: []
id: 3559c6be-d784-4280-b817-24988d85e917
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Zomato Review Dashboard Endpoint

## Summary

This procedure involves reconnaissance to identify the vulnerable /████dashboard_handler.php endpoint on Zomato.com, which handles review administrative actions without authorization checks, setting the stage for privilege escalation exploitation.

## Description

In the context of web application testing, this step focuses on discovering backend endpoints exposed to authenticated users. The target is Zomato's review system, where the dashboard handler processes sensitive actions like moderation and editing. By inspecting network requests during normal review interactions, attackers can uncover the endpoint and its parameters. Prerequisites include an authenticated session; expected outcomes are a list of exploitable actions leading to unauthorized access.

## Requirements

1. Authenticated Zomato user account
2. Web browser with developer tools (e.g., Chrome DevTools) or proxy like Burp Suite
3. Direct access to zomato.com over HTTPS

## Defense

Defensive measures and detection strategies:

- Implement proper authorization checks on all admin endpoints
- Use web application firewalls (WAF) to monitor anomalous POST requests to handler endpoints
- Log and alert on access to sensitive actions from non-admin IPs or sessions

## Objectives

1. Locate the review dashboard handler endpoint
2. Enumerate supported administrative actions
3. Confirm lack of privilege verification

## Instructions

### Step 1: Inspect Application Traffic

**Context**: Use browser tools to capture requests while interacting with review features, revealing hidden endpoints.

No specific command; manually navigate to review pages on Zomato.com and monitor the Network tab in DevTools for requests to paths containing 'dashboard_handler'.

> Look for POST requests to /████dashboard_handler.php and note parameters like action=edit or action=moderate.

### Step 2: Test Endpoint Accessibility

**Context**: Verify if the endpoint responds to basic requests from a standard user account.

Send a simple GET or POST probe to the endpoint URL to check for exposure.

> Expected output: Response without 403 Forbidden, indicating missing auth checks. Success if actions like get_manager_status return data.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[web-scanning]]
