---
id: proc-capture-sso-cookies
tags:
  - cookie-theft
  - sso
  - phishing
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
  - '[[Pass the Hash]]'
updated_at: '2025-12-14T04:39:01.853Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Pass the Hash]]'
---
# Capture Victim's SSO Cookies Via Malicious Page

## Summary

This procedure hosts a malicious page on the taken-over subdomain to lure victims, initiating an SSO flow that captures shared session cookies and CSRF tokens for later replay.

## Description

The victim, already logged into auth.uber.com and riders.uber.com, visits https://saostatic.uber.com/prepareuberattack.php. The page triggers a redirect to riders.uber.com, capturing the auth.uber.com URL (with state=CSRFTOKEN), state cookie, and _csid Set-Cookie header. This exploits shared .uber.com domain cookies leaking to the compromised subdomain.

## Requirements

1. Control over subdomain (from takeover)
2. PHP or similar scripting capability on origin server
3. Victim authenticated to target SSO services

## Defense

Defensive measures and detection strategies:

- Set cookies to Secure, HttpOnly, and SameSite=Strict
- Validate IP binding for session tokens
- Monitor for anomalous logins from compromised subdomains

## Objectives

1. Steal shared session cookies without interaction
2. Capture CSRF state for relay
3. Enable impersonation preparation

## Instructions

### Step 1: Host Malicious PHP Script

**Context**: Deploy a script to initiate SSO and log headers.

**Instructions**: Upload prepareuberattack.php to origin, which redirects to riders.uber.com/login and logs request/response headers via file or remote exfil.

> Example script: Use curl or header() to capture. Expected: Logs show auth URL, Cookie: state=..., Set-Cookie: _csid=...

### Step 2: Lure Victim to Page

**Context**: Trick victim into visiting via email/link/iframe.

**Instructions**: Send link to https://saostatic.uber.com/prepareuberattack.php. Victim visit triggers capture automatically.

> Success: Captured data stored for relay step.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Pass the Hash]] Use Alternate Authentication Material: Pass the Cookie

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- cookie-theft
- sso
- phishing
