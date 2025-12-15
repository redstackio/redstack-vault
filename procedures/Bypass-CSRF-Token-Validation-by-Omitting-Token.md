---
tags:
  - csrf
  - bypass
  - exploit
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
updated_at: '2025-12-14T17:27:36.108Z'
sub_techniques: []
id: 22aa3c2a-b4e6-4051-87d6-9bc3680efcbb
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-CSRF-Token-Validation-by-Omitting-Token

## Summary

This procedure exploits a CSRF token validation flaw by submitting requests without the required token, allowing unauthorized actions in Reverb.com's messaging features.

## Description

Discovered in the Reverb.com sandbox, this bypass occurs because the server fails to enforce the presence of the CSRF token in POST requests for reply and send message actions. Removing the token parameter enables the request to proceed, facilitating CSRF attacks where an attacker tricks a victim into performing actions via a malicious site. The impact is low severity, as it targets non-critical messaging, and was promptly fixed.

## Requirements

1. Authenticated session in the target application.
2. Ability to intercept and modify HTTP requests (e.g., via browser tools or proxy).
3. Knowledge of the form's POST endpoint.

## Defense

Defensive measures and detection strategies:

- Enforce strict token presence and validation on all mutable requests.
- Use same-site cookies and monitor for tokenless submissions in logs.

## Objectives

1. Demonstrate successful request without CSRF token.
2. Enable unauthorized messaging actions.
3. Validate the vulnerability for reporting.

## Instructions

### Step 1: Intercept Form Submission

**Context**: Capture the normal form submission to understand the request structure.

Submit a test reply or send message and use developer tools (Network tab) or a proxy to intercept the POST request.

### Step 2: Modify and Resubmit Request

**Context**: Remove the CSRF token to test bypass.

Edit the request by deleting the CSRF token parameter (e.g., `csrf_token=abc123`). Forward the modified POST request to the server.

> Expected output: Server accepts the request and processes the message without validation error, confirming the bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf-bypass]]
- [[web-exploit]]
