---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: Denial of Service Crash via Code Injection in PHP locale_get_keywords Function
tags:
  - php
  - dos
  - code-injection
  - crash
  - vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - PHP
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Trigger-PHP-locale_get_keywords-Crash]]'
step_count: 1
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:20.261Z'
description: >-
  A low-severity vulnerability in PHP's locale_get_keywords function that allows
  code injection leading to application crash and denial of service through
  improper handling of locale inputs.
skill_level: intermediate
impact_level: low
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# Denial of Service Crash via Code Injection in PHP locale_get_keywords Function

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Trigger Vulnerability] --> B[Application Crash]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None required (uses native PHP execution)

### Target Environment

- PHP runtime environment (version affected by bug #73371)
- Access to execute PHP code, such as a web server or CLI
- No specific services/ports required beyond PHP execution

### Initial Access Requirements

- Code execution privileges on the target PHP application
- Ability to invoke internal PHP functions like locale_get_keywords
- No prior network access needed if local; remote if web-exposed

## Detailed Attack Procedures

### Step 1: Trigger the Crash
procedure: [[procedures/Trigger-PHP-locale_get_keywords-Crash]]

**Objective**: Exploit improper handling in the locale_get_keywords function to cause a crash and denial of service.

**Instructions**: Prepare a PHP script that calls the locale_get_keywords function with a malformed or invalid locale string to trigger the code injection and subsequent crash. For example, in a controlled test environment:

```php
<?php
// Example invocation with potentially malformed input
$keywords = locale_get_keywords('invalid_locale_string');
print_r($keywords);
?>
```

Execute the script via PHP CLI or embed in a web application to observe the crash.

**Expected Output**: The PHP process crashes, resulting in a segmentation fault or abrupt termination, leading to denial of service.

**Success Indicators**:
- PHP application or process terminates unexpectedly
- Error logs show crash related to locale_get_keywords (e.g., segfault in bug #73371)
- No further responses from the affected PHP instance

## Attack Chain Summary

### Key Achievements

1. Successful invocation of vulnerable function leading to crash
2. Demonstration of denial of service impact on PHP runtime
3. Identification of code injection vector in locale handling

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Impact]]

---
*Last updated: 2023-10-01T12:00:00Z*
