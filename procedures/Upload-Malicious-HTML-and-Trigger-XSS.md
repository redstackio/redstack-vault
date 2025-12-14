---
tags:
  - xss
  - execution
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-trigger-xss]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:25.261Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: f7976a2c-7ae0-4dff-b9c4-cbbb78577a90
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Upload-Malicious-HTML-and-Trigger-XSS

## Summary

This procedure completes the upload of the manipulated HTML file and triggers the stored XSS by loading the file on the s2.booth.pm domain, executing arbitrary JavaScript in the victim's browser.

## Description

After bypassing validation, the server stores the HTML file and serves it from the sandboxed domain s2.booth.pm without proper MIME enforcement, causing browsers to render it as HTML and run the embedded script. This leads to stored XSS, where any user viewing the affected design page executes the payload. Prerequisites include a successful bypass from prior steps. The impact includes potential data theft or session hijacking via the JS.

## Requirements

1. Successful upload from previous procedure
2. Knowledge of the stored file URL (typically constructed as https://s2.booth.pm/path/to/file)
3. Victim browser to load the page

## Defense

Defensive measures and detection strategies:

- Serve uploaded files with strict Content-Disposition: attachment or no-sniff headers
- Sandbox uploads to isolated domains with CSP enforcing no JS
- Scan stored files for script tags and reject/quarantine suspicious content

## Objectives

1. Confirm file storage and accessibility
2. Execute the XSS payload in a browser context
3. Demonstrate impact on victims loading the malicious resource

## Instructions

### Step 1: Submit Upload Request

**Context**: Finalize the upload using the manipulated headers.

**Command** ([[commands/curl-trigger-xss]]):
```bash
curl -X POST https://manage.booth.pm/design/edit -H "Cookie: session=your_session_cookie" -H "Content-Type: multipart/form-data" --form "header_image=@malicious.html" --form "submit=Upload" -v
```

> Adjust based on form; expected output: Success message or redirect, file ID in response.

### Step 2: Locate and Load Stored File

**Context**: Find the served URL and access it to trigger execution.

**Instructions**: After upload, inspect the design page source or API response for the image src attribute pointing to s2.booth.pm. Open that URL in a browser.

> The file loads as HTML, running the <script> tag. Expected: Alert or console log confirming JS execution on s2.booth.pm domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-trigger-xss]]

## Tools Used


## Tags

- [[xss]]
- [[Execution]]
