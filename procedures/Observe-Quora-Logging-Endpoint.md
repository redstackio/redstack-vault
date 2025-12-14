---
id: proc-observe-logging-001
name: Observe Quora Logging Endpoint
tags:
  - reconnaissance
  - web-endpoint
  - logging
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-send-normal-log]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:26:30.781Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Observe Quora Logging Endpoint

## Summary

This procedure involves monitoring and capturing legitimate HTTP POST requests to Quora's logging endpoint to understand its structure, enabling subsequent modification for exploitation.

## Description

Quora's logging system uses an unauthenticated POST endpoint at https://log.quora.com/ajax/batched_log_POST to store JSON-formatted log data. By observing normal traffic, attackers can identify the 'json' parameter format, which is URL-encoded and contains small log messages. This reconnaissance step is crucial for crafting malicious payloads without triggering anomalies. The target environment is any web browser or tool accessing Quora, with no special privileges required. Expected outcome: A baseline request template for modification.

## Requirements

1. Access to Quora website via browser
2. Network interception tool (e.g., developer tools or proxy)
3. Ability to send HTTP requests (curl or similar)

## Defense

Defensive measures and detection strategies:

- Monitor unusual traffic patterns to the logging endpoint
- Implement rate limiting on logging requests
- Log and alert on request sizes exceeding thresholds

## Objectives

1. Capture normal request structure and payload format
2. Confirm endpoint accessibility and response behavior
3. Prepare template for payload modification

## Instructions

### Step 1: Monitor Traffic

**Context**: Interact with Quora to generate logging events, such as page views or searches, and capture the request.

**Command** ([[commands/curl-send-normal-log]]):
```bash
curl -X POST 'https://log.quora.com/ajax/batched_log_POST' -d 'json=%5B%7B%22event%22%3A%22page_view%22%2C%22data%22%3A%22small%22%7D%5D'
```

> This replicates a normal log request. Expected output: HTTP 200 with no errors, confirming small payload acceptance.

### Step 2: Analyze Response

**Context**: Inspect the request body to note the 'json' parameter encoding.

No specific command; use tools like jq or manual inspection on the response.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-send-normal-log]]

## Tools Used


## Tags

- [[Reconnaissance]]
- [[web-endpoint]]
