---
tags:
  - xss
  - data-exfiltration
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 72317a52-96e3-40a1-8399-e276b0135720
created_at: '2025-12-14T00:11:16.791Z'
updated_at: '2025-12-14T00:11:16.791Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Exfiltrate Data via Blind XSS

## Summary

This procedure covers the exfiltration phase of a blind XSS attack, where the injected payload executes in the victim's browser and sends sensitive data to an attacker-controlled server.

## Description

After submission, the payload is viewed by internal staff on the Big Data panel subdomain, triggering execution. The script collects data like document content or cookies and uses fetch or similar to send it externally. The attacker monitors their server for incoming data.

## Requirements

1. Pre-injected XSS payload
2. Web server listening for exfiltration requests
3. Patience, as execution depends on staff viewing the ticket

## Defense

Defensive measures and detection strategies:

- Regularly scan for stored XSS in user inputs
- Implement web application firewalls (WAF) to detect malicious payloads
- Monitor network traffic for anomalous outbound connections from internal systems

## Objectives

1. Receive exfiltrated data from the internal context
2. Analyze stolen information for further exploitation
3. Confirm vulnerability impact

## Instructions

### Step 1: Set Up Exfiltration Server

**Context**: Configure a simple web server to log incoming requests containing exfiltrated data.

Use a tool like netcat or a basic HTTP server to listen on the specified endpoint (e.g., https://attacker.com/exfil).

### Step 2: Monitor for Data

**Context**: Wait for the payload to trigger and check server logs for GET/POST requests with query parameters containing encoded data.

Decode the received data to reveal sensitive information like internal cookies or page sources.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques

None

## Commands Used

None

## Tools Used

None

## Tags

- [[data-exfiltration]]
- [[xss]]
