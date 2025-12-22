---
id: proc-001
tags:
  - csrf
  - account-creation
  - oauth-linking
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
updated_at: '2025-12-14T17:27:15.311Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create Liberapay Account and Link External Service

## Summary

This procedure creates a new Liberapay account and links an external third-party service like Google+ or Facebook via the 'Accounts Elsewhere' feature, setting up the environment to test CSRF token behavior during subsequent actions.

## Description

In the context of demonstrating CSRF token reuse in Liberapay, this procedure involves standard user registration on the Liberapay web platform followed by OAuth-based linkage to external accounts. It targets the profile management section where tokens are involved in sensitive operations. Prerequisites include a web browser and access to an external account for linking. Expected outcomes are a functional Liberapay account with verified external linkage, preparing for deletion tests that expose token persistence.

## Requirements

1. Web browser with cookies enabled (e.g., Chrome)
2. Access to an external platform account (e.g., Google+ or Facebook credentials)
3. Internet connection to liberapay.com

## Defense

Defensive measures and detection strategies:

- Implement account-specific CSRF token generation and binding to sessions or user IDs
- Monitor for unusual account creation patterns in the same session (e.g., multiple sign-ups without logout)
- Use browser fingerprinting to detect session reuse across accounts

## Objectives

1. Establish a test Liberapay account for vulnerability demonstration
2. Link external service to enable deletion actions involving CSRF tokens
3. Verify setup without triggering any security alerts

## Instructions

### Step 1: Register New Liberapay Account

**Context**: Begin by creating a fresh account to ensure a clean session for token observation.

Navigate to https://liberapay.com and click 'Sign Up'. Provide a username and email, then complete the registration process without linking any external services yet.

> Expected output: Redirect to the new account dashboard with profile access.

### Step 2: Access Profile and Link External Service

**Context**: Use the profile section to initiate OAuth linkage, which sets the stage for token-protected deletions.

Go to the user profile, select 'Accounts Elsewhere', and choose to link Google+ (or Facebook). Authenticate with the external service credentials to complete the connection.

> Expected output: External account listed as linked in the profile; no errors in linkage.

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
- [[account-creation]]
- [[oauth]]
