---
tags:
  - malware-prep
  - file-upload
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:29:44.625Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 6988d0d4-598f-4736-9abd-803b099e4787
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Prepare-Malicious-SCORM-Package

## Summary

This procedure involves crafting or obtaining a SCORM-compliant ZIP package embedded with an ASPX webshell, which will be extracted and executed on the server post-upload.

## Description

SCORM packages are ZIP files with a specific structure, including imsmanifest.xml. The malicious variant includes an ASPX file (cdlcdlcdl.aspx) in the shared/ directory that executes system commands like whoami when accessed. The server extracts without validation, deploying the shell under /CServer/Courseware/<ID>/.

## Requirements

1. Knowledge of SCORM 2004 structure
2. ASP.NET webshell code (e.g., simple cmd executor)
3. ZIP tool to package files

## Defense

Defensive measures and detection strategies:

- Validate SCORM packages against schema before extraction
- Scan uploads for executable content (e.g., .aspx)
- Restrict extraction to non-executable directories

## Objectives

1. Create valid SCORM ZIP with hidden payload
2. Ensure shell references in manifest for deployment
3. Test package integrity locally

## Instructions

### Step 1: Craft Webshell

**Context**: Develop the ASPX file to execute commands.

Create cdlcdlcdl.aspx with code to run [[commands/whoami]] and display output.

> Expected output: Functional shell file ready for embedding.

### Step 2: Build SCORM Structure

**Context**: Assemble ZIP with manifest referencing the shell.

Place shell in shared/ and update imsmanifest.xml to include it.

> Expected output: ZIP file named e.g., malicious_scorm.zip.

### Step 3: Validate Package

**Context**: Ensure the package mimics legitimate SCORM.

Unzip and verify structure without errors.

> Expected output: Valid imsmanifest.xml and shell path.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used

- [[commands/whoami]]

## Tools Used


## Tags

- malware-prep
- file-upload
