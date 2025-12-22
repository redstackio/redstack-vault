---
id: proc-222224-navigate-edit
tags:
  - navigation
  - wordpress
  - account-edit
type: procedure
tools:
  - '[[tools/Chrome]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques: []
updated_at: '2025-12-14T03:16:30.748Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Navigate-to-Account-Edit-Page

## Summary

This procedure accesses the vulnerable account edit form on mercantile.wordpress.org, where input validation is weaker than during registration.

## Description

After authentication, the /my-account/edit-account/ endpoint loads a form using AngularJS for rendering, allowing unrestricted input in name fields. This sets up the environment for payload injection in a self-XSS attack scenario.

## Requirements

1. Active user session from registration
2. [[tools/Chrome]] browser
3. Site accessibility

## Defense

Defensive measures and detection strategies:

- Rate-limit access to edit endpoints
- Log all profile edit attempts

## Objectives

1. Load the edit form
2. Expose vulnerable input fields
3. Confirm AngularJS rendering

## Instructions

### Step 1: Log In and Access Dashboard

**Context**: Ensure authenticated state and reach the account section.

In [[tools/Chrome]], log in if needed and navigate to the My Account dashboard.

> Dashboard shows user profile options.

### Step 2: Proceed to Edit Endpoint

**Context**: Directly access the edit form to prepare for injection.

Click the edit account link or enter /my-account/edit-account/ in the URL bar.

> Form loads with First Name and Last Name fields.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome]]

## Tags

- navigation
- wordpress
- account-edit
