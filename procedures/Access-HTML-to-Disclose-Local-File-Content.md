---
tags:
  - ssrf
  - file-disclosure
  - local-access
  - ios
  - nextcloud
type: procedure
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
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:24:40.113Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 097e1a3f-b962-4058-943a-e92c3cac4080
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Access-HTML-to-Disclose-Local-File-Content

## Summary

This procedure views an uploaded HTML iframe file in the Nextcloud iOS app to exploit SSRF, loading and displaying the content of a targeted local file.

## Description

Viewing the iframe HTML triggers the src attribute to make a file:// request to the proof file's path, bypassing restrictions due to inadequate protocol validation in the app's viewer. This results in the iframe rendering the local file's content (e.g., 'test ssrf'), proving arbitrary local disclosure. The scenario completes the SSRF chain; outcomes include visible sensitive data, scalable to any local document or system file.

## Requirements

1. Uploaded iframe HTML from SSRF upload procedure
2. Valid local path and target file existence
3. App viewer capable of rendering iframes

## Defense

Defensive measures and detection strategies:

- Block file:// and other local protocols in web view configurations
- Use isolated rendering engines for user-uploaded content
- Implement runtime monitoring for cross-origin or local resource fetches

## Objectives

1. Execute iframe to fetch local file via SSRF
2. Display proof file content as validation
3. Demonstrate potential for broader data exfiltration

## Instructions

### Step 1: Open the File

**Context**: Trigger the iframe load in the viewer.

Select and view 'ssrf-iframe.html' in the Nextcloud app.

### Step 2: Observe Disclosure

**Context**: Confirm SSRF success through content rendering.

The iframe should load and show the content of 'ssrfpoc.txt' within its frame.

**Expected Output**: 'test ssrf' displayed in the 400x400 iframe area.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Local System]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[file-disclosure]]
- [[local-access]]
- [[ios]]
- [[nextcloud]]
