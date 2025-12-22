---
id: proc-uuid-5
tags:
  - csrf-forgery
  - impersonation
  - request-forging
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Forge Web Credentials]]'
updated_at: '2025-12-14T17:27:57.290Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Forge Web Credentials]]'
---
# Forge-CSRF-Protected-Requests-with-Stolen-Token

## Summary

This procedure uses the stolen CSRF token to craft and submit forged POST requests to Shopify's protected endpoints, bypassing protections and performing actions as the victim.

## Description

With the authenticity_token, the attacker can impersonate the victim by including it in form data or headers for state-changing requests, such as editing app listings (/services/shopify_applications/edit), submitting reviews, or sending support messages. This exploits the token's role in CSRF validation without additional auth checks.

## Requirements

1. Stolen authenticity_token from GA
2. Victim's session context (token is session-bound)
3. Tools like browser dev tools or curl for request crafting

## Defense

Defensive measures and detection strategies:

- Implement additional CSRF defenses like double-submit cookies or origin checks
- Log and monitor anomalous POSTs from non-standard sources
- Shorten token lifetimes and bind to IP/user-agent

## Objectives

1. Bypass CSRF validation
2. Execute unauthorized actions (edit, submit, message)
3. Achieve persistent impact on victim's account

## Instructions

### Step 1: Craft Forged Request

**Context**: Prepare a POST request to a target endpoint, embedding the stolen token.

No specific command; use browser tools or curl: curl -X POST https://apps.shopify.com/services/shopify_applications/edit -d "authenticity_token=[stolen_token]&other_params=value" -H "Cookie: session_id=victim_session".

> Expected output: Server accepts request as valid, processes changes.

### Step 2: Submit and Verify Action

**Context**: Execute the request and check for success.

No specific command; send the request and monitor response for 200 OK or redirect; verify in victim's account for changes like edited listing.

> Expected output: Successful response; unauthorized action completed.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Forge Web Credentials]] Forge Web Credentials

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- csrf-forgery
- impersonation
- request-forging
