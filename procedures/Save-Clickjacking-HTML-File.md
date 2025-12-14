---
tags:
  - clickjacking
  - html
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:12.817Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: dd05945b-3606-4ee0-817e-08409a760ce8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Save-Clickjacking-HTML-File

## Summary

This procedure saves the created HTML PoC as a file with .html extension, preparing it for browser execution and distribution.

## Description

Saving the file ensures the iframe code is persisted locally. In an attack scenario, this file can be hosted on a web server or sent directly to victims. The target environment is any OS with file system access; expected outcome is a runnable HTML file demonstrating the embedding.

## Requirements

1. Text editor with save functionality
2. Write permissions in a local directory
3. The HTML content from the creation procedure

## Defense

Defensive measures and detection strategies:

- Educate users on avoiding unknown HTML attachments
- Scan emails for .html files with iframe tags
- Endpoint detection for suspicious file saves

## Objectives

1. Persist the PoC HTML file
2. Ensure file is executable in browsers
3. Prepare for distribution to victims

## Instructions

### Step 1: Select Save Option

**Context**: Use the text editor's save feature to create the file.

In the text editor, go to File > Save As.

### Step 2: Name and Extension

**Context**: Choose a filename and ensure .html extension.

Enter a name like "clickjack-demo.html" and select All Files to avoid .txt extension.

> This step confirms the file is saved as HTML, allowing browser rendering.

### Step 3: Choose Location

**Context**: Save in an accessible directory.

Select a local folder like Desktop or Documents.

**Expected Output**: File saved successfully, size around 200 bytes.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[file-save]]
- [[poc]]
