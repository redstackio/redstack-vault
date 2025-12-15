---
id: proc-uuid-1
tags:
  - recon
  - source-code-review
  - command-injection
type: procedure
tools:
  - '[[tools/WebPageTest]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Software]]'
updated_at: '2025-12-14T17:23:41.153Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
---
# Review-WebPageTest-Source-Code-for-Vulnerabilities

## Summary

This procedure involves analyzing the open-source WebPageTest codebase to identify a command injection vulnerability in the testlog.php file, focusing on inadequate sanitization of the 'filter' parameter.

## Description

In a security assessment, review the GitHub repository for WebPageTest to locate flaws in input handling. The vulnerability arises because user input from $_GET['filter'] is minimally sanitized (lowercased, trimmed, quotes/backslashes replaced, and escapeshellarg applied) before being used in PHP's exec() for a grep command, allowing bypass with shell metacharacters like $() for command substitution. This targets PHP web applications on Linux servers.

## Requirements

1. Access to GitHub repository https://github.com/WPO-Foundation/webpagetest
2. Basic knowledge of PHP and shell command injection
3. Text editor or browser for code review

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and whitelisting for parameters used in system calls
- Use parameterized queries or avoid direct exec() with user input
- Monitor logs for anomalous delays or external connections from web servers

## Objectives

1. Identify vulnerable code patterns in testlog.php
2. Document sanitization weaknesses
3. Plan exploitation based on bypass techniques

## Instructions

### Step 1: Access and Examine Source Code

**Context**: Navigate to the relevant file and inspect variable handling.

No command executed; manually review https://github.com/WPO-Foundation/webpagetest/blob/master/www/testlog.php.

> Focus on lines assigning $filter = $_GET['filter'], applying strtolower, trim, str_replace for quotes/backslashes, escapeshellarg, and usage in exec('grep -i -F "$pattern" "$fileName"'). Note that $() bypasses the filtering.

### Step 2: Identify Bypass Opportunity

**Context**: Analyze how shell features like command substitution can evade protections.

No command; document the flaw.

> Expected: Recognition that escapeshellarg does not prevent $() nested commands.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Software]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/WebPageTest]]

## Tags

- recon
- source-code-review
