---
id: proc-csrf-referrer-bypass
tags:
  - csrf
  - bypass
  - referrer
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-trigger-csrf]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:49.877Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-Referrer-Protection-via-Subdomain-Redirect

## Summary

This procedure bypasses partial referrer-based protections in the CSRF attack by using the www subdomain to spoof the Referer header through a 404 redirect.

## Description

HackerOne partially relies on Referer headers for validation, but accessing https://www.hackerone.com/{program}?apply=true results in a 404 that redirects to the main domain, setting Referer to the www URL. This evades strict same-origin checks, allowing the CSRF to succeed.

## Requirements

1. Access to www subdomain (publicly resolvable)
2. Target URL from prior procedures
3. Victim's browser to follow redirects

## Defense

Defensive measures and detection strategies:

- Implement strict referrer policy (strict-origin-when-cross-origin)
- Validate referrers against whitelists, ignoring subdomains
- Log cross-subdomain redirects for anomaly detection
- Use CSRF tokens instead of referrer reliance

## Objectives

1. Spoof Referer to bypass partial protections
2. Ensure CSRF works despite domain checks
3. Enhance attack reliability via redirects

## Instructions

### Step 1: Access Subdomain URL

**Context**: Initiate the redirect chain to set spoofed Referer.

**Command** ([[commands/curl-trigger-csrf]]):
```bash
curl -X GET "https://www.hackerone.com/hackthedts?apply=true" -L -H "Referer: https://www.hackerone.com" -v
```

> -L follows 404 redirect; expect final GET with www Referer, leading to submission.

### Step 2: Confirm Bypass

**Context**: Verify the request succeeds with altered Referer.

Inspect headers in response; successful if application submits as in core CSRF.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-trigger-csrf]]

## Tools Used


## Tags

- [[csrf]]
- [[bypass]]
