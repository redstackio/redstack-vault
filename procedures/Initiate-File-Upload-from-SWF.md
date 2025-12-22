---
id: p3b2c3d4-e5f6-7890-abcd-ef1234567893
tags:
  - file-upload
  - flash-upload
  - redirect-trigger
type: procedure
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Browser (Google Chrome)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T05:32:09.979Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Initiate File Upload from SWF

## Summary

This procedure triggers the file upload from the loaded SWF to the redirect endpoint, using a 307 or 308 status code to forward the request to the target site without cross-domain validation.

## Description

Once the SWF is loaded, the FileReference.upload() method is called with the redirect URL. The PHP redirect responds with 307/308, causing Chrome to resend the upload to the final target. This exploits Chrome's handling, bypassing Flash's cross-domain policy checks during the redirect follow.

## Requirements

1. Loaded SWF in Chrome from previous step
2. Redirect endpoint configured with 307/308 status
3. A local file for upload (e.g., dummy.txt)

## Defense

Defensive measures and detection strategies:

- Patch Chrome to address Flash redirect handling flaws
- Disable automatic redirect following for uploads in browser policies
- Monitor network traffic for unexpected upload redirects to cross-origin sites

## Objectives

1. Start upload to redirect URL
2. Trigger 307/308 redirect to target
3. Ensure request resends without policy enforcement

## Instructions

### Step 1: Select and Upload File

**Context**: In the SWF, select a file and initiate upload.

No command; SWF handles via user interaction or auto:

```actionscript
fileRef.browse(); // Prompts selection
// After select: fileRef.upload(url);
```

> Upload request hits redirect.php, which redirects with 307.

### Step 2: Verify Redirect Trigger

**Context**: Confirm the redirect occurs.

Use browser dev tools to inspect network:

```javascript
// In console, but SWF-driven; watch for 307 response
```

> Network tab shows initial POST to redirect, then resent to target.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[file-upload]]
- [[flash-upload]]
- [[redirect-trigger]]
