---
tags:
  - web
  - auth-bypass
  - information-disclosure
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
updated_at: '2025-12-14T17:24:44.771Z'
sub_techniques: []
id: 3b7fe095-3dc5-4e3e-bea7-092f8d80928e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Direct-Browser-Access-to-Exposed-Passenger-Endpoint

## Summary

This procedure exploits the exposed auth_token in the URL to access the Grab passenger endpoint directly in a browser, disclosing private messages without app authentication.

## Description

The endpoint `https://grab-attention.grabtaxi.com/passenger/passenger.html` accepts the auth_token via GET query parameters, allowing any browser to load private content like OTP pins and group invites if the token is known. This bypasses the app's security controls and highlights the risks of URL-based authentication.

## Requirements

1. Captured URL from the app's network request including auth_token
2. Standard web browser (e.g., Chrome)
3. Internet access to the grab-attention.grabtaxi.com domain

## Defense

Defensive measures and detection strategies:

- Enforce server-side checks for request origin (e.g., referer headers or app-specific signatures)
- Implement short-lived tokens and rate limiting on the endpoint
- Use robots.txt or meta tags to prevent indexing, though this doesn't fix the core issue

## Objectives

1. Load the endpoint to view unauthorized private data
2. Confirm lack of authentication enforcement
3. Assess scope of disclosed information

## Instructions

### Step 1: Prepare the URL

**Context**: Use the captured URL from the app inspection.

No command required.

> Ensure the URL includes `?auth_token=[your_token]&view=268435456`.

### Step 2: Access in Browser

**Context**: Paste and load the URL to exploit the misconfiguration.

No command required; perform in browser.

> Open a browser and navigate to the full URL. The page should load private messages directly.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web]]
- [[auth-bypass]]
- [[information-disclosure]]
