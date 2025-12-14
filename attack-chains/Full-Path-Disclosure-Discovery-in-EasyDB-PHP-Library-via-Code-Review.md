---
id: ac-uuid-119494
name: Full Path Disclosure Discovery in EasyDB PHP Library via Code Review
tags:
  - information-disclosure
  - path-disclosure
  - php
  - code-review
  - easydb
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Review-Previous-Vulnerability-Reports]]'
  - '[[procedures/Code-Review-EasyDB-Single-Function]]'
  - '[[procedures/Propose-Array-Validation-Fix]]'
step_count: 3
techniques:
  - '[[File and Directory Discovery]]'
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:26:00.558Z'
description: >-
  A vulnerability research chain identifying an unpatched full path disclosure
  in the EasyDB PHP library's 'single' function through code review, leading to
  information disclosure of server file paths.
skill_level: intermediate
impact_level: low
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
  - '[[Gather Victim Host Information]]'
---
# Full Path Disclosure Discovery in EasyDB PHP Library via Code Review

Multi-stage vulnerability research chain demonstrating the discovery of a full path disclosure in the EasyDB PHP library through code review, highlighting unpatched issues from prior reports.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~30 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Review Prior Reports] --> B[Code Review Single Function]
    B --> C[Propose Fix]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Code editor (e.g., VS Code)
- Access to EasyDB source code

### Target Environment

- PHP web application using EasyDB library
- Source code repository access

### Initial Access Requirements

- Read access to vulnerability reports (e.g., HackerOne)
- Knowledge of PHP and array handling

## Detailed Attack Procedures

### Step 1: Review Previous Reports
procedure: [[procedures/Review-Previous-Vulnerability-Reports]]

**Objective**: Identify patterns in prior full path disclosures to guide further review.

**Instructions**: Access and analyze report #115337 on HackerOne, which addressed similar issues in EasyDB but overlooked the 'single' function. Note unresolved paths in error handling.

**Expected Output**: Summary of fixed vs. unpatched functions in EasyDB.

**Success Indicators**:
- Prior fixes documented
- Gaps in coverage identified

### Step 2: Code Review EasyDB Single Function
procedure: [[procedures/Code-Review-EasyDB-Single-Function]]

**Objective**: Detect lack of input validation leading to path disclosure errors.

**Instructions**: Examine EasyDB.php around line 366 in the 'single' function. Check for $params array validation; identify that multi-dimensional arrays trigger errors revealing server paths without checks.

**Expected Output**: Confirmation of vulnerability in error messages exposing file structure.

**Success Indicators**:
- Invalid array structures cause path leaks
- No existing 1D array enforcement found

### Step 3: Propose Array Validation Fix
procedure: [[procedures/Propose-Array-Validation-Fix]]

**Objective**: Suggest mitigation to prevent disclosure by validating inputs.

**Instructions**: Recommend inserting validation code before line 366: use [[commands/validate-params-1d-array]] to throw an exception for non-1D arrays, halting execution and avoiding errors. Test in a PHP environment to verify it blocks invalid inputs.

```php
if(count($params) != count($params,COUNT_RECURSIVE)){ throw new \InvalidArgumentException("Invalid params"); }
```

**Expected Output**: Exception thrown for recursive arrays, no path disclosure.

**Success Indicators**:
- Validation prevents error-based leaks
- Fix aligns with PHP best practices

## Attack Chain Summary

### Key Achievements

1. Linked prior report to new gap in EasyDB
2. Pinpointed 'single' function vulnerability
3. Provided actionable fix for information disclosure

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[File and Directory Discovery]] File and Directory Discovery
- [[Gather Victim Host Information]] Gather Victim Host Information

### MITRE ATT&CK Tactics

- [[Discovery]] Discovery
- [[Reconnaissance]] Reconnaissance

---

*Last updated: 2023-10-01T00:00:00Z*
