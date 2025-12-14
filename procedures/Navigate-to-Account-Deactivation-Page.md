---
tags:
  - navigation
  - endpoint-access
  - evernote
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:57.159Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 7ed601c9-8362-46c2-b0d1-534a633fea02
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Navigate to Account Deactivation Page

## Summary

This procedure logs into an Evernote account and accesses the secure account deactivation page, preparing the environment for request interception in a CSRF vulnerability assessment.

## Description

To exploit the CSRF flaw, the attacker must first reach the deactivation endpoint (/secure/CloseAccount.action) while authenticated. This page allows selection of deactivation reasons but lacks CSRF protection, making it vulnerable. The procedure assumes a logged-in session and focuses on safe navigation without triggering deactivation.

## Requirements

1. Active Evernote account credentials
2. Browser with proxy support (for later steps)
3. Internet access

## Defense

Defensive measures and detection strategies:

- Log access to sensitive endpoints like deactivation pages
- Require additional authentication for destructive actions

## Objectives

1. Load the deactivation interface
2. Verify endpoint accessibility
3. Prepare for request capture

## Instructions

### Step 1: Log In to Account

**Context**: Authenticate to establish a session cookie necessary for endpoint access.

Use the web login:

1. Go to https://www.evernote.com/Login.action
2. Enter credentials and submit

> Dashboard loads upon success; session cookie is set.

### Step 2: Access Deactivation Page

**Context**: Navigate directly to the secure endpoint to view the form.

In the browser:

1. Enter URL: https://www.evernote.com/secure/CloseAccount.action
2. Confirm page loads with deactivation options

> Page should display warning popup and reason checkboxes; do not proceed to deactivate yet.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- navigation
- endpoint-access
- evernote
