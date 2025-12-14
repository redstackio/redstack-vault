---
id: 123e4567-e89b-12d3-a456-426614174004
name: Capture-and-Analyze-Network-Traffic
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.792Z'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Active Scanning]]'
sub_techniques: []
tags:
  - traffic-analysis
  - wireshark
  - verification
commands: []
platforms:
  - Web
tools:
  - '[[tools/Wireshark]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---

# Capture-and-Analyze-Network-Traffic

## Summary

This procedure captures HTTP requests and responses during SSRF exploitation to verify server-side behavior and connections.

## Description

Using a tool like Wireshark, record traffic while sending SSRF requests. Analyze for outbound fetches to redirectors and targets, confirming the vulnerability without client-side exposure. Attachments like http.7z can store dumps for review.

## Requirements

1. Network interface access for capture
2. Running SSRF requests during capture
3. Knowledge of HTTP filters (e.g., http.request.method == "POST")

## Defense

Defensive measures and detection strategies:

- Encrypt internal traffic to obscure analysis
- Log all outbound connections from app servers
- Use IDS to alert on unusual fetch patterns

## Objectives

1. Verify SSRF triggers actual connections
2. Document evidence for reporting
3. Identify any additional leaks

## Instructions

### Step 1: Start Capture

**Context**: Launch Wireshark and select the interface to monitor client-server traffic.

Use [[tools/Wireshark]] with filter "http".

### Step 2: Replay Requests and Stop Capture

**Context**: Send SSRF payloads and halt capture after a few requests.

No specific command; execute prior SSRF commands during capture.

### Step 3: Analyze Packets

**Context**: Inspect for POST to /images, redirects, and timing anomalies.

Look for response times correlating to port status.

> Expected: Evidence of server connecting to targets like scanme.nmap.org:22.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Wireshark]]

## Tags

- [[traffic-analysis]]
- [[tools/Wireshark]]
- [[verification]]
