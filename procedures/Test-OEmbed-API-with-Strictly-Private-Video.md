---
tags:
  - privacy-testing
  - api
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-vimeo-oembed-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:32:01.478Z'
sub_techniques: []
id: 791986e2-4957-440c-abd5-efdfa7d5756c
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Test-OEmbed-API-with-Strictly-Private-Video

## Summary

This procedure tests the oEmbed API response for a video set to the strictest privacy ('Only me'), confirming proper 404 enforcement to baseline against weaker settings.

## Description

Vimeo's privacy options include 'Only me', which should block all access. This step uses a known private video URL to query the API, expecting a denial, which highlights inconsistencies in other privacy levels.

## Requirements

1. A test Vimeo account with a video set to 'Only me' privacy
2. The video's URL or ID (e.g., 152133387)
3. HTTP client like curl

## Defense

Defensive measures and detection strategies:

- Ensure uniform privacy enforcement across all endpoints
- Log and alert on API queries to private resources
- Use consistent access controls in API gateways

## Objectives

1. Verify 404 response for strict privacy
2. Confirm no metadata leakage
3. Establish baseline for comparison

## Instructions

### Step 1: Query API with Private Video URL

**Context**: Send a request to the oEmbed endpoint using the encoded private video URL.

**Command** ([[commands/curl-vimeo-oembed-test]]):
```bash
curl "https://vimeo.com/api/oembed.json?url=https%3A//vimeo.com/152133387"
```

> Response should be empty or 404, indicating no disclosure.

### Step 2: Verify Direct Page Access

**Context**: Confirm the video page itself is inaccessible.

**Command** ([[commands/curl-vimeo-oembed-test]]):
```bash
curl -I "https://vimeo.com/152133387"
```

> HTTP headers show 404 Not Found, matching API behavior for this setting.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-vimeo-oembed-test]]

## Tools Used


## Tags

- [[privacy-testing]]
- [[api]]
