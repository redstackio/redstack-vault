---
id: proc-736522-initial-auth
tags:
  - authentication
  - jwt
  - magic-link
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:10.856Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Perform-Initial-User-Authentication

## Summary

This procedure simulates legitimate user login to the authmagic app, obtaining initial access and refresh tokens required for the subsequent JWT forgery attack.

## Description

The authmagic example app uses magic link authentication: users enter an email, receive a link via console/email, and click it to authenticate. This generates JWT access and refresh tokens. The vulnerability arises later during refresh, but this step establishes a baseline session. The process targets http://localhost:3000 and relies on the vulnerable core module's token issuance.

## Requirements

1. Running authmagic server on localhost:3000
2. Web browser
3. Console access for link preview

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on authorization links
- Validate email domains and use secure email transport (e.g., SMTP over TLS)
- Log all authentication attempts for anomaly detection

## Objectives

1. Obtain valid tokens
2. Establish user session
3. Prepare for token refresh exploitation

## Instructions

### Step 1: Access App and Request Link

**Context**: Initiate the magic link flow.

**Instructions**: Open http://localhost:3000 in a browser, enter an email (e.g., test@example.com), and click 'Send authorization link'. The link appears in the console.

No command; browser action.

> Expected output: Console shows preview URL like 'http://localhost:3000/auth?token=...'.

### Step 2: Follow Authorization Link

**Context**: Open the magic link to proceed.

**Instructions**: Copy the console URL and open it in the browser.

No command; browser action.

> Expected output: Redirect to authorization page.

### Step 3: Complete Authentication

**Context**: Finalize login to receive tokens.

**Instructions**: Click the 'Click here' link in the email simulation.

No command; browser action.

> Expected output: Access and refresh tokens displayed in the app.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authentication
- jwt
- magic-link
