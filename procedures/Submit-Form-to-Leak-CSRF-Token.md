---
tags:
  - csrf-leak
  - xhr
  - token-theft
type: procedure
tools:
  - '[[tools/Sinatra]]'
tactics:
  - '[[Credential Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T12:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:27:03.502Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 286fd8c2-b05e-45cb-9b36-8e5c965d8cfd
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Submit-Form-to-Leak-CSRF-Token

## Summary

This procedure triggers the submission of the injected data-remote form in an authenticated Rails session, causing an XHR POST to the external server and leaking the X-CSRF-Token header for capture.

## Description

With the form in place and server ready, submitting from a browser authenticated to the Rails app sends the token via XHR due to the lack of origin checks in rails-ujs. This step completes the leakage, providing the attacker with the token to forge CSRF-protected requests, such as state-changing POSTs. Testing involves browser interaction and server log verification.

## Requirements

1. Authenticated session in the vulnerable Rails app
2. Injected form visible in the browser
3. Running external Sinatra server on attacker.com

## Defense

Defensive measures and detection strategies:

- Enable origin validation in Rails UJS for XHR requests
- Audit and sanitize user-input forms to prevent external action attributes
- Log and alert on cross-origin XHR with auth headers

## Objectives

1. Initiate XHR submission from the form
2. Verify token transmission in network requests
3. Confirm capture on the attacker server

## Instructions

### Step 1: Authenticate to Target

**Context**: Ensure a valid session with CSRF token generated.

Log in to the Rails app via browser.

### Step 2: Interact with Form

**Context**: Click the submit button to trigger the XHR POST.

In the browser, locate and click the injected form's button.

> Browser sends POST to http://attacker.com/capture with X-CSRF-Token: <token_value>.

### Step 3: Verify Capture

**Context**: Check browser dev tools and server logs for success.

Open Network tab; look for the XHR request and headers.

**Expected Output**: Request status 200, server logs show captured token.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Sinatra]]

## Tags

- [[csrf-leak]]
- [[xhr]]
- [[token-theft]]
