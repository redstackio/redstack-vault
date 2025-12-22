---
tags:
  - ssrf
  - javascript
  - path-discovery
  - ios
  - nextcloud
type: procedure
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - iOS
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:40.121Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: a972bb28-a5be-4f2f-a3dc-c053603382c6
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Discover-Application-Path-via-JavaScript-in-Uploaded-HTML

## Summary

This procedure manipulates an uploaded file in the Nextcloud iOS app to HTML format containing JavaScript that discloses the application's local path when viewed, enabling targeted SSRF attacks.

## Description

Targeting the unsanitized file upload and viewing in Nextcloud iOS, this step involves modifying a common file (e.g., .txt) to include HTML with the payload `<svg/onload=document.write(document.location)>`. Upon upload and viewing, the JavaScript executes in the app's web view, revealing the full path to the app's documents directory (e.g., /private/var/mobile/Containers/Data/Application/[ID]/Documents/). This path is crucial for crafting precise file:// URIs in follow-on SSRF exploits. Prerequisites include app access; outcomes provide reconnaissance data for local file targeting.

## Requirements

1. Nextcloud iOS app with upload access
2. Text editor to craft the HTML payload
3. Knowledge of the proof file from prior steps

## Defense

Defensive measures and detection strategies:

- Sanitize uploaded files to strip HTML/JS elements before storage
- Disable JavaScript execution in the app's file viewer component
- Log and alert on script execution in local viewers

## Objectives

1. Execute JavaScript via uploaded content to gather path information
2. Identify the base directory for local SSRF
3. Enable precise targeting of local resources

## Instructions

### Step 1: Craft the Manipulated File

**Context**: Convert a standard file to HTML with a path-disclosing payload.

Create or edit a file (e.g., 'pathfinder.txt') and replace its content with: `<svg/onload=document.write(document.location)>`. Save it with a .html extension if possible, or rely on content type for execution.

### Step 2: Upload the File

**Context**: Store the payload in local storage for later execution.

In the Nextcloud iOS app, upload 'pathfinder.html' via the local files interface.

**Expected Output**: Upload succeeds, file is listed without content rejection.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[JavaScript]]
- [[path-discovery]]
- [[ios]]
- [[nextcloud]]
