---
id: uuid2
tags:
  - xss
  - stored-xss
  - subdomain
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:50.235Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Establish-Control-Over-Subdomain-via-Stored-XSS

## Summary

Exploit a Stored XSS vulnerability on a subdomain (e.g., marketing.victim.com) to gain persistent control over page content, enabling CSRF injection against Argo CD on a sibling subdomain.

## Description

Stored XSS allows attacker-controlled scripts to execute for all visitors. In this scenario, assume an existing XSS vuln on the marketing site. The subdomain shares the parent domain, allowing cookie inclusion due to Lax SameSite. This sets up the vector for tricking users into CSRF.

## Requirements

1. Existing Stored XSS on target subdomain
2. Browser dev tools for payload testing
3. Same parent domain as Argo CD

## Defense

Defensive measures and detection strategies:

- Sanitize user inputs to prevent XSS
- Implement Content Security Policy (CSP)
- Monitor for anomalous script injections in web logs

## Objectives

1. Persist malicious script on subdomain
2. Verify execution on page load
3. Prepare for JS injection

## Instructions

### Step 1: Identify XSS Endpoint

**Context**: Find input fields vulnerable to Stored XSS.

**Command** (no specific, manual):

> Submit payload like `<script>alert('XSS')</script>` via form. Expected output: Alert on page refresh.

### Step 2: Persist Control

**Context**: Store the payload to affect multiple users.

**Command** (no specific, via app interface):

> Use vulnerable comment or profile field. Expected output: Script runs for visitors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- stored-xss
