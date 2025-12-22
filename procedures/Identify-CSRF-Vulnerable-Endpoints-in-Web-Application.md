---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Identify-CSRF-Vulnerable-Endpoints-in-Web-Application
tags:
  - csrf
  - recon
  - web-testing
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-test-csrf]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T12:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:27:15.819Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-CSRF-Vulnerable-Endpoints-in-Web-Application

## Summary

This procedure involves inspecting a web application's POST endpoints to detect the absence of CSRF protection, such as missing tokens, allowing potential exploitation through forged requests.

## Description

In the context of the Localize application, attackers examine endpoints like POST /pages/create_project, POST /pages/settings, and POST /add_phrase/{id}/languages/{lang} for anti-CSRF measures. By referencing OWASP guidelines, the procedure confirms if requests can be replayed without tokens, enabling unauthorized actions on behalf of authenticated users. This reconnaissance step is crucial before crafting exploits and can lead to data manipulation or account compromise.

## Requirements

1. Access to the web application (authenticated session preferred for realistic testing)
2. Browser developer tools or a web proxy (e.g., Burp Suite)
3. Knowledge of the application's endpoints from source code, documentation, or network inspection

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing forms and validate them server-side
- Use SameSite cookie attributes (Strict or Lax) to prevent cross-site requests
- Monitor for anomalous POST requests from unexpected referers

## Objectives

1. Confirm absence of CSRF protections on targeted endpoints
2. Document vulnerable locations for subsequent exploitation
3. Assess potential impact on user actions like project creation or settings changes

## Instructions

### Step 1: Inspect Network Requests

**Context**: Use browser tools to capture legitimate POST requests and analyze for CSRF tokens.

Navigate to the application, perform actions like creating a project, and inspect the request in the Network tab. Look for headers like X-CSRF-Token or form fields named csrf_token.

**Command** (N/A - manual inspection):

No command; use browser dev tools.

> If no token is present or required, note the endpoint as vulnerable.

### Step 2: Test Forged Request with Curl

**Context**: Replay the request without any CSRF token to verify vulnerability.

Execute [[commands/curl-test-csrf]] to simulate a cross-site POST:

```bash
curl -X POST http://localize.example.com/pages/create_project -d "project_name=test_project" -b "session=authenticated_cookie_value"
```

> Expected output: HTTP 200 or 302 redirect indicating successful creation without token validation. If it fails with a token error, the endpoint is protected.

### Step 3: Repeat for Other Endpoints

**Context**: Apply the same test to /pages/settings and /add_phrase/{id}/languages/{lang}.

Adapt the curl command for each, e.g., for settings:

```bash
curl -X POST http://localize.example.com/pages/settings -d "email=new@email.com" -b "session=authenticated_cookie_value"
```

> Success confirms multiple vectors for CSRF exploitation.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-csrf]]

## Tools Used


## Tags

- [[csrf]]
- [[web-vulnerability]]
- [[Reconnaissance]]
