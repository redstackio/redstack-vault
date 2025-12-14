---
tags:
  - session-capture
  - cookie-interception
  - web-auth
type: procedure
tools:
  - '[[tools/Burp-Proxy]]'
  - '[[tools/Burp-Repeater]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:30.806Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 9c352d84-2664-4f81-9f94-f7d76cd89bdc
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Admin-Page-and-Capture-Cookies

## Summary

This procedure involves accessing a protected admin edit page in an authenticated session and capturing session cookies using a proxy tool, setting up for later session hijacking.

## Description

In scenarios with broken session management, accessing sensitive endpoints like admin edit pages (e.g., /admin.101/edit/username) while authenticated allows interception of cookies such as __cfduid, csrf_token, and session. These can be stolen or intercepted and reused post-logout, leading to impersonation. Prerequisites include a valid login to the target account and a proxy configured for the browser.

## Requirements

1. Authenticated session to the web application
2. Burp Suite with Proxy enabled and browser traffic routed through it
3. Target URL for admin endpoint (e.g., https://liberapay.com/admin.101/edit/username)

## Defense

Defensive measures and detection strategies:

- Implement proper session invalidation on logout by regenerating or destroying cookies
- Use HttpOnly and Secure flags on cookies to limit theft
- Monitor for anomalous session reuse across IP addresses or user agents

## Objectives

1. Obtain valid session cookies from an authenticated request
2. Prepare cookies for replay in an unauthenticated context
3. Enable subsequent account impersonation

## Instructions

### Step 1: Configure Proxy and Access Page

**Context**: Set up interception to capture the initial request to the admin page.

Configure your browser to route traffic through Burp Proxy. Navigate to the admin edit page in the authenticated session.

### Step 2: Intercept and Capture Cookies

**Context**: Refresh the page to trigger a request and extract the cookies.

Intercept the request using Burp Proxy. Copy the cookie values (__cfduid, csrf_token, session) from the headers.

**Expected Output**: Cookie strings noted for manual insertion later.

### Step 3: Forward to Repeater for Preparation

**Context**: Prepare the request for modification and replay.

Forward the intercepted request to Burp Repeater to store it with the captured cookies.

**Expected Output**: Request ready in Repeater with original cookies intact.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Proxy]]
- [[tools/Burp-Repeater]]

## Tags

- session-capture
- cookie-interception
