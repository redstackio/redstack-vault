---
tags:
  - auth-bypass
  - form-manipulation
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:52.508Z'
sub_techniques: []
id: 79a62ee5-0e7d-43f5-8fa6-b16d51f3a4d7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Manipulate-Form-Fields-via-Redirect-Tampering

## Summary

This procedure allows filling and interacting with form elements, such as dropdowns, by repeatedly intercepting and changing 302 redirects to 200 responses during the appeal creation process.

## Description

Once the initial form is loaded, interactions like selecting options trigger additional auth checks via redirects. Tampering with these ensures uninterrupted access, enabling full form completion in an unauthenticated state.

## Requirements

1. Proxy intercepting all traffic to the application
2. Form loaded via prior bypass
3. Understanding of form submission flow

## Defense

Defensive measures and detection strategies:

- Validate user sessions on every AJAX/form interaction server-side
- Implement CSRF tokens to prevent unauthorized submissions
- Monitor for repeated 302-to-200 anomalies in access logs

## Objectives

1. Complete form without auth interruptions
2. Select restricted options
3. Prepare for submission

## Instructions

### Step 1: Interact with Form

**Context**: Begin filling fields and trigger checks.

In the browser, select dropdown options or enter data; intercept any new requests/responses.

**Expected Output**: Requests to sub-endpoints (e.g., for validation).

### Step 2: Tamper Ongoing Redirects

**Context**: Bypass each auth redirect encountered.

For each 302 response during interactions, change to 200 and forward.

**Expected Output**: Form updates dynamically without login prompts.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[auth-bypass]]
- [[form-manipulation]]
