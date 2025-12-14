---
url: >-
  https://symfony.com/doc/current/components/http-foundation.html#component-http-foundation-iputils
tags:
  - validation
  - ip
type: tool
verified: false
platforms:
  - PHP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.219Z'
id: 9025c45d-2eb2-498a-abaf-fc3684453561
validated: true
submitted: true
---
# Symfony-IpUtils

**Status**: Unverified

## Overview

Symfony IpUtils is a PHP component for checking if IPs fall within specified ranges, replicating Nextcloud's local IP detection.

## Description

Used in test scripts to validate against ranges like 100.64.0.0/10, helping identify SSRF bypasses when combined with filter_var.

## Features

- Feature 1: checkIp method for CIDR range matching
- Feature 2: Supports IPv4/IPv6
- Feature 3: Lightweight, no external deps beyond Symfony

## Installation

### Requirements

- Composer
- PHP 7.1+

### Install Commands

```bash
composer require symfony/http-foundation
```

## Basic Usage

```php
use Symfony\Component\HttpFoundation\IpUtils; IpUtils::checkIp('192.168.1.1', ['192.168.0.0/16']);
```

### Common Options

| Option | Description |
|--------|-------------|
| `checkIp($ip, $ranges)` | Returns bool if IP in ranges |

## Examples

### Example 1: Basic Usage

```php
IpUtils::checkIp('100.64.0.1', ['100.64.0.0/10']); // true
```

### Example 2: Advanced Usage

```php
$ranges = ['100.64.0.0/10', '192.0.0.0/24']; IpUtils::checkIp($ip, $ranges);
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Standard Application Layer Protocol]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Dependency scans showing Symfony in PHP apps
- Validation log entries

## Related Procedures


## Related Tools

- [[tools/PHP]]

## References

- Official documentation: https://symfony.com/doc/current/components/http-foundation.html#iputils
- Related resources: Symfony components
