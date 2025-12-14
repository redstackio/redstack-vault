---
id: proc-phab-verify-guest-edit-denied
tags:
  - phabricator
  - verification
  - access-control
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:44.820Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Guest-Access-Denied-to-Edit-Endpoint

## Summary

This procedure tests that guest users are correctly denied access to the repository edit endpoint in Phabricator Diffusion, confirming the vulnerability's specificity to the delete action.

## Description

Phabricator enforces permissions on edit operations but overlooks them in the mirror delete controller. As a guest (unauthenticated user), attempting to access the edit URL should result in a denial, validating that the bypass is not a general access issue. This step uses direct URL navigation and observes the response.

## Requirements

1. Existing repository (e.g., 'TEST') created by admin
2. Guest access (no login) to Phabricator
3. Web browser for URL access

## Defense

Defensive measures and detection strategies:

- Implement consistent permission checks across all Diffusion controllers
- Log failed access attempts to edit endpoints
- Use Phabricator's Herald rules for automated policy enforcement

## Objectives

1. Confirm edit endpoint protection
2. Isolate the vulnerability to delete functionality
3. Ensure test environment integrity

## Instructions

### Step 1: Access as Guest User

**Context**: Simulate unauthenticated access to verify restrictions.

Open a browser in incognito mode or log out, then navigate to http://phabricator/diffusion/TEST/edit/.

> Expected: Permission denied page or 403 error, indicating access control is active for edits.

### Step 2: Observe Response

**Context**: Validate the denial without proceeding to exploitation.

Check for error messages like 'You do not have permission to view this page'.

> Success: No edit form or repository details exposed to guest.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[phabricator]]
- [[access-denied]]
- [[verification]]
