---
id: proc-uuid-001
tags:
  - setup
  - quicklink
  - file-creation
type: procedure
tools:
  - '[[tools/curl]]'
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
updated_at: '2025-12-14T17:29:44.492Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Test-Files-and-Generate-QuickLink

## Summary

This procedure sets up test files and folders in Files.com with shared prefixes and generates a public QuickLink for one file, preparing the environment for access control testing.

## Description

In the Files.com platform, create specific files and a subdirectory to simulate a real file system. Share one file via QuickLink to obtain a bundle code, which will be used to test prefix-based access flaws. This targets web-based file sharing services vulnerable to improper path validation.

## Requirements

1. Authenticated access to Files.com dashboard
2. Ability to upload/create files and folders
3. Web browser or API access for sharing

## Defense

Defensive measures and detection strategies:

- Enforce exact path matching in access controls
- Log all QuickLink access attempts with path parameters
- Monitor for anomalous file downloads from shared links

## Objectives

1. Establish test environment with prefix-sharing files
2. Generate valid QuickLink for exploitation setup
3. Verify initial bundle isolation

## Instructions

### Step 1: Create Test Files

**Context**: Upload files to mimic shared and unshared content.

Log in to Files.com and create:
- File: '1bar'
- File: 'foo'
- File: 'footer.php'
- Folder: 'foobar/' with file 'secret' inside

**Expected Output**: Files and folder visible in the file manager.

### Step 2: Generate QuickLink

**Context**: Share 'foo' to get the public bundle.

Select 'foo' and click 'Copy Public QuickLink'.

**Expected Output**: URL like https://pwn.brickftp.com/f/23a17148e with code '23a17148e'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/curl]]

## Tags

- [[setup]]
- [[quicklink]]
