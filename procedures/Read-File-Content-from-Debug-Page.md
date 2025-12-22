---
tags:
  - file-read
  - data-exfiltration
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Local System]]'
updated_at: '2025-12-14T05:32:10.281Z'
sub_techniques: []
id: 7136b7cf-4002-458f-8a87-f61d3408c334
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Local System]]'
---
# Read File Content from Debug Page

## Summary

This procedure retrieves and displays the contents of files via the debug interface, facilitating data exposure especially for JSON files.

## Description

The debug page's 'Read File Content' feature allows selecting and viewing files without restrictions, bypassing normal access controls. This can expose configuration files, logs, or uploaded data in a DoD web app, leading to information disclosure.

## Requirements

1. Uploaded or existing file in the list
2. Debug page access
3. Preference for JSON files for best rendering

## Defense

Defensive measures and detection strategies:

- Disable read functions on debug pages
- Encrypt sensitive files and restrict path access
- Implement content security policies and monitor for anomalous reads

## Objectives

1. Exfiltrate file data
2. Identify sensitive information
3. Validate upload success

## Instructions

### Step 1: Select Target File

**Context**: Choose the file whose contents to view.

From the file list, click on the desired file (e.g., uploaded JSON).

> Selection highlights the file.

### Step 2: Trigger Read

**Context**: Display the file's contents.

Click the 'Read File Content' button.

> Contents appear on the page; JSON formats render cleanly.

**Expected Output**: Raw file data visible in browser.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Data from Local System]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[file-read]]
- [[data-exfiltration]]
