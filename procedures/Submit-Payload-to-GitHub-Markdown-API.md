---
tags:
  - dos
  - api-exploit
  - github
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:32:39.291Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: d4aeb93f-36c7-4a10-b0da-59b543f85d42
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[OS Exhaustion Flood]]'
---
# Submit-Payload-to-GitHub-Markdown-API

## Summary

This procedure submits the crafted malicious markdown payload to GitHub's unauthenticated markdown API, triggering resource exhaustion and denial of service on the rendering service.

## Description

GitHub's markdown API uses cmark-gfm for processing, which is vulnerable to polynomial time issues in the autolink extension. Submitting a large repeated pattern causes the parser to hang, impacting availability for all users relying on the service. No authentication is required, making it accessible to unauthenticated attackers.

## Requirements

1. Internet access to reach https://api.github.com/markdown/raw
2. The payload file from the crafting procedure
3. Curl or equivalent HTTP client

## Defense

Defensive measures and detection strategies:

- Rate limiting on API requests
- Input validation for markdown size and patterns
- Anomaly detection on parsing CPU usage

## Objectives

1. Deliver payload to vulnerable endpoint
2. Observe DoS effects on service availability
3. Confirm remote impact without local access

## Instructions

### Step 1: Prepare API Request

**Context**: Load the payload and set up the POST request to the raw markdown endpoint.

**Command** (using curl):
```bash
curl -X POST -H "Content-Type: text/plain" --data-binary @payload.txt https://api.github.com/markdown/raw
```

> The request should timeout or delay significantly. Expected output: partial or no response due to server-side hang.

### Step 2: Monitor Response Time

**Context**: Time the request to quantify the DoS impact.

**Command** (timed curl):
```bash
curl -w "%{time_total}s" -X POST -H "Content-Type: text/plain" --data-binary @payload.txt --max-time 60 https://api.github.com/markdown/raw
```

> Look for times exceeding 30 seconds. Success if request fails or exceeds normal latency.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[OS Exhaustion Flood]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- dos
- api-exploit
