---
id: ac-php-openssl-pbkdf2-dos
tags:
  - memory-corruption
  - dos
  - php
  - openssl
  - integer-overflow
type: attack_chain
tools:
  - '[[tools/AddressSanitizer]]'
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Linux
  - PHP
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-Invalid-Parameter-Handling-in-openssl_pbkdf2]]'
  - '[[procedures/Trigger-Memory-Corruption-with-AddressSanitizer]]'
step_count: 2
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Application or System Exploitation]]'
updated_at: '2025-12-14T17:28:20.641Z'
description: >-
  Demonstrates exploitation of integer overflow in PHP 5.6's openssl_pbkdf2
  function leading to memory corruption and application crash for
  denial-of-service.
skill_level: intermediate
impact_level: medium
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Application or System Exploitation]]'
---
# Memory Corruption Denial-of-Service via Invalid key_length in PHP openssl_pbkdf2

Multi-stage attack chain demonstrating a complete vulnerability exploitation workflow for denial-of-service through memory corruption in PHP's OpenSSL integration.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Vulnerability] --> B[Trigger Exploitation]
    B --> C[Application Crash]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/AddressSanitizer]]

### Target Environment

- Target OS/Platform: Linux
- Required services/ports: None (local PHP execution)
- Network access requirements: Local access to PHP 5.6 installation

### Initial Access Requirements

- Credential requirements: Local user with PHP execution privileges
- Network position: Localhost
- Prior access needed: Installed PHP 5.6 with OpenSSL extension

## Detailed Attack Procedures

### Step 1: Identify Invalid Parameter Handling
procedure: [[procedures/Identify-Invalid-Parameter-Handling-in-openssl_pbkdf2]]

**Objective**: Analyze PHP source code to identify lack of bounds checking on key_length in openssl_pbkdf2, leading to signed integer overflow when passed to OpenSSL.

**Instructions**: Review the PHP extension source at ext/openssl/openssl.c, focusing on line 4080 in zif_openssl_pbkdf2. Note the absence of overflow checks before calling PKCS5_PBKDF2_HMAC, which interprets key_length > 0x7fffffff as negative in memcpy.

**Expected Output**: Confirmation of vulnerability in code review, highlighting potential for negative size parameter error.

**Success Indicators**:
- Identified unvalidated key_length parameter
- Understood overflow leading to memcpy issue

### Step 2: Trigger Memory Corruption
procedure: [[procedures/Trigger-Memory-Corruption-with-AddressSanitizer]]

**Objective**: Execute a PHP script with oversized key_length to trigger memory corruption, detected by AddressSanitizer, resulting in application crash.

**Instructions**: Compile PHP 5.6 with AddressSanitizer enabled (linked to /usr/lib/x86_64-linux-gnu/libasan.so.2). Create and run a PHP script calling openssl_pbkdf2 with key_length exceeding 0x7fffffff, such as 2147483648. Use [[commands/php-execute-vulnerable-script]] to run the script and observe the crash.

```bash
php vulnerable_script.php
```

**Expected Output**: AddressSanitizer reports "negative-size-param" error in memcpy within OpenSSL's PKCS5_PBKDF2_HMAC, followed by application termination.

**Success Indicators**:
- Memory error detected by AddressSanitizer
- PHP process crashes due to corruption

## Attack Chain Summary

### Key Achievements

1. Identified integer overflow vulnerability in PHP-OpenSSL integration
2. Triggered detectable memory corruption leading to DoS
3. Demonstrated fix avoidance in PHP 7 via conversion checks

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[Application or System Exploitation]] Application or System Crashes

### MITRE ATT&CK Tactics

- [[Impact]] Impact

---
*Last updated: 2023-10-01T00:00:00Z*
