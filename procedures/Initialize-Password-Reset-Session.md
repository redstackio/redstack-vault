---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - csrf
  - session-initialization
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
updated_at: '2025-12-14T17:27:43.024Z'
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
# Initialize-Password-Reset-Session

## Summary

This procedure loads the password reset link in the victim's browser to establish a session state that activates the vulnerable reset form, without completing the password change.

## Description

After obtaining the reset link, this step involves opening it in the victim's browser, which sets session variables and loads the reset form at /customer/account/resetpassword/. The form lacks CSRF protection (no form key or token), making it susceptible to cross-site requests. The page is then closed, leaving the session active and exploitable for ~30 minutes or until timeout.

## Requirements

1. Valid reset link from the previous procedure
2. Victim's browser access (via social engineering)
3. OpenMage instance accessible over the web

## Defense

Defensive measures and detection strategies:

- Add CSRF tokens to all POST forms, including reset
- Implement session timeouts for reset links
- Log and alert on incomplete reset sessions followed by submissions

## Objectives

1. Activate the password reset session
2. Expose the CSRF-vulnerable form state
3. Prepare for automated form submission

## Instructions

### Step 1: Open Reset Link

**Context**: Load the link to initialize the session.

Direct the victim to click the reset link (e.g., https://demo.openmage.org/customer/account/resetpassword/?key=abc123&id=456).

> The page loads a form for new password entry. Expected output: Form appears with fields for password and confirmation; session cookies set.

### Step 2: Close Without Submitting

**Context**: Maintain the session without altering the password yet.

Instruct or trick the victim to close the tab or navigate away immediately after loading.

> Session remains active in the background. Verify by checking browser dev tools for set cookies related to the reset key.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[session-initialization]]
