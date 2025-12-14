---
tags:
  - dos
  - cookie
  - authentication
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
detection_risk: medium
sub_techniques: []
id: 1628d4ac-0496-461f-817f-1e31cf2c0511
created_at: '2025-12-14T17:26:37.556Z'
updated_at: '2025-12-14T17:26:37.556Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
---
# Trigger-DoS-via-Large-Authentication-Cookie

## Summary

This procedure crafts HTTP requests with oversized MMAUTHTOKEN cookies (>64KB) to exploit logging at INFO (POST) or WARN (GET) levels in Mattermost, causing server hangs without requiring authentication for GET vectors.

## Description

Mattermost logs invalid or large authentication tokens from cookies during request processing. No size validation allows payloads to overwhelm console logging, leading to DoS. This vector works at lower log levels than slash commands and can be unauthenticated, affecting public endpoints.

## Requirements

1. Running Mattermost server with console logging enabled (INFO or WARN)
2. Burp Suite for request crafting
3. Target endpoint (any POST or GET URL)
4. Large string generator for cookie value

## Defense

Defensive measures and detection strategies:

- Validate and limit cookie sizes server-side
- Strip or truncate logged cookie values
- Use secure logging libraries with size caps
- Alert on oversized incoming requests

## Objectives

1. Inject large cookie payload
2. Trigger log-based exhaustion
3. Achieve unauthenticated DoS

## Instructions

### Step 1: Craft POST Request with Large Cookie

**Context**: Target any authenticated POST endpoint at INFO level.

In Burp Repeater, create POST to e.g., /api/v4/users/me with header Cookie: MMAUTHTOKEN= followed by >66,000 '0's, then send.

> Expected: Server hangs on logging the invalid token.

### Step 2: Craft GET Request with Large Cookie

**Context**: Use unauthenticated GET at WARN level.

In Burp, send GET to e.g., / with Cookie: MMAUTHTOKEN= oversized string.

> Expected: Immediate server unresponsiveness without auth.

### Step 3: Recover Server

**Context**: Restart to mitigate DoS.

Execute [[commands/make-run-server]] in the terminal.

> Expected: Server restarts, restoring access.

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
- [[cookie]]
