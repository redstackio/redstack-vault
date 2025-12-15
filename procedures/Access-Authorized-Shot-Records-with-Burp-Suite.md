---
id: proc-uuid-002
tags:
  - web
  - proxy
  - burp
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:30.014Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Access-Authorized-Shot-Records-with-Burp-Suite

## Summary

This procedure retrieves an authorized medical shot record from the DoD application using Burp Suite to intercept the HTTP response, revealing the 302 redirect format with embedded PDF content for baseline understanding.

## Description

After authentication, the shot records endpoint is accessed via a URL parameter containing the user's own ID. The application responds with a 302 redirect that unusually includes the PDF in the response body rather than a separate download. Burp Suite is used to proxy and inspect this traffic. This step confirms normal behavior before manipulation. Prerequisites include an active session and Burp Suite configured as the browser proxy.

## Requirements

1. Active CAC-authenticated session
2. Burp Suite running and browser proxy set to 127.0.0.1:8080
3. Knowledge of the user's own ID parameter

## Defense

Defensive measures and detection strategies:

- Validate all requests against session ownership and log proxy-like traffic anomalies
- Remove sensitive data from redirect responses; use proper download endpoints
- Monitor for unusual response body sizes in redirects

## Objectives

1. Observe the authorized PDF in the 302 response body
2. Confirm endpoint URL structure
3. Establish baseline for ID manipulation

## Instructions

### Step 1: Configure Burp Proxy

**Context**: Set up Burp Suite to intercept browser traffic to the DoD application.

No command; in Burp, go to Proxy > Options and ensure it's listening on port 8080; configure browser to use this proxy.

> Install Burp CA certificate in browser to avoid HTTPS errors.

### Step 2: Browse to Authorized Endpoint

**Context**: Navigate to https://███████=[own_id] to trigger the request.

Intercept in Burp Repeater or Proxy history.

> Forward the request; inspect the 302 response for PDF in body, redirecting to █████.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[web]]
- [[proxy]]
- [[burp]]
