---
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
'tags | [':
  - redirect
  - reauth
platforms:
  - Web
techniques:
  - '[[Malicious Link]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: e1bb3d2a-f472-47b1-8b05-10574c1b8001
created_at: '2025-12-13T23:56:03.993Z'
updated_at: '2025-12-13T23:56:03.993Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Malicious Link]]'
---
# Use Redirect to Re-Authenticate Embedded App

## Summary

This procedure uses a redirect from shopify.com to the victim's store to re-authenticate the embedded app with the victim's session.

## Description

By navigating to https://www.shopify.com/admin/oauth/authorize, which redirects to the last logged-in store, this step switches the context to the victim's store and triggers re-authentication. This abuses the redirect to align sessions for XSS execution. Requires prior CSRF login.

## Requirements

1. Victim logged in via CSRF
2. Access to the redirect URL
3. Embedded app setup

## Defense

Defensive measures and detection strategies:

- Validate redirects in auth flows
- Use session-specific tokens

## Objectives

1. Trigger redirect
2. Re-authenticate app
3. Align sessions

## Instructions

### Step 1: Navigate to Redirect URL

**Context**: Load the shopify.com authorize page.

> This automatically redirects to victim's store.

### Step 2: Trigger Auth Flow

**Context**: Initiate the embedded app auth in the new context.

> Load the app to complete re-auth.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Malicious Link]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- redirect
- reauth
