---
id: proc-retrieve-uploaded-file
tags:
  - file-retrieval
  - public-access
  - verification
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:10.329Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Retrieve and Verify Uploaded File

## Summary

This procedure accesses the publicly stored uploaded file via a predictable path to confirm successful exploitation and demonstrate public retrievability, highlighting risks like XSS or content hosting.

## Description

Following the upload, files are stored in a web-accessible directory on the PHP server, allowing direct retrieval. For the DoD vulnerability, accessing /delete.me verifies control over hosted content, enabling further attacks like embedding malicious scripts.

## Requirements

1. Known path from upload response (e.g., /delete.me)
2. Browser access to the target domain
3. Original file for content comparison

## Defense

Defensive measures and detection strategies:

- Restrict upload directories to non-public paths
- Implement access controls on uploaded file retrieval
- Use content security policies (CSP) to mitigate XSS from hosted files
- Log and alert on direct access to upload directories

## Objectives

1. Confirm public accessibility of uploaded files
2. Verify file integrity and content
3. Illustrate potential for malicious exploitation

## Instructions

### Step 1: Construct Access URL

**Context**: Use the leaked path to form the full retrieval URL.

Based on the success message, navigate to https://██████████/delete.me.

> The path is predictable and public, bypassing any checks.

### Step 2: Verify Content

**Context**: Download or view the file to ensure it matches the upload.

Open the URL in a browser; the file (e.g., image) should render or download.

> Compare content hash or visual/text to confirm no alterations.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[file-retrieval]]
- [[public-access]]
- [[verification]]
