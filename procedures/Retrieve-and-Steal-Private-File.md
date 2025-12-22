---
tags:
  - idor
  - exfiltration
  - web
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:28.662Z'
sub_techniques: []
id: 6d2e7753-aa2c-4cf3-86a2-d1e038bb1b5e
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Retrieve-and-Steal-Private-File

## Summary

This procedure captures and exfiltrates the content of a private file accessed via the IDOR exploit in Lark's Compose Email function, enabling theft of sensitive data.

## Description

Following successful manipulation, the API response includes the unauthorized file's data. This procedure focuses on extracting and saving that content, which could include documents, images, or other private assets. Targeted at the web platform, it requires capturing the response in real-time. The outcome is local possession of stolen data, with potential for further misuse like data leakage or analysis.

## Requirements

1. Successful prior manipulation step
2. Ability to view and save HTTP responses
3. Local storage for exfiltrated files

## Defense

Defensive measures and detection strategies:

- Encrypt sensitive file contents and enforce decryption only after auth
- Audit logs for file access discrepancies and automate alerts
- Implement data loss prevention (DLP) scanning on API responses

## Objectives

1. Capture the full file content from the response
2. Download or copy the data securely
3. Verify the theft of private information

## Instructions

### Step 1: Capture and Save Response Data

**Context**: Extract the file from the server's unauthorized response.

After sending the manipulated request, inspect the API response in developer tools. The body will contain the file content (e.g., base64-encoded or direct binary). Copy the data and decode/save it locally, or if a download link is provided, initiate the download to obtain the file.

> Without ownership checks, the response delivers the complete private file, confirming the IDOR impact.

**Expected Output**: Saved file matching the target private document.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[idor]]
- [[Exfiltration]]
- [[web]]
