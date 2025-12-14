---
id: proc-uuid-3
tags:
  - ssti
  - php
  - execution
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/smarty-php-hello]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:24:08.584Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Test-PHP-Execution-in-Smarty-Templates

## Summary

This procedure verifies arbitrary PHP code execution within Smarty templates by injecting a {php} block that prints a test string, confirming RCE potential in the email rendering process.

## Description

Smarty's {php} tags allow direct PHP execution if enabled. In Unikrn's setup, injecting such tags into profile fields executes during email template processing, printing output directly. This step escalates from detection to execution testing, requiring prior confirmation of Smarty.

## Requirements

1. Confirmed Smarty version with PHP support
2. Profile modification access
3. Email sending and viewing

## Defense

Defensive measures and detection strategies:

- Disable {php} tags in Smarty configuration
- Use sandboxed template execution
- Monitor for PHP code in logs or WAF rules

## Objectives

1. Confirm PHP interpreter access via templates
2. Demonstrate code execution control
3. Identify execution context (e.g., server-side rendering)

## Instructions

### Step 1: Inject PHP Test

**Context**: Embed a simple print statement in Smarty's PHP block.

**Command** ([[commands/smarty-php-hello]]):
```smarty
{php}print "Hello"{/php}
```

> Inject into profile field and save.

### Step 2: Execute via Email

**Context**: Trigger server-side rendering.

**Instructions**: Send invitation email and check the body.

> Expected output: "Hello" printed in the email, indicating successful execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques


## Commands Used

- [[commands/smarty-php-hello]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[ssti]]
- [[php]]
- [[Execution]]
