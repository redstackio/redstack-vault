---
id: 3642ea6b-1a6a-4508-9e38-9bf9bc4c98f1
name: Large File Upload - Disk Denial of Service
type: procedure
verified: true
submitted: true
created_at: '2020-08-17T19:32:40.732456+00:00'
updated_at: '2023-05-26T01:15:28.652033+00:00'
tactics:
  - '[[Impact]]'
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
sub_techniques: []
tags:
  - denial-of-service
  - dos
  - file-uploads
  - web-applications
commands:
  - '[[commands/dd-generate-large-file]]'
  - '[[commands/curl-file-upload]]'
platforms:
  - Web
tools:
  - '[[tools/cURL]]'
skill_level: beginner
impact_level: high
detection_risk: high
validated: true
---

# Large File Upload - Disk Denial of Service

## Summary

This procedure demonstrates how to perform a disk-based denial of service attack by uploading large files through a web application's file upload functionality. By repeatedly uploading oversized files of an allowed type, an attacker can exhaust the server's disk space, leading to service degradation or complete unavailability.

## Description

Web applications often include file upload features without strict size limits or rate throttling, making them vulnerable to resource exhaustion attacks. This technique targets disk storage by flooding the server with large files, such as PDFs or images, until the available space is depleted. The attack is effective against applications hosted on resource-constrained environments and can cause failures in file processing, database writes, or other disk-dependent operations. It requires only unauthenticated access to the upload endpoint and knowledge of accepted file types. Success depends on the server's disk quota and monitoring; repeated uploads amplify the impact.

## Requirements

1. Access to a web application with file upload functionality (no authentication required in many cases).
2. Knowledge of accepted file types (e.g., PDF, JPG) and upload endpoint URL.
3. Tools for generating large files and performing HTTP uploads (e.g., dd and curl on Linux).
4. Network connectivity to the target server.

## Defense

Defensive measures and detection strategies:

- Implement file size limits (e.g., <10MB per upload) and rate limiting on upload endpoints.
- Monitor disk usage and upload logs for anomalous large file patterns; use tools like fail2ban for automated blocking.
- Store uploads in isolated, quota-enforced directories or cloud storage with built-in limits (e.g., AWS S3).
- Enable web application firewall (WAF) rules to detect and block excessive upload attempts.

## Objectives

1. Generate a large file that complies with the application's accepted types to bypass basic validation.
2. Upload the file to the target endpoint, confirming successful storage on the server.
3. Repeat the process multiple times to exhaust disk space and verify DoS impact.
4. Observe server responses for signs of degradation, such as upload failures or timeouts.

## Instructions

### Step 1: Generate a Large Test File

**Context**: Create a large dummy file (e.g., 200MB PDF-like) using system tools to simulate a legitimate upload without needing actual content. This ensures the file is of an accepted type and size to trigger disk exhaustion without immediate rejection.

**Command** ([[commands/dd-generate-large-file]]):
```bash
dd if=/dev/zero of=largefile.pdf bs=1M count=200
```

> This command generates a 200MB file filled with zeros, named 'largefile.pdf' to mimic a PDF. Adjust 'count' for larger sizes if needed. The file type extension helps bypass MIME checks, but verify against the target's validation.

### Step 2: Upload the Large File to the Target

**Context**: Use an HTTP client to POST the file to the application's upload endpoint. This step confirms the file is accepted and stored on disk. Monitor the response for success indicators like a confirmation message or file ID.

**Command** ([[commands/curl-file-upload]]):
```bash
curl -X POST -F "file=@largefile.pdf" http://target.com/upload-endpoint
```

> Replace 'http://target.com/upload-endpoint' with the actual URL. The '-F' flag handles multipart form data for file uploads. Expected success: HTTP 200 OK with a message like "File uploaded successfully." If rejected, check size limits or file type.

### Step 3: Repeat Uploads to Exhaust Disk Space

**Context**: Automate or manually repeat the upload process multiple times to fill the server's disk. Track the number of successful uploads and monitor for errors indicating space exhaustion, such as 500 errors or "disk full" messages.

**Instructions**: Run the upload command from Step 2 in a loop (e.g., via a bash script: for i in {1..10}; do curl ...; done). After 5-10 uploads, test the application for functionality (e.g., attempt a small upload or page load) to confirm DoS.

> No specific command here; reuse [[commands/curl-file-upload]]. Expected output on failure: Server errors like "No space left on device" or timeouts.
