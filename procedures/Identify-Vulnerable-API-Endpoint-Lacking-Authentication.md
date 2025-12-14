---
id: proc-uuid-001
name: Identify-Vulnerable-API-Endpoint-Lacking-Authentication
tags:
  - access-control
  - api
  - recon
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:18.122Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-Vulnerable-API-Endpoint-Lacking-Authentication

## Summary

This procedure identifies API endpoints on a web application that lack proper authentication and authorization checks, specifically those handling sensitive operations like user registration and profile updates, allowing unauthenticated access to critical functions.

## Description

In the context of the Mars website vulnerability, the procedure involves inspecting network traffic and testing endpoints for missing auth mechanisms. The target environment is a web API over HTTPS, where the absence of tokens or session checks enables direct manipulation. Prerequisites include basic knowledge of HTTP requests and access to developer tools. Expected outcomes include confirmation of vulnerable endpoints that can be exploited for unauthorized actions.

## Requirements

1. Network access to the target website
2. Tools for sending HTTP requests (e.g., browser dev tools or curl)
3. Understanding of API structures and JSON payloads

## Defense

Defensive measures and detection strategies:

- Implement JWT or session-based authentication on all API endpoints
- Use rate limiting and input validation to prevent enumeration
- Monitor for anomalous API calls without auth headers using WAF logs

## Objectives

1. Locate endpoints vulnerable to unauthenticated access
2. Verify lack of authorization for user management operations
3. Prepare for exploitation by documenting endpoint details

## Instructions

### Step 1: Inspect Network Traffic

**Context**: Use browser tools to capture requests during user interactions and identify potential endpoints.

Open developer tools (F12 in Chrome), navigate to user registration or profile pages, and monitor the Network tab for API calls. Look for endpoints like `/api/users` or similar.

No specific command, but test manually:

```bash
curl -X GET https://target.com/api/users -v
```

> The verbose output will show if auth headers are required or if the request succeeds without them. Expect a 200 response if vulnerable.

### Step 2: Test for Authentication Bypass

**Context**: Send direct requests without any auth to confirm the vulnerability.

Attempt a POST to the registration endpoint without login:

```bash
curl -X POST https://target.com/api/users/register -H "Content-Type: application/json" -d '{}'
```

> If it returns without 401/403 errors, the endpoint is vulnerable. Document the exact path for further steps.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[access-control]]
- [[api]]
- [[recon]]
