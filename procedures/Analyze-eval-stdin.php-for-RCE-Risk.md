---
id: proc-analyze-eval-stdin-rce
tags:
  - rce
  - analysis
  - php
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/cat-file]]'
verified: false
platforms:
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:23:27.793Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[JavaScript]]'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Analyze-eval-stdin.php-for-RCE-Risk

## Summary

This procedure examines the eval-stdin.php file from PHPUnit to assess its potential for remote code execution by evaluating arbitrary input from php://stdin in vulnerable PHP configurations.

## Description

The file, part of PHPUnit's PHP evaluation utility, uses eval() on stdin content, which in CGI/FastCGI setups allows POST payloads to execute as PHP code. This has been confirmed risky by PHP developers and linked to incidents like PrestaShop RCE. Analysis involves code review to understand the execution flow and exploitation prerequisites.

## Requirements

1. PHPUnit src directory from extracted package
2. cat or text editor for viewing code
3. Understanding of PHP streams and eval()

## Defense

Defensive measures and detection strategies:

- Remove or restrict access to vendor/ files via .htaccess or nginx rules
- Disable CGI/FastCGI for PHP if possible, use mod_php
- Monitor for anomalous eval() usage in logs

## Objectives

1. Identify the eval() mechanism on php://stdin
2. Evaluate exploitation conditions (e.g., web-accessible, no auth)
3. Document risk for reporting

## Instructions

### Step 1: View File Contents

**Context**: Read the PHP code to locate the vulnerable eval statement.

**Command** ([[commands/cat-file]]):
```bash
cat vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
```

> Displays the script. Expected output: Code including eval('?>' . file_get_contents('php://stdin')).

### Step 2: Manual Code Review

**Context**: Analyze for RCE vectors, noting stdin input handling.

No command; use editor to annotate. Cross-check with https://thephp.cc/news/2020/02/phpunit-a-security-risk.

> Expected: Confirmation of arbitrary code exec potential.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter

### Sub-Techniques

- [[JavaScript]] JavaScript (adapted for PHP eval)

## Commands Used

- [[commands/cat-file]]

## Tools Used


## Tags

- rce
- analysis
- php
