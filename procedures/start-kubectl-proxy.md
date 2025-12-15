---
id: proc-k8s-proxy-start
tags:
  - kubernetes
  - proxy
  - api-access
type: procedure
tools:
  - '[[tools/kubectl]]'
tactics:
  - '[[Lateral Movement]]'
commands:
  - '[[commands/kubectl-proxy-start]]'
verified: false
platforms:
  - Kubernetes
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Protocol Tunneling]]'
updated_at: '2025-12-14T17:26:30.564Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Protocol Tunneling]]'
---
# Start kubectl Proxy

## Summary

This procedure launches kubectl proxy to locally expose the Kubernetes API on port 8001, bypassing direct auth for script-based API calls.

## Description

Kubectl proxy authenticates once and forwards requests to the API server, ideal for scripting without token management. Enables curl access to endpoints like deployment/scale without additional setup.

## Requirements

1. Configured kubeconfig
2. Port 8001 free locally
3. kubectl installed

## Defense

Defensive measures and detection strategies:

- Disable proxy if not needed; monitor for proxy processes on nodes
- Use RBAC to limit proxy access
- Log all proxied requests

## Objectives

1. Provide local API endpoint
2. Simplify scripting
3. Maintain auth via kubectl

## Instructions

### Step 1: Run Proxy

**Context**: Start the proxy server.

**Command** ([[commands/kubectl-proxy-start]]):

```bash
kubectl proxy
```

> Starts serving on 127.0.0.1:8001. Expected: Logs confirm startup; keep terminal open.

### Step 2: Verify Access

**Context**: Test connectivity.

**Command** (curl):

```bash
curl http://127.0.0.1:8001/version
```

> Returns cluster version JSON.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Protocol Tunneling]] Protocol Tunneling

### Sub-Techniques


## Commands Used

- [[commands/kubectl-proxy-start]]

## Tools Used

- [[tools/kubectl]]

## Tags

- kubernetes
- proxy
- api-access
