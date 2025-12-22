---
tags:
  - ssrf
  - observation
  - exfiltration
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: c7e213cd-f1b2-4724-83d5-88b772a19400
created_at: '2025-12-14T03:46:09.106Z'
updated_at: '2025-12-14T03:46:09.106Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-and-Observe-SSRF

## Summary

This procedure monitors the SSRF execution by capturing server-initiated connections to attacker-controlled endpoints, confirming the vulnerability and gathering evidence of internal access.

## Description

Upon SVG processing, the converter fetches the malicious URLs, revealing the server's IP, user-agent, and potentially sensitive data in query params or responses. Screenshots from PoCs show connections to external IPs like 178.249.60.9:12345.

## Requirements

1. Listener server (e.g., nc -lvp 12345 or simple HTTP server)
2. Payloads targeting internal resources (e.g., metadata services)

## Defense

Defensive measures and detection strategies:

- Network segmentation to prevent internal fetches from public apps
- WAF rules blocking suspicious outbound traffic patterns

## Objectives

1. Receive and log SSRF callbacks
2. Identify internal network details
3. Validate payload success

## Instructions

### Step 1: Set Up Listener

**Context**: Prepare to capture incoming requests from the vulnerable server.

Run a netcat listener: nc -lvp 12345 on your server.

### Step 2: Analyze Incoming Connections

**Context**: Review logs after triggering the fetch.

Check for GET requests to /image.gif or similar, noting the source IP (Shopify internal) and any exfiltrated data in headers.

**Expected Output**: Connection logs like "GET /payload HTTP/1.1" from converter server IP.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[observation]]
