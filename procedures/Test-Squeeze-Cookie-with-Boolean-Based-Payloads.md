---
tags:
  - sqli
  - boolean-based
  - blind
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:04.838Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 5f0bc31f-27d7-46dd-90f1-dbeae5c55b2a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test Squeeze Cookie with Boolean-Based Payloads

## Summary

This procedure verifies boolean-based blind SQL injection in the 'squeeze' cookie by injecting true/false conditions into login requests to https://reviews.zomato.com, where differing responses (e.g., redirect vs. no redirect) reveal query manipulation.

## Description

Boolean-based blind SQLi uses conditional logic to alter query outcomes, observable via response differences without data output. Payloads like '1 ' OR true#' force true results (e.g., successful login behavior), while false variants do not. Targeting 'squeeze' in Zomato's login, this exploits unsanitized cookies in WHERE clauses. It's less noisy than time-based but requires clear true/false indicators. Prerequisites: fuzzing confirmation; outcomes: validated injection for data extraction.

## Requirements

1. Clear baseline for true/false responses (e.g., 302 vs. 200)
2. Payloads with comment terminators (e.g., # for MySQL)
3. Iteration for condition refinement

## Defense

Defensive measures and detection strategies:

- Parameterize cookie values in SQL
- Validate boolean conditions server-side
- Monitor for inconsistent login outcomes from malformed inputs

## Objectives

1. Confirm conditional query control
2. Establish true/false response oracle
3. Enable boolean data exfiltration

## Instructions

### Step 1: Inject True Payload

**Context**: Force a true condition to alter response.

Set 'squeeze' to '1 ' OR true#', submit login request.

**Expected Output**: Behavior matching successful query (e.g., 302 redirect).

### Step 2: Inject False Payload

**Context**: Test false to confirm difference.

Set 'squeeze' to '1 ' OR false#', submit and compare.

**Expected Output**: Failed behavior (e.g., 200 without redirect).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- sqli
- boolean-based
- blind
