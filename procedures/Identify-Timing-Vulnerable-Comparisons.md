---
id: proc-uuid-002
tags:
  - timing-attack
  - side-channel
  - php
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:24:35.055Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Identify-Timing-Vulnerable-Comparisons

## Summary

This procedure scans PHP code for strict equality operators (===, !==) in sensitive contexts like token or hash comparisons, which are prone to timing side-channel attacks allowing information leakage.

## Description

Timing attacks exploit differences in execution time for string comparisons; PHP's === stops at the first mismatch, revealing prefix lengths. In WP-API/OAuth1, lines 290 and 562 use these for tokens, enabling attackers to recover secrets by measuring API response times. This applies to web-based PHP applications with OAuth. Prerequisites: code access and knowledge of crypto best practices. Outcomes: documented vulnerabilities with remediation suggestions.

## Requirements

1. Access to PHP source code
2. Reference materials on timing attacks (e.g., articles on constant-time crypto)
3. Ability to simulate requests for time measurement

## Defense

Defensive measures and detection strategies:

- Replace with constant-time functions like hash_equals()
- Use timing-attack resistant libraries for auth
- Conduct static analysis with tools flagging variable-time ops

## Objectives

1. Flag non-constant-time comparisons in auth code
2. Explain risk of token leakage via timing
3. Recommend fixes like constant-time alternatives

## Instructions

### Step 1: Search for Equality Operators

**Context**: Locate all instances of === and !== in authentication files.

Use grep in the codebase:

```bash
grep -n '===' lib/class-wp-json-authentication-oauth1.php
grep -n '!==' lib/class-wp-json-authentication-oauth1.php
```

> Focus on lines involving user inputs like tokens; lines 290 and 562 are critical.

### Step 2: Assess Context and Risk

**Context**: Determine if comparisons are on sensitive data.

Review surrounding code for token/hash vars and note potential for remote timing via API calls.

> Cross-reference with external resources on PHP timing vulnerabilities.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques


## Commands Used

- [[grep-search-operators]]

## Tools Used


## Tags

- timing-attack
- cryptographic
