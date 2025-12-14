---
id: proc-array-input-sqli
tags:
  - sqli
  - wordpress
  - prepare
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/test-array-input-prepare]]'
verified: false
platforms:
  - Web
  - PHP
  - MySQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:56.639Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Demonstrate Array Input Handling Issue

## Summary

This procedure exploits the $wpdb->prepare() method's flawed handling of array inputs by passing malicious arrays that bypass sanitization, enabling arbitrary SQL injection in WordPress core database operations.

## Description

The $wpdb->prepare() in wp-includes/wp-db.php checks if the query is an array and directly uses its elements without preparation, allowing attackers to inject SQL fragments. Applicable to any plugin or theme calling prepare() with user-controlled arrays, such as in bulk operations. In a test environment, craft an array with a benign query and injected payload. Outcomes include successful execution of unauthorized SELECT or UPDATE statements, leading to info disclosure.

## Requirements

1. WordPress core access for custom plugin/script testing.
2. Database with sample tables (e.g., wp_users).
3. PHP execution environment to run prepare() calls.
4. Error reporting enabled to capture injection results.

## Defense

Defensive measures and detection strategies:

- Avoid passing arrays to $wpdb->prepare(); validate inputs as strings.
- Audit all prepare() usages in code for array handling.
- Use strict type checking in PHP 7+ for query parameters.
- Log all prepare() calls and monitor for array anomalies.

## Objectives

1. Bypass preparation by exploiting array direct usage.
2. Inject and execute custom SQL payloads.
3. Demonstrate impact on data extraction.

## Instructions

### Step 1: Set Up Test Script

**Context**: Create a PHP file to mimic vulnerable prepare() call.

In a custom plugin, define $wpdb and prepare an array query.

### Step 2: Execute Array Injection

**Context**: Pass a crafted array to trigger bypass.

**Command** ([[commands/test-array-input-prepare]]):
```php
$query = array('SELECT * FROM wp_users WHERE id = %d', 1, ' UNION SELECT user_pass FROM wp_users --');
$result = $wpdb->prepare($query[0], $query[1], $query[2]);
$wpdb->query($result);
```

> The array elements are used directly, injecting the UNION. Expected output: Hashed passwords dumped in results.

### Step 3: Verify Injection

**Context**: Query results or logs to confirm execution.

Print $result and execute; check for extra rows from UNION.

**Expected Output**: Query string with injected SQL, e.g., "SELECT * FROM wp_users WHERE id = 1 UNION SELECT user_pass FROM wp_users".

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/test-array-input-prepare]]

## Tools Used


## Tags

- sqli
- wordpress
- prepare
