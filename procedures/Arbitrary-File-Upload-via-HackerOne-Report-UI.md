---
tags:
  - arbitrary-file-upload
  - aws-s3
  - web-vulnerability
  - malware-hosting
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:10.057Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 87c2281a-7c7d-4c8e-87a0-686d98330531
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Arbitrary-File-Upload-via-HackerOne-Report-UI

## Summary

This procedure exploits the absence of file type validation in HackerOne's report submission UI to upload arbitrary files directly to a public AWS S3 bucket, allowing attackers to host malicious content that can be shared to trick users into execution.

## Description

The HackerOne platform's file attachment feature in the vulnerability report submission UI lacks restrictions on file types, content scanning, or sanitization. Files are stored on the public bucket hackerone-attachments.s3.amazonaws.com, accessible via signed URLs. This enables free file hosting and social engineering attacks, where malware can be disguised with benign filenames (e.g., .jpg.exe) to exploit user trust in the domain. The attack requires only basic user access to the platform and can be executed in minutes, with high impact on platform integrity and user safety.

## Requirements

1. Valid HackerOne user account (free registration possible)
2. Web browser with ability to handle file uploads
3. Malicious file prepared (e.g., executable renamed to appear harmless)
4. Internet access to hackerone.com

## Defense

Defensive measures and detection strategies:

- Implement server-side file type validation and content scanning (e.g., using AWS Lambda or ClamAV) before S3 storage
- Restrict S3 bucket permissions to private access with signed URLs expiring quickly
- Monitor upload logs for anomalous file types or patterns (e.g., via AWS CloudTrail)
- Educate users on risks of downloading attachments from reports

## Objectives

1. Upload unrestricted files to public S3 storage
2. Obtain direct public access URLs for shared malicious content
3. Enable social engineering for malware distribution via trusted domain

## Instructions

### Step 1: Prepare Malicious File

**Context**: Create or select a file to upload, disguising it to evade basic checks and entice downloads.

Prepare a payload file, such as a Metasploit-generated executable, and rename it with an innocent extension like "report-evidence.jpg.exe" to appear as an image while hiding the executable nature.

### Step 2: Access and Use Upload Feature

**Context**: Navigate to the UI component that handles file attachments without validation.

Log in to HackerOne, go to the "Submit a Report" section, and use the file attachment field intended for vulnerability evidence. Select the prepared file and submit the form (a dummy report description can be used).

### Step 3: Verify Public Access

**Context**: Confirm the file is stored publicly and accessible to validate exploitation.

After submission, inspect the response or network tab for the AWS S3 signed URL (e.g., https://hackerone-attachments.s3.amazonaws.com/...). Open the URL in a browser to ensure the file downloads without authentication.

> Note: No specific command-line tools are required; this is UI-driven. For automation, browser developer tools or scripts like Selenium could mimic the upload, but manual testing suffices.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[arbitrary-file-upload]]
- [[aws-s3]]
- [[web-vulnerability]]
- [[malware-hosting]]
