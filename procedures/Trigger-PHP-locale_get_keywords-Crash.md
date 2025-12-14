---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Trigger-PHP-locale_get_keywords-Crash
tags:
  - php
  - dos
  - code-injection
  - crash
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - PHP
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:20.258Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-PHP-locale_get_keywords-Crash

## Summary

This procedure exploits a vulnerability in PHP's locale_get_keywords function (bug #73371) by providing invalid or malformed locale input, leading to code injection and an application crash that results in denial of service. Discovered through internal PHP analysis and reported via HackerOne, it affects PHP runtimes and was resolved by the PHP team with a $500 bounty.

## Description

The locale_get_keywords function in PHP is designed to retrieve keywords associated with a given locale. However, due to improper handling of certain inputs, it can be induced to crash via code injection, causing the PHP process to terminate abruptly. This vulnerability was identified by analyzing PHP internals and is classified as low-severity due to its limited scope, primarily affecting applications that expose or invoke this function with untrusted input. In a real-world scenario, this could occur in internationalization features of web applications. The attack requires code execution on the target and results in immediate DoS without data compromise. Prerequisites include access to a vulnerable PHP version; post-exploitation involves monitoring for crash indicators in logs.

## Requirements

1. Vulnerable PHP version (prior to the fix for bug #73371)
2. Ability to execute PHP code, either via CLI or a web server hosting PHP scripts
3. Basic knowledge of PHP internals and locale handling
4. Test environment to avoid impacting production systems

## Defense

Defensive measures and detection strategies:

- Update to the latest PHP version to include the fix for bug #73371
- Input validation and sanitization for locale parameters in applications using locale_get_keywords
- Monitor PHP error logs for segmentation faults or crashes related to locale functions
- Use PHP's error reporting and logging to detect anomalous terminations

## Objectives

1. Cause a crash in the PHP process to deny service to the application
2. Demonstrate the impact of code injection in internal PHP functions
3. Validate vulnerability presence in target environments

## Instructions

### Step 1: Prepare Test Script

**Context**: Create a simple PHP script to invoke the vulnerable function with malformed input, simulating untrusted data injection.

**Instructions**: Write and save the following PHP code to a file, e.g., test_crash.php. The 'invalid_locale_string' represents a crafted input that triggers improper handling (exact string details from bug report analysis; adjust based on reproduction).

```php
<?php
// Invoke locale_get_keywords with malformed locale
$keywords = locale_get_keywords('invalid_locale_string');
if ($keywords) {
    print_r($keywords);
} else {
    echo "No keywords retrieved.";
}
?>
```

> This script attempts to parse keywords from an invalid locale, leading to a crash due to code injection in the function's internals.

### Step 2: Execute the Script

**Context**: Run the script in the PHP environment to trigger the vulnerability and observe the DoS effect.

**Instructions**: Execute via PHP CLI for local testing or access via a web browser if hosted. For CLI:

```bash
php test_crash.php
```

For web: Place on a server and request http://target/test_crash.php.

> Expected behavior: The PHP interpreter crashes immediately upon function call, resulting in no output and process termination. Check system logs for segfault or similar errors confirming the DoS.

### Step 3: Verify Impact

**Context**: Confirm the crash and assess DoS by checking application availability.

**Instructions**: After execution, attempt to run other PHP scripts or access the application. Monitor with tools like top or htop for process death.

> Successful exploitation shows the target PHP instance unresponsive until restart, validating the low-severity DoS.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- php
- dos
- code-injection
- crash
- vulnerability
