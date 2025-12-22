---
id: 14ddf3a6-b4f3-43f1-8a3d-68aa58c02cb2
name: Test-Anti-Virus-Using-EICAR-File-Upload
type: procedure
verified: true
submitted: true
created_at: '2020-08-06T13:56:44.771583+00:00'
updated_at: '2023-05-26T18:17:36.578357+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Security Software Discovery]]'
sub_techniques: []
tags:
  - EICAR
  - File Uploads
  - Web Applications
  - Anti-Virus
  - Security Testing
commands:
  - '[[commands/create-eicar-test-file]]'
platforms:
  - Web
tools: []
validated: true
---

# Test-Anti-Virus-Using-EICAR-File-Upload

## Summary

This procedure tests for the presence and effectiveness of anti-virus (AV) software on a web server by uploading the standard EICAR test file through a file upload functionality. The EICAR file is a harmless string designed to trigger AV detection without containing actual malware. If the file uploads successfully and remains accessible, it indicates that AV is either absent or not configured to scan uploads; if blocked, AV is likely present and active.

## Description

In web applications, file upload features are common entry points for attackers to introduce malicious payloads. This procedure uses the EICAR test file—a 68-byte string recognized by most AV engines—to safely assess whether server-side AV scanning is enforced on uploaded files. It is particularly useful during penetration testing or red team engagements to discover security controls without risking real malware deployment. The test targets web-based file upload endpoints and verifies post-upload accessibility, helping map the target's defense posture against file-based attacks. This aligns with discovery of security software, as it reveals AV capabilities without exploitation.

## Requirements

1. Access to a web application with a file upload functionality (e.g., authenticated or public upload form).
2. A local testing environment or browser to perform the upload (e.g., Firefox, Chrome, or Burp Suite for interception).
3. Network access to the target server, including the ability to download and access uploaded files.
4. Basic knowledge of the target's file storage path or URL structure for post-upload verification.

## Defense

Defensive measures and detection strategies:

- Implement server-side file scanning with AV tools like ClamAV or Windows Defender integrated into the upload pipeline.
- Enforce file type validation, size limits, and quarantine of suspicious uploads before storage.
- Monitor upload logs for EICAR patterns or anomalous file contents; use WAF rules to block known test strings.
- Enable logging of file access attempts to detect repeated testing behaviors.

## Objectives

1. Determine if AV software is present and scanning uploaded files on the server.
2. Verify if uploaded files are stored and accessible without AV intervention.
3. Identify potential bypass opportunities for malicious file uploads in the target's environment.
4. Document the AV response (block, quarantine, or allow) for further testing.

## Instructions

### Step 1: Create the EICAR Test File

**Context**: Generate the standard EICAR test file locally using a simple command. This file contains a non-malicious string that AV engines detect as a threat, allowing safe testing without downloading from external sources.

**Command** ([[commands/create-eicar-test-file]]):
```bash
echo 'X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*' > eicar.txt
```

> This command creates a file named `eicar.txt` with the exact EICAR string. Verify the file was created by checking its contents: `cat eicar.txt`. The output should match the string exactly, confirming it's ready for upload. This step ensures you control the file creation and avoid any local AV interference during testing.

### Step 2: Upload the EICAR File to the Target

**Context**: Use the web application's file upload feature to submit the EICAR file. This simulates an attacker attempting to introduce a potentially malicious file, testing if server-side AV intercepts it during upload.

**Instructions**: Open the target web application's upload form in a browser. Select the `eicar.txt` file and submit it. If the upload requires authentication, use valid credentials. Note any error messages during submission, such as "file blocked" or "upload successful." For advanced testing, intercept the request with a proxy like Burp Suite to inspect headers and payloads.

> Expected behavior: If AV is active, the upload may fail with a security warning. If successful, the server will return a confirmation or the file's storage path/URL.

### Step 3: Verify File Accessibility Post-Upload

**Context**: Attempt to access the uploaded file via its URL or path to check if AV quarantined, deleted, or allowed it. This reveals whether scanning occurs during storage or retrieval.

**Instructions**: If the upload provided a direct link (e.g., `/uploads/eicar.txt`), navigate to it in the browser or use a tool like curl: `curl http://target.com/uploads/eicar.txt`. Observe the response: successful download indicates no AV block; a 404, 403, or AV warning suggests detection.

> If the file loads and displays the EICAR string, AV is not effectively scanning uploads. If blocked, note the exact error for AV identification (e.g., "Virus detected by ClamAV").
