---
tags:
  - ssrf
  - port-9200
  - connection-refused
  - gitlab-webhook
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:39:10.147Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 01cda799-1f68-4c63-88e7-db17afbd404e
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
---
# Test-SSRF-on-Port-9200-via-GitLab-Webhook

## Summary

This procedure tests SSRF by targeting port 9200 with a localhost URL in the GitLab webhook, observing connection refusal to map internal services.

## Description

Similar to port 80 testing, enter http://127.0.0.1:9200/haha.txt in the webhook URL. The server-side request fails due to no service on that port, but the error confirms internal reachability, aiding in intranet enumeration.

## Requirements

1. Configured webhook integration access
2. Authenticated GitLab session
3. Target port knowledge (e.g., common Elasticsearch port 9200)

## Defense

Defensive measures and detection strategies:

- Enforce strict URL validation in webhook processing
- Log and alert on TCP connection failures to internal addresses
- Segment internal services to limit SSRF impact

## Objectives

1. Probe internal port 9200 via SSRF
2. Analyze failure responses for network insights
3. Expand scanning to identify open/closed ports

## Instructions

### Step 1: Update SSRF Payload

**Context**: Modify the URL to target port 9200.

Enter http://127.0.0.1:9200/haha.txt in the webhook URL field.

> URL is accepted without restrictions.

### Step 2: Execute and Observe

**Context**: Trigger the request and review output.

Test the integration.

> Response: 'Hook execution failed: Failed to open TCP connection to 127.0.0.1:9200 (Connection refused)'.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[port-9200]]
- [[connection-refused]]
- [[gitlab-webhook]]
