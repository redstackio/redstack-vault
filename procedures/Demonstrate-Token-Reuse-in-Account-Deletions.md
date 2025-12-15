---
id: proc-002
tags:
  - csrf
  - token-reuse
  - deletion-action
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
updated_at: '2025-12-14T17:27:15.307Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Demonstrate Token Reuse in Account Deletions

## Summary

This procedure performs deletion of linked third-party accounts within a single Liberapay account, capturing and verifying that the same CSRF token is reused across multiple deletion actions, exposing the lack of token regeneration.

## Description

Targeting Liberapay's 'Accounts Elsewhere' section, this procedure involves initiating deletions of linked external services (e.g., Google+) and inspecting network requests via browser tools to observe the CSRF token. The token is stored in a generic 7-day cookie not tied to the account, allowing reuse. This is key to showing the vulnerability in a same-session environment. Outcomes include captured token values confirming reuse, with potential for CSRF exploitation if paired with other flaws.

## Requirements

1. Existing Liberapay account with at least one linked external service
2. Browser Developer Tools enabled for network inspection
3. Same browser session as account creation

## Defense

Defensive measures and detection strategies:

- Regenerate CSRF tokens per action or session change (e.g., on login/logout)
- Bind tokens to user sessions or account IDs to prevent cross-account reuse
- Log and alert on repeated use of the same token for sensitive endpoints

## Objectives

1. Execute deletion actions to trigger CSRF token usage
2. Capture and compare tokens across deletions to prove reuse
3. Highlight risks of non-regenerating generic cookies

## Instructions

### Step 1: Initiate First Deletion and Capture Token

**Context**: Delete a linked account to expose the initial CSRF token in the request.

In the profile's 'Accounts Elsewhere', select and confirm deletion of the Google+ link. Open Developer Tools > Network tab, filter for the POST request to the deletion endpoint (e.g., /unlink/google), and copy the CSRF token from the request body or Authorization header (example: 'J0Lk5iXTpp40iDN5KNcrI24bulPcF0PV').

> Expected output: Account unlinked; token value noted as a 32-character string.

### Step 2: Perform Additional Deletion with Token Comparison

**Context**: Link and delete another service to verify token persistence.

Link a second external service (e.g., another platform), then delete it. Inspect the new deletion request and confirm the CSRF token matches the previous one.

> Expected output: Identical token used; deletion succeeds without regeneration.

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
- [[token-reuse]]
- [[web-deletion]]
