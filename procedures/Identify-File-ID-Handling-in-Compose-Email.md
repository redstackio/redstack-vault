---
tags:
  - idor
  - recon
  - web
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:28:28.672Z'
sub_techniques: []
id: 28d95098-1680-43e0-ace2-c514939b28d1
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Identify-File-ID-Handling-in-Compose-Email

## Summary

This procedure involves examining the Lark Compose Email function to identify how file attachments are referenced using alphanumeric IDs, revealing the lack of authorization checks that enables IDOR exploitation.

## Description

In the Lark web application, the Compose Email feature allows users to attach files, but the underlying API uses direct alphanumeric file IDs without verifying user ownership. This procedure uses browser tools to inspect the interface and network traffic, confirming the vulnerability in file reference handling. The target environment is the Lark web platform, requiring an authenticated session. Expected outcomes include understanding the ID format and API endpoints for subsequent manipulation.

## Requirements

1. Authenticated Lark account
2. Web browser with developer tools enabled
3. Basic knowledge of HTTP requests and API inspection

## Defense

Defensive measures and detection strategies:

- Implement server-side authorization checks for all file ID references
- Log and monitor unusual file access patterns across user sessions
- Use indirect object references or encrypted IDs to obscure direct access

## Objectives

1. Locate the Compose Email attachment mechanism
2. Confirm alphanumeric file ID usage without permission validation
3. Prepare for ID manipulation in follow-on steps

## Instructions

### Step 1: Access and Inspect Compose Email

**Context**: Log into Lark and navigate to the email composition area to observe file handling.

Open the Lark web application in a browser, authenticate, and start composing a new email. Attempt to attach a file from your own account and open developer tools (F12) to monitor the Network tab.

> Inspect the outgoing request to the attachment API (e.g., POST /api/v1/compose/attach). Note the file ID parameter, typically an alphanumeric string like 'abc123def456', passed in the request body or query string without additional auth tokens tied to ownership.

**Expected Output**: API request details showing direct file ID usage.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[idor]]
- [[web]]
- [[recon]]
