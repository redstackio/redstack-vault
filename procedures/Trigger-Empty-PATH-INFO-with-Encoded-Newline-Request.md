---
tags:
  - trigger
  - pathinfo
  - encoded-newline
  - nginx
  - fastcgi
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-trigger-empty-pathinfo]]'
platforms:
  - Web
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 79fd7e3b-dd7d-4e8e-add4-caea16893c79
created_at: '2025-12-14T17:23:49.472Z'
updated_at: '2025-12-14T17:23:49.472Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-Empty-PATH-INFO-with-Encoded-Newline-Request

## Summary

This procedure crafts and sends an HTTP request to Nginx that uses an encoded newline (%0a) in the URL path to break the fastcgi_split_pathinfo directive's regexp, resulting in an empty PATH_INFO variable being passed to php-fpm and priming the buffer underflow vulnerability.

## Description

In vulnerable Nginx setups, the fastcgi_split_pathinfo directive relies on a regexp to split SCRIPT_NAME and PATH_INFO. Injecting %0a (URL-encoded newline) disrupts this parsing, setting PATH_INFO to empty. This triggers the missing bounds check in php-fpm's fpm_main.c, leading to an invalid pointer calculation. The procedure uses standard tools like curl for the request, requiring only HTTP access to the target.

## Requirements

1. Running vulnerable Nginx/php-fpm stack (e.g., from setup procedure)
2. Network access to the web server (port 80/443)
3. Curl or similar HTTP client

## Defense

Defensive measures and detection strategies:

- URL-decode and validate all path parameters in Nginx, rejecting %0a or newlines
- Enable strict regexp escaping in fastcgi_split_pathinfo
- Log and alert on anomalous PATH_INFO values in php-fpm

## Objectives

1. Manipulate Nginx parsing to empty PATH_INFO
2. Confirm trigger without crashing the server
3. Set stage for underflow exploitation

## Instructions

### Step 1: Craft the Malicious URL

**Context**: Prepare the URL with encoded newline to target a PHP endpoint.

**Command** ([[commands/curl-trigger-empty-pathinfo]]):
```bash
URL="http://localhost/index.php/%0a"
```

> Sets the URL variable; %0a decodes to newline, breaking the split.

### Step 2: Send the Trigger Request

**Context**: Transmit the request to Nginx, observing the forwarding to php-fpm.

**Command** ([[commands/curl-trigger-empty-pathinfo]]):
```bash
curl "$URL" -v
```

> Verbose curl shows headers and response; expect 200 OK or PHP error, with logs confirming empty PATH_INFO.

### Step 3: Validate Trigger in Logs

**Context**: Check server logs for the empty PATH_INFO indicator.

**Command** ([[commands/docker-build-vulnerable-env]]):
```bash
docker logs vuln-php | grep PATH_INFO
```

> Should show empty or malformed PATH_INFO entries.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-trigger-empty-pathinfo]]
- [[commands/docker-build-vulnerable-env]]

## Tools Used


## Tags

- trigger
- pathinfo
