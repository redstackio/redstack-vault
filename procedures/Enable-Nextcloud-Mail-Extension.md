---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - nextcloud
  - setup
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-request]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:48.599Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Enable-Nextcloud-Mail-Extension

## Summary

This procedure installs and enables the Nextcloud mail extension, which bundles the vulnerable cerdic/csstidy module, exposing the SSRF endpoint for exploitation.

## Description

In a Nextcloud environment, the mail app must be enabled to access the third-party cerdic/csstidy library. This step assumes administrative access or a pre-enabled setup; in wild scenarios, the extension may already be active. Once enabled, the /apps/mail/vendor/cerdic/css-tidy/css_optimiser.php endpoint becomes publicly accessible without authentication, setting the stage for SSRF attacks targeting internal services or remote data downloads.

## Requirements

1. Access to Nextcloud admin interface or server console
2. Nextcloud instance version supporting mail app (e.g., 20+)
3. Web browser or curl for verification

## Defense

Defensive measures and detection strategies:

- Disable unused apps like mail if not needed
- Monitor app installations via Nextcloud logs
- Use web application firewall (WAF) to block unauthorized app access

## Objectives

1. Expose the vulnerable CSS optimizer endpoint
2. Prepare for unauthenticated SSRF exploitation
3. Verify endpoint accessibility

## Instructions

### Step 1: Install Mail App

**Context**: Navigate to the Nextcloud apps section and search for 'mail'.

**Command** ([[commands/enable-mail-app]]):
```bash
# Via occ command on server (admin access required)
occ app:install mail
occ app:enable mail
```

> This installs and enables the mail app, bundling cerdic/csstidy. Expected output: 'mail enabled'.

### Step 2: Verify Endpoint

**Context**: Confirm the vulnerable file is now accessible.

**Command** ([[commands/curl-request]]):
```bash
curl -i http://target.com/apps/mail/vendor/cerdic/css-tidy/css_optimiser.php
```

> Returns HTTP 200 with PHP interface if successful.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/enable-mail-app]]
- [[commands/curl-request]]

## Tools Used


## Tags

- nextcloud
- setup

