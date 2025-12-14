---
tags:
  - web-cache-poisoning
  - cache-manipulation
type: procedure
tools:
  - '[[tools/Custom-POC-HTML-JS-Script]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:13.490Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: f06cbd1a-81d2-4101-9fd9-01a71317f5bd
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Poison-Web-Cache-with-Authenticated-User-Content

## Summary

This procedure poisons a web server's cache by requesting a public-like URL (ending in .css) while authenticated, causing user-specific content to be stored and served to unauthenticated users later.

## Description

In the context of Lyst.com, the server fails to key cache entries on authentication state, treating .css endpoints as static resources. By visiting such a URL while logged in, the response includes personalized data (e.g., username, email) and gets cached publicly. This enables information disclosure attacks. Prerequisites include valid user credentials and browser access to the site.

## Requirements

1. Valid login credentials for the target web application
2. Browser session capable of maintaining authentication cookies
3. Knowledge of cacheable endpoints (e.g., .css URLs)

## Defense

Defensive measures and detection strategies:

- Implement cache keying based on authentication status and user session
- Use cache-busting headers (e.g., Vary: Authorization) for authenticated responses
- Monitor for anomalous cache hits on static-like URLs with user data

## Objectives

1. Inject authenticated content into public cache entries
2. Enable unauthenticated access to sensitive user information
3. Demonstrate impact on user privacy and login security

## Instructions

### Step 1: Authenticate to the Target

**Context**: Establish a logged-in session to include user-specific data in responses.

Log in to the target site (e.g., Lyst.com) using provided credentials. Verify authentication by checking for personalized elements on the dashboard.

> Expected output: User profile details visible, confirming session is active.

### Step 2: Request Crafted Cacheable URL

**Context**: Trigger caching of authenticated response under a public endpoint.

Navigate to a URL like `https://www.lyst.com/shop/trends/mens-dress-shoes/blahblah.css` in the authenticated browser session. The server processes the request as if for a static file but includes dynamic user data.

> Expected output: Response body contains personalized content such as `<span class="username">user@example.com</span>` or similar, now cached.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Custom-POC-HTML-JS-Script]]

## Tags

- [[web-cache-poisoning]]
- [[information-disclosure]]
