---
tags:
  - ssrf
  - testing
  - php
type: procedure
tools:
  - '[[tools/PHP]]'
  - '[[tools/cURL]]'
  - '[[tools/Symfony-IpUtils]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/throw-if-local-ip-validation]]'
  - '[[commands/throw-if-local-address-validation]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:53:38.297Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 540ddcb6-f750-405a-a62a-3f29a1f1645e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Set-Up-Local-PHP-Test-Environment

## Summary

This procedure sets up a local PHP environment to replicate Nextcloud's SSRF validation logic for safe payload testing.

## Description

Create a dummy PHP script that mimics `ThrowIfLocalIp` and `ThrowIfLocalAddress`, using Symfony's IpUtils for range checks. The script accepts URL parameters (?ip= or ?host=), validates them, and uses cURL to fetch content if they pass, allowing simulation of SSRF without targeting a live instance. Expected outcomes include echoing 'Pass' for bypassed payloads or fetched internal content.

## Requirements

1. PHP 7+ installed with cURL extension
2. Composer for Symfony HttpFoundation (IpUtils)
3. Local web server (e.g., php -S localhost:8000)

## Defense

Defensive measures and detection strategies:

- Use containerized environments to isolate tests
- Log all cURL requests to detect unintended internal access

## Objectives

1. Replicate exact validation from Nextcloud
2. Enable iterative payload testing
3. Confirm bypasses lead to cURL execution

## Instructions

### Step 1: Install Dependencies

**Context**: Set up Symfony for IpUtils.

**Command** ([[commands/composer-require-symfony]]):
```bash
composer require symfony/http-foundation
```

> Installs IpUtils; expected: vendor/autoload.php created.

### Step 2: Create Test Script

**Context**: Implement validation functions.

Execute [[commands/throw-if-local-ip-validation]] in a PHP file:

```php
<?php
require 'vendor/autoload.php';
use Symfony\Component\HttpFoundation\IpUtils;

function ThrowIfLocalIp($ip) {
    $flags = FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE;
    if (!filter_var($ip, FILTER_VALIDATE_IP, ['flags' => $flags])) {
        throw new Exception('Invalid IP');
    }
    $ranges = ['100.64.0.0/10', '192.0.0.0/24'];
    if (IpUtils::checkIp($ip, $ranges)) {
        throw new Exception('Local IP');
    }
    echo 'Pass';
}
if (isset($_GET['ip'])) ThrowIfLocalIp($_GET['ip']);
?>
```

> Expected: Script ready for ?ip= testing.

### Step 3: Add cURL Fetching

**Context**: Extend for host validation and fetching.

Execute [[commands/throw-if-local-address-validation]] with embedded cURL:

```php
function ThrowIfLocalAddress($host) {
    $parsed = parse_url($host);
    $hostname = strtolower($parsed['host'] ?? '');
    if (substr_count($hostname, '.') === 0) throw new Exception('Local host');
    // TLD checks omitted for brevity
    ThrowIfLocalIp($parsed['host']);
    $ch = curl_init($host);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HEADER, 0);
    $data = curl_exec($ch);
    curl_close($ch);
    echo $data;
}
if (isset($_GET['host'])) ThrowIfLocalAddress($_GET['host']);
?>
```

> Expected: Fetches content on pass.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/throw-if-local-ip-validation]]
- [[commands/throw-if-local-address-validation]]

## Tools Used

- [[tools/PHP]]
- [[tools/cURL]]
- [[tools/Symfony-IpUtils]]

## Tags

- ssrf
- testing
