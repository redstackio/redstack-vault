---
id: proc-enumerate-csrf-css-selectors
tags:
  - csrf-leak
  - css-injection
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:34.311Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Enumerate CSRF Token using CSS Selectors

## Summary

This procedure exploits CSS injection to target elements containing the CSRF token, using selectors like nth-child or attributes to reveal token characters through visual styling or timing side-channels.

## Description

Once CSS injection is confirmed, craft payloads to select token-containing elements (e.g., input[name="csrf_token"]). Use conditional styling based on character values (e.g., [value^="a"] for 'a') to change colors, enabling enumeration. This works in victim contexts where the token is rendered. Expected outcome: Full token reconstruction via iterative requests.

## Requirements

1. Confirmed CSS injection from prior procedure.
2. Knowledge of token element structure (e.g., via inspection).
3. Browser or proxy for payload iteration.

## Defense

Defensive measures and detection strategies:

- Obfuscate or avoid rendering tokens in DOM; use server-side validation only.
- Apply strict CSP to block style attribute modifications.
- Detect repeated requests with varying CSS payloads via rate limiting or anomaly detection.

## Objectives

1. Target and style token elements selectively.
2. Leak token characters visually or via timing.
3. Enable CSRF bypass for further attacks.

## Instructions

### Step 1: Identify Token Element

**Context**: Inspect the page to locate the CSRF token element.

Use browser dev tools to find elements like <input type="hidden" name="csrf_token" value="...">

### Step 2: Inject Selective CSS Payload

**Context**: Encode and inject CSS to style based on token chars (e.g., for digit '1', use nth-child(2) if positioned accordingly).

Example payload in URL: bgcolor=%7D%20input%5Bname%3D%22csrf_token%22%5D%5Bvalue%5E%3D%221%22%5D%7Bbackground%3Ared%7D

> This targets inputs starting with '1' and colors them red. Iterate for each position/character (a-z, 0-9).

**Expected Output**: Colored elements revealing matching characters; repeat to build full token.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf-leak]]
- [[css-injection]]
