---
id: proc-uuid-003
tags:
  - file-read
  - data-exposure
  - web-vuln
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:09.918Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Read-JSON-File-Contents

## Summary

This procedure retrieves and displays the contents of JSON-formatted files from the server using the debug page, enabling unauthorized data access.

## Description

The read function on the debug page parses and shows JSON files directly in the browser, limited to that format but sufficient for extracting configuration or sensitive data stored in JSON.

## Requirements

1. Access to the debug page with uploaded or existing JSON files
2. Web browser
3. Target file in JSON format

## Defense

Defensive measures and detection strategies:

- Restrict read access to authenticated users only
- Encrypt sensitive files and avoid JSON for configs if possible
- Monitor for repeated read requests to debug endpoints

## Objectives

1. View unauthorized file contents
2. Extract data for further analysis or exfiltration
3. Confirm file integrity post-upload

## Instructions

### Step 1: Select File

**Context**: Identify the JSON file to read from the server list.

From the file list on the debug page, select the target JSON file.

> Ensure the file is JSON; non-JSON may not display properly.

### Step 2: Read Contents

**Context**: Trigger the read operation to display the file.

Click the 'Read File Content' button.

> Contents appear in the browser; copy or inspect for sensitive info.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[file-read]]
- [[data-exposure]]
