---
tags:
  - web-cache-poisoning
  - bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/get-job-listing-js]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 25966d67-dcac-410f-b6fb-49f52063d8be
created_at: '2025-12-13T09:00:34.783Z'
updated_at: '2025-12-13T09:00:34.783Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass Previous Fix via URL Caching

## Summary

This procedure bypasses a previous fix for web cache poisoning by accessing URLs with specific file extensions like .js, triggering caching and exposing sensitive data such as anti-CSRF tokens.

## Description

The attack targets endpoints that cache responses based on file extensions without proper validation, allowing bypass of prior mitigations and exposure of tokens across pages. This is applicable in web environments using caching proxies like Cloudflare.

## Requirements

1. Access to the target web application
2. HTTP client for sending requests
3. Knowledge of vulnerable endpoints

## Defense

Defensive measures and detection strategies:

- Implement explicit cache-control headers to prevent poisoning
- Use Cloudflare web cache armor
- Monitor for anomalous cache hits on sensitive endpoints

## Objectives

1. Trigger caching of sensitive responses
2. Expose anti-CSRF tokens
3. Validate bypass of previous fixes

## Instructions

### Step 1: Send Request to Vulnerable URL

**Context**: Access the job listing URL with .js extension to force caching.

**Command** ([[commands/get-job-listing-js]]):

```bash
curl 'https://www.glassdoor.com/job-listing/011.js?jl=1007452474740'
```

> This request returns a 200 OK and caches the response, exposing gdToken.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/get-job-listing-js]]

## Tools Used



## Tags

- [[web-cache-poisoning]]
- [[bypass]]
