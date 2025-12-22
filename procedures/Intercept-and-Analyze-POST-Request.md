---
id: proc-intercept-post-001
tags:
  - intercept
  - analyze
  - mitm
  - token
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Adversary-in-the-Middle]]'
  - '[[Network Sniffing]]'
updated_at: '2025-12-14T17:27:29.277Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
  - '[[Network Sniffing]]'
---
# Intercept-and-Analyze-POST-Request

## Summary

This procedure uses a proxy to capture and examine the HTTP POST request from the subscription form, revealing the leaked CSRF token for potential MiTM exploitation.

## Description

The request to the external endpoint (e.g., a newsletter service) includes the CSRF token in plaintext over HTTP. Analysis confirms the vulnerability. Expected: Token visible in body, protocol unencrypted.

## Requirements

1. Burp Suite proxy configured and intercepting
2. Form submission triggered
3. Knowledge of request structure (POST body params)

## Defense

Defensive measures and detection strategies:

- Encrypt all token transmissions with HTTPS
- Use token binding to sessions and validate on server
- Detect MiTM via traffic anomaly monitoring (e.g., HTTP in HTTPS contexts)

## Objectives

1. Capture the leaking request
2. Extract CSRF token from body
3. Validate MiTM bypass potential

## Instructions

### Step 1: Enable Interception

**Context**: Pause requests in proxy for inspection.

In Burp Proxy > Intercept, ensure "Intercept is on".

### Step 2: Trigger and Capture

**Context**: Submit form to queue the request.

Forward the intercepted POST; inspect in HTTP history if needed.

### Step 3: Analyze Request

**Context**: Examine for token and protocol.

View raw request: Confirm HTTP URL and search body for CSRF param (e.g., _token=abc123).

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle
- [[Network Sniffing]] Network Sniffing

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[intercept]]
- [[mitm]]
- [[token-leak]]
