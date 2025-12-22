---
id: proc-access-capture-request
tags:
  - ssrf
  - capture
  - victim-simulation
type: procedure
tools:
  - '[[tools/Firefox-Browser]]'
  - '[[tools/ngrok]]'
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
updated_at: '2025-12-14T17:32:01.828Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Malicious-URL-and-Capture-Victim-Request

## Summary

This procedure simulates victim access to the malicious URL using a separate browser/device, triggering the SSRF payload and capturing the resulting request on the ngrok listener.

## Description

In the attack on the DoD site, accessing the injected URL causes server-side processing of the source parameter, executing the fetch to the attacker's ngrok. This captures full request details from the victim's perspective. Use a different device to mimic real victim traffic.

## Requirements

1. Constructed malicious URL
2. Active ngrok listener
3. Separate device/browser for access

## Defense

Defensive measures and detection strategies:

- Implement request rate limiting on login pages
- Scan for anomalous outbound requests to unknown domains
- User-agent and referer header validation

## Objectives

1. Trigger SSRF execution
2. Receive and log victim request
3. Confirm data exfiltration

## Instructions

### Step 1: Open Malicious URL

**Context**: Simulate victim by accessing the URL in Firefox on another device.

**Instructions**: Launch Firefox 80.0.1 and navigate to the full malicious URL.

> The page loads, but server processes source, sending fetch to ngrok. Monitor ngrok interface simultaneously.

### Step 2: Verify Capture

**Context**: Check ngrok for incoming request.

**Instructions**: Refresh http://127.0.0.1:4040 to see the POST/GET request with headers.

> Expected: Request shows victim's IP, User-Agent (browser/OS), and other metadata.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox-Browser]]
- [[tools/ngrok]]

## Tags

- ssrf
- access
- capture
