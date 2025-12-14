---
tags:
  - dos
  - payload
  - slash-command
  - logging
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/make-run-server]]'
platforms:
  - Web
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: d3730f8c-eb08-47af-94ff-ffe834e7ff44
created_at: '2025-12-14T17:26:37.558Z'
updated_at: '2025-12-14T17:26:37.558Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
---
# Trigger-DoS-via-Large-Slash-Command-Payload

## Summary

This procedure intercepts a slash command API request in Mattermost, modifies the 'command' parameter to exceed 64KB, and sends it to cause a server hang during console logging at DEBUG level, resulting in denial of service to all users.

## Description

Authenticated users can execute slash commands, which trigger POST requests to /api/v4/commands/execute. Invalid commands are logged including the full payload. Without size limits, payloads >65,535 bytes overwhelm the logging process, hanging the server. Use Burp Suite to capture and replay modified requests in a test environment.

## Requirements

1. Running Mattermost server with DEBUG console logging
2. Authenticated user access to a channel
3. Burp Suite configured as browser proxy
4. Ability to generate large strings (e.g., via text editor)

## Defense

Defensive measures and detection strategies:

- Enforce size limits on slash command inputs (<64KB)
- Disable DEBUG logging in production
- Use asynchronous or buffered logging to prevent hangs
- Monitor for large API payloads in logs

## Objectives

1. Inject oversized payload into slash command
2. Trigger logging exhaustion
3. Confirm server-wide DoS

## Instructions

### Step 1: Intercept Slash Command Request

**Context**: Execute a non-existent command to capture the API call.

Type `/invalidcommand` in a channel and submit; use Burp Suite Proxy to intercept the POST /api/v4/commands/execute request with JSON body including 'command': '/invalidcommand'.

> Expected: Request captured in Burp, showing JSON payload.

### Step 2: Modify and Replay Payload

**Context**: Inflate the payload to trigger logging hang.

Forward to Repeater, replace 'command' value with a string >66,000 characters (e.g., repeat '0' 70,000 times), then send.

> Expected: Server responds initially but hangs on logging the error.

### Step 3: Verify and Recover

**Context**: Confirm DoS and restart server.

Attempt additional requests; server unresponsive. Execute [[commands/make-run-server]] to restart.

> Expected: All endpoints fail until restart; service resumes post-restart.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[OS Exhaustion Flood]] OS Exhaustion

### Sub-Techniques


## Commands Used

- [[commands/make-run-server]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[dos]]
- [[payload]]
