---
id: proc-uuid-001
tags:
  - information-disclosure
  - reconnaissance
  - apache
  - htaccess
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-retrieve-htaccess]]'
verified: false
platforms:
  - Web
  - Apache
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Software]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:18.100Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
  - '[[Exploit Public-Facing Application]]'
---
# Retrieve-Public-Htaccess-Configuration-File

## Summary

This procedure exploits a misconfiguration allowing public access to the .htaccess file on an Apache server, disclosing configuration details like CGI handlers, PHP paths, and rewrite rules for reconnaissance purposes.

## Description

In this attack scenario, attackers target web subdomains where .htaccess files are not protected by access controls. By appending /.htaccess to the base URL, the file is downloaded, revealing server internals. This is common in static sites with legacy configurations. Expected outcomes include exposure of directives that could inform further attacks, though impact is low if no sensitive data is present. Prerequisites include public internet access to the target.

## Requirements

1. Publicly accessible web subdomain (e.g., https://subdomain.example.com)
2. HTTP client like curl or a web browser
3. No authentication or special privileges needed

## Defense

Defensive measures and detection strategies:

- Implement access controls on configuration files using Apache directives like <Files ".htaccess"> Require all denied </Files>
- Monitor web server logs for unusual requests to /.htaccess endpoints
- Use web application firewalls (WAF) to block access to sensitive paths

## Objectives

1. Download and analyze .htaccess contents for server configuration insights
2. Identify potential misconfigurations for chained attacks
3. Gather reconnaissance data without triggering alerts

## Instructions

### Step 1: Append Path and Fetch File

**Context**: Directly request the .htaccess file via URL manipulation to trigger disclosure.

**Command** ([[commands/curl-retrieve-htaccess]]):
```bash
curl https://_domainkey.launchpad.37signals.com/.htaccess -o htaccess.txt
```

> This command fetches the .htaccess file and saves it locally. In a browser, navigating to the URL prompts a download. Expected output includes lines like "Options +ExecCGI +MultiViews +FollowSymLinks" and rewrite rules for sprockets.js.

### Step 2: Analyze Contents

**Context**: Review the file for actionable intelligence.

**Command** (No specific command; use text editor):

> Open htaccess.txt and scan for directives. Look for AddHandler, php_value, and RewriteEngine rules that reveal tech stack and paths.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Software]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-retrieve-htaccess]]

## Tools Used


## Tags

- information-disclosure
- reconnaissance
- apache
- htaccess
