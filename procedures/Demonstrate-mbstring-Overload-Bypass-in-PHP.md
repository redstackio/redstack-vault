---
id: proc-uuid-placeholder-001
tags:
  - php
  - mbstring
  - string-bypass
  - serialization
  - validation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/php-mbstring-overload-poc]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Python]]'
updated_at: '2025-12-14T17:28:13.048Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
---
# Demonstrate-mbstring-Overload-Bypass-in-PHP

## Summary

This procedure demonstrates how PHP applications using raw substr and strlen functions can be affected by mbstring.func_overload, leading to incorrect string handling that may bypass security checks in serialization, length validation, or CSRF token processing.

## Description

In PHP codebases like Airship, manual code reviews reveal usage of unsafe string functions (e.g., in src/Engine/Security/CSRF.php and src/Engine/Security/Util.php) without safe wrappers like Binary::safe_substr or CryptoUtil::safe_strlen. When mbstring.func_overload is set (e.g., to 2 for full overload), these functions treat strings as multibyte, causing discrepancies between byte counts and character counts. This can enable attackers to inject multibyte characters to alter validation logic, similar to historical issues in phpMyAdmin's safe unserialization. The procedure sets up a POC environment to replicate and validate the issue, focusing on low-impact but consistency-promoting fixes.

## Requirements

1. PHP 7+ with mbstring extension installed
2. Access to a PHP runtime or server shell
3. Sample POC script file (poc.php) mimicking vulnerable code
4. No network access required; local execution suffices

## Defense

Defensive measures and detection strategies:

- Use safe string functions (e.g., Binary::safe_substr) in all security code
- Disable or monitor mbstring.func_overload in php.ini (set to 0)
- Audit codebase for raw substr/strlen usage via static analysis tools like PHPStan
- Log and alert on multibyte string anomalies in security logs

## Objectives

1. Replicate string length/substring miscalculation under overload
2. Show potential bypass in serialization or validation routines
3. Recommend code fixes to mitigate edge-case risks

## Instructions

### Step 1: Prepare POC Script

**Context**: Create a simple PHP script that uses raw substr and strlen on a string with multibyte characters, mimicking vulnerable code in Airship (e.g., CSRF token handling).

Add the following to poc.php:

```php
<?php
$input = "\xE3\x81\x82\xE3\x81\B3\xE3\x81\A7"; // Multibyte Japanese characters
$len = strlen($input); // Unsafe: may count bytes incorrectly under overload
echo "Length: " . $len . "\n";
$sub = substr($input, 0, 3); // Unsafe: may extract wrong substring
echo "Substring: " . $sub . "\n";
// Simulate unserialize bypass
$serialized = serialize(new stdClass()); // Placeholder for vulnerable unserialize
if (strpos($sub, '\x00') !== false) { // Hypothetical check
    echo "Bypass possible\n";
} else {
    echo "Safe\n";
}
?>
```

This sets up a scenario where overload causes $len to report character count instead of bytes, potentially allowing oversized inputs to pass validation.

### Step 2: Execute with Overload Enabled

**Context**: Run the POC with mbstring.func_overload=2 to simulate a misconfigured PHP environment, demonstrating the discrepancy.

**Command** ([[commands/php-mbstring-overload-poc]]):
```bash
php -d mbstring.func_overload=2 ./poc.php
```

> This command enables full string function overloading by mbstring, causing strlen to return character count (e.g., 3 for the example string) instead of byte count (9), and substr to handle multibyte encoding. Expected output: "Length: 3\nSubstring: \xE3\x81\x82\nBypass possible\n" (if check is tricked), illustrating how this could bypass length limits or extract unintended substrings in security functions like those in Airship's CSRF.php.

### Step 3: Validate Without Overload

**Context**: Compare output without overload to confirm the issue is configuration-dependent.

**Command** (modified [[commands/php-mbstring-overload-poc]]):
```bash
php ./poc.php
```

> Without -d flag, strlen returns 9 (bytes), substr extracts first 3 bytes (\xE3\x81\x82 partial), and bypass check fails. This highlights the risk in environments where overload is enabled (common in some hosting setups).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Python]]

### Sub-Techniques


## Commands Used

- [[commands/php-mbstring-overload-poc]]

## Tools Used


## Tags

- php
- mbstring
- string-bypass
- serialization
- validation
