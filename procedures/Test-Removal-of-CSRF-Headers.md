---
id: proc-test-csrf-removal
tags:
  - csrf-test
  - header-bypass
  - vulnerability-validation
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:57.317Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Removal-of-CSRF-Headers

## Summary

This procedure tests the CSRF vulnerability by replaying the donation settings request without X-CSRF and X-XSRF headers, confirming the server's failure to validate them.

## Description

CSRF protection relies on token validation via headers. By removing these from the intercepted request and resending it, this step proves the endpoint accepts unauthorized updates, paving the way for exploitation. The test uses the same JSON payload but omits protections, expecting a successful 200 OK.

## Requirements

1. Captured legitimate request from prior step
2. Browser DevTools or proxy tool for request replay
3. Active authenticated session

## Defense

Defensive measures and detection strategies:

- Enforce strict CSRF token validation on all state-changing endpoints.
- Log and alert on requests missing CSRF headers.

## Objectives

1. Validate lack of header enforcement.
2. Confirm update succeeds without tokens.
3. Assess vulnerability severity.

## Instructions

### Step 1: Prepare Replay

**Context**: Modify the captured request.

In DevTools Network tab, right-click the POST request and select 'Copy as cURL' or edit directly.

### Step 2: Remove Headers

**Context**: Strip CSRF protections.

Delete X-CSRF and X-XSRF headers from the request, keeping the JSON body intact (e.g., {"username":{"value":"shirley","autofill":false},...}).

### Step 3: Send Modified Request

**Context**: Execute and observe.

Replay the request to /api/v6/viewer-portal/viewer-settings/donation_settings and check for 200 OK response.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- csrf-test
- header-bypass
- vulnerability-validation
