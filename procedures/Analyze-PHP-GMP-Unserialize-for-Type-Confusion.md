---
id: proc-gmp-analyze-001
tags:
  - deserialization
  - type-confusion
  - php
  - gmp
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:23:54.838Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Analyze-PHP-GMP-Unserialize-for-Type-Confusion

## Summary

This procedure involves static analysis of PHP's GMP extension source code to identify a type confusion vulnerability in the gmp_unserialize function, enabling attackers to manipulate object properties during deserialization.

## Description

By examining the PHP source code, particularly gmp_unserialize and related handlers, attackers can discover how unserializing a GMP object converts it to an integer ZVAL, allowing access to the global object store via zend_hash_copy. This occurs because __wakeup() can alter the ZVAL type to integer or bool, bypassing type checks and enabling arbitrary property updates on existing objects. This is foundational for exploiting applications like MyBB that use unserialize on user input.

## Requirements

1. Access to PHP source code (e.g., from php.net or local installation)
2. Knowledge of PHP internals (ZVAL, zend_hash)
3. Development environment for testing unserialization

## Defense

Defensive measures and detection strategies:

- Avoid using unserialize on untrusted input; prefer JSON or validated formats
- Enable PHP's allow_url_include off and validate serialized data structure
- Monitor for anomalous deserialization in logs (e.g., GMP object usage)

## Objectives

1. Identify type confusion in GMP unserialization
2. Understand property copy mechanism via zend_hash_copy
3. Prepare for payload crafting based on source insights

## Instructions

### Step 1: Examine gmp_unserialize Function

**Context**: Locate and analyze the gmp_unserialize function in ext/gmp/gmp.c to see how it handles property unserialization into an array and copies to the object.

No command required; manually review source code for zend_hash_copy usage and lack of ZVAL type validation post-__wakeup.

> Focus on how converting GMP to integer ZVAL (via Z_OBJ_P) allows access to global handles like object store index 5 for templates.

### Step 2: Test ZVAL Type Alteration

**Context**: Verify how __wakeup in referenced objects (e.g., DateInterval) can change ZVAL type to integer, enabling confusion.

Use [[commands/gmp-to-integer-cast-demo]] to demonstrate:

```php
<?php var_dump(unserialize('a:2:{i:0;C:3:"GMP":17:{s:4:"1234";a:0:{}}i:1;O:12:"DateInterval":1:{s:1:"y";R:2;}}')); ?>
```

> Expected output shows integer conversion from GMP, confirming type confusion.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used

- [[commands/gmp-to-integer-cast-demo]]

## Tools Used


## Tags

- deserialization
- type-confusion
- php
- gmp
