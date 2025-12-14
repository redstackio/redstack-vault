---
id: proc-rockstar-xss-bypass4-001
tags:
  - xss
  - chained-bypass
  - mathml-injection
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
updated_at: '2025-12-13T23:56:03.358Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Chain-Multiple-Techniques-for-MathML-JavaScript-Injection

## Summary

This advanced procedure chains eight techniques (control chars, Unicode, fake URLs) to bypass enhanced WAF/filters in Rockstar Social Club, injecting a MathML element with javascript: URI for click-based JS execution and UI disruption.

## Description

By combining evasions, the payload reassembles into a functional MathML tag with xml:base pointing to javascript:alert(document.domain), executing on click. This also breaks reply/delete functionality, amplifying stored XSS impact.

## Requirements

1. Iterative testing access to comments
2. Knowledge of prior bypasses
3. Browser supporting MathML rendering

## Defense

Defensive measures and detection strategies:

- Block MathML and XML namespaces in user input
- Parse and sanitize chained encodings server-side
- Detect URI schemes like javascript: in attributes

## Objectives

1. Chain evasions for complex injection
2. Execute JS via clickable element
3. Disrupt comment interactions

## Instructions

### Step 1: Build Chained Payload

**Context**: Layer techniques to form MathML.

Payload:

```
&<>lt;%&<>lt;m\bath xml:base=\"j<>avascript:alert(document.domain)//\" href=#\"[bad.url.pls]
```

> Post; renders as '&lt%<math xml:base="javascript:alert(document.domain)//" href="#" x="" class="badLink">[bad.url.pls]'.

### Step 2: Trigger and Verify

**Context**: Interact to execute.

Click the injected element in the viewed comment.

> Expected: Alert pops with document.domain; comments un-repliable.

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
- [[chained-bypass]]
