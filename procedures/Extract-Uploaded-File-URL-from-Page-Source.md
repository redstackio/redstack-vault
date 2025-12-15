---
tags:
  - source-code-analysis
  - path-discovery
  - web
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T17:23:27.922Z'
sub_techniques: []
id: 6a4b3117-ea99-4f68-acc1-6ce5ee168dac
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Extract-Uploaded-File-URL-from-Page-Source

## Summary

This procedure involves inspecting the HTML source of the post-upload page to locate the full server path of the uploaded file.

## Description

After upload, the application often embeds the file path in the page's HTML (e.g., as an <img src> attribute). Viewing source reveals the exact URL, confirming the file's web-accessible location for execution.

## Requirements

1. Successful upload completion
2. Web browser developer tools or view source capability
3. Uploaded file reference in page

## Defense

Defensive measures and detection strategies:

- Obfuscate or randomize upload paths to hinder discovery
- Avoid embedding raw paths in client-side HTML
- Log access to upload directories for anomalies

## Objectives

1. Identify the stored file's URL
2. Confirm web accessibility
3. Prepare for direct access

## Instructions

### Step 1: Load Post-Upload Page

**Context**: Ensure the page refreshes to include the new profile photo reference.

Submit the upload and wait for the page to update.

### Step 2: View Page Source

**Context**: Inspect HTML for file path.

Right-click page > 'View Page Source' (or Ctrl+U), search for 'upload' or file extension.

### Step 3: Locate Full URL

**Context**: Extract the complete path.

Find element like <img src="/uploads/shell.php"> and note the absolute URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[System Information Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- source-code-analysis
- path-discovery
