---
id: proc-uuid-instacart-xss-bypass-001
tags:
  - xss
  - bypass
  - filter-evasion
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:12.870Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Bypass-Filtering-with-URL-Fragment

## Summary

This procedure modifies the XSS payload by appending a URL fragment with comments to evade basic sanitization filters that might block standalone javascript: protocols, ensuring the injection remains effective.

## Description

Some applications may filter or strip plain javascript: schemes. By using 'javascript:alert(1)//https://example.com', the // comments out the trailing valid URL, fooling regex-based checks while preserving execution. This builds on prior injection and trigger steps, enhancing reliability against partial defenses in the Instacart recipe_url handling.

## Requirements

1. Initial payload that was potentially blocked
2. Knowledge of common filtering patterns (e.g., blocking 'javascript:')
3. Web browser for re-testing

## Defense

Defensive measures and detection strategies:

- Use comprehensive protocol whitelisting (e.g., only allow http/https)
- Parse and normalize URLs server-side before reflection
- Employ advanced WAF rules to detect comment-based evasions in parameters

## Objectives

1. Circumvent basic input filters
2. Maintain payload integrity for execution
3. Increase attack success rate against defended targets

## Instructions

### Step 1: Modify the Payload

**Context**: Update recipe_url to include the bypass fragment.

Replace the original payload with the evasive version in the URL construction.

Example updated parameter:
```url
recipe_url=javascript:alert(1)//https://example.com
```

> The // treats the following as a comment, so only the alert executes.

### Step 2: Re-execute and Verify

**Context**: Repeat access and click from prior procedures with the new payload.

Load the modified URL and click the link.

> Confirm execution (alert pops) without filtering interference.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[bypass]]
- [[filter-evasion]]
