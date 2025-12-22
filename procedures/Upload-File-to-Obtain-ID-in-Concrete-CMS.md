---
id: proc-concrete-upload-file-id
tags:
  - file-upload
  - concrete-cms
  - web
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
updated_at: '2025-12-14T03:15:31.576Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload-File-to-Obtain-ID-in-Concrete-CMS

## Summary

This procedure involves uploading a benign file to the Concrete CMS file manager to obtain a unique file ID (fID), which is required for subsequent exploitation steps like associating files with malicious filesets.

## Description

In Concrete CMS 5.7.3, the file manager at /dashboard/files allows authenticated users to upload files, assigning each an incremental fID. This ID is used in API calls for file operations, including adding files to sets. The procedure sets up the necessary prerequisite for CSRF-based fileset manipulation by ensuring a valid fID exists. It targets web-based CMS environments and assumes attacker or victim authentication.

## Requirements

1. Authenticated session to Concrete CMS 5.7.3
2. Access to /dashboard/files endpoint
3. A small test file (e.g., empty.txt) for upload

## Defense

Defensive measures and detection strategies:

- Implement file upload size/type restrictions
- Log all file uploads with user IDs and timestamps
- Monitor for unusual file ID usage in subsequent requests

## Objectives

1. Obtain a valid fID for file association
2. Confirm file manager functionality
3. Prepare for fileset addition without raising alerts

## Instructions

### Step 1: Authenticate and Navigate to File Manager

**Context**: Log in to gain access to the dashboard and reach the file upload interface.

No specific command; use browser to visit http://target/conc573/index.php/login, authenticate, then go to http://target/conc573/index.php/dashboard/files.

> Expected: Dashboard loads with file manager visible.

### Step 2: Upload Test File

**Context**: Select and upload a file to trigger ID assignment.

Use the web form to upload a file (e.g., drag-and-drop or browse). Monitor network requests in browser dev tools for the fID in the response.

> Expected: Upload success message; file listed with fID (e.g., 1) in URL like /dashboard/files?fID=1.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- file-upload
- concrete-cms
