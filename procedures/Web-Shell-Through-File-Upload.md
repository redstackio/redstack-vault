---
id: 37533e0a-ced4-4b3b-a52b-06219f8981c1
type: procedure
name: Web-Shell-Through-File-Upload
verified: true
submitted: true
created_at: '2020-07-28T18:31:14.822835+00:00'
updated_at: '2023-05-26T01:08:50.637436+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Server Software Component]]'
sub_techniques: []
tags:
  - file-uploads
  - web-applications
  - web-shell
commands:
  - '[[commands/curl-upload-webshell]]'
platforms:
  - Web
tools: []
validated: true
---

# Web-Shell-Through-File-Upload

## Summary

This procedure demonstrates how to exploit vulnerable file upload functionality in web applications to deploy a web shell, providing remote command execution capabilities on the server. It involves identifying the upload endpoint, preparing a malicious PHP file, uploading it, and accessing it to execute system commands, commonly used in web application penetration testing to gain persistent access.

## Description

Web applications often include file upload features for user content, such as profile images or documents, but insufficient validation can allow attackers to upload executable scripts like PHP web shells. Once uploaded, the shell acts as a backdoor, enabling command execution directly on the server via a simple web interface. This technique targets public-facing web apps and assumes the upload directory is web-accessible. Success depends on bypassing any file type restrictions, such as by renaming the shell to mimic allowed extensions (e.g., shell.php.jpg) or using null byte injection. The procedure maps to MITRE ATT&CK techniques for exploiting public-facing applications and deploying web shells for execution.

## Requirements

1. Validated access to a web application with a file upload feature (e.g., via browser or API endpoint).
2. Knowledge of the upload endpoint URL and any required authentication (e.g., session cookies or API keys).
3. A prepared web shell file, such as a PHP script for command execution.
4. Tools like curl for automated uploads or a browser/proxy like Burp Suite for manual testing.
5. Server-side execution environment supporting PHP (common on Linux/Apache/Nginx stacks).

## Defense

Defensive measures include strict file type validation (e.g., checking MIME types and extensions server-side), scanning uploads for malicious content using antivirus or WAF rules, storing files outside the web root, and implementing least-privilege execution (e.g., disabling PHP exec functions via php.ini). Detection can involve monitoring for anomalous uploads (e.g., .php files), web server logs for suspicious access patterns, and behavioral analysis for command execution via HTTP requests.

## Objectives

1. Identify and exploit a vulnerable file upload endpoint to deploy a web shell.
2. Verify successful upload and accessibility of the shell.
3. Establish command execution interface for further post-exploitation.
4. Achieve remote code execution on the target server with minimal footprint.

## Instructions

### Step 1: Identify File Upload Functionality

**Context**: Locate the file upload feature in the web application, typically found in user profile sections, admin panels, or API endpoints. Use manual browsing or automated scanning to confirm the endpoint accepts files without proper validation.

Inspect the application for forms with <input type="file"> elements and note the submission URL (e.g., /upload.php). Test with benign files to understand response behavior, such as success messages or returned file paths.

### Step 2: Prepare the Web Shell

**Context**: Create or obtain a simple PHP web shell script that allows command input via GET parameters and executes them using system calls. This payload provides an interactive interface without requiring additional tools.

Use the following code snippet as the web shell content: [[codes/PHP-Basic-Command-Execution-Web-Shell]]. Save it as shell.php on your local machine, ensuring no modifications that could break execution (e.g., preserve PHP tags).

### Step 3: Upload the Web Shell

**Context**: Submit the prepared web shell to the upload endpoint, bypassing any client-side restrictions. If the server enforces MIME checks, use tools to spoof the content type or append null bytes.

**Command** ([[commands/curl-upload-webshell]]):
```bash
curl -X POST -F "file=@shell.php" -H "Content-Type: multipart/form-data" http://target.example.com/upload.php
```

This command uploads the file via HTTP POST. Replace http://target.example.com/upload.php with the actual endpoint. If authentication is required, add cookies or headers (e.g., -H "Cookie: session=abc123").

Expected output includes a success response, such as JSON {"status":"success","path":"/uploads/shell.php"} or HTML confirmation. Verify the response body for the uploaded file's server path.

### Step 4: Access and Verify the Web Shell

**Context**: Navigate to the uploaded file's URL to load the shell interface. If the path is relative (e.g., /uploads/shell.php), construct the full URL (http://target.example.com/uploads/shell.php).

Open the URL in a browser. The page should display a form with a text input for commands and a submit button. Test by entering a harmless command like "whoami" and submitting; the output should appear in a <pre> tag below the form, confirming execution.

If no output appears, check for PHP errors (e.g., disabled system() function) or path issues. Success indicates the shell is operational for further commands like directory listing ("ls -la") or file downloads.
