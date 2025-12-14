---
id: proc-uuid-discover-wp-admin
tags:
  - reconnaissance
  - wordpress
  - admin-endpoint
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
updated_at: '2025-12-14T17:29:20.495Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Discover WordPress Admin Login Endpoint

## Summary

This procedure identifies the WordPress admin login page by accessing the standard /wp-admin/ path, confirming basic authentication requirements through HTTP responses.

## Description

In WordPress sites, the admin panel is typically exposed at /wp-admin/, protected by basic HTTP authentication or form-based login. This step involves direct access to observe the 401 response, indicating authentication is required but no advanced protections like rate limiting are in place. It's a foundational reconnaissance step for authentication attacks on public-facing web applications.

## Requirements

1. Network access to the target domain (e.g., https://www.stellar.org)
2. Web browser (e.g., Chrome, Firefox)
3. Optional: Developer tools for inspecting responses

## Defense

Defensive measures and detection strategies:

- Implement directory traversal protections or hide admin paths
- Monitor access logs for /wp-admin/ probes
- Use WAF rules to block anomalous reconnaissance

## Objectives

1. Confirm existence of admin login endpoint
2. Identify authentication mechanism
3. Assess initial exposure level

## Instructions

### Step 1: Access Admin URL

**Context**: Directly navigate to the admin path to trigger authentication response.

No specific command; use browser:

Open https://target.com/wp-admin/ in a browser.

> The server responds with HTTP 401 Unauthorized, displaying a login form or basic auth prompt. Inspect the response headers for confirmation.

### Step 2: Inspect Response

**Context**: Verify the authentication type and lack of additional security headers.

Use browser dev tools (F12) to check network tab.

> Expected: No rate-limit headers; standard WWW-Authenticate: Basic realm="admin".

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[wordpress]]
