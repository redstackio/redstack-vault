---
tags:
  - xss
  - trigger
  - browser-execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/browser-access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:13.984Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: 48770841-c347-46c4-ab6a-de19aaaac886
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-via-File-Access

## Summary

This procedure involves accessing the served directory or file in a web browser, causing the tianma-static server to render the malicious filename and execute the embedded JavaScript payload.

## Description

Once the server is running, HTTP requests to the root path (/) or specific file trigger a directory listing or file serve, where the filename is inserted into HTML without escaping. The payload '<img src=x onerror=alert(1)>' creates an invalid image tag that fires the onerror event, running alert(1). In a real attack, replace with payloads for cookie theft or keylogging. Targets browsers accessing the site; outcomes include full JS execution in victim context, limited by same-origin policy but powerful for client-side attacks.

## Requirements

1. Running tianma-static server on localhost:3000.
2. Malicious file in the served directory.
3. Victim browser (e.g., Chrome, Firefox) with JavaScript enabled.

## Defense

Defensive measures and detection strategies:

- Browser extensions like NoScript or uBlock Origin to block XSS.
- Server-side: Encode filenames in HTML output (e.g., replace < with &lt;).
- Monitor browser console for unexpected alerts or network requests from onload/onerror.
- Educate users on phishing and avoid accessing untrusted static file shares.

## Objectives

1. Render the stored payload in a browser context.
2. Execute arbitrary JavaScript as the victim user.
3. Demonstrate potential for data exfiltration or session manipulation.

## Instructions

### Step 1: Access Server in Browser

**Context**: Navigate to the server's root to list files, triggering the XSS in the listing.

**Command** ([[commands/browser-access]]):
```bash
# Manual: Open browser to http://localhost:3000/
# Or use curl for verification (no JS execution): curl http://localhost:3000/
```

> In a browser, visit http://localhost:3000/. Expected output: Directory listing with filenames; alert(1) pops up due to rendered <img> tag.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/browser-access]]

## Tools Used


## Tags

- [[xss]]
- [[web]]
- [[Execution]]
