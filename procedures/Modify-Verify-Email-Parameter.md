---
id: proc-003-modify-parameter
tags:
  - parameter-tampering
  - auth-bypass
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
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:10.283Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Modify-Verify-Email-Parameter

## Summary

This procedure tampers with the intercepted signup request by setting options[verify_email] to false, bypassing the email confirmation step and allowing immediate API key issuance.

## Description

The root cause is the backend's failure to enforce or validate the options[verify_email] parameter, which defaults to true but can be client-overridden. By changing it to false in the POST body, the server skips sending a verification email and generates the API key directly. This can be combined with modifying options[email_from_name] for spoofing the welcome email sender, e.g., to impersonate another organization.

## Requirements

1. Intercepted POST request from previous step
2. Editing capabilities in dev tools or proxy
3. Knowledge of URL-encoded form data

## Defense

Defensive measures and detection strategies:

- Server-side enforcement of email verification regardless of client parameters
- Input validation and sanitization for all options[] fields
- Alert on discrepancies between client-submitted flags and default behavior

## Objectives

1. Disable email verification in the request
2. Optionally spoof email sender for phishing potential
3. Prepare request for submission without errors

## Instructions

### Step 1: Edit the verify_email Parameter

**Context**: Locate and alter the verification flag in the POST body to skip checks.

In the request editor, find options[verify_email]=true and change to options[verify_email]=false.

> The body is URL-encoded; ensure the change maintains format, e.g., &options[verify_email]=false.

### Step 2: Optional Email Spoofing Modification

**Context**: Enhance impact by altering the sender name for impersonation.

Set options[email_from_name]=Yahoo Company (or similar) to spoof the welcome email sender.

> Expected: Modified body includes the spoofed parameter; no immediate validation occurs client-side.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox-Browser-Developer-Tools]]

## Tags

- [[parameter-tampering]]
- [[auth-bypass]]
