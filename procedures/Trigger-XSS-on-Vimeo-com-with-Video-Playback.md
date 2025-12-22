---
id: proc-trigger-vimeo-site-xss-001
tags:
  - xss
  - video-playback
  - vimeo
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
updated_at: '2025-12-14T03:16:14.335Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-on-Vimeo-com-with-Video-Playback

## Summary

This procedure triggers the XSS on vimeo.com by navigating via the prepared HTML, clicking to watch, playing the video, and waiting for the thumbnail to execute the payload with minimal interaction.

## Description

From the HTML file, clicking the link carries the window.name to vimeo.com. Playing the short video leads to thumbnail display after 10 seconds, injecting the SVG and evaluating the payload for cookie theft. This requires two interactions: click link and play video.

## Requirements

1. 'name_xss.html' file.
2. Browser with video playback enabled.

## Defense

Defensive measures and detection strategies:

- Escape thumbnails consistently across site and player.
- Reset window.name on navigation or use postMessage for safe comms.
- Detect and block suspicious prompts or eval in video contexts.

## Objectives

1. Navigate with payload intact.
2. Require minimal victim actions.
3. Execute and exfil data.

## Instructions

### Step 1: Open HTML and Click Link

**Context**: Load payload and navigate to video.

Open 'name_xss.html', click 'Watch video'.

### Step 2: Play Video

**Context**: Start playback to reach end state.

On vimeo.com, click play button.

### Step 3: Wait for Thumbnail

**Context**: Allow end and execution.

Wait 10 seconds; observe prompt.

**Expected Output**: Alert with domain/cookies.

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
- [[video-playback]]
