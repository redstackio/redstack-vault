---
id: proc-expose-mock-server-ngrok
tags:
  - tunneling
  - ngrok
  - exposure
type: procedure
tools:
  - '[[tools/ngrok]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/ngrok-http-tunnel]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Connection Proxy]]'
updated_at: '2025-12-14T17:24:14.612Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Connection Proxy]]'
---
# Expose-Mock-Server-via-Ngrok-Tunnel

## Summary

This procedure uses ngrok to create a public tunnel to the local Flask mock API server, allowing the GitLab instance to fetch malicious import_source during the bulk import process.

## Description

Ngrok exposes localhost:5000 securely to the internet, providing a URL that GitLab uses as the import source. This bridges the local mock to the remote GitLab, enabling payload delivery without direct exposure.

## Requirements

1. Ngrok account and binary installed
2. Local Flask server running on port 5000
3. Internet access for tunneling

## Defense

Defensive measures and detection strategies:

- Block outbound connections to dynamic tunnels like ngrok
- Inspect import URLs for suspicious domains
- Use firewall rules to restrict API callbacks

## Objectives

1. Make mock API accessible to GitLab
2. Facilitate payload injection over the internet
3. Maintain control over the mock responses

## Instructions

### Step 1: Start Ngrok Tunnel

**Context**: Expose the Flask port publicly.

**Command** ([[commands/ngrok-http-tunnel]]):
```bash
ngrok http 5000
```

> Outputs a forwarding URL like https://abc123.ngrok-free.app; use this in GitLab import.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Connection Proxy]] Proxy (tunneling)

### Sub-Techniques


## Commands Used

- [[commands/ngrok-http-tunnel]]

## Tools Used

- [[tools/ngrok]]

## Tags

- tunneling
- exposure
