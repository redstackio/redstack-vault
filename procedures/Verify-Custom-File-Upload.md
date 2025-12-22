---
tags:
  - verification
  - file-retrieval
  - parameter-exploitation
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[File and Directory Discovery]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: be028dab-780b-46e3-bb46-2aa8cf4dab09
created_at: '2025-12-14T05:32:10.172Z'
updated_at: '2025-12-14T05:32:10.172Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Verify-Custom-File-Upload

## Summary

This procedure retrieves and inspects the uploaded file using the custom 'imgnum' value to confirm the bypass success, ensuring the server accepted the tampered upload and stored it with the intended name.

## Description

After tampering, LISTSERV stores logos accessibly via wa.cgi with the imgnum query parameter. This step constructs the retrieval URL using the session's Y parameter and downloads the file for forensic check of appended data. Target: Browser or wget for download. Prerequisites: Successful upload and known Y/imgnum values. Outcomes: Proof of bypass, visible custom naming, and validation for DoS escalation.

## Requirements

1. Browser or download tool
2. Session Y parameter from upload response
3. Text/hex editor for inspection

## Defense

Defensive measures and detection strategies:

- Log all wa.cgi accesses with imgnum; flag non-numeric values
- Restrict file retrieval to authenticated sessions only
- Scan uploaded files for anomalies like trailing text

## Objectives

1. Confirm server-side acceptance of arbitrary imgnum
2. Validate custom naming and payload integrity
3. Identify if bypass enables further exploitation

## Instructions

### Step 1: Build Retrieval URL

**Context**: Use tampered imgnum in the access endpoint.

No command; URL construction:

Format: http://█████/scripts/wa.cgi?VL&Y=9e44b517&imgnum=cow

> Expected output: Valid URL string. Success if parameters match session.

### Step 2: Access and Download File

**Context**: Fetch the uploaded logo.

No command; browser navigation:

Enter URL in browser; right-click image and save as file.

> Expected output: Image loads or downloads. Success if no 404/403.

### Step 3: Inspect File Contents

**Context**: Check for appended value to prove tampering.

No command; editor open:

Open downloaded file in Notepad++ or hex editor; scroll to end.

> Expected output: Image data ends with 'cow'. Success if append visible without corruption.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
- [[file-retrieval]]
