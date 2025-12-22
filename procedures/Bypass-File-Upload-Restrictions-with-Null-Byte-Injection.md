---
id: e6d5df54-85ff-4c9f-8181-d2361d41acd6
name: Bypass-File-Upload-Restrictions-with-Null-Byte-Injection
type: procedure
verified: true
submitted: true
created_at: '2020-08-01T14:40:52.823830+00:00'
updated_at: '2023-05-26T01:30:10.499969+00:00'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - '[[tags/injection]]'
  - '[[tags/Null Byte Injection]]'
  - '[[tags/owasp]]'
  - '[[tags/owasp top 10]]'
  - '[[tags/Web Applications]]'
commands:
  - '[[commands/curl-upload-file-with-null-byte]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/cURL]]'
validated: true
---

# Bypass-File-Upload-Restrictions-with-Null-Byte-Injection

## Summary

This procedure demonstrates how to bypass file upload restrictions in web applications by appending a decoy extension to a malicious file and injecting a null byte (%00) into the filename during the upload request. This tricks the server into processing the file as the malicious type (e.g., .exe) while ignoring the decoy extension, allowing unauthorized file execution or further exploitation.

## Description

Null byte injection exploits vulnerabilities in file handling where servers or applications terminate string processing at a null byte (\x00), often due to legacy C-based parsing in languages like PHP or misconfigured filters. In file upload scenarios, attackers rename a malicious executable (e.g., shell.exe) to something like shell.exe%00.jpg, causing the server to validate only the .jpg extension but store and potentially execute the .exe portion. This is common in older web apps without proper input sanitization. The technique requires intercepting or crafting the HTTP multipart/form-data request to include the null byte. Success enables initial access via uploaded malware, leading to RCE or persistence. Target environments include web apps with file upload features lacking secure extensions checks, such as content management systems or custom portals.

## Requirements

1. Access to a web application with a file upload functionality that restricts extensions (e.g., allows only .jpg but not .exe).
2. A malicious file ready for upload (e.g., a reverse shell executable).
3. Network access to intercept or send HTTP requests (e.g., via proxy or direct curl).
4. Tools like curl for request crafting or Burp Suite for interception.
5. Basic knowledge of HTTP multipart/form-data encoding.

## Defense

Defensive measures and detection strategies:

- Validate file types using MIME type detection and content scanning (e.g., ClamAV) rather than just filename extensions.
- Sanitize all user inputs, stripping or rejecting null bytes and unusual characters in filenames.
- Store uploaded files outside the web root and serve them via secure scripts that re-validate on access.
- Enable web application firewall (WAF) rules to block requests containing %00 or \x00 in filenames.
- Log and monitor file uploads for anomalies, such as unexpected MIME types or hex-encoded nulls.

## Objectives

1. Primary objective: Upload a restricted file type (e.g., .exe) by bypassing extension filters.
2. Secondary objective: Achieve code execution or persistence on the server via the uploaded malicious file.
3. Expected outcome: Successful upload and potential execution of the malicious payload, granting initial access.

## Instructions

### Step 1: Prepare the Malicious File with Decoy Extension

**Context**: Rename the malicious executable to include a decoy allowed extension (e.g., .jpg) separated by a placeholder character that will be replaced with a null byte. This ensures the filename passes initial client-side checks.

Use a simple bash command to rename the file, though this is manual preparation.

> The file should now be named something like malicious.exeA.jpg, where 'A' is the placeholder (hex 41) to be replaced later.

### Step 2: Craft and Send the Upload Request with Null Byte Injection

**Context**: Intercept or directly send the HTTP POST request for file upload, modifying the filename to include a null byte (%00 in URL encoding or \x00 in binary) between the malicious extension and decoy. This causes the server to truncate at the null byte during validation.

**Command** ([[commands/curl-upload-file-with-null-byte]]):
```bash
curl -X POST -F "file=@malicious.exe%00.jpg" http://target.com/upload
```

> This command uploads the file with the null byte embedded in the filename using URL encoding (%00). If using a proxy like Burp Suite, intercept the request, switch to the Hex tab, locate the placeholder (e.g., 41 for 'A'), replace it with 00, and forward. Expected output is a server response indicating successful upload (e.g., 200 OK with upload confirmation), without rejection due to extension.

### Step 3: Verify Upload and Access the File

**Context**: Confirm the file was uploaded and processed as the malicious type by checking server responses or accessing the upload directory if exposed. Test execution if the app auto-processes uploads.

> Look for success messages like "File uploaded successfully" or errors indicating truncation. If the server executes the file (e.g., via image processing), monitor for callback connections from a reverse shell.

### Step 4: Clean Up and Escalate

**Context**: If successful, use the uploaded file for further exploitation, such as executing a reverse shell. Remove traces if operating in a red team context.

> Success is indicated by the ability to download or execute the original malicious file from the server path.
