---
tags:
  - csrf
  - web
  - recon
type: procedure
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-csrf-endpoint]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:15.412Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: eaa631b6-afb3-4889-b1a8-303ace771a9c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify CSRF Vulnerable Endpoint for Private Messages

## Summary

This procedure identifies the CSRF-vulnerable endpoint in the Informatica community site's private messaging system by analyzing requests and testing for missing security controls like Referrer headers or tokens.

## Description

In the attack scenario, the attacker inspects the private messages interface to find the deletion functionality. The endpoint https://community.informatica.com/pm-delete.jspa accepts GET requests with a messageID parameter to move messages to Trash but lacks CSRF protections, allowing cross-origin forgery. This is tested in a controlled manner to confirm vulnerability without causing unintended deletions. Prerequisites include access to the site and basic web debugging tools. Expected outcome: Confirmation that forged GET requests can trigger deletions.

## Requirements

1. Access to https://community.informatica.com with an account to observe messaging
2. Browser with developer tools or a proxy tool like Burp Suite
3. Victim's session cookie (for testing; use your own for verification)
4. Basic knowledge of HTTP requests

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints
- Enforce strict Referrer-Policy and validate origin headers
- Monitor for anomalous deletion requests from unexpected sources
- Rate-limit deletion actions per user session

## Objectives

1. Locate the pm-delete.jspa endpoint and its parameters
2. Verify absence of CSRF protections
3. Test request acceptance without authentication checks beyond session

## Instructions

### Step 1: Inspect Private Messages Interface

**Context**: Navigate to the private messages section to trigger a legitimate deletion and capture the request.

Use browser dev tools (Network tab) to monitor a test deletion of your own message.

**Expected Output**: Request URL reveals https://community.informatica.com/pm-delete.jspa?messageID=XXX as GET.

### Step 2: Test Endpoint with Forged Request

**Context**: Simulate a cross-origin request to check for protections.

Execute [[commands/curl-test-csrf-endpoint]] to verify:

```bash
curl -X GET "https://community.informatica.com/pm-delete.jspa?messageID=123" -H "Cookie: JSESSIONID=your_session_cookie" -v
```

> This command sends a GET request mimicking a forged one. Look for a 200/302 response indicating success, with no errors about missing tokens or invalid referrer.

### Step 3: Confirm Lack of Protections

**Context**: Attempt from a different origin (e.g., local HTML file) to ensure cross-site requests work.

Load a simple <img src="https://community.informatica.com/pm-delete.jspa?messageID=123"> in a local HTML while logged in.

**Expected Output**: Message deleted without browser blocking the request.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-test-csrf-endpoint]]

## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[recon]]
