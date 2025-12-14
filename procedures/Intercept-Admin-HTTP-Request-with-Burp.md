---
id: proc-intercept-request
tags:
  - http-intercept
  - burp-suite
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Adversary-in-the-Middle]]'
updated_at: '2025-12-14T17:28:51.672Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Intercept-Admin-HTTP-Request-with-Burp

## Summary

This procedure captures an HTTP request for an admin action in the Omise dashboard using Burp Suite, allowing later replay to test access control bypass.

## Description

As an admin user, perform a privileged action like editing or adding a link at https://dashboard.omise.co/v2/links while proxying traffic through Burp Suite to intercept the request. This targets POST/PUT requests containing action payloads and session data. Prerequisites include Burp configured as proxy (e.g., browser set to 127.0.0.1:8080) and admin access. Outcome: Request details saved for replay.

## Requirements

1. Burp Suite installed and running
2. Admin role in Omise dashboard
3. Browser proxy configured for Burp

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS with HSTS to prevent interception
- Monitor for proxy anomalies in network traffic
- Use request signing or nonces to invalidate replays

## Objectives

1. Capture privileged HTTP request payload
2. Preserve session context for replay
3. Identify backend endpoint vulnerabilities

## Instructions

### Step 1: Configure Burp Proxy

**Context**: Set up Burp to intercept dashboard traffic.

No specific command; launch Burp, ensure Proxy tab is active, and set browser to use Burp proxy.

> Traffic from https://dashboard.omise.co routes through Burp.

### Step 2: Perform Admin Action and Intercept

**Context**: Execute edit/add link to trigger interceptable request.

No specific command; navigate to https://dashboard.omise.co/v2/links, perform action (e.g., edit link), and intercept in Burp.

> Request appears in Burp Proxy > Intercept; forward or drop as needed, then save to Repeater.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Adversary-in-the-Middle]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- http-intercept
- burp-suite
