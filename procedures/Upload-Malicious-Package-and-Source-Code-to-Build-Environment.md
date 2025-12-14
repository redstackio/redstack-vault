---
id: proc-002
tags:
  - upload
  - source-code
  - build-environment
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Linux
  - Container
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:30:58.239Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-Malicious-Package-and-Source-Code-to-Build-Environment

## Summary

This procedure uploads the malicious .deb package and backdoor binary alongside legitimate source code to the Semmle build repository, positioning them for access during the prepare step.

## Description

Source code import in Semmle places files at /opt/src/. The .deb (work.deb) and binary (run) are uploaded without validation, allowing them to be referenced in build configs. This step requires authenticated access to the repository but no special privileges.

## Requirements

1. Valid Semmle user account with upload permissions
2. Prepared .deb and binary files
3. Git or direct import mechanism

## Defense

Defensive measures and detection strategies:

- Scan uploads for .deb and binary files; quarantine suspicious ones
- Implement content-type validation on imports
- Log and alert on non-source file uploads

## Objectives

1. Position malicious artifacts in build path
2. Avoid detection during import
3. Ensure files are readable in container

## Instructions

### Step 1: Prepare Upload Bundle

**Context**: Bundle source code with malicious files in repository structure.

Include work.deb and run in the root or src directory.

### Step 2: Import to Semmle Repository

**Context**: Use Semmle interface or API to commit and push.

Push via git: git add . && git commit -m "Update" && git push.

> Expected: Import succeeds, files at /opt/src/ in build env.

### Step 3: Verify Placement

**Context**: Confirm files are staged pre-build.

Check build logs or pre-prepare snapshot for /opt/src/work.deb and /opt/src/run.

**Expected Output**: Files listed in environment.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- upload
- source-code
- build-environment
