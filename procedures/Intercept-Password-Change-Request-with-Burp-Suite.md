---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567893
name: Intercept-Password-Change-Request-with-Burp-Suite
tags:
  - interception
  - burp-suite
  - csrf
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:11.964Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-Password-Change-Request-with-Burp-Suite

## Summary

This procedure uses Burp Suite to capture the HTTP POST request from a legitimate password change submission, revealing parameters needed for CSRF forgery.

## Description

With Burp Suite proxying traffic, submitting a test password change intercepts the request to https://████████.mil/scripts/wa.exe. Parameters like GETPW2 (possibly a flag), Y, p (new password), q (email), and X are extracted. This is key for replicating the request without tokens in the CSRF PoC. Target is IIS-based web app.

## Requirements

1. Burp Suite installed and configured as browser proxy
2. Authenticated session active
3. Test credentials (secondary email and password) for submission

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS and HSTS to prevent interception
- Implement request signing or tokens to invalidate forged requests
- Monitor proxy-like traffic anomalies in network logs

## Objectives

1. Capture exact POST parameters and values
2. Analyze endpoint behavior
3. Identify lack of CSRF protection

## Instructions

### Step 1: Enable Interception in Burp Suite

**Context**: Set up Burp to capture outgoing requests from the browser.

No specific command; in Burp, go to Proxy > Intercept and turn it on.

> Browser traffic routes through Burp at localhost:8080.

### Step 2: Submit Test Password Change

**Context**: Fill and submit the form to trigger the intercept.

No specific command; enter secondary email in q field, new password in p, and submit.

> Burp halts on the POST to /scripts/wa.exe; forward after inspection to complete.

### Step 3: Analyze Captured Request

**Context**: Extract parameters for PoC crafting.

No specific command; view raw request in Burp Repeater or Inspector.

> Expected: POST data with p=attackerpass, q=victim@email.com, etc.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- interception
- burp-suite
- csrf
