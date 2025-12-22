---
id: proc-infogram-inject-001
tags:
  - xss-injection
  - payload
  - dom-xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:02.898Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-in-Overview-Table

## Summary

This procedure involves inserting a malicious HTML/JavaScript payload into the Overview Table of an Infogram report, exploiting lack of sanitization to store executable code for later DOM-based XSS.

## Description

The Overview Table in Infogram's Report Designer accepts user input without proper escaping, allowing storage of HTML tags and event handlers like onmouseover. The payload used is an anchor tag that triggers a JavaScript alert on hover. This stored payload renders in published reports, executing in the viewer's browser context. Prerequisites include access to the editor from the prior step.

## Requirements

1. Active report editor session
2. Knowledge of basic HTML/JS for payload crafting
3. No additional tools; browser form input suffices

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs with HTML entity encoding or libraries like DOMPurify
- Monitor for suspicious HTML patterns in report content via backend validation

## Objectives

1. Store malicious code in the report
2. Ensure payload survives saving
3. Verify rendering in editor preview

## Instructions

### Step 1: Locate Overview Table Field

**Context**: Identify the input area vulnerable to injection.

In the report editor, scroll to the Overview Table section and click into the text/content field.

> Field becomes editable for direct input.

### Step 2: Enter Payload

**Context**: Insert the XSS payload to test execution.

Type or paste: <a href="" onmouseover="javascript:alert('HackerOne MkSecurity Dom XSS');">Click for Detail</a>

> Payload displays as a link in the table; hover in preview to test if alert fires (may not in editor).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-injection]]
- [[payload]]
- [[dom-xss]]
