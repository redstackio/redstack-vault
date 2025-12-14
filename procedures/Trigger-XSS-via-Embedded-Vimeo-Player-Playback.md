---
tags:
  - xss
  - flash
  - vimeo
  - playback
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Flash
submitted: true
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 218bf328-40c9-4cc4-97be-032b66c1ff8f
created_at: '2025-12-14T03:16:14.575Z'
updated_at: '2025-12-14T03:16:14.575Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Embedded-Vimeo-Player-Playback

## Summary

This procedure triggers the cross-site scripting payload by embedding the vulnerable Vimeo moogaloop Flash player on a target site and initiating video playback, causing videoControllerProgressive.swf to load the poisoned SharedObject's malicious SWF and execute arbitrary JavaScript in the embedding domain's context.

## Description

Sites using deprecated Vimeo embed code load moogaloop.swf, which integrates Conviva LivePass for analytics. Upon playback, videoControllerProgressive.swf (loaded from the CDN) reads 'com.conviva.livePass.lastSwfUrls' from SharedObject and includes the cached SWF without validation. The malicious SWF executes JS via ExternalInterface, bypassing same-origin policy since Flash runs in the embedding page's context. This results in full XSS control, such as stealing cookies or keylogging.

## Requirements

1. Poisoned SharedObject from prior procedures
2. Target site or test page with Vimeo embed code using moogaloop.swf (e.g., <embed src="http://f.vimeocdn.com/.../moogaloop.swf?clip_id=VIDEO_ID">)
3. Valid Vimeo video ID for playback
4. Flash-enabled browser on the target domain

## Defense

Defensive measures and detection strategies:

- Deprecate and remove all Flash-based embeds; use Vimeo's HTML5 player
- Validate and sanitize SharedObject reads in custom Flash integrations
- Implement strict Flash sandboxing and policy files to restrict ExternalInterface
- Monitor for unexpected JS execution from CDN-loaded SWFs in WAF logs

## Objectives

1. Load the embedding player on the target domain
2. Initiate playback to trigger SharedObject read and malicious SWF load
3. Achieve arbitrary JS execution as XSS

## Instructions

### Step 1: Embed Vulnerable Player

**Context**: Create or access a page embedding moogaloop.swf with a valid clip_id.

Use deprecated embed code:

```html
<embed src="http://f.vimeocdn.com/p/flash/moogaloop/6.0.31/moogaloop.swf?clip_id=38626783" type="application/x-shockwave-flash" width="640" height="360"></embed>
```

Or load directly:

```url
http://f.vimeocdn.com/p/flash/moogaloop/6.0.31/moogaloop.swf?clip_id=38626783&autoplay=true
```

> Replace 38626783 with any public Vimeo video ID.

### Step 2: Initiate Playback

**Context**: Start the video to invoke the controller SWF, which checks the SharedObject.

Click play in the Flash player.

> The controller loads the cached malicious SWF from SharedObject, executing JS.

**Expected Output**: Confirm dialog or custom JS effect (e.g., alert) on the embedding domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[flash]]
- [[vimeo]]
- [[playback]]
