---
tags:
  - verification
  - file-creation
  - windows
type: procedure
tools:
  - '[[tools/IRB]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/dir-verify-file-creation]]'
platforms:
  - Windows
  - Ruby
techniques:
  - '[[File and Directory Discovery]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 8456696d-8204-41a1-a096-a78c62dea5f6
created_at: '2025-12-14T17:26:22.904Z'
updated_at: '2025-12-14T17:26:22.904Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Verify Arbitrary File Creation

## Summary

This procedure confirms the success of the path traversal by listing the target directory contents to check for the maliciously created file.

## Description

After exploiting Tempfile.open, use Windows dir command via Ruby backticks in IRB to inspect C:\Users\rootx\ for the placed file (e.g., malicious20210321-22472-fvuodx.rb). This verifies the traversal worked and the file is in an arbitrary location, highlighting the vulnerability's impact.

## Requirements

1. Successful execution of prior Tempfile.open step
2. IRB session active
3. Permissions to execute system commands in Ruby

## Defense

Defensive measures and detection strategies:

- Enable file system auditing on Windows to log unexpected creations in user directories
- Use application-level logging for Tempfile operations
- Scan for anomalous .rb files in non-temp locations

## Objectives

1. Confirm file placement outside temp directory
2. Validate exploit success through directory listing
3. Identify potential RCE vectors

## Instructions

### Step 1: Execute Dir Command in IRB

**Context**: Run the Windows dir command via backticks to list the target directory and spot the created file.

**Command** ([[commands/dir-verify-file-creation]]):
```ruby
puts `dir C:\\Users\\rootx\\`
```

> This executes 'dir C:\Users\rootx\' and prints the output. Expected output includes the malicious file entry like '21-03-2021 00:45 0 malicious20210321-22472-fvuodx.rb'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/dir-verify-file-creation]]

## Tools Used

- [[tools/IRB]]

## Tags

- verification
- file-creation
- windows
