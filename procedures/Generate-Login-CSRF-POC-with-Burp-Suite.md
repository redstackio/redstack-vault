---
id: proc-uuid-5
name: Generate-Login-CSRF-POC-with-Burp-Suite
tags:
  - csrf
  - poc-generation
  - burp-suite
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T00:11:09.567Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Generate-Login-CSRF-POC-with-Burp-Suite

## Summary

This procedure intercepts a login request and uses Burp Suite to auto-generate a CSRF proof-of-concept HTML file that can force a victim's browser to authenticate as the attacker.

## Description

CSRF exploits lack of token protection on login forms. Burp's tool creates an HTML form with auto-submit JS, embedding credentials to forge logins cross-origin.

## Requirements

1. Burp Suite proxy configured in browser
2. Attacker credentials
3. Target login endpoint

## Defense

Defensive measures and detection strategies:

- Add CSRF tokens to all forms
- Use SameSite cookies
- Monitor for cross-origin POSTs to auth endpoints

## Objectives

1. Capture login request
2. Generate exploitable HTML PoC
3. Enable forced authentication

## Instructions

### Step 1: Intercept Login Request

**Context**: Proxy traffic through Burp.

Configure browser proxy to Burp, attempt login, and capture the POST request in Proxy/HTTP history.

> Request shows credentials in form data.

### Step 2: Generate PoC

**Context**: Create malicious HTML.

Right-click request > Action > Engagement Tools > Generate CSRF PoC; copy the HTML.

> HTML includes <form> with hidden fields and JS to submit.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- csrf
- poc-generation
- burp-suite
