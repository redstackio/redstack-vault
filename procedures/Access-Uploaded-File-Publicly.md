---
id: proc-access-uploaded-file-publicly
tags:
  - file-access
  - public-exposure
  - web
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-file-retrieve]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T05:32:13.121Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
---
# Access-Uploaded-File-Publicly

## Summary

This procedure demonstrates retrieval of an uploaded file via a predictable public URL, highlighting the lack of access controls and enabling validation of the arbitrary file upload vulnerability's impact.

## Description

After successful upload to an insecure endpoint, files are often stored in web-accessible directories with predictable paths (e.g., based on filename). This procedure targets such exposures on PHP web apps, like the DoD site, where visiting /filename directly serves the content. It confirms public readability, which amplifies risks like XSS or RCE. Requires a prior successful upload.

## Requirements

1. Knowledge of the uploaded filename (e.g., 'delete.me')
2. The base URL of the target (e.g., https://█████████)
3. Browser or curl for retrieval

## Defense

Defensive measures and detection strategies:

- Restrict direct access to upload directories using .htaccess rules or server configurations
- Rename uploaded files with random UUIDs to prevent predictable URLs
- Implement directory listing protections and monitor for direct file access logs

## Objectives

1. Retrieve and view the uploaded file contents publicly
2. Confirm no authentication or authorization is enforced
3. Validate the full vulnerability chain

## Instructions

### Step 1: Construct Predictable URL

**Context**: Based on the upload response or filename, build the access path.

Assume filename 'delete.me'; URL is https://█████████/delete.me.

> Expected output: Ready URL for access.

### Step 2: Retrieve File via Browser or Curl

**Context**: Request the file to check if it's served without restrictions.

**Command** ([[commands/curl-file-retrieve]]):
```bash
curl https://█████████/delete.me
```

> This fetches the file contents. Expected output: Raw response showing 'test file' or similar. In browser, navigate to the URL; contents should display directly.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used

- [[commands/curl-file-retrieve]]

## Tools Used

- [[tools/curl]]

## Tags

- [[file-access]]
- [[public-exposure]]
- [[web]]
