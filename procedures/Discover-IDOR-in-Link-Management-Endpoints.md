---
tags:
  - idor
  - discovery
  - web
  - authorization
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-inspect-link-endpoint]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: a8ae573f-86e6-43cc-a8b4-7d5322aea85a
created_at: '2025-12-14T17:30:07.427Z'
updated_at: '2025-12-14T17:30:07.427Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Discover-IDOR-in-Link-Management-Endpoints

## Summary

This procedure involves inspecting the okl.lt URL shortener's dashboard API endpoints for link hiding and deletion to uncover an IDOR vulnerability, where user IDs are referenced directly without verifying ownership, allowing potential privilege escalation.

## Description

In the okl.lt service, authenticated users manage shortened links via dashboard endpoints. Testing reveals that requests to hide or delete links include user ID parameters that are not validated against the authenticated user's ownership. This procedure guides manual inspection using network tools to identify the flaw, typically in a web-based environment requiring login. Expected outcomes include confirmation of unauthorized access to other users' objects.

## Requirements

1. Authenticated account on okl.lt with dashboard access
2. Browser with developer tools or a proxy like Burp Suite
3. Basic knowledge of HTTP requests and JSON payloads

## Defense

Defensive measures and detection strategies:

- Implement server-side ownership checks on all object references
- Log and monitor API requests for anomalous user ID manipulations
- Use rate limiting on management endpoints to detect abuse

## Objectives

1. Identify endpoints vulnerable to direct object references
2. Confirm lack of authorization validation
3. Document parameters for exploitation

## Instructions

### Step 1: Authenticate and Create Test Link

**Context**: Gain access to the dashboard and generate a legitimate link to inspect its management requests.

Log in to okl.lt and create a shortened URL. This establishes a baseline request.

### Step 2: Inspect Legitimate Request

**Context**: Capture the HTTP request for hiding a link to understand the structure.

**Command** ([[commands/curl-inspect-link-endpoint]]):
```bash
curl -X POST 'https://okl.lt/api/hide-link' -H 'Authorization: Bearer YOUR_TOKEN' -H 'Content-Type: application/json' -d '{"link_id": "YOUR_LINK_ID", "user_id": "YOUR_USER_ID"}'
```

> This command replicates a hide request. Inspect the response and parameters in tools like Burp or dev tools. Note the `user_id` field.

### Step 3: Test Modified Parameter

**Context**: Alter the `user_id` to a non-owned value and resend to check for IDOR.

Modify the `user_id` in the payload to another user's ID and execute the request again. A successful response without errors indicates the vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-inspect-link-endpoint]]

## Tools Used


## Tags

- idor
- discovery
- web
