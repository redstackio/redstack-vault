---
tags:
  - ssti
  - rce
  - php-execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/smarty-php-hello-test]]'
platforms:
  - Web
  - Linux
techniques:
  - '[[Command-Line Interface]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: a3e07d2a-5379-4bf6-a8e0-4bcc1094e531
created_at: '2025-12-13T09:01:17.033Z'
updated_at: '2025-12-13T09:01:17.033Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Test PHP Code Execution in Smarty

## Summary

This procedure tests arbitrary PHP code execution using Smarty's {php} tags by injecting a simple print statement into profile fields and verifying output in the email.

## Description

Building on SSTI confirmation, this exploits Smarty's allowance of PHP tags to execute code, printing a test string to confirm capability for further RCE.

## Requirements

1. Confirmed Smarty version supporting {php} tags
2. Profile and invitation access
3. Secondary email

## Defense

Defensive measures and detection strategies:

- Disable {php} tags in Smarty configuration
- Sanitize all user inputs in templates

## Objectives

1. Execute simple PHP code
2. Confirm RCE potential
3. Escalate to file reading

## Instructions

### Step 1: Inject PHP Test Payload

**Context**: Set profile fields and trigger email to test execution.

**Command** ([[commands/smarty-php-hello-test]]):
```bash
{php}print "Hello"{/php}
```

> Set profile fields to this payload; invite user; observe 'Hello' in email.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used

- [[commands/smarty-php-hello-test]]

## Tools Used



## Tags

- [[ssti]]
- [[rce]]
- [[php-execution]]
