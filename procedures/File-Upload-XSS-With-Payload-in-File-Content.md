---
type: procedure
description: >-
  Exploit a web application's file upload functionality by uploading an HTML
  file containing a JavaScript XSS payload, leading to arbitrary code execution
  when the file is accessed.
verified: true
submitted: true
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - owasp
  - owasp-top-10
  - web-applications
  - xss
commands: []
platforms:
  - Web
tools: []
skill_level: beginner
impact_level: medium
detection_risk: low
validated: true
---

# File-Upload-XSS-With-Payload-in-File-Content

## Summary

This procedure demonstrates a stored XSS attack by uploading an HTML file containing a JavaScript payload to a web application with insecure file upload handling. When a user accesses the uploaded file, the payload executes in their browser, potentially leading to session hijacking, data theft, or further exploitation.

## Description

Cross-site scripting (XSS) via file upload occurs when a web application allows users to upload files without validating content or type, enabling attackers to upload malicious HTML files with embedded JavaScript. Accessing the file URL triggers the script execution in the viewer's context, making this a form of stored XSS. This technique targets applications with public or low-privilege upload endpoints, such as user profile image uploads or document sharing features. Success relies on the server serving the file with the correct MIME type (text/html) and no content sanitization. It maps to MITRE ATT&CK technique T1059.007 (JavaScript) under the Execution tactic, as it leverages client-side script execution for malicious purposes.

## Requirements

1. Access to a web application with a file upload feature that does not restrict file types or scan contents.
2. A standard web browser to interact with the upload interface and view the file.
3. No special privileges required if the upload is unauthenticated; otherwise, valid user credentials.
4. The application must serve uploaded files directly to users without isolation (e.g., no CDN stripping scripts).

## Defense

Defensive measures and detection strategies:

- Implement strict file type validation (e.g., allow only images/PDFs) and extension whitelisting on the server side.
- Scan uploaded files for malicious content using antivirus or custom script detectors before storage.
- Serve user-uploaded files from a different domain or with a 'Content-Security-Policy' header to block inline scripts.
- Monitor access logs for unusual file requests and implement rate limiting on uploads.
- Use Web Application Firewalls (WAFs) to detect common XSS patterns in file contents.

## Objectives

1. Upload a malicious HTML file containing an XSS payload to the target application.
2. Access the uploaded file to execute the JavaScript payload in a browser context.
3. Demonstrate arbitrary code execution, such as displaying an alert, to confirm vulnerability.
4. Highlight the risks of unvalidated file uploads leading to stored XSS attacks.

## Instructions

### Step 1: Identify and Access the File Upload Functionality

**Context**: Locate the file upload endpoint or form in the web application to prepare for exploitation. This step ensures you have the necessary interface to submit files.

Navigate to the application's upload page, such as a profile editor, document submission form, or media upload section. Verify that the upload accepts HTML files or has weak validation (e.g., renames .html to .txt but serves as HTML).

**Expected Output**: The upload form is visible, with options to browse and submit files.

### Step 2: Create the Malicious HTML File with XSS Payload

**Context**: Prepare a simple HTML file embedding a JavaScript payload. This file will be uploaded and executed when accessed, proving the XSS vulnerability.

Use a text editor to create a file named 'xss.html' containing the payload. Reference the standalone code snippet [[codes/Simple-XSS-Alert-in-HTML]] for the exact content. Save the file locally.

**Expected Output**: A valid HTML file of approximately 50 bytes, viewable in a browser to confirm the alert triggers locally.

### Step 3: Upload the Malicious File

**Context**: Submit the prepared HTML file through the application's upload mechanism to store it on the server.

In the upload form, click 'Browse' or 'Choose File', select 'xss.html', and click 'Submit' or 'Upload'. Note any success message or redirect.

**Expected Output**: Confirmation of upload success, possibly with a file path or URL (e.g., '/uploads/xss.html'). Check the application's file list or server response for the location.

### Step 4: Access the Uploaded File to Trigger XSS

**Context**: Retrieve and load the uploaded file in a browser to execute the embedded JavaScript payload.

Construct the full URL to the uploaded file (e.g., 'https://target.com/uploads/xss.html') and navigate to it in your browser. Observe the execution of the script.

**Expected Output**: The page loads as HTML, and the JavaScript payload executes, displaying an alert box with 'XSS' or similar message.

**Success Indicators**:
- Alert box appears without errors.
- Browser developer tools show the script running in the page context.
- No file type blocking or sanitization occurs during access.
