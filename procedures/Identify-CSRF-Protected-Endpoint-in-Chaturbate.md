---
id: proc-uuid-1
tags:
  - csrf
  - recon
  - web
  - chaturbate
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-post-csrf-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:27:29.615Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-CSRF-Protected-Endpoint-in-Chaturbate

## Summary

This procedure involves inspecting Chaturbate's chat functionality to identify the endpoint for canceling group shows and verifying that POST requests are protected by CSRF tokens, setting the stage for potential bypass attempts.

## Description

In the context of testing Chaturbate's web application, start a group show as a logged-in user and monitor network traffic to discover the cancellation endpoint. The endpoint `/tipping/group_show_cancel/{broadcaster_username}/` handles cancellations, with POST requests requiring a valid CSRF token in the headers. This reconnaissance step confirms the protection mechanism before attempting exploits. Expected outcome: Understanding of the vulnerability scope, applicable to authenticated users in live shows.

## Requirements

1. Active Chaturbate account with tokens for group shows
2. Browser with developer tools (e.g., Chrome DevTools) or curl for request simulation
3. Network access to chaturbate.com

## Defense

Defensive measures and detection strategies:

- Implement consistent CSRF protection across all HTTP methods on sensitive endpoints
- Monitor for anomalous cancellation requests in application logs
- Use Web Application Firewall (WAF) rules to detect missing CSRF tokens

## Objectives

1. Locate the exact API endpoint for show cancellation
2. Confirm CSRF validation on POST requests
3. Identify potential bypass vectors like alternative methods

## Instructions

### Step 1: Simulate Group Show and Monitor Traffic

**Context**: Join or start a group show to trigger the cancellation flow, capturing the request details.

**Command** ([[commands/curl-post-csrf-test]]):
```bash
curl -X POST -H "Cookie: auth_token=your_session_cookie" -H "X-CSRFToken: extracted_token" -d "" https://chaturbate.com/tipping/group_show_cancel/broadcaster_username/
```

> This command attempts a POST cancellation with a valid CSRF token. If successful, the show cancels; if token is omitted, expect a 403 Forbidden response indicating protection.

### Step 2: Extract Endpoint Details

**Context**: Use browser tools to inspect the request URL, method, and headers during a legitimate UI-based cancellation.

No specific command; manually note the endpoint path and required headers.

> Expected: Confirmation that POST to `/tipping/group_show_cancel/{username}/` checks for `X-CSRFToken`.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/curl-post-csrf-test]]

## Tools Used


## Tags

- [[csrf]]
- [[recon]]
- [[web]]
