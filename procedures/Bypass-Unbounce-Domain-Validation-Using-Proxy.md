---
id: proc-unbounce-bypass-001
tags:
  - api-bypass
  - domain-validation
  - proxy-intercept
  - subdomain-takeover
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
  - '[[Exploit Public-Facing Application]]'
  - '[[T1073.004]]'
updated_at: '2025-12-14T04:38:49.868Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1073.004]]'
---
# Bypass Unbounce Domain Validation Using Proxy

## Summary

This procedure intercepts and modifies HTTP requests to Unbounce's API endpoint, changing the domain parameter to an arbitrary value, exploiting the absence of server-side validation to enable subdomain takeover.

## Description

Unbounce's client-side restrictions prevent specifying custom domains during URL changes, but the API at /pages/{id}/url/confirm_or_update lacks backend checks. Using a proxy like Burp Suite, attackers alter the page[domain] from unbouncepages.com to a target (e.g., info.hacker.one with CNAME to unbouncepages.com). This allows claiming the subdomain for malicious hosting. Target environment is the web API; outcomes include successful domain override without errors.

## Requirements

1. Active Unbounce page from prior setup
2. Proxy tool configured ([[tools/Burp-Suite]])
3. Browser traffic routed through proxy
4. Knowledge of target subdomain's CNAME

## Defense

Defensive measures and detection strategies:

- Implement server-side domain whitelisting or validation
- Log and alert on mismatched domain parameters in API requests
- Use WAF to inspect and block parameter tampering

## Objectives

1. Intercept URL confirmation API call
2. Modify domain to victim subdomain
3. Achieve API acceptance for takeover

## Instructions

### Step 1: Configure Proxy

**Context**: Set up interception for Unbounce traffic.

Launch [[tools/Burp-Suite]] and configure browser proxy to 127.0.0.1:8080.

> Expected: All HTTP traffic intercepted.

### Step 2: Trigger API Request

**Context**: Initiate the URL change to generate interceptable POST.

In Unbounce dashboard, select 'CHANGE URL' on the page and attempt to set a path, using default domain.

> Expected: POST to /pages/{id}/url/confirm_or_update intercepted.

### Step 3: Modify and Forward Request

**Context**: Alter the domain parameter to bypass validation.

In Burp, edit page[domain]=unbouncepages.com to page[domain]=info.hacker.one (target subdomain), then forward.

> Expected: 200 OK response from API, no validation error.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[T1073.004]] Web Service

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- api-bypass
- subdomain-takeover
