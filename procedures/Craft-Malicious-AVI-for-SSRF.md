---
id: proc-avi-ssrf-craft-001
tags:
  - ssrf
  - avi-craft
  - hex-edit
type: procedure
tools:
  - '[[tools/Hex-Editor]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Linux
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:09.419Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malicious-AVI-for-SSRF

## Summary

This procedure crafts a malicious AVI file by embedding an external HTTP URL in an HLS playlist within the GAB2 subtitle chunk, enabling SSRF when processed by FFmpeg in WordPress.com's video upload feature.

## Description

The attack targets WordPress.com's /media/videos/ endpoint, where uploaded AVI files with GAB2 subtitles containing HLS playlists are processed by FFmpeg on internal servers. By replacing the playlist URL with an attacker-controlled HTTP endpoint, FFmpeg fetches external resources during conversion, allowing SSRF. This requires a paid account and preserves the AVI's binary structure to avoid detection.

## Requirements

1. Base AVI file (e.g., http_q.avi) with existing GAB2 HLS structure
2. Hex editor tool installed
3. Attacker-controlled server URL ready

## Defense

Defensive measures and detection strategies:

- Validate and sanitize uploaded file contents, especially subtitle chunks
- Restrict FFmpeg network access to whitelisted domains
- Monitor FFmpeg processes for unexpected outbound connections

## Objectives

1. Embed external HTTP reference in HLS playlist
2. Ensure AVI remains valid for upload
3. Trigger SSRF on processing

## Instructions

### Step 1: Open and Locate URL in AVI

**Context**: Load the base AVI in a hex editor to find the embedded HTTP link in the GAB2 chunk.

No command required; use GUI hex editor to search for the string 'http://45.55.40.92/ssrf_test'.

> Locate the offset of the URL in the binary data.

### Step 2: Replace URL with Attacker Endpoint

**Context**: Overwrite the URL with your server (e.g., http://your-server.com/test_ssrf) while maintaining file length by padding if needed.

No command; manually edit in hex editor and save as modified.avi.

> Verify the change by searching for the new URL; ensure no corruption by testing file open in media player.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Hex-Editor]]

## Tags

- ssrf
- avi-exploit
