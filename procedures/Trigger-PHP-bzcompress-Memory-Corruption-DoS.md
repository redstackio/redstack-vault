---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Trigger PHP bzcompress Memory Corruption DoS
tags:
  - php
  - dos
  - memory-corruption
  - bzcompress
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
updated_at: '2025-12-14T17:28:20.265Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Trigger PHP bzcompress Memory Corruption DoS

## Summary

This procedure exploits an unspecified memory corruption vulnerability in PHP's bzcompress function, which compresses data using bzip2. By providing crafted input to the function, an attacker can cause the PHP application to crash, resulting in a denial of service. The vulnerability was identified through fuzzing or testing and affects PHP installations with the bz2 extension enabled.

## Description

The bzcompress function in PHP is used for bzip2 compression of strings. Due to an underlying memory corruption issue, certain malformed inputs lead to a crash during compression, potentially exploitable in web applications that process user-supplied data through this function (e.g., file uploads or data serialization). The impact is limited to denial of service as it causes the PHP process to terminate, but it requires code execution or function invocation privileges. This was reported to the Internet Bug Bounty program, earning a $500 bounty for its low-severity classification. Prerequisites include a PHP environment where bzcompress can be called, such as via a vulnerable web endpoint or direct script execution.

## Requirements

1. PHP installation with bz2 extension enabled (common in most distributions)
2. Ability to execute PHP code, either via CLI, web shell, or an application endpoint that invokes bzcompress on user input
3. Crafted input data that triggers the corruption (typically discovered via fuzzing tools like AFL or libFuzzer)
4. Access to the target PHP application or server

## Defense

Defensive measures and detection strategies:

- Update PHP to a patched version where the bzcompress vulnerability is resolved (check PHP changelog for fixes post-report)
- Avoid direct user input to bzcompress; validate and sanitize all data before compression
- Monitor PHP error logs for segmentation faults or memory errors related to bz2
- Use fuzzing tools in development to identify similar issues early
- Implement process isolation (e.g., via containers) to limit crash impact to single instances

## Objectives

1. Cause a crash in the PHP process handling the bzcompress call
2. Disrupt service availability leading to denial of service
3. Demonstrate vulnerability for reporting or testing purposes

## Instructions

### Step 1: Prepare Malicious Input

**Context**: Identify or craft input that triggers the memory corruption. Since the exact input is unspecified, use fuzzing results or known PoC from the report to generate a string that corrupts memory during compression.

Create a PHP script (e.g., exploit.php) with the following structure:

```php
<?php
// Example crafted input; replace with actual fuzz-discovered payload
$malicious_input = str_repeat("A", 10000) . "\xFF\x00"; // Placeholder for corrupting input

try {
    $compressed = bzcompress($malicious_input, 9); // Level 9 for maximum compression
    echo "No crash occurred.";
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
?>
```

> This script attempts compression and will crash the PHP interpreter if the input triggers the vulnerability. Expected output on success: immediate process termination without echo.

### Step 2: Execute the Exploit

**Context**: Run the script in the target environment to invoke bzcompress and trigger the crash.

If via CLI (assuming shell access):

```bash
php exploit.php
```

If via web (upload script to a writable directory and access http://target/exploit.php):

No specific command needed; browser or curl request suffices.

```bash
curl http://target/exploit.php
```

> Upon execution, the PHP process crashes due to memory corruption. Check server logs for confirmation (e.g., segfault in bz2 library).

### Step 3: Verify Impact

**Context**: Confirm the denial of service by observing service disruption.

Monitor the application: attempt additional requests to see if the service is unresponsive until PHP-FPM or Apache restart.

**Expected Output**: PHP fatal error or process crash in logs, such as "Segmentation fault (core dumped)".

**Success Indicators**:
- PHP process terminates
- Application returns 500 errors or becomes unavailable
- No compression output is produced

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- php
- dos
- memory-corruption
- bzcompress
