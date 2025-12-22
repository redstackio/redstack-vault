---
tags:
  - exploitation
  - http-smuggling
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
id: df921284-14a1-4e77-9249-d2851991dba9
created_at: '2025-12-13T09:01:22.127Z'
updated_at: '2025-12-13T09:01:22.127Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send Crafted HTTP Request for Smuggling

## Summary

This procedure crafts and sends an HTTP request exploiting the smuggling vulnerability by using duplicate Transfer-Encoding headers to bypass proxy restrictions and access forbidden endpoints.

## Description

A POST request is crafted with two Transfer-Encoding headers (chunked and chunked-false), where the body contains chunked data embedding a smuggled GET /flag request. This causes desynchronization: HAProxy processes differently than Node.js, allowing the smuggled request to reach the backend.

## Requirements

1. Running HAProxy and Node.js setup from prior steps
2. Tool or method to send raw HTTP requests (e.g., netcat or custom script)
3. Knowledge of HTTP chunked encoding

## Defense

Defensive measures and detection strategies:

- Configure proxies to reject duplicate headers
- Use WAFs to detect anomalous Transfer-Encoding usage

## Objectives

1. Bypass proxy ACLs
2. Access restricted /flag endpoint
3. Demonstrate unauthorized resource access

## Instructions

### Step 1: Craft Request

**Context**: Manually construct the HTTP request with duplicate headers and smuggled content.

> Create a request like: POST / HTTP/1.1\r\nHost: localhost\r\nTransfer-Encoding: chunked\r\nTransfer-Encoding: chunked-false\r\nContent-Length: 0\r\n\r\n[chunked data with smuggled GET /flag].

### Step 2: Send Request

**Context**: Transmit the crafted request to the proxy on port 80.

> Use a tool like netcat: echo -e '[request]' | nc localhost 80; expect response including /flag content.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[exploitation]]
- [[http-smuggling]]
