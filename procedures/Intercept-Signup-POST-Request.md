---
id: proc-002-intercept-post
tags:
  - request-interception
  - web-proxy
type: procedure
tools:
  - '[[tools/Firefox-Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:10.293Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-Signup-POST-Request

## Summary

This procedure captures the HTTP POST request sent during form submission to the /api-umbrella/v1/users.json endpoint, enabling modification for bypassing verification.

## Description

The api.data.gov signup form submits user data via POST to /api-umbrella/v1/users.json. By intercepting this request using browser developer tools (e.g., Firefox Network tab) or a proxy, attackers can inspect and alter parameters like options[verify_email]. The default request includes user details and sets verification to true, which can be tampered with. This step is crucial for exploiting the lack of server-side validation on client-submitted parameters.

## Requirements

1. Browser with developer tools enabled
2. Form filled with test data (e.g., email: hacker@gmail.com)
3. Ability to pause and inspect network requests

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS and validate all client inputs server-side
- Log and monitor anomalous request patterns to the users endpoint
- Use WAF rules to detect request tampering attempts

## Objectives

1. Capture the full POST request body
2. Identify default parameters for modification
3. Prevent direct submission until altered

## Instructions

### Step 1: Enable Request Interception

**Context**: Configure browser tools to monitor and pause network requests from the signup form.

In Firefox Developer Tools, open the Network tab, start recording, and submit the form while pausing on the POST request.

> Expected: Request details appear, including headers (e.g., Content-Type: application/x-www-form-urlencoded) and body with user[email], options[verify_email]=true.

### Step 2: Inspect Request Details

**Context**: Review the captured request for the target endpoint and parameters.

Examine the POST body for keys like user[first_name], user[email], and options[verify_email].

> Success: Endpoint is /api-umbrella/v1/users.json; body length around 500+ characters with form data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox-Browser-Developer-Tools]]

## Tags

- [[request-interception]]
- [[web-proxy]]
