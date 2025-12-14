---
id: proc-rockstar-xss-bypass1-001
tags:
  - xss
  - waf-bypass
  - control-characters
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:03.367Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Bypass-WAF-with-Control-Characters-for-XSS

## Summary

This procedure exploits a WAF misconfiguration in Rockstar Social Club comments by injecting '<' followed by control characters like \t, evading pattern matching like '<.*' and allowing partial HTML tag injection for stored XSS.

## Description

In the context of Rockstar Games Social Club, the WAF removes tags based on patterns but fails to handle control characters immediately after '<'. This enables injecting payloads that partially form tags, leading to arbitrary JS execution when comments are viewed. Iterative testing reveals this after initial discovery, with impact on users viewing comments via alert(document.domain).

## Requirements

1. Valid Social Club account with comment posting privileges
2. Web browser for payload submission and DOM inspection
3. Knowledge of target comment sections (e.g., general comments)

## Defense

Defensive measures and detection strategies:

- Update WAF rules to strip control characters before pattern matching
- Implement comprehensive input sanitization normalizing whitespace and controls
- Monitor for anomalous comment payloads with logging of injection attempts

## Objectives

1. Evade WAF to inject partial '<' tag
2. Enable follow-on XSS payloads
3. Execute JS in viewed comments

## Instructions

### Step 1: Craft and Submit Payload

**Context**: Prepare a payload that places control characters after '<' to break WAF detection.

Inject the following in a comment field:

```
<\tscript>alert('xss')</script>
```

> Submit the comment via the Social Club interface. The WAF should not trigger on '<.*' due to \t interrupting the pattern.

### Step 2: Verify Injection

**Context**: Inspect the rendered comment to confirm partial tag survival.

View the posted comment and use browser dev tools to check the DOM.

> Expected: '<\tscript>' appears unstripped, allowing tag formation and potential JS execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[waf-bypass]]
