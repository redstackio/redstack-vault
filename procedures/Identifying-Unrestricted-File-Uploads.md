---
type: procedure
description: >-
  Test web application file upload functionality to determine if it allows
  unrestricted uploads of executable or dangerous file types, potentially
  leading to code execution.
verified: true
submitted: true
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
sub_techniques: []
tags:
  - File Uploads
  - Web Applications
commands:
  - '[[commands/curl-upload-malicious-file]]'
tools:
  - '[[tools/Burp-Suite]]'
platforms:
  - Web
skill_level: beginner
impact_level: high
detection_risk: low
validated: true
---

# Identifying-Unrestricted-File-Uploads

## Summary

This procedure tests for unrestricted file upload vulnerabilities in web applications by attempting to upload files with dangerous extensions such as .php, .exe, or .py. If the upload succeeds without validation, it may allow attackers to execute arbitrary code on the server, leading to remote code execution (RCE).

## Description

Unrestricted file uploads occur when a web application fails to properly validate or sanitize uploaded files, permitting executable content to be placed on the server. This is a common vulnerability in applications with user-facing upload features, such as invoice or document submission forms. The technique involves identifying the upload endpoint, preparing a test file with a malicious payload (e.g., a simple webshell), and submitting it. Success is indicated if the file is stored in an accessible location without rejection. This maps to exploiting public-facing applications and ingress tool transfer, often resulting in execution if the file type is processed by the server (e.g., PHP on Apache).

## Requirements

1. Valid user session or access to the web application's upload functionality.
2. A prepared malicious test file (e.g., shell.php containing webshell code).
3. Network access to the target web application.
4. Tools like a web browser or [[tools/Burp-Suite]] for manual testing, or curl for automated uploads.

## Defense

- Implement server-side validation for file types, extensions, and content (e.g., MIME type checking, virus scanning).
- Store uploads outside the web root or rename files to non-executable extensions.
- Use Web Application Firewalls (WAFs) to detect anomalous upload patterns.
- Enable logging of upload attempts and monitor for execution of uploaded files.

## Objectives

1. Confirm if the application rejects or accepts dangerous file types.
2. Verify if uploaded files are stored in web-accessible directories.
3. Establish a potential foothold for RCE if execution is possible.
4. Expected outcome: Successful upload and access to the malicious file, enabling command execution.

## Instructions

### Step 1: Identify File Upload Functionality

**Context**: Locate the upload feature in the application, such as a form for documents or images, to understand the endpoint and parameters.

Navigate to the web application and search for upload options (e.g., 'Upload Invoice' in a product return section). Use browser developer tools or [[tools/Burp-Suite]] to inspect the form's action URL, method (POST), and fields (e.g., file input name).

**Expected Output**: Form details, such as POST to /upload.php with enctype="multipart/form-data".

### Step 2: Prepare Malicious Test File

**Context**: Create or reference a simple executable file to test restrictions. This step ensures the file mimics a real threat without causing unintended damage.

Use the [[codes/Simple-PHP-Webshell]] code to create shell.php. Save it locally for upload.

**Expected Output**: A file named shell.php containing the webshell code.

### Step 3: Attempt Upload via Browser or Proxy

**Context**: Submit the file through the identified form to test server-side validation. Using a proxy allows interception and modification if needed.

In the browser, select the Browse button, choose shell.php, and click Submit. Alternatively, intercept with [[tools/Burp-Suite]] to modify headers or parameters.

**Expected Output**: Success message or redirect indicating upload completion, without errors like "Invalid file type".

### Step 4: Verify Upload Success and Accessibility

**Context**: Check if the file was stored and is executable. This confirms the vulnerability.

After upload, note any provided URL or directory path. Access the uploaded file directly (e.g., http://target/uploads/shell.php?cmd=whoami). If accessible, append a command parameter to test execution.

**Command** ([[commands/curl-upload-malicious-file]]):
```bash
curl -X POST -F "file=@shell.php" -F "submit=Upload" http://target.com/upload-endpoint
```

> This curl command simulates the form submission. Replace the URL and field names based on Step 1 inspection. Expected output includes a 200 OK response or success message.

**Expected Output**: File listed in upload directory or direct access returns PHP execution (e.g., output of 'whoami').

### Step 5: Test for Execution

**Context**: If uploaded, attempt to execute the payload to confirm RCE potential.

Use a browser or curl to invoke the webshell: http://target/uploads/shell.php?cmd=id. Monitor for command output.

**Expected Output**: Server response showing command results, indicating successful execution.
