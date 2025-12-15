---
tags:
  - ssrf
  - iframe
  - local-file
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
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:24:40.116Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 0835be99-b870-47a3-a5ed-810307b21c75
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Data from Local System]]'
---
# Upload-HTML-with-Iframe-for-Local-File-SSRF

## Summary

This procedure uploads an HTML file to the Nextcloud iOS app containing an iframe that uses the file:// protocol to reference a local proof file, setting up SSRF for content disclosure.

## Description

Building on the discovered app path, this step crafts an HTML file with `<iframe src="file://[PATH]/ssrfpoc.txt" width="400" height="400"></iframe>`, where [PATH] is the base directory from prior reconnaissance. The upload exploits the same validation gaps, allowing the iframe to load local resources when viewed. This enables SSRF to bypass sandbox restrictions and fetch arbitrary files. Prerequisites: known path and proof file; outcomes prepare for direct data exposure.

## Requirements

1. Discovered app path from previous procedure
2. Existing proof file 'ssrfpoc.txt' in local storage
3. Text editor for payload creation

## Defense

Defensive measures and detection strategies:

- Validate and strip iframe tags or file:// schemes in uploaded content
- Enforce strict origin policies in app web views
- Scan for protocol abuse in file metadata or content

## Objectives

1. Upload SSRF-enabling HTML with targeted iframe
2. Ensure payload uses correct local path
3. Position for file content loading

## Instructions

### Step 1: Build the Payload

**Context**: Insert the iframe referencing the proof file path.

Edit a new file to HTML: `<iframe src="file://[FULL-PATH-FROM-STEP-3]/ssrfpoc.txt" width="400" height="400"></iframe>`, substituting the exact path.

### Step 2: Perform Upload

**Context**: Add the SSRF file to local storage.

Upload the HTML file (e.g., 'ssrf-iframe.html') via the app's interface.

**Expected Output**: File stored successfully, ready for viewing.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Data from Local System]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[iframe]]
- [[local-file]]
- [[ios]]
- [[nextcloud]]
