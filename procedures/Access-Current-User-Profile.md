---
id: proc-wakatime-access-current-profile
tags:
  - api
  - authentication
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:47.939Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Current-User-Profile

## Summary

This procedure establishes an authenticated session with WakaTime's API by accessing the current user's profile endpoint, providing a legitimate request that can be intercepted and modified for further exploitation in IDOR attacks.

## Description

In the context of testing WakaTime's API for authorization flaws, this step involves logging in as a valid user and triggering a GET request to /api/v1/users/current?, which returns the authenticated user's own profile data. This serves as the foundation for identifying IDOR by modifying the endpoint later. Prerequisites include a WakaTime account and browser access. Expected outcomes confirm API accessibility and authentication validity.

## Requirements

1. Valid WakaTime account credentials for login
2. Browser or HTTP client capable of sending authenticated requests
3. Proxy tool like Burp Suite configured for traffic interception

## Defense

Defensive measures and detection strategies:

- Implement session validation on all API endpoints to ensure requests match the authenticated user
- Log and monitor API access patterns for anomalous endpoint modifications
- Use rate limiting on profile access requests to detect automated probing

## Objectives

1. Verify authenticated access to own profile data
2. Capture a baseline request for manipulation
3. Confirm API responsiveness without errors

## Instructions

### Step 1: Authenticate and Trigger Request

**Context**: Log in to WakaTime and perform an action that invokes the profile API, such as viewing your dashboard, to generate the legitimate request.

No specific command; use browser navigation to https://wakatime.com and inspect network traffic.

> The request will appear as a GET to /api/v1/users/current? with authentication cookies. Expected output: JSON with your profile details.

### Step 2: Verify Response

**Context**: Ensure the response is successful to validate the session.

Inspect the response in browser dev tools or proxy.

> Look for HTTP 200 and personal data fields like name and bio.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[api]]
- [[authentication]]
