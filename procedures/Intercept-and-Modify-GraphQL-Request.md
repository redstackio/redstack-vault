---
id: proc-intercept-graphql-request
tags:
  - intercept
  - proxy
  - graphql
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:56.721Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept and Modify GraphQL Request

## Summary

This procedure uses a web proxy to capture and alter the GraphQL POST request from the CreateStructuredScope mutation, preparing it for oversized payload insertion in a DoS exploitation.

## Description

Targeting web applications with GraphQL endpoints, this step intercepts traffic to /graphql, examines the JSON structure (query, variables like instruction), and modifies it while preserving authentication (X-Auth-Token, cookies). It's a prerequisite for flooding attacks, assuming a Ruby on Rails backend without strict validation. Outcomes include a tampered request ready for automation, with minimal risk if done manually first.

## Requirements

1. Burp Suite or similar proxy running and browser configured to route through it (e.g., 127.0.0.1:8080)
2. Valid session from prior authentication
3. Knowledge of GraphQL payload structure

## Defense

Defensive measures and detection strategies:

- Deploy WAF rules to detect proxy-like modifications (e.g., anomalous User-Agent or Referer)
- Enable HTTPS interception detection via certificate pinning
- Audit logs for repeated intercepted requests

## Objectives

1. Capture the exact request format for replication
2. Modify the instruction field placeholder for large payload
3. Maintain request integrity to avoid immediate rejection

## Instructions

### Step 1: Configure Proxy Interception

**Context**: Set up the tool to capture the mutation request.

**Instructions**: Launch Burp Suite, enable intercept on the Proxy tab, and perform the scope creation action from Step 1 to trigger the request.

> The request appears in Burp with headers (Content-Type: application/json, Referer: https://hackerone.com/testingfordos/scopes/new) and JSON body.

### Step 2: Inspect and Modify Payload

**Context**: Alter the variables to prepare for oversized input.

**Instructions**: In Burp Repeater or Inspector, locate variables.instruction and note its position; forward the request once unmodified to confirm success, then edit for testing (e.g., add extra characters).

> Expected output: Modified request sent; response shows was_successful: true if under limits.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[intercept]]
- [[proxy]]
- [[graphql]]
