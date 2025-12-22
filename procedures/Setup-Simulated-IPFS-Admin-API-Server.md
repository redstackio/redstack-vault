---
tags:
  - setup
  - simulation
  - ipfs
type: procedure
tools:
  - '[[tools/Python]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/start-ipfs-admin-api]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:53:38.420Z'
sub_techniques: []
id: 4689b3a8-b6ee-4d95-a3ae-7136259bdd5a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup Simulated IPFS Admin API Server

## Summary

This procedure sets up a simple HTTP server to simulate an IPFS gateway's internal admin API, allowing logging of incoming SSRF requests for demonstration purposes.

## Description

In the attack scenario, the internal IPFS gateway runs admin endpoints like /api/v0/shutdown and /api/v0/id. This simulation uses Python's http.server to mimic that on localhost:5001, capturing requests that traverse from the /ipfs/ path via the vulnerable curl rewrite. Prerequisites include Python 3 installed and the admin_api.py script available.

## Requirements

1. Python 3.10+ installed
2. Localhost access on port 5001
3. admin_api.py script defining the HTTP handler

## Defense

Defensive measures and detection strategies:

- Firewall rules to restrict admin API to localhost only
- Request logging and anomaly detection for unexpected paths
- Input validation on all URL handlers

## Objectives

1. Simulate internal service for exploitation testing
2. Log unauthorized access attempts
3. Verify SSRF reachability

## Instructions

### Step 1: Start the Admin API Server

**Context**: Launch the server to listen for internal requests from the exploited proxy.

**Command** ([[commands/start-ipfs-admin-api]]):
```bash
python3 admin_api.py
```

> This runs the script to start an HTTP server on 127.0.0.1:5001, logging all requests including paths like /api/v0/shutdown. Expected output: "Admin API listening on 127.0.0.1:5001" and subsequent request logs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/start-ipfs-admin-api]]

## Tools Used

- [[tools/Python]]

## Tags

- setup
- simulation
- ipfs
