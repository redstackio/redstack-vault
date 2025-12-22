---
tags:
  - xss
  - payload-craft
  - url-injection
type: procedure
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:20.496Z'
sub_techniques: []
id: 073b116a-e25e-4454-9cb4-48773dad9929
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Malicious-Twitter-Intent-URL

## Summary

This procedure constructs a malicious URL for Twitter's /intent/favorite endpoint, injecting an XSS payload into the original_referer parameter to embed HTML attributes like style and event handlers.

## Description

The original_referer parameter is URL-encoded and includes payloads that inject attributes directly into the DOM when processed. Example payload targets multiple events (autocompleteerror, blur, error, etc.) to ensure execution on various interactions. This exploits lack of escaping when Referer is from twitter.com.

## Requirements

1. Target tweet ID
2. URL encoder tool or manual encoding knowledge
3. Understanding of HTML attribute injection

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all referer parameters
- Validate incoming URLs against whitelist
- Use Content Security Policy (CSP) to block inline scripts

## Objectives

1. Create injectable payload
2. Encode for URL transmission
3. Test payload viability

## Instructions

### Step 1: Design Payload

**Context**: Build the injection string with attributes.

Create payload: ' style=font-size:1000px;onautocompleteerror=alert(0) onblur=alert(0) onerror=alert(0) onfocus=alert(0) onmouseover=alert(0)'.

### Step 2: Encode and Assemble URL

**Context**: URL-encode the payload and append to intent endpoint.

Encode payload (e.g., %20style%3Dfont-size%3A1000px%3Bonautocompleteerror%3Dalert(0)%20...) and form: https://twitter.com/intent/favorite?original_referer=[encoded]&tweet_id=440322224407314432.

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
- [[payload-craft]]
