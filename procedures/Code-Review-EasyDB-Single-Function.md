---
id: proc-uuid-2
name: Code-Review-EasyDB-Single-Function
tags:
  - code-review
  - information-disclosure
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:00.550Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Code-Review-EasyDB-Single-Function

## Summary

This procedure conducts a static code review of the EasyDB library's 'single' function to uncover full path disclosure risks from unvalidated array inputs, enabling server file structure reconnaissance.

## Description

The 'single' function in EasyDB.php (line ~366) processes $params without checking if it's a one-dimensional array. Multi-dimensional inputs can trigger PHP errors that leak server paths. This review simulates an attacker's analysis to expose the flaw, with outcomes including proof-of-concept error reproduction in a test environment.

## Requirements

1. Source code access to EasyDB.php
2. PHP runtime for testing error reproduction
3. Knowledge of PHP array functions and exceptions

## Defense

Defensive measures and detection strategies:

- Implement input sanitization in all library functions
- Enable error logging without path exposure (e.g., custom error handlers)
- Use static analysis tools like PHPStan for validation checks

## Objectives

1. Confirm lack of array dimensionality validation
2. Reproduce path disclosure in error messages
3. Assess impact on server reconnaissance

## Instructions

### Step 1: Inspect Function Code

**Context**: Locate and analyze the 'single' function for input handling flaws.

Open EasyDB.php and navigate to the 'single' function around line 366. Examine $params usage in queries or error contexts.

> Look for absence of checks like count() comparisons; note potential error triggers.

### Step 2: Test Invalid Inputs

**Context**: Simulate multi-dimensional $params to observe error outputs.

In a PHP script, call the 'single' function with a nested array (e.g., $params = ['key' => ['nested']]) and capture errors.

> Expected: Error messages revealing paths like /var/www/...; validate disclosure.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[code-review]]
- [[information-disclosure]]
