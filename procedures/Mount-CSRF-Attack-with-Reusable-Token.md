---
tags:
  - csrf
  - token-leakage
  - web-attack
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:27:29.214Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: c85cd60d-a238-4c61-94cb-faba7a78c935
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Mount CSRF Attack with Reusable Token

## Summary

This procedure uses the leaked, non-expiring CSRF token to forge requests to the Robocoin wallet, bypassing built-in protections and executing actions on the victim's behalf.

## Description

With the token in hand, an attacker crafts cross-site requests (e.g., via HTML forms on a malicious site) that mimic legitimate actions like fund transfers or account changes. The token's reusability allows repeated attacks without regeneration. This targets the authenticated session, assuming the victim remains logged in. The attack exploits the verification flaw's impact across the application.

## Requirements

1. Retrieved CSRF token from previous steps
2. Knowledge of target endpoints (e.g., /transfer or /update)
3. Victim's session must be active

## Defense

Defensive measures and detection strategies:

- Enforce token expiration and single-use
- Implement same-site cookies (Lax/Strict)
- Log and alert on mismatched or reused tokens

## Objectives

1. Forge a request including the stolen token
2. Execute unauthorized action successfully
3. Confirm bypass of CSRF protections

## Instructions

### Step 1: Construct Forged Request

**Context**: Build an HTML form or use developer tools to simulate a POST with the token.

Create a simple HTML page with a form targeting https://wallet.robocoin.com/action (replace with actual endpoint), including hidden input <input name="_csrf" value="leaked_token"> and action fields (e.g., amount=100).

> Load the page in the victim's browser context (e.g., via iframe or link) to auto-submit.

### Step 2: Submit and Verify

**Context**: Trigger the request and check for success.

Submit the form or use curl in console for testing: Open dev tools, go to console, and execute a fetch or XMLHttpRequest with the token in headers.

> Expected: Server accepts the request without CSRF error, performing the action (e.g., balance change). Token remains valid for reuse.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[token-leakage]]
