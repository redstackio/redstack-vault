---
tags:
  - credential-theft
  - autofill
  - password-manager
type: procedure
tools:
  - '[[tools/Chrome-Password-Manager]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Keychain]]'
updated_at: '2025-12-14T17:30:07.586Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: c3a809af-cde8-46e3-983a-50d56ca08f05
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Keychain]]'
---
# Save-Credentials-for-Autofill-Leak

## Summary

This procedure stores credentials in the browser's password manager for the target domain, enabling demonstration of autofill leakage when submitting injected forms to arbitrary domains due to missing CSP form-action.

## Description

Browser password managers like Chrome's automatically fill username/password fields on forms for matching domains. Without a restrictive 'form-action' CSP directive, injected forms can submit to external hosts, capturing autofilled data. This targets sites with saved logins and CSP fallback to default-src (allowing *). Requires prior access to the password manager interface.

## Requirements

1. Chrome or similar browser with password manager
2. Target domain (e.g., portswigger.net)
3. Fake credentials for testing

## Defense

Defensive measures and detection strategies:

- Specify 'form-action self' or specific domains in CSP
- Disable autofill for sensitive sites via browser settings
- Monitor for anomalous form submissions in server logs
- Use client-side checks to validate form actions

## Objectives

1. Store credentials for autofill
2. Enable leakage via injected forms
3. Simulate real user credential exposure

## Instructions

### Step 1: Access Password Manager

**Context**: Open the password manager to add an entry.

**Instructions**: Navigate to chrome://password-manager/passwords in the browser.

> Expected output: Password manager interface loads.

### Step 2: Add Saved Credentials

**Context**: Create a new entry for the target site.

**Instructions**: Click 'Add' and enter details: Site = https://portswigger.net, Username = testuser, Password = testpass.

> Expected output: Credentials saved; will autofill on forms for the domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Keychain]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome-Password-Manager]]

## Tags

- [[credential-theft]]
- [[autofill]]
- [[password-manager]]
