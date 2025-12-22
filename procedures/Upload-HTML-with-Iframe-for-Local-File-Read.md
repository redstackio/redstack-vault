---
tags:
  - ssrf
  - iframe
  - file-read
  - nextcloud
  - ios
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - iOS
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T04:39:09.534Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 0ca44e48-5804-48b2-81a5-bf6748567c7b
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# Upload-HTML-with-Iframe-for-Local-File-Read

## Summary

This procedure uploads an HTML file containing an iframe that targets a local file via file:// protocol, exploiting SSRF in Nextcloud iOS local storage for arbitrary file disclosure.

## Description

Using the app path from prior discovery, this step crafts an iframe src to load a specific local file (e.g., the test ssrfpoc.txt). The HTML is disguised and uploaded, leveraging the app's failure to sanitize file:// requests. In the attack, this positions the payload for content exfiltration. Prerequisites: Known app path and test file existence. Outcomes: Successful upload, ready for SSRF trigger.

## Requirements

1. Revealed application path from previous step
2. Target local file (e.g., ssrfpoc.txt) in app directory
3. HTML payload: <iframe src="file://[path]/ssrfpoc.txt" width="400" height="400"></iframe>

## Defense

Defensive measures and detection strategies:

- Block file:// protocol in all embedded content
- Validate and restrict iframe sources
- Scan uploads for iframe and protocol abuse

## Objectives

1. Upload iframe payload targeting local file
2. Bypass protocol sanitization
3. Enable SSRF-based file content loading

## Instructions

### Step 1: Prepare Iframe HTML Payload

**Context**: Construct the SSRF payload using the known path.

Create a file with `<iframe src="file://[revealed-path]/ssrfpoc.txt" width="400" height="400"></iframe>`, disguising extension as .txt.

> Replace [revealed-path] with the actual app path.

### Step 2: Upload the Payload

**Context**: Store the file in local storage for later access.

Use the app's upload feature to add the iframe HTML file.

> Expected output: File uploads and is listed without issues.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[iframe]]
- [[file-read]]
- [[nextcloud]]
- [[ios]]
