---
id: 7da278b8-88fe-463e-b7d6-ac027aaa0f32
name: Monitor-and-Confirm-SSRF-via-Collaborator
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:00.411Z'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Vulnerability Scanning]]'
sub_techniques: []
tags:
  - ssrf
  - monitoring
  - confirmation
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Collaborator]]'
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---

# Monitor-and-Confirm-SSRF-via-Collaborator

## Summary

This procedure monitors Burp Collaborator for incoming interactions triggered by the SSRF exploitation, confirming the vulnerability through DNS resolutions and HTTP requests, and allowing extension to port scanning or internal endpoint probing.

## Description

After injecting the payload, Collaborator captures blind interactions from the server (e.g., pwapi.ex2b.com). DNS hits confirm resolution attempts, while HTTP GETs show full fetches. This enables blind scanning, such as varying ports (e.g., :80, :8080) or internal IPs, to map the network without response data. Outcomes include proof of SSRF and identification of open internal services.

## Requirements

1. Active Collaborator polling from prior setup.
2. Recent SSRF trigger execution.
3. Knowledge of target server IP for verification.

## Defense

Defensive measures and detection strategies:

- Implement DNS sinkholing for anomalous queries.
- Monitor application logs for GraphQL queries with external URLs.
- Use endpoint detection to flag unusual outbound connections from app servers.

## Objectives

1. Capture and analyze interaction logs.
2. Verify SSRF by matching source IP.
3. Extend to internal reconnaissance if confirmed.

## Instructions

### Step 1: Poll for Interactions

**Context**: Check Collaborator for new events post-trigger.

No specific command; in Burp Collaborator tab, click "Poll now".

> Expected output: List of DNS/HTTP events with timestamps, source IPs, and paths.

### Step 2: Analyze and Test Further

**Context**: Review logs and iterate with port/internal tests.

Repeat Step 2 of prior procedure with variations like `http://[collaborator-domain]:1234/` for ports or `http://169.254.169.254/latest/meta-data/` for cloud metadata.

> Expected output: Additional interactions confirming open ports or endpoints. Success if hits from target IP.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Vulnerability Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Collaborator]]

## Tags

- [[ssrf]]
- [[monitoring]]
- [[confirmation]]
