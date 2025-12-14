---
tags:
  - ssrf
  - javascript-execution
  - path-revelation
  - ios
  - nextcloud
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - iOS
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:40.119Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 08cf400f-af63-4e6b-993f-f9d0699b3cdb
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Access-Manipulated-HTML-to-Reveal-App-Path

## Summary

This procedure views an uploaded HTML file in the Nextcloud iOS app to trigger JavaScript execution, disclosing the application's local storage path for SSRF preparation.

## Description

By opening the previously uploaded HTML file containing `<svg/onload=document.write(document.location)>` in the app's file viewer, this step leverages the lack of JS sanitization to execute code that outputs the current document's location. This reveals the app's sandboxed path, essential for constructing file:// URIs to access local files like the proof-of-concept. The attack scenario assumes prior upload; outcomes include the exact path string, e.g., 'file:///private/var/mobile/Containers/Data/Application/[GUID]/Documents/', facilitating data exfiltration.

## Requirements

1. Uploaded HTML file from path discovery procedure
2. Nextcloud iOS app file viewer access
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Render uploaded files in a secure, JS-disabled viewer
- Implement content security policies (CSP) in web views
- Detect and block document.write or location access attempts

## Objectives

1. Trigger JS to output the app path
2. Capture the path for SSRF payload crafting
3. Validate execution without app interruption

## Instructions

### Step 1: View the File

**Context**: Open the HTML to execute the embedded script.

Navigate to the uploaded 'pathfinder.html' in the Nextcloud app and select to view it.

### Step 2: Capture Output

**Context**: Read the executed result displaying the path.

Observe the viewer rendering the JavaScript output, which writes the full local path to the page.

**Expected Output**: Path string visible, e.g., 'file:///private/var/mobile/.../Documents/'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[javascript-execution]]
- [[path-revelation]]
- [[ios]]
- [[nextcloud]]
