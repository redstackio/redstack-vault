---
id: proc-determine-version
tags:
  - version-detection
  - file-upload
  - telerik-ui
type: procedure
tools:
  - '[[tools/RAU_crypto.py]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/create-test-file]]'
  - '[[commands/loop-through-versions-for-upload]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Client Configurations]]'
updated_at: '2025-12-14T17:23:36.053Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Client Configurations]]'
---
# Determine-Telerik-UI-Version-via-Upload-Attempts

## Summary

This procedure brute-forces the Telerik UI version by attempting encrypted file uploads with [[tools/RAU_crypto.py]] across a list of possible versions, identifying the vulnerable one (e.g., 2016.2.607) that allows successful arbitrary upload under CVE-2017-11317.

## Description

Telerik UI versions use specific encryption keys for the RadAsyncUpload handler. By looping through candidate versions from a file (versions.txt) and attempting uploads to the rau endpoint, the procedure detects success via the presence of 'fileInfo' in the JSON response. This targets ASP.NET applications on Windows, requiring a test file and the RAU_crypto script.

## Requirements

1. List of possible Telerik versions in versions.txt
2. Python 3 environment with RAU_crypto.py
3. Network access to the target endpoint
4. Test file for upload attempts

## Defense

Defensive measures and detection strategies:

- Patch Telerik UI to version 2017.2.621 or later
- Enable encryption key rotation and validation
- Log and alert on multiple failed upload attempts to .axd endpoints

## Objectives

1. Pinpoint the exact vulnerable Telerik version
2. Confirm encryption bypass feasibility
3. Prepare for targeted file upload exploitation

## Instructions

### Step 1: Create Test File

**Context**: Generate a simple text file to use in upload attempts for version detection.

**Command** ([[commands/create-test-file]]):

```bash
echo 'test' > testfile.txt
```

> This creates testfile.txt with 'test' content, serving as a harmless payload for probing uploads.

### Step 2: Loop Through Versions

**Context**: Iterate over versions, attempting encrypted uploads and checking for success indicators.

**Command** ([[commands/loop-through-versions-for-upload]]):

```bash
for VERSION in $(cat versions.txt); do echo -n "$VERSION: " python3 RAU_crypto.py -P 'C:\Windows\Temp' "$VERSION" testfile.txt https://target/apps/XTRAHome/Telerik.Web.UI.WebResource.axd?type=rau 2>/dev/null | grep fileInfo || echo; done
```

> The loop runs RAU_crypto.py for each version, suppressing errors and grepping for 'fileInfo'. Success for the vulnerable version shows JSON output; others are empty.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Client Configurations]] Vulnerability Scanning

### Sub-Techniques


## Commands Used

- [[commands/create-test-file]]
- [[commands/loop-through-versions-for-upload]]

## Tools Used

- [[tools/RAU_crypto.py]]

## Tags

- version-detection
- file-upload
- telerik-ui
