---
id: acronis-intercept-api-001
tags:
  - api-interception
  - proxy
  - burp
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:28.699Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-Recovery-Plan-API-Requests-with-Burp-Suite

## Summary

This procedure uses Burp Suite to capture API requests during recovery plan execution in Acronis, focusing on the run operation endpoint to extract parameters for IDOR exploitation.

## Description

Targeted at the Acronis recovery API, this involves proxying traffic to intercept POST requests to /bc/api/ams/recovery/plan_operations/run. It assumes a configured recovery plan from prior steps. The goal is to identify vulnerable parameters like machineId and planId, which lack tenant validation, enabling later replay attacks.

## Requirements

1. Burp Suite running with browser proxy (e.g., 127.0.0.1:8080)
2. Active Acronis session with prepared recovery plan
3. CA certificate installed for HTTPS interception

## Defense

Defensive measures and detection strategies:

- Enforce TLS certificate pinning to block proxy interception
- Log and alert on unusual API request patterns (e.g., high-frequency drafts)
- Use request signing or tenant-specific tokens

## Objectives

1. Capture the recovery run API request
2. Extract key parameters for manipulation
3. Validate request structure for replay compatibility

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp to intercept traffic.

In Burp, enable Intercept in Proxy tab and configure browser to use the proxy.

> Traffic routes through Burp.

### Step 2: Trigger Recovery Run

**Context**: Initiate the action to generate the target request.

In Acronis UI, proceed to run the recovery plan.

> Request appears in Burp Intercept.

### Step 3: Analyze and Forward

**Context**: Inspect the POST to /bc/api/ams/recovery/plan_operations/run.

Note body: {"planId": "<id>", "machineId": "<uuid>", "subscriptionId": "<id>", "operationId": "<id>"} and headers including X-Apigw-Session.

> Forward the request to complete the action, then copy to Repeater.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- api-interception
- proxy
- burp
