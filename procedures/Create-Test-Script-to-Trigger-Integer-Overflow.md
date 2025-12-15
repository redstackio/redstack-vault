---
tags:
  - php
  - exploit-trigger
  - integer-overflow
type: procedure
tools:
  - '[[tools/PHP]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/php-trigger-overflow]]'
platforms:
  - Linux
  - PHP
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 49c1ecee-ca54-4660-bc86-83f0675b94c6
created_at: '2025-12-14T17:28:20.074Z'
updated_at: '2025-12-14T17:28:20.074Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Test-Script-to-Trigger-Integer-Overflow

## Summary

This procedure creates and executes a PHP script that generates a maximally sized string and passes it to htmlentities(), triggering the integer overflow and preparing for heap corruption.

## Description

The script bypasses memory limits and uses str_repeat() to create a string of PHP_INT_MAX 'A' characters, then calls htmlentities() with ENT_COMPAT flags, double_encode true, and empty charset. This forces the vulnerable maxlen calculation, allocating a small buffer for a huge input. Targeted at 32-bit PHP 7.1 on Linux; expect potential crash without debugger.

## Requirements

1. PHP 7.1 32-bit installed
2. Unlimited memory allowance (handled in script)
3. Local execution environment

## Defense

Defensive measures and detection strategies:

- Limit input sizes to functions like htmlentities() (e.g., via max_input_vars or custom wrappers)
- Monitor for high memory usage or crashes in PHP processes
- Use PHP's error logging to detect segmentation faults

## Objectives

1. Force integer overflow in maxlen calculation
2. Allocate undersized buffer via zend_string_alloc()
3. Set up conditions for subsequent heap overflow

## Instructions

### Step 1: Write the Trigger Script

**Context**: Compose the PHP code to create the large string and invoke the vulnerable function.

Create a file trigger.php with the content from [[commands/php-trigger-overflow]]:

```php
<?php ini_set('memory_limit',-1); $s=str_repeat("A",PHP_INT_MAX); htmlentities($s,0,"",true); ?>
```

> This sets unlimited memory, repeats 'A' PHP_INT_MAX times, and calls htmlentities(). Expected: Script starts processing but may OOM or crash.

### Step 2: Execute the Script

**Context**: Run the script using PHP CLI to trigger the vulnerability.

Execute with `php trigger.php` in the terminal.

> Expected: Integer overflow occurs internally; may lead to heap issues visible in logs or debugger.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/php-trigger-overflow]]

## Tools Used

- [[tools/PHP]]

## Tags

- [[tools/PHP]]
- [[exploit]]
- [[overflow]]
