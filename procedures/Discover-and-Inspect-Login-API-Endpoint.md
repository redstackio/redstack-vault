---
tags:
  - reconnaissance
  - api-discovery
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:33:12.180Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 3279df11-d1ef-43f7-99db-07390e7c33d8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Discover-and-Inspect-Login-API-Endpoint

## Summary

This procedure involves accessing the target web application's login page, observing redirects, and inspecting network requests to identify the underlying authentication API endpoint, setting the stage for further enumeration and exploitation.

## Description

In the context of the Outpost application, users start by visiting https://www.teamoutpost.com/, which redirects to https://app.outpost.co/sign-in. Submitting test credentials reveals the API call to https://api.outpost.co/api/v1/login. This step requires no special tools beyond browser developer tools or a proxy like Burp Suite to capture and analyze the HTTP POST request, including headers, payload (JSON with username and password), and response format. Prerequisites include public internet access to the target.

## Requirements

1. Web browser with developer tools enabled
2. Optional: Intercepting proxy (e.g., Burp Suite) for detailed request inspection
3. Network access to https://www.teamoutpost.com/

## Defense

Defensive measures and detection strategies:

- Implement consistent error messages to avoid endpoint leakage
- Monitor for unusual login page access patterns or proxy traffic
- Use WAF rules to detect automated request inspection attempts

## Objectives

1. Identify the exact API endpoint for authentication
2. Understand request/response structure for automation
3. Confirm redirect flow without authentication

## Instructions

### Step 1: Access Login Page

**Context**: Navigate to the public login interface to trigger the redirect and observe the authentication flow.

No specific command; use a browser to visit https://www.teamoutpost.com/ and confirm redirect to https://app.outpost.co/sign-in.

> Expected: Login form displayed after redirect.

### Step 2: Submit Test Credentials and Inspect

**Context**: Trigger an API call by attempting login with invalid credentials to capture the request.

Use browser dev tools (F12 > Network tab) or Burp Suite to intercept the POST to https://api.outpost.co/api/v1/login.

> Expected: Request payload like {"username": "test", "password": "test"} and response with error.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[Reconnaissance]]
- [[api-discovery]]
