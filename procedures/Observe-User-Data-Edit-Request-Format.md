---
id: proc-observe-edit-request-1624421
tags:
  - observation
  - request-analysis
  - web
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
updated_at: '2025-12-14T17:33:06.757Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Observe User Data Edit Request Format

## Summary

This procedure captures and analyzes the standard request format used for editing user data, revealing the application's expectation of JSON content-type for updates.

## Description

During a pentest, observing the edit request on https://█████/user/account helps identify discrepancies in server validation, such as accepting alternative content types without CSRF protection. The scenario involves a logged-in user attempting a benign edit, with network inspection showing JSON payloads, setting the stage for CSRF exploitation.

## Requirements

1. Active test account from registration
2. Browser with developer tools (e.g., Chrome DevTools)
3. Access to the user account edit page

## Defense

Defensive measures and detection strategies:

- Enforce strict content-type validation on endpoints
- Log all edit requests for anomaly detection
- Use WAF rules to block unexpected request formats

## Objectives

1. Document normal request structure (JSON, headers)
2. Identify potential bypass opportunities
3. Prepare for request modification testing

## Instructions

### Step 1: Log In and Navigate to Edit Page

**Context**: Authenticate and access the vulnerable endpoint.

Log in with the test account and go to https://█████/user/account.

### Step 2: Attempt a Test Edit

**Context**: Perform a simple data change while monitoring traffic.

Edit a field like display name, submit the form, and open DevTools Network tab to inspect the request.

**Expected Output**: Request details showing POST to /user/account with Content-Type: application/json and JSON body.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[observation]]
- [[request-analysis]]
