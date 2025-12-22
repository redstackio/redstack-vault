---
tags:
  - ssrf
  - observation
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Active Scanning]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: c0fec50f-f71b-46f7-a101-9548717ee34a
created_at: '2025-12-14T03:46:14.365Z'
updated_at: '2025-12-14T03:46:14.365Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Observe SSRF Interaction on External Server

## Summary

Monitors the attacker-controlled server for incoming requests from the target, confirming SSRF exploitation.

## Description

After upload, the target's image parser fetches the external URL, sending a GET request with specific headers. This reveals the SSRF despite the 422 response, useful for validating the vector.

## Requirements

1. Web server on attacker machine (e.g., Python http.server) logging requests
2. Publicly accessible attacker server

## Defense

Defensive measures and detection strategies:

- Proxy outbound requests through a firewall with logging
- Block or monitor fetches to unknown domains from processing services
- Anomaly detection on image parser traffic

## Objectives

1. Detect incoming GET from target IP
2. Analyze headers for server details
3. Validate SSRF success

## Instructions

### Step 1: Set Up Logging Server

**Context**: Host a simple server to capture requests.

Run on attacker-server:

```bash
python3 -m http.server 80 --bind 0.0.0.0
```

> Use a logging proxy like nginx or tcpdump for detailed captures.

### Step 2: Analyze Logs Post-Upload

**Context**: Check for GET /image.jpeg HTTP/1.0 with Host: attacker-server and Accept-Encoding: gzip.

Review access logs for target IP and headers.

> Confirms interaction from Shopify server.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[Reconnaissance]]
