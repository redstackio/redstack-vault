---
tags:
  - access-bypass
  - file-upload
  - hackerone
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/curl-upload-attachment-to-scoping-form]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T05:32:13.644Z'
sub_techniques: []
id: 242f2fb1-60d9-4087-b7e4-f4d4da50bc45
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---
# Upload-Attachment-to-Foreign-Form

## Summary

This procedure exploits the /attachments endpoint on HackerOne by sending a POST request with a known form ID (tracer) from an unauthorized account, allowing attachment of files to foreign scoping forms without validation.

## Description

The vulnerability stems from the endpoint only requiring authentication and the form ID, without checking user ownership or org membership. This business logic flaw enables any authenticated user to modify forms via attachments, potentially introducing malicious content. The request uses multipart form data with 'tracer' for the form ID, 'context_type' as 'PentestOpportunity', and the file.

## Requirements

1. Extracted form ID (tracer) from the target scoping form
2. Authenticated session cookies from the second account
3. A test file (e.g., PNG image) for upload
4. curl or equivalent HTTP client

## Defense

Defensive measures and detection strategies:

- Add ownership validation in the /attachments endpoint (e.g., check user-form association)
- Log all attachment uploads with form ID and user details for anomaly detection
- Restrict uploads to same-org or owned forms only

## Objectives

1. Bypass access controls to attach files to unauthorized forms
2. Demonstrate business logic error in attachment handling
3. Introduce potential malicious content to compromise integrity

## Instructions

### Step 1: Prepare the Request

**Context**: Gather parameters for the multipart POST.

**Command** (Manual Prep):

Set tracer to the form ID (e.g., 989953fa-5635-43c9-b584-48736d224b15), context_type to 'PentestOpportunity', and select a file.

> Ensure cookies are from the second account session.

### Step 2: Execute Upload

**Context**: Send the unauthorized attachment request.

**Command** ([[commands/curl-upload-attachment-to-scoping-form]]):

```bash
curl -X POST https://hackerone.com/attachments \
  -H "Cookie: your_session_cookies" \
  -F "tracer=989953fa-5635-43c9-b584-48736d224b15" \
  -F "context_type=PentestOpportunity" \
  -F "file=@test-file.png"
```

> The command uploads the file; success is indicated by a 2xx response with attachment metadata.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/curl-upload-attachment-to-scoping-form]]

## Tools Used


## Tags

- [[access-bypass]]
- [[file-upload]]
- [[hackerone]]
