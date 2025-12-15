---
id: proc-001
tags:
  - information-disclosure
  - web-access
type: procedure
tools:
  - '[[tools/Burp-Suite-Repeater]]'
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
updated_at: '2025-12-14T17:25:12.694Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Manage-Users-Endpoint

## Summary

This procedure outlines the initial navigation and interception of the Manage Users endpoint in a web application like staging.seatme.us, setting the stage for vulnerability testing by capturing the baseline request structure.

## Description

In the context of testing for information disclosure, this step involves accessing the user management feature without authentication, identifying the endpoint that processes user_id queries. The target environment is a public-facing web app on staging.seatme.us, where improper access controls allow unauthenticated requests. Expected outcomes include capturing the HTTP request format for further manipulation.

## Requirements

1. Network access to staging.seatme.us over HTTP/HTTPS
2. Burp Suite or similar proxy tool installed and configured
3. Basic knowledge of web request interception

## Defense

Defensive measures and detection strategies:

- Implement authentication checks on all admin endpoints
- Log and monitor access to user management features for anomalies
- Use rate limiting on ID-based queries

## Objectives

1. Gain access to the Manage Users endpoint
2. Intercept and understand the request parameters
3. Prepare for parameter tampering

## Instructions

### Step 1: Navigate to the Endpoint

**Context**: Locate the Manage Users feature to initiate the request.

Intercept the request using Burp Proxy while browsing to the user management page on staging.seatme.us.

> No specific command; use browser navigation and proxy interception. Expected output: Captured GET/POST request showing user_id parameter.

### Step 2: Verify Endpoint Accessibility

**Context**: Confirm unauthenticated access is possible.

Send the intercepted request through Burp Repeater without modifications.

> Expected output: 200 OK response with partial user data or form, indicating no auth required.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Repeater]]

## Tags

- [[information-disclosure]]
- [[web-access]]
