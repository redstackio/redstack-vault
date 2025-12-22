---
tags:
  - xss
  - upload
  - vtt
  - captions
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: a23b5af9-7c6d-475d-9537-423978d75954
created_at: '2025-12-14T03:16:30.641Z'
updated_at: '2025-12-14T03:16:30.641Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Upload-and-Configure-Malicious-VTT-Captions

## Summary

This procedure involves preparing a Vimeo account, uploading a video, and configuring malicious .vtt captions containing unescaped HTML/JavaScript to set up a stored XSS payload exploitable in the Flash player.

## Description

In the context of Vimeo's video management, users can upload .vtt files for captions/subtitles without proper escaping, allowing injection of script tags. This procedure covers account setup, video upload, and caption configuration to persist the payload. It requires a Vimeo account and targets the Advanced settings tab. Expected outcome is the payload being stored server-side, ready for rendering in vulnerable players.

## Requirements

1. Active Vimeo account with video upload permissions
2. Public or embeddable video (new or existing)
3. Malicious .vtt file (e.g., with `<script>alert(document.domain)</script>` embedded in subtitle text)
4. Web browser access to Vimeo's management interface

## Defense

Defensive measures and detection strategies:

- Implement client-side and server-side sanitization for .vtt content (e.g., escape HTML entities)
- Deprecate Flash support and enforce HTML5 player, which properly escapes content
- Monitor uploads for anomalous .vtt files containing script tags via content scanning
- Rate-limit or validate subtitle uploads to prevent abuse

## Objectives

1. Persist unescaped JavaScript payload in video captions
2. Enable captions for the target language (English)
3. Prepare video for embedding in vulnerable Flash player

## Instructions

### Step 1: Prepare Account and Video

**Context**: Ensure a clean environment by creating a new account or privatizing existing videos to avoid interference.

Navigate to Vimeo and create a new account if needed, or log in and make existing videos private. Then, upload a new video or select an existing public one accessible for embedding.

**Expected Output**: Video ready in management interface.

### Step 2: Access Video Settings and Advanced Tab

**Context**: Reach the captions upload section.

Go to the video's settings page on Vimeo, then click the Advanced tab to open the captions/subtitles section.

**Expected Output**: Advanced settings visible, including 'Add Captions & Subtitles'.

### Step 3: Upload and Enable Malicious VTT

**Context**: Inject the payload via file upload.

Download or prepare the malicious English.vtt file. In the 'Add Captions & Subtitles' section, click 'Choose file', select the .vtt, upload it, toggle status from OFF to ON, select 'English' in Language and 'Captions' in Type, then click 'Save Changes'.

**Expected Output**: Upload succeeds without validation errors; captions enabled and saved.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[upload]]
- [[vtt]]
- [[vimeo]]
