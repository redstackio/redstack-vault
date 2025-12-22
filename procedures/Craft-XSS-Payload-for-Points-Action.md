---
id: proc-craft-xss-payload-concrete
tags:
  - xss
  - payload-craft
  - stored-xss
  - concrete-cms
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:31.891Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft XSS Payload for Points Action

## Summary

This procedure details creating a JavaScript payload for the `upaName` and `upaHandle` parameters in Concrete CMS to exploit stored XSS when rendered in the admin panel.

## Description

The vulnerability stems from unsanitized storage and output of user inputs in points actions. By crafting payloads like `<sVg/OnLOaD=prompt(1)>` for `upaHandle`, attackers can inject executable HTML/JS. This targets admins viewing the actions page, potentially leading to code execution in their session. Prerequisites include understanding HTML entity encoding to evade filters.

## Requirements

1. Knowledge of XSS payloads and HTML attributes
2. Testing environment for Concrete CMS
3. Proxy for request construction

## Defense

Defensive measures and detection strategies:

- Sanitize all inputs with HTML entity encoding (e.g., htmlspecialchars in PHP)
- Implement content security policy (CSP) to block inline scripts
- Scan database for suspicious strings in points action fields

## Objectives

1. Develop a payload that survives storage
2. Ensure execution on admin page render
3. Test for alert or console execution

## Instructions

### Step 1: Select Payload Type

**Context**: Choose a stored XSS vector using onload attributes to execute JS.

Opt for `<sVg/OnLOaD=prompt(1)>` to mimic SVG tags, which may bypass weak filters.

> Combine with benign `upaName` like 'XSS the admin2' for realism.

### Step 2: Assemble Full Parameters

**Context**: Build the complete POST body.

Include: `upaID=''`, `upaIsActive=1`, `upaDefaultPoints=1000`, `gBadgeID=''`, plus the payload fields.

> Use URL encoding if needed: e.g., %3C for <.

### Step 3: Validate Payload

**Context**: Test in a safe environment.

Submit to a local CMS instance and inspect stored data in database or page source.

> Confirm payload appears as `<sVg/OnLOaD=prompt(1)>` without alteration.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- Burp Suite (for payload testing)

## Tags

- xss
- payload-craft
- stored-xss
