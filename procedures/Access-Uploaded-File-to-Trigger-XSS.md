---
id: proc-mopub-trigger-xss-001
tags:
  - xss
  - stored-xss
  - payload-execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-access-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:20.368Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Access-Uploaded-File-to-Trigger-XSS

## Summary

This procedure accesses the URL of the uploaded malicious HTML file on images.mopub.com, causing the server to serve it as content and execute the embedded JavaScript, confirming stored XSS.

## Description

After successful upload, the file is stored under /app_icons/[hash] and served without MIME enforcement, leading to JS execution in any browser viewing the URL. This can impact users or admins accessing the 'image', enabling attacks like session theft. Requires the URL from the upload response.

## Requirements

1. Valid upload URL from previous step (e.g., https://images.mopub.com/app_icons/[hash])
2. Web browser or curl for access
3. No special authentication for image domain

## Defense

Defensive measures and detection strategies:

- Enforce image MIME types and content scanning on storage/serve
- Block script tags in uploaded files
- Monitor access logs for non-image responses on image endpoints

## Objectives

1. Execute stored JavaScript payload
2. Demonstrate arbitrary code execution
3. Highlight impact on viewers of the URL

## Instructions

### Step 1: Retrieve Upload URL

**Context**: Note the hashed URL from the server response.

From the upload response, copy the location like https://images.mopub.com/app_icons/126cb3308e1a464385a49c4c7aaeac56.

> This URL serves the file directly.

### Step 2: Access and Execute

**Context**: Load the URL to trigger XSS.

Open the URL in a browser, or use [[commands/curl-access-url]] to fetch:

```bash
curl -v https://images.mopub.com/app_icons/126cb3308e1a464385a49c4c7aaeac56
```

> Browser will render HTML and run <script>alert('XSS')</script>; curl shows HTML response.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-url]]

## Tools Used


## Tags

- xss-trigger
- js-execution
