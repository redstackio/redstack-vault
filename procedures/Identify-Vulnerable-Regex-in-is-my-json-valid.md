---
tags:
  - redos
  - regex-analysis
  - node.js
type: procedure
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:30.719Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 49c8d1be-cbe4-4a4f-aed5-d0be5c228acb
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Identify Vulnerable Regex in is-my-json-valid

## Summary

This procedure involves static analysis of the 'is-my-json-valid' Node.js module to identify the ReDoS vulnerability in its email validation regex, enabling targeted exploitation for denial of service.

## Description

The 'is-my-json-valid' module, used for JSON schema validation, contains a regex in formats.js for email checking that suffers from catastrophic backtracking. Introduced in commit 34a1a706 in 2014, the pattern `/^\S+@\S+$/` uses nested quantifiers (`\S+`) without bounds, leading to exponential time complexity on crafted inputs. This procedure reviews the source code to confirm the issue, typically in a development or auditing context against Node.js applications relying on this module.

## Requirements

1. Access to the module's source code (e.g., via npm install is-my-json-valid and inspection of node_modules).
2. Basic knowledge of regular expressions and Node.js module structure.
3. Text editor or IDE for code review.

## Defense

Defensive measures and detection strategies:

- Update to patched versions of the module or use alternatives like 'ajv' with bounded regex.
- Implement regex timeout wrappers in Node.js validation functions.
- Static analysis tools like 'ret' or 'regex' linters to detect vulnerable patterns.

## Objectives

1. Confirm the presence of the vulnerable regex in formats.js.
2. Document the root cause for reporting or patching.
3. Prepare for exploitation testing.

## Instructions

### Step 1: Locate and Inspect Module Source

**Context**: Download or access the module source to find the formats.js file.

Install the module if needed:

```bash
npm install is-my-json-valid
```

Navigate to `node_modules/is-my-json-valid/lib/formats.js` and search for the email export.

**Expected Output**: Line defining `exports['email'] = /^\S+@\S+$/;`.

### Step 2: Analyze Regex for Backtracking

**Context**: Examine the pattern for nested quantifiers that allow repeated failure retries.

Review the regex: The `\S+` before and after '@' can backtrack extensively on inputs like long strings of characters that partially match but fail at boundaries.

**Expected Output**: Identification of catastrophic backtracking risk due to lack of possessive quantifiers (e.g., `\S++`) or atomic groups.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[redos]]
- [[regex-analysis]]
- [[node.js]]
