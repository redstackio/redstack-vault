---
id: proc-uuid-4
tags:
  - dos-validation
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:55.771Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Repeat-Request-to-Trigger-Delay

## Summary

This procedure resends the modified large-payload request multiple times to validate and observe the DoS effect, including processing delays and error responses.

## Description

Repeating the intercepted request exploits the absence of rate-limiting, causing cumulative resource strain. Scenario: Manual resends via proxy. Outcomes: ~30s delays and 502 errors. Prerequisites: Intercepted request ready.

## Requirements

1. Burp Suite with saved intercepted request
2. Timer or monitoring for response times
3. Target endpoint responsive

## Defense

Defensive measures and detection strategies:

- Apply rate-limiting to POST endpoints (e.g., 5 req/min per user)
- Monitor for repeated large requests and block IPs

## Objectives

1. Confirm delay per request
2. Observe error escalation
3. Validate single-instance impact

## Instructions

### Step 1: Resend Request

**Context**: Use Burp's Repeater to simulate multiple submissions.

Load the modified request in Repeater and click 'Send' 3-5 times.

> Each send takes ~30s, ends in HTTP/2 502 Bad Gateway. Expected: Increasing backend load.

### Step 2: Log Responses

**Context**: Document timings to quantify the vulnerability.

Note response headers and times in Burp history.

> Success: Consistent delays > normal (1-2s) processing.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- dos-validation
- web
