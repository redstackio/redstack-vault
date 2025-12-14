---
id: proc-prepare-vimeo-site-payload-001
tags:
  - xss
  - payload
  - vimeo-com
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:14.337Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Prepare-Payload-for-Vimeo-com-Site

## Summary

This procedure adapts the window.name payload for use on the main vimeo.com site, creating an HTML file with a link to the attacker's video, requiring minimal interaction to trigger.

## Description

Similar to the iframe version, this HTML sets window.name before navigating to vimeo.com/video/ID. The victim clicks the link, plays the video, and upon end, the thumbnail executes the payload. This targets direct site visitors rather than embeds.

## Requirements

1. Text editor.
2. Attacker's video URL on vimeo.com.

## Defense

Defensive measures and detection strategies:

- Validate and escape all rendered user content on the main site.
- Implement referrer checks for suspicious external links.
- Block navigation from pages with tainted window.name.

## Objectives

1. Set payload before site navigation.
2. Enable click-to-trigger XSS.
3. Steal data from direct viewers.

## Instructions

### Step 1: Create HTML Base

**Context**: Set window.name in the file.

Write: `<html><body><script>window.name = 'prompt(document.domain,document.cookie)';</script>`.

### Step 2: Add Video Link

**Context**: Include hyperlink to video.

Add: `<a href="https://vimeo.com/YOUR_VIDEO_ID">Watch video</a>`. Replace ID.

### Step 3: Save File

**Context**: Name it 'name_xss.html'.

Save and verify link works.

**Expected Output**: File ready with functional link.

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
- [[vimeo-com]]
