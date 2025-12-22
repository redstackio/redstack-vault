---
id: proc-003
tags:
  - csrf
  - cross-account
  - token-reuse
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
updated_at: '2025-12-14T17:27:15.302Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create Second Account and Verify Cross-Account Token Reuse

## Summary

This procedure creates a second Liberapay account in the same browser session, links an external service like Facebook, and deletes it to confirm the CSRF token from the first account is reused, demonstrating cross-account persistence via the generic cookie.

## Description

Building on prior account setup, this targets multi-account scenarios in Liberapay where the 7-day CSRF cookie remains unchanged across sign-ups. It involves registration, OAuth linking, and deletion with network inspection. The scenario exploits session continuity to show token non-specificity, potentially aiding attacks like unauthorized deletions if tokens are predictable or leaked. Outcomes validate the vulnerability through identical token observation.

## Requirements

1. Persistent browser session with existing CSRF cookie from first account
2. Access to another external account (e.g., Facebook)
3. Developer Tools for request inspection

## Defense

Defensive measures and detection strategies:

- Scope CSRF cookies to specific paths or domains tied to user sessions
- Invalidate or regenerate tokens on new account creation
- Detect and flag multi-account activity in short sessions via logging

## Objectives

1. Create additional account without session reset
2. Link and delete external service to trigger token usage
3. Confirm cross-account token reuse for vulnerability proof

## Instructions

### Step 1: Sign Up for Second Account

**Context**: Register a new account while preserving the original cookie.

Without logging out or clearing cookies, navigate to Liberapay sign-up and create a second account with different credentials.

> Expected output: Access to second account dashboard; original cookie intact.

### Step 2: Link and Delete External Service, Capture Token

**Context**: Perform linkage and deletion to observe token continuity.

In the second profile's 'Accounts Elsewhere', link Facebook via OAuth, then delete it. Inspect the deletion POST request for the CSRF token and compare to the first account's value (e.g., 'J0Lk5iXTpp40iDN5KNcrI24bulPcF0PV').

> Expected output: Same token reused; successful deletion.

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
- [[cross-account]]
- [[token-reuse]]
