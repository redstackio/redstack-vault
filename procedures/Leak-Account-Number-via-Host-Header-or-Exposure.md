---
tags:
  - host-header-injection
  - info-leak
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques:
  - '[[T1190.003]]'
id: ab1a2428-f5fb-48ba-9ee5-c77d3a77716f
created_at: '2025-12-14T17:27:15.801Z'
updated_at: '2025-12-14T17:27:15.801Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Leak-Account-Number-via-Host-Header-or-Exposure

## Summary

This procedure leaks sensitive account numbers from Coinbase by exploiting exposed URLs in browser history/logs or via Host Header Injection to misdirect requests to attacker-controlled domains.

## Description

Account numbers are exposed in GET request URLs on Coinbase, retrievable from history, proxies, or logs. Without Host header validation, attackers can alter the header (e.g., to evil.com) in requests, causing server logs or referrals to leak numbers, aiding CSRF without direct victim access.

## Requirements

1. Proxy tool for header manipulation (e.g., Burp)
2. Control over a domain for logging leaks
3. Victim's partial interaction or log access

## Defense

Defensive measures and detection strategies:

- Validate and sanitize Host headers strictly
- Avoid logging sensitive params in error responses
- Monitor for anomalous Host values in requests

## Objectives

1. Extract account number from exposures
2. Demonstrate injection for leakage
3. Enable follow-on CSRF attacks

## Instructions

### Step 1: Check for URL Exposure

**Context**: Gather account numbers from accessible sources.

Review browser history or proxy logs for requests like /accounts/12345/set_as_primary to extract the number.

### Step 2: Perform Host Header Injection

**Context**: Manipulate header to leak via misdirection.

Intercept a Coinbase request with a proxy, change Host: coinbase.com to Host: evil.com, and forward. Check evil.com logs or referrals for leaked account_number in query params.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

- [[T1190.003]]

## Commands Used


## Tools Used


## Tags

- [[host-header-injection]]
- [[info-leak]]
