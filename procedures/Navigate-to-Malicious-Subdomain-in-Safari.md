---
id: proc-uuid-2
tags:
  - csrf
  - domain-bypass
type: procedure
tools:
  - '[[tools/Safari-Browser]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:49.686Z'
skill_level: basic
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Navigate-to-Malicious-Subdomain-in-Safari

## Summary

This procedure loads an attacker-controlled subdomain with special characters that bypasses Referer checks in Safari, setting up the CSRF environment.

## Description

The vulnerability stems from a regex flaw allowing domains like new.cs.money{.nnez.me}. Safari loads these without stripping characters, unlike other browsers, enabling CORS and Referer spoofing for CSRF.

## Requirements

1. Control over a domain like nnez.me to register the subdomain
2. Safari browser
3. Hosted malicious page on the subdomain

## Defense

Defensive measures and detection strategies:

- Validate Referer with strict regex excluding special characters
- Enforce SameSite=Strict on cookies
- Block subdomains with non-standard characters

## Objectives

1. Load the exploit page
2. Ensure Referer appears valid to target
3. Avoid browser blocking

## Instructions

### Step 1: Open New Tab

**Context**: Isolate the malicious load from the authenticated session.

No command; create a new tab in Safari.

> Expected: Blank tab ready.

### Step 2: Enter Malicious URL

**Context**: Direct navigation to trigger the load.

Manually enter https://new.cs.money{.nnez.me} in the address bar.

> Expected: Page loads; check network tab for no CORS errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Safari-Browser]]

## Tags

- csrf
- domain-bypass
