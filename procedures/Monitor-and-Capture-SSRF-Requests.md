---
id: proc-k8s-monitor-requests
tags:
  - ssrf
  - monitoring
  - network-capture
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote System Discovery]]'
updated_at: '2025-12-14T04:08:54.840Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Remote System Discovery]]'
---
---

# Monitor-and-Capture-SSRF-Requests

## Summary

This procedure sets up a listener on the attacker server to capture the incoming POST request from kube-controller-manager, verifying the half-blind SSRF exploitation.

## Description

The SSRF request is half-blind because the attacker receives the request but cannot directly see the response unless escalated. Tools like netcat or a simple HTTP server log the payload, confirming internal origin and control.

## Requirements

1. Attacker server accessible via the resturl (e.g., public IP:6666)
2. Firewall allows inbound on port 6666
3. Basic networking tools (netcat)

## Defense

Defensive measures and detection strategies:

- Block outbound requests from masters to untrusted endpoints
- Log and alert on provisioning to external URLs
- Use network segmentation for control plane

## Objectives

1. Confirm SSRF request delivery
2. Analyze payload for further exploitation
3. Validate arbitrary URL control

## Instructions

### Step 1: Start Listener

**Context**: Listen for incoming connections on the specified port.

**Command** (netcat):
```bash
nc -l 6666
```

> Expected output: Connection from cluster IP, followed by POST / HTTP/1.1 with JSON body containing volume request details.

### Step 2: Log and Verify

**Context**: Capture the full request headers and body.

**Command** (enhanced with tee for logging):
```bash
nc -l 6666 | tee request.log
```

> Expected output: Logged request showing internal source IP and provisioning data.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Remote System Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- monitoring
- network-capture

---
