---
tags:
  - xss
  - fuzzing
  - rails
type: procedure
tools:
  - '[[tools/IRB]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T00:11:16.358Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 39551034-49ed-432c-8d11-e729f0f71384
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Perform-Fuzz-Testing-on-Rails-HTML-Sanitizer-Allow-Lists

## Summary

This procedure involves fuzz testing the Rails HTML sanitizer's allowlists to identify combinations of tags that fail to properly strip dangerous elements, specifically targeting 'math+style' and 'svg+style' for XSS bypasses.

## Description

In a Rails application, developers may override the default sanitizer allowtags to include custom elements like math or svg for rich content. This procedure uses manual fuzzing, inspired by prior reports, to test nested structures and attributes. The target is Rails::Html::SafeListSanitizer in versions like 1.4.3, where certain combinations allow script injection without filtering. Prerequisites include a Ruby environment with the gem installed.

## Requirements

1. Ruby environment with rails-html-sanitizer gem installed
2. Knowledge of HTML tags and potential bypass vectors
3. Access to IRB for interactive testing

## Defense

Defensive measures and detection strategies:

- Avoid allowing 'style' with 'math' or 'svg' in sanitizer configs; use strict allowlists
- Implement Content Security Policy (CSP) to block inline scripts
- Monitor for anomalous JavaScript execution in web logs

## Objectives

1. Discover vulnerable tag combinations in the sanitizer
2. Validate potential for XSS injection
3. Document bypass payloads for reporting

## Instructions

### Step 1: Prepare Test Environment

**Context**: Set up for fuzzing by loading the sanitizer in an interactive session.

No specific command; use IRB to experiment with various tag arrays like ["svg", "style"] and payloads containing <script> or onerror attributes.

> Manually input payloads and observe if sanitization removes dangerous parts.

### Step 2: Test Tag Combinations

**Context**: Focus on inspired combinations to identify improper handling of nested elements.

Test payloads like <svg><style><script>alert(1)</script></style></svg> with tags: ["svg", "style"]

> Expected: Payload not stripped, indicating bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/IRB]]

## Tags

- xss
- fuzzing
