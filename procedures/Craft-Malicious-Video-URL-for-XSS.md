---
id: proc-uuid-003
tags:
  - xss
  - payload-crafting
  - video-parser
  - attribute-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:37.906Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malicious-Video-URL-for-XSS

## Summary

This procedure crafts a malicious video URL to exploit the video parser in Discourse's onebox engine, using attribute injection to execute JavaScript via an onerror handler.

## Description

Similar to the audio parser, video_onebox.rb fails to escape single quotes in URLs, enabling injection into <video> tags. Attackers post the URL in a forum, triggering parsing and JS execution. Targets Discourse forums; impacts include defacement or data exfiltration in the site context.

## Requirements

1. Access to post videos/links in forum
2. Understanding of video tag attributes
3. Vulnerable Discourse setup for testing

## Defense

Defensive measures and detection strategies:

- Escape all user-supplied URLs in media parsers
- Scan posts for injection patterns like unescaped quotes
- Deploy WAF rules to block malformed media URLs

## Objectives

1. Inject JS via onerror in video element
2. Achieve code execution on page load
3. Validate cross-parser vulnerability pattern

## Instructions

### Step 1: Build Payload

**Context**: Engineer a URL to inject attributes in the src.

Use `http://host/path'onerror=alert(1);//k.mp4` to close the src and add the handler.

> The trailing comment prevents parsing issues.

### Step 2: Embed in Post

**Context**: Activate the video onebox by posting the URL.

Share the URL in a thread: "Watch this video: http://host/path'onerror=alert(1);//k.mp4".

> Results in <video src="...onerror=alert(1)..."> triggering on error.

### Step 3: Test Impact

**Context**: Ensure JS executes as intended.

View the post and monitor for alert or use advanced payloads like keylogging scripts.

> Confirmation: JS runs, enabling theft of session tokens.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[video-injection]]
