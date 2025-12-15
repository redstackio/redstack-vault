---
id: p2b3c4d5-e6f7-8901-bcde-f2345678901
tags:
  - extraction
  - information-disclosure
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:25:17.313Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
---
# Extract-Trip-ID-from-WebSocket-Response

## Summary

This procedure parses WebSocket message payloads to extract the exposed trip_no identifier, which is leaked to unauthorized drivers in Bykea's implementation prior to bid acceptance.

## Description

The vulnerability stems from WebSocket responses including sensitive trip_no without proper checks, allowing any connected driver to capture it. This step involves inspecting the JSON structure of messages, typically under event types like 'trip_update', to isolate the ID for further exploitation. Applicable to web apps with real-time comms lacking segmentation.

## Requirements

1. Active WebSocket session from previous connection
2. JSON parsing capability (browser console or text editor)
3. Knowledge of message format (e.g., trip_no as string key-value)

## Defense

Defensive measures and detection strategies:

- Encrypt or hash identifiers in transit and enforce role-based message filtering
- Log and alert on extraction patterns in WebSocket logs
- Rate-limit WebSocket connections per user to detect monitoring attempts

## Objectives

1. Isolate leaked trip_no from message payload
2. Confirm lack of authorization in response
3. Prepare ID for URL construction

## Instructions

### Step 1: Inspect Payload

**Context**: Review the captured WebSocket frame in dev tools.

In the Network tab, click the WS frame, go to 'Messages' sub-tab, and expand the JSON. Search for "trip_no" key.

### Step 2: Copy Identifier

**Context**: Extract the value for use in next steps.

Copy the trip_no value (e.g., "TRIP123456") from the payload. Verify it's sent before any bid action by checking timestamps.

**Expected Output**: Isolated trip_no string ready for exploitation.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Information Repositories]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[extraction]]
- [[information-disclosure]]
