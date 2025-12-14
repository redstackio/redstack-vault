---
id: proc-observe-get-csrf-exposure
tags:
  - csrf
  - information-disclosure
  - get-method
  - web-vulnerability
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1213.003]]'
updated_at: '2025-12-14T17:27:22.790Z'
skill_level: basic
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[T1213.003]]'
---
# Observe-GET-Login-Exposure-of-CSRF-Token

## Summary

This procedure demonstrates how a web application's use of the GET method for account login exposes the CSRF protection token directly in the URL query parameters, making it susceptible to logging, caching, and unintended disclosure.

## Description

In secure web applications, login forms should use POST requests to avoid embedding sensitive data like CSRF tokens in URLs, which can be stored in browser history, server logs, or leaked via headers. This procedure involves navigating to the login page, inspecting the form submission, and confirming the token's exposure. The target environment is a web platform with services like CloudFront for CDN. Expected outcomes include visual confirmation of the token in network requests, highlighting the root cause of information disclosure.

## Requirements

1. Access to a browser with developer tools (e.g., Chrome, Firefox)
2. Valid or test credentials for the login endpoint
3. Network connectivity to the target web application

## Defense

Defensive measures and detection strategies:

- Enforce POST method for all login and state-changing forms
- Implement Referer header policies (e.g., strict-origin-when-cross-origin) to suppress sensitive URLs
- Monitor server logs for anomalous GET requests to login endpoints
- Use Content Security Policy (CSP) to control third-party resource loading

## Objectives

1. Confirm CSRF token inclusion in GET login URL
2. Document the exposure for vulnerability reporting
3. Assess potential for further leakage or misuse

## Instructions

### Step 1: Access Login Page

**Context**: Navigate to the account login endpoint to initiate the observation.

Open your browser and go to the target's login page, such as `https://target.com/login`. Ensure developer tools are open (press F12 or right-click > Inspect).

> No command required; use browser navigation.

### Step 2: Inspect Form and Submit

**Context**: Examine the login form's method and parameters to identify CSRF token placement.

In the Elements tab, locate the `<form>` tag for login and confirm `method="GET"`. Fill in credentials and submit. Switch to the Network tab to capture the request.

> Expected: Request logged as GET with URL like `/login?csrf_token=TOKEN_VALUE&username=...&password=...`.

### Step 3: Verify Token Exposure

**Context**: Analyze the captured request to confirm sensitive data visibility.

Click on the login request in Network tab. Check the Request URL for query parameters including the CSRF token. Note any additional sensitive values.

> Success: Token plainly visible, e.g., `csrf_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...`.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[T1213.003]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[information-disclosure]]
- [[get-method]]
