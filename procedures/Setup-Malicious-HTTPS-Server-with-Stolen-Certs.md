---
tags:
  - malicious-server
  - https
  - redirect
type: procedure
tools:
  - '[[tools/maliciousHttpsServer.py]]'
tactics:
  - '[[Lateral Movement]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[Hijack Execution Flow]]'
skill_level: advanced
impact_level: critical
detection_risk: medium
sub_techniques: []
id: 3e1786b7-3388-4f0c-9035-5681a8d2da3f
created_at: '2025-12-14T04:08:48.113Z'
updated_at: '2025-12-14T04:08:48.113Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Hijack Execution Flow]]'
---
# Setup Malicious HTTPS Server with Stolen Certs

## Summary

This procedure deploys a Python-based HTTPS server on the attacker's machine using stolen Docker certificates to impersonate the daemon and issue HTTP redirects for SSRF exploitation.

## Description

The custom script creates a TLS-enabled server listening on port 1111, responding to Docker API calls with 3xx redirects to internal targets (e.g., Google metadata). When the hijacked port 2376 forwards traffic, the Runner's client follows redirects blindly due to no policy in official_docker_client.go, enabling SSRF to localhost/link-local networks.

## Requirements

1. Stolen server.pem and server-key.pem files
2. Python 3 with http.server and ssl modules
3. Attacker machine with public IP reachable from executor

## Defense

Defensive measures and detection strategies:

- Implement redirect limits in HTTP clients (e.g., max redirects)
- Validate Docker daemon endpoints strictly (no external forwards)
- Monitor for anomalous TLS connections to Docker port
- Use certificate pinning for daemon comms

## Objectives

1. Mimic Docker daemon with valid TLS
2. Redirect API calls to internal services
3. Facilitate blind SSRF with request methods

## Instructions

### Step 1: Prepare Certificates

**Context**: Place stolen certs in the script directory.

Copy server.pem and server-key.pem to the working directory on attacker machine.

### Step 2: Run Malicious Server

**Context**: Start the HTTPS server configured for redirects.

**Command** (using [[tools/maliciousHttpsServer.py]]):
```bash
python3 maliciousHttpsServer.py --cert server.pem --key server-key.pem --port 1111
```

> The script handles Docker API paths, e.g., redirects GET /v1.41/images/create to metadata endpoint. Customize redirects for POST/DELETE.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]]

### Techniques

- [[Hijack Execution Flow]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/maliciousHttpsServer.py]]

## Tags

- malicious-server
- https
- redirect
