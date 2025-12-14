---
id: proc-uuid-intercept-request
tags:
  - http-intercept
  - proxy
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:29.057Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-Support-Rider-Request

## Summary

This procedure uses a web proxy to capture the HTTP request sent when adding a support rider donation during Zomato checkout, allowing inspection of the payload before modification.

## Description

Targeting the Zomato web application, this involves routing browser traffic through a proxy tool to pause and examine the POST request for donation addition. The request typically contains JSON with price fields vulnerable to tampering. Prerequisites include proxy configuration; outcomes include access to modifiable parameters without server interaction yet.

## Requirements

1. Burp Suite or similar proxy installed and running
2. Browser proxy settings configured (e.g., 127.0.0.1:8080)
3. Active Zomato checkout session
4. CA certificate installed in browser to handle HTTPS

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS with HSTS to complicate proxy interception
- Log and alert on proxy-like user agents or IP anomalies
- Validate request signatures or tokens to prevent tampering

## Objectives

1. Capture the exact donation addition request
2. Identify price parameter fields in the payload
3. Pause execution for safe modification

## Instructions

### Step 1: Configure Proxy

**Context**: Set up interception for all traffic.

Launch Burp Suite; configure browser to use proxy at 127.0.0.1:8080.

> Expected: Traffic routes through proxy; HTTPS handled via cert.

### Step 2: Trigger and Intercept Request

**Context**: Generate the target request.

In checkout, select donation option; request pauses in Burp's Proxy tab.

> Expected: POST request to /api/donation or similar endpoint visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- http-intercept
- proxy
