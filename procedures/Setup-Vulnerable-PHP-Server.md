---
id: proc-php-setup-vuln-server-001
tags:
  - php
  - setup
  - vulnerable-environment
type: procedure
tools:
  - '[[tools/PHP-Built-in-Web-Server]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/php-start-builtin-server]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:09.959Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-Vulnerable-PHP-Server

## Summary

This procedure configures and starts a PHP built-in web server with session.upload_progress.cleanup disabled, enabling the null pointer dereference vulnerability in PHP's session upload progress handling for testing DoS exploits.

## Description

The vulnerability occurs in PHP versions 5.4 through 7 when handling multipart form-data uploads without proper file start events, leaving progress data uninitialized. This setup mimics a vulnerable production environment by disabling cleanup, allowing progress data to persist and trigger the dereference during failed uploads. It requires creating a simple web directory with an index.php file to process requests.

## Requirements

1. PHP 5.4-7 installed on Linux
2. Access to create directories and files in /www/web/
3. Port 8000 available

## Defense

Defensive measures and detection strategies:

- Enable session.upload_progress.cleanup=1 in php.ini to auto-clean progress data
- Monitor PHP-FPM logs for segmentation faults or null pointer errors
- Use web application firewalls to validate multipart requests

## Objectives

1. Establish a testable vulnerable PHP endpoint
2. Verify configuration allows upload progress tracking without cleanup
3. Prepare for PoC execution without server-side modifications

## Instructions

### Step 1: Create Web Directory

**Context**: Set up the document root for the server to serve a basic index.php that can handle POST requests.

**Command** ([[commands/mkdir-create-web-dir]]):
```bash
mkdir -p /www/web/
echo '<?php echo "Hello"; ?>' > /www/web/index.php
```

> This creates the directory and a minimal index.php. Expected output: No errors, files created successfully.

### Step 2: Start Vulnerable Server

**Context**: Launch the PHP development server with the cleanup directive disabled to enable the vulnerability.

**Command** ([[commands/php-start-builtin-server]]):
```bash
php -S localhost:8000 -t /www/web/ -d session.upload_progress.cleanup=0
```

> Starts the server on port 8000 serving from /www/web/, disabling cleanup. Expected output: '[Date] PHP Development Server started at http://localhost:8000'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/php-start-builtin-server]]
- [[commands/mkdir-create-web-dir]]

## Tools Used

- [[tools/PHP-Built-in-Web-Server]]

## Tags

- php
- setup
- vulnerable-environment
