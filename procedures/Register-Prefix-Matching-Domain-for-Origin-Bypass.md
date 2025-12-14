---
tags:
  - domain-registration
  - origin-bypass
  - xss
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 81e78403-8250-4996-b05c-84f9358568ce
created_at: '2025-12-13T23:55:38.319Z'
updated_at: '2025-12-13T23:55:38.319Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Register-Prefix-Matching-Domain-for-Origin-Bypass

## Summary

This procedure involves registering a domain that serves as a prefix for the target origin (e.g., Marketo's 'app-sj17.marketo.com') to bypass flawed origin validation in JavaScript postMessage handlers, enabling subsequent XSS attacks.

## Description

In scenarios like the Marketo forms2.min.js library, origin checks use i.indexOf(origin) === 0, which verifies if the expected origin starts with the event origin. By registering a domain like 'app-sj17.ma', the attacker creates an origin 'https://app-sj17.ma' that the expected origin starts with, allowing malicious postMessage events to pass validation. This is particularly effective against web applications integrating third-party scripts like Marketo forms on sites such as www.hackerone.com. Prerequisites include access to a domain registrar supporting .ma TLDs; expected outcome is control over a domain usable for hosting XSS payloads.

## Requirements

1. Account with a domain registrar supporting .ma domains (e.g., Moroccan providers)
2. Budget for registration (~€60)
3. Basic DNS knowledge for propagation

## Defense

Defensive measures and detection strategies:

- Implement strict origin equality checks (e.g., origin === expectedOrigin) instead of prefix matching
- Use Content Security Policy (CSP) with strict postMessage directives
- Monitor for unusual domain registrations or postMessage events from unexpected origins

## Objectives

1. Acquire a domain enabling origin bypass in postMessage handlers
2. Set up for hosting malicious payloads
3. Facilitate DOM-based XSS execution

## Instructions

### Step 1: Select and Register Domain

**Context**: Choose a prefix like 'app-sj17' to match the target's Marketo subdomain structure.

No specific command; use registrar UI to search and purchase 'app-sj17.ma'.

> Register via provider website; confirm ownership via email. Expected: Domain active after DNS propagation (up to 48 hours).

### Step 2: Configure DNS

**Context**: Point the domain to a hosting server for POC deployment.

No specific command; set A/AAAA records in registrar DNS panel to your server's IP.

> Ensure HTTPS support with SSL certificate. Expected: Domain resolves to hosting server.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[domain-registration]]
- [[origin-bypass]]
