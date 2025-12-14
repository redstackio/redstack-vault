---
tags:
  - dos
  - spam
  - replay
type: procedure
tools:
  - '[[tools/Burp-Intruder]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T12:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:32:01.883Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 357f995b-9092-43ab-a7ab-fd1253b67cb3
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Replay-Requests-with-Burp-Intruder

## Summary

This procedure automates the replay of intercepted POST requests to the contact form endpoint multiple times, exploiting missing rate limits to cause email spamming and potential denial-of-service on the server.

## Description

Using Burp Intruder, the captured POST request is sent repeatedly (e.g., 100+ times) without modifications, flooding the /contact/ endpoint. In Weblate's Django setup, this leads to excessive email dispatches and server resource exhaustion due to no IP blacklisting or token checks.

## Requirements

1. Intercepted request from prior step in Burp
2. Burp Intruder module access
3. Target endpoint responsive

## Defense

Defensive measures and detection strategies:

- Implement rate limiting (e.g., 5 requests/min per IP) using Django middleware
- Use WAF to detect and block rapid repeated POSTs to forms
- Monitor email queue and server load for anomalies

## Objectives

1. Flood the endpoint with unlimited submissions
2. Trigger spam emails to recipients
3. Overload server for DoS effect

## Instructions

### Step 1: Send to Intruder

**Context**: Load the intercepted request into Burp Intruder for automation.

Right-click the request in Burp Proxy and select 'Send to Intruder'.

> No payload positions needed for simple replay; set attack type to 'Sniper' with no positions marked for unmodified floods.

### Step 2: Configure and Launch Attack

**Context**: Set iteration count and start replay to simulate spam.

In Intruder, set threads to 1-5, iterations to 100+, and start the attack targeting POST /contact/.

> Observe responses: Multiple 200 OKs confirm bypass; increasing load may cause delays or errors indicating DoS onset.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Network Denial of Service]] Network Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Intruder]]

## Tags

- [[dos]]
- [[spam]]
- [[replay]]
