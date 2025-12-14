---
id: 123e4567-e89b-12d3-a456-426614174003
name: Intercept-and-Observe-SSRF-Response
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:47.960Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Data from Local System]]'
tags:
  - ssrf
  - interception
  - exfiltration
platforms:
  - Web
commands: []
tools:
  - '[[tools/Burp-Suite]]'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---

# Intercept-and-Observe-SSRF-Response

## Summary

This procedure uses a proxy tool to capture and analyze the full HTTP response from the SSRF exploitation, revealing exfiltrated internal data.

## Description

After triggering SSRF, the server's response includes the raw content from the target URL, such as internal file data. Burp Suite intercepts this to inspect headers, body, and any sensitive information. This step confirms exploitation success and allows data extraction. It assumes prior authentication and request initiation; outcomes include visibility into internal network resources.

## Requirements

1. Active SSRF request in progress
2. Burp Suite configured as proxy
3. Knowledge of the proxy endpoint response format

## Defense

Defensive measures and detection strategies:

- Sanitize and filter SSRF responses to prevent data leakage
- Implement response size limits and content-type checks
- Detect proxy tool usage via anomalous traffic patterns

## Objectives

1. Capture SSRF-generated response
2. Extract internal data from response body
3. Validate exploitation

## Instructions

### Step 1: Configure Interception

**Context**: Set up Burp Suite to intercept traffic from the browser or client.

No command; configure browser proxy to 127.0.0.1:8080 and enable interception.

> Expected output: Requests paused for inspection.

### Step 2: Trigger and Intercept Response

**Context**: Perform the SSRF request and forward to observe the response.

No specific command; forward the subscription request in Burp.

> Expected output: Full HTTP response with internal content like "secret" file displayed in Burp Repeater or Inspector.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Local System]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[ssrf]]
- [[interception]]
- [[Exfiltration]]
