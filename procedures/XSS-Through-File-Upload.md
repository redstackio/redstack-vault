---
id: 303072f8-9f50-4254-9db9-36e1a6321f4b
name: XSS Through File Upload
type: procedure
verified: true
submitted: true
created_at: '2020-08-01T14:18:38.490107+00:00'
updated_at: '2023-05-26T18:17:23.654841+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - '[[tags/File Uploads]]'
  - '[[tags/owasp]]'
  - '[[tags/owasp top 10]]'
  - '[[tags/Web Applications]]'
  - '[[tags/xss]]'
commands: []
platforms:
  - Web
tools: []
validated: true
---

# XSS Through File Upload

## Summary

This procedure demonstrates how to exploit a cross-site scripting (XSS) vulnerability in a web application's file upload functionality by embedding a malicious payload in the uploaded file's filename. If the application reflects the unsanitized filename in its response without proper escaping, the payload executes as JavaScript in the user's browser, potentially leading to session hijacking, data theft, or further attacks.

## Description

File upload features in web applications often fail to sanitize or validate filenames adequately, allowing attackers to inject XSS payloads into the filename. When the server responds with a success message or list that includes the reflected filename (e.g., "File test'><script>alert('XSS')</script>.txt uploaded successfully"), the HTML context breaks out via quote closure, injecting executable script. This is a reflected XSS variant targeting the upload response. It requires no server-side execution of the file contents, only reflection of the metadata. Common in legacy or poorly coded upload handlers, this aligns with OWASP Top 10 risks like A7: Cross-Site Scripting. Use this in penetration testing to assess upload security, but ensure authorization and scope.

## Requirements

1. Access to a web application with an unrestricted or weakly validated file upload endpoint.
2. The upload response must reflect the original filename in HTML without encoding (e.g., no htmlspecialchars).
3. A standard web browser (e.g., Chrome, Firefox) for manual testing; optionally, a proxy like Burp Suite for interception and manipulation.
4. A benign file to upload (e.g., empty text file) that can be renamed locally.

## Defense

Defensive measures and detection strategies:

- Sanitize filenames on the server: Remove special characters, quotes, and script tags; generate random or UUID-based names.
- Encode reflected output: Use HTML entity encoding (e.g., htmlspecialchars in PHP) for any user-supplied data in responses.
- Implement Content Security Policy (CSP) to block inline scripts and restrict script sources.
- Validate file extensions and MIME types strictly; scan uploads for malicious content.
- Monitor for anomalous JavaScript execution in browser logs or via Web Application Firewall (WAF) rules targeting script injection patterns.

## Objectives

1. Identify and exploit filename reflection in file upload responses to execute arbitrary JavaScript.
2. Verify the vulnerability by triggering a proof-of-concept alert.
3. Demonstrate potential for more severe payloads, like cookie theft or keylogging.
4. Expected outcome: Successful XSS execution confirming the vulnerability for reporting or remediation.

## Instructions

### Step 1: Identify File Upload Functionality

**Context**: Locate the upload form to confirm it accepts files and observe how responses handle filenames. This step ensures the target is suitable and helps map the reflection point.

Navigate to the web application's upload page (e.g., /upload or similar endpoint). Inspect the form using browser developer tools (F12) to note the method (typically POST), enctype (multipart/form-data), and any client-side validations. Submit a benign file like "test.txt" and examine the response for filename reflection, such as in a success message or file list.

### Step 2: Prepare Malicious Filename with XSS Payload

**Context**: Craft a filename that closes any open HTML attributes or tags in the reflection context, injecting a script tag. This exploits improper output encoding.

Create an empty text file locally. Rename it to include the XSS payload, for example: "test"><script>alert('XSS')</script>.txt". Use the payload from [[codes/simple-xss-filename-payload]] for the injection part. Ensure the extension remains valid (e.g., .txt, .jpg) to bypass basic checks. The payload assumes a common reflection like <input value="filename">; adjust for context (e.g., add more quotes if needed).

### Step 3: Submit the Malicious File

**Context**: Upload the renamed file to trigger the server response. If using a proxy, intercept to confirm the filename is sent unaltered.

Select the renamed file in the upload form and submit it. If available, use browser dev tools or a proxy to monitor the request payload, ensuring the Content-Disposition header includes the malicious filename.

### Step 4: Verify Payload Execution

**Context**: Check the response for execution. Success indicates the filename was reflected unsafely, allowing script injection.

Examine the server response in the browser. If vulnerable, the alert('XSS') should pop up immediately. Inspect the HTML source to confirm the injected <script> tag. If no execution, iterate on the payload (e.g., try different quote escapes like \" or context-specific variants).

**Expected Output**: A JavaScript alert dialog displaying 'XSS' or the injected message, confirming execution. In the page source, the reflected filename should show the unescaped payload, e.g., value="test"><script>alert('XSS')</script>.txt".
