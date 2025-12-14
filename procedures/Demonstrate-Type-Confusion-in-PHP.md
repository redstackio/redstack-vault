---
id: proc-uuid-003
tags:
  - type-confusion
  - php
  - auth-bypass
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/php-type-confusion-demo]]'
verified: false
platforms:
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:35.051Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques:
  - '[[Domain Accounts]]'
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Demonstrate-Type-Confusion-in-PHP

## Summary

This procedure demonstrates PHP's type juggling with loose comparison operators like !=, which can lead to false equalities and auth bypasses, complementing timing risks in strict comparisons.

## Description

PHP treats strings starting with '0e' as scientific notation, causing "0e123" != "0e456" to evaluate false if both parse to 0. This is exploitable in auth checks, e.g., WP-API/Key-Auth line 50. Use online eval or local PHP to show risks. Prerequisites: PHP interpreter. Outcomes: Understanding of why strict operators are preferred, despite their timing issues.

## Requirements

1. PHP 5+ environment or online evaluator like eval.in
2. Basic PHP scripting knowledge
3. Context of auth code using loose operators

## Defense

Defensive measures and detection strategies:

- Enforce strict comparisons (===) everywhere
- Static analysis to detect loose operators in auth
- Input validation to prevent type coercion exploits

## Objectives

1. Show unexpected equality with != on numeric strings
2. Relate to auth token validation flaws
3. Highlight need for balanced comparison security

## Instructions

### Step 1: Prepare Demo Script

**Context**: Create a simple PHP snippet to illustrate juggling.

Write the code:

```php
<?php
echo ("0e123" != "0e456") ? 'Not equal' : 'Equal';
?>
```

> This outputs 'Equal' due to both being treated as 0 in scientific notation.

### Step 2: Execute and Observe

**Context**: Run the demo to confirm behavior.

Execute [[commands/php-type-confusion-demo]] via PHP CLI or online:

```bash
php -r "echo ('0e123' != '0e456') ? 'Not equal' : 'Equal';"
```

> Expected: 'Equal', demonstrating bypass potential.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- [[Domain Accounts]] Domain Accounts

## Commands Used

- [[commands/php-type-confusion-demo]]

## Tools Used


## Tags

- type-confusion
- php-vulnerability
