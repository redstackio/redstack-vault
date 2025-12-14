---
id: 00000000-0000-0000-0000-000000000003
name: Craft-SSRF-Bypass-WebCal-URL
type: procedure
verified: false
submitted: true
created_at: '2023-12-14T00:00:00Z'
updated_at: '2025-12-14T04:08:48.773Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
tags:
  - ssrf
  - ipv6
  - bypass
platforms:
  - Web
  - PHP
commands:
  - '[[commands/php-filter-var-validate-ip]]'
  - '[[commands/php-filter-var-validate-ip-no-flags]]'
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Craft-SSRF-Bypass-WebCal-URL

## Summary

This procedure constructs a WebCal URL that embeds an IPv4 address within an IPv6 format (e.g., [0:0:0:0:0:ffff:127.0.0.1]) to bypass Nextcloud's SSRF filters, which remove brackets before PHP filter_var validation, allowing access to private IPs like localhost.

## Description

The vulnerability stems from improper handling of IPv6 addresses in the Calendar and DAV apps. By wrapping the embedded IPv4 in brackets, the application removes them for validation, but PHP's filter_var does not correctly reject the embedded private IP, enabling SSRF to internal resources. This is used in ICS files for WebCal subscriptions.

## Requirements

1. Knowledge of target internal IP (e.g., 127.0.0.1) and resource path (e.g., /secret.ics)
2. PHP environment for testing validation (optional, for verification)
3. Understanding of IPv6 syntax for embedding IPv4 (::ffff: notation)

## Defense

Defensive measures and detection strategies:

- Implement stricter IP validation that parses and checks embedded IPv4 in IPv6
- Use libraries like ipaddress in Python or equivalent to fully validate addresses
- Log and block requests to private/reserved ranges in webcal fetches

## Objectives

1. Create a URL that evades filter_var(FILTER_VALIDATE_IP) with NO_PRIV/NO_RES flags
2. Target internal files for exfiltration
3. Ensure compatibility with ICS format for calendar import

## Instructions

### Step 1: Construct Embedded URL

**Context**: Build the base URL with IPv6 embedding to point to localhost.

**Command** (Manual Construction):

Form the URL: `http://[0:0:0:0:0:ffff:127.0.0.1]:80/secret.ics`

> The brackets are removed by the app before validation, turning it into `0:0:0:0:0:ffff:127.0.0.1`, which passes as IPv6 but resolves to 127.0.0.1.

### Step 2: Test Validation Bypass

**Context**: Verify the bypass using PHP's filter_var to simulate server logic.

**Command** ([[commands/php-filter-var-validate-ip-no-flags]]):
```php
<?php echo filter_var("0:0:0:0:0:ffff:127.0.0.1", FILTER_VALIDATE_IP) ? 'true' : 'false'; ?>
```

> Outputs 'false' due to invalid IPv6 recognition, but in app context, it proceeds if not fully checked; adjust for full bypass test.

**Command** ([[commands/php-filter-var-validate-ip]]):
```php
<?php echo filter_var("[0:0:0:0:0:ffff:127.0.0.1]", FILTER_VALIDATE_IP, FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE) ? 'true' : 'false'; ?>
```

> Outputs 'false' with brackets, confirming removal is key to bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/php-filter-var-validate-ip]]
- [[commands/php-filter-var-validate-ip-no-flags]]

## Tools Used


## Tags

- ssrf
- ipv6
- bypass
