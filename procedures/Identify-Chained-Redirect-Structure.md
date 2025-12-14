---
id: proc-starbucks-identify-redirect
tags:
  - open-redirect
  - parameter-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-chained-redirect]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:47:23.407Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Identify-Chained-Redirect-Structure

## Summary

This procedure uncovers the payload structure for open redirects by testing specific malformed inputs that exploit tag stripping and chained logic in Starbucks web applications.

## Description

Following initial testing, further manipulation reveals that structures like '<>//google.com' in GET parameters trigger redirects after partial HTML tag stripping. This allows arbitrary external redirects, useful for phishing. The procedure assumes prior access to the target and focuses on iterative payload refinement.

## Requirements

1. Basic HTTP client (e.g., curl).
2. Knowledge of target parameters (e.g., prefn1).
3. Monitoring capability for redirect chains.

## Defense

Defensive measures and detection strategies:

- Validate redirect URLs against a whitelist.
- Sanitize inputs to remove or escape '<>' prefixes.
- Implement redirect rate limiting.

## Objectives

1. Determine exact bypass payload.
2. Confirm arbitrary redirect capability.
3. Document chained behavior.

## Instructions

### Step 1: Test Specific Payload Structure

**Context**: Inject the '<>//external-site' format into a GET parameter to observe post-sanitization redirect.

**Command** ([[commands/curl-chained-redirect]]):
```bash
curl -v "https://shop.starbucks.de/?prefn1=<>//google.com" 2>&1 | grep Location
```

> The command follows the redirect chain implicitly via -v output, showing the final Location as google.com if successful.

### Step 2: Verify Chaining

**Context**: Ensure the redirect occurs after internal processing, indicating a chain.

Use browser dev tools to trace multiple 302s.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used

- [[commands/curl-chained-redirect]]

## Tools Used


## Tags

- [[open-redirect]]
- [[parameter-bypass]]
