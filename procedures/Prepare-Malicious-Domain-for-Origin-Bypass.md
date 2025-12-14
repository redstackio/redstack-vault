---
tags:
  - domain-registration
  - origin-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 812c408c-8157-4836-9369-26a727ac5005
created_at: '2025-12-14T17:33:34.478Z'
updated_at: '2025-12-14T17:33:34.478Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Prepare-Malicious-Domain-for-Origin-Bypass

## Summary

This procedure involves registering a domain that exploits the Digits SDK's flawed origin validation, where dots in the origin string are treated as regex wildcards, allowing partial matches to the legitimate 'https://www.digits.com'.

## Description

The Digits SDK at https://cdn.digits.com/1/sdk.js uses String.prototype.search() for origin checks, implicitly converting the origin to a regex. Dots (.) match any character, so a domain like 'www.d.gits.co' matches 'www.digits.com' because .gits. matches igits. The attacker registers such a domain to host a malicious page that can send postMessage events accepted by the SDK.

## Requirements

1. Access to a domain registrar (e.g., GoDaddy, Namecheap)
2. Web hosting service for static pages (e.g., GitHub Pages, AWS S3)
3. Knowledge of the target site's Digits integration

## Defense

Defensive measures and detection strategies:

- Update SDK to use strict string comparison instead of search()
- Implement Content Security Policy (CSP) to restrict postMessage origins
- Monitor for anomalous domain registrations matching known patterns

## Objectives

1. Create a domain that bypasses regex-based origin validation
2. Set up hosting for the exploit page
3. Validate the bypass in a test environment

## Instructions

### Step 1: Register Bypass Domain

**Context**: Select and register a domain that partially matches 'digits.com' via wildcard dots, such as www.d.gits.co.

**Instructions**: Use a domain registrar to search for and purchase the domain. Ensure it's HTTPS-enabled to match the expected origin protocol.

### Step 2: Host Malicious Page

**Context**: Upload an HTML file that will load in the victim's browser and prepare to send postMessage.

**Instructions**: Create fabric.html with basic structure including a script for postMessage. Upload to the hosted domain.

### Step 3: Verify Domain Match

**Context**: Test if the domain fools the regex check.

**Instructions**: In browser dev tools, simulate the search: console.log('https://www.digits.com'.search('https://www.d.gits.co')) – should return 0 for match.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[domain-bypass]]
- [[regex-flaw]]
