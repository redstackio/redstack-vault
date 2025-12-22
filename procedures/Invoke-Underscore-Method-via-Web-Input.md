---
id: proc-redos-invoke-web-001
tags:
  - redos
  - dos
  - web-exploit
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-post-malicious-input]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:30.851Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
---
# Invoke-Underscore-Method-via-Web-Input

## Summary

This procedure delivers the ReDoS malicious string to a vulnerable Ruby on Rails web endpoint that processes input through the underscore method or related inflectors, resulting in server-side resource exhaustion and DoS.

## Description

In Rails applications, methods like underscore are often used in controllers or views to process user inputs such as table names, foreign keys, or titles (e.g., in API responses or form handling). By submitting a crafted payload to an unauthenticated or authenticated endpoint, the server invokes the vulnerable regex, leading to CPU/memory spikes. This affects services like search APIs or dynamic naming features. Prerequisites: Knowledge of the target's endpoint and the crafted payload from prior procedure. Expected outcomes include server hang and denial of service to other users.

## Requirements

1. Access to the target Rails web application (HTTP/HTTPS)
2. Crafted malicious string from previous procedure
3. Tool for sending HTTP requests (e.g., curl)
4. Monitoring capability for server resources (e.g., via logs or external observer)

## Defense

Defensive measures and detection strategies:

- Patch Active Support to fixed versions
- Implement timeout wrappers around inflector calls
- Use regex libraries with backtracking limits (e.g., Oniguruma options)
- Log and alert on long-running requests or regex timeouts

## Objectives

1. Identify and target an endpoint using vulnerable methods
2. Submit payload to trigger backtracking
3. Confirm DoS via response delay or resource exhaustion

## Instructions

### Step 1: Identify Vulnerable Endpoint

**Context**: Review app docs or test endpoints to find those using underscore (e.g., /api/tableize or /naming/endpoint).

No command; manual reconnaissance via browsing or API testing.

### Step 2: Submit Malicious Payload

**Context**: Use HTTP POST to send the string as input parameter, triggering the method call.

**Command** ([[commands/curl-post-malicious-input]]):
```bash
curl -X POST 'http://target-rails-app.com/api/underscore' -d 'name=aaaaaaaaaaaaaaaa...AbcDef' -H 'Content-Type: application/x-www-form-urlencoded'
```

> Replace URL and payload. Expected output: Request hangs or times out after 30+ seconds; check server for high load.

### Step 3: Verify DoS Impact

**Context**: Send follow-up benign requests to confirm service denial.

**Command** ([[commands/curl-post-malicious-input]]):
```bash
curl -X GET 'http://target-rails-app.com/health'
```

> Expected: 503 or timeout errors post-attack.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[OS Exhaustion Flood]] Application or Service Exhaustion

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-post-malicious-input]]

## Tools Used

- None

## Tags

- redos
- web-exploit
- dos
