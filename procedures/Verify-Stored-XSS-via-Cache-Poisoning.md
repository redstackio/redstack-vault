---
tags:
  - xss
  - cache-poisoning
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/verify-xss-payload]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e2f1590f-5013-4ba3-937e-d7e1a4a9a52d
created_at: '2025-12-14T00:11:25.427Z'
updated_at: '2025-12-14T00:11:25.427Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Verify Stored XSS via Cache Poisoning

## Summary

This procedure verifies the success of cache poisoning by checking if the injected XSS payload is served from the cache, interfering with page integrity.

## Description

After poisoning, access the affected page to confirm that malicious content is rendered, leading to stored XSS on PayPal's sign-in page without affecting backend data.

## Requirements

1. Poisoned cache
2. Browser or tool to access the page
3. XSS payload knowledge

## Defense

Defensive measures and detection strategies:

- Use CSP headers to prevent XSS
- Regularly flush suspicious cache entries

## Objectives

1. Confirm XSS execution
2. Assess impact on page functionality
3. Validate exploit chain

## Instructions

### Step 1: Access Poisoned Page

**Context**: Request the sign-in page to trigger poisoned cache.

**Command** ([[commands/verify-xss-payload]]):

```bash
curl https://paypal.com/signin
```

> Inspect for injected content.

### Step 2: Test XSS Execution

**Context**: Execute in browser to verify script runs.

**Command** ([[commands/verify-xss-payload]]):

```bash
# Use browser developer tools
```

> Check for alerts or DOM changes.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/verify-xss-payload]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[cache-poisoning]]
