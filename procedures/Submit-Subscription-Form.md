---
id: proc-subscribe-form-001
tags:
  - form
  - submit
  - csrf
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:29.290Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit-Subscription-Form

## Summary

This procedure interacts with the Coinbase developer subscription form to trigger a POST request that leaks the CSRF token over unencrypted HTTP.

## Description

Entering an email and submitting the form sends a POST to an external HTTP endpoint with the token in the body. This exposes the token to MiTM. Target: Subscription form on API docs page. Expected: Request sent, token leaked.

## Requirements

1. Authenticated session on API docs page
2. Valid email for form (test address)
3. Proxy active to capture request

## Defense

Defensive measures and detection strategies:

- Force HTTPS for all form submissions
- Validate external endpoints with HSTS
- Audit forms for token exposure in requests

## Objectives

1. Initiate the leaking POST request
2. Include CSRF token in submission
3. Enable interception for analysis

## Instructions

### Step 1: Fill Email Field

**Context**: Prepare form data for submission.

Locate the email input under "Developer Updates" and enter a test email (e.g., test@example.com).

### Step 2: Submit Form

**Context**: Trigger the vulnerable request.

Click the "Subscribe" button to send the POST.

### Step 3: Monitor Submission

**Context**: Watch for request in proxy or network tab.

Observe the outgoing POST to confirm HTTP protocol.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[form]]
- [[csrf]]
- [[submit]]
