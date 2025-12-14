---
tags:
  - ssrf
  - token-leak
  - logs
type: procedure
tools:
  - '[[tools/kubectl]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Kubernetes
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Application Access Token]]'
updated_at: '2025-12-14T17:32:38.957Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: aa74b1fb-2eed-4caf-be2c-e91a1acb3cb7
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
---
# Observe-Redirected-Traffic-and-Token-Leakage

## Summary

Monitors control plane components interacting with the hijacked metrics-server, capturing 30X redirects that leak bearer tokens via SSRF to external endpoints.

## Description

Control plane clients like kube-controller-manager and azurepolicyaddon blindly follow redirects from the malicious server, sending requests (with auth headers) to attacker endpoints. Involves logging traffic; outcomes include token exfiltration and potential spamming. Requires hijacked setup; observe in logs or external server.

## Requirements

1. Hijacked pod active
2. External endpoint (e.g., IP 20.85.59.5) to receive redirects
3. Access to cluster logs or output capture

## Defense

Defensive measures and detection strategies:

- Disable blind redirect following in API clients
- Log and alert on 30X responses from internal services
- Monitor external connections from control plane

## Objectives

1. Confirm SSRF via redirect following
2. Capture leaked Authorization: Bearer tokens
3. Demonstrate impact like spamming from cloud IPs

## Instructions

### Step 1: Trigger API Calls

**Context**: Wait for or induce control plane polling of metrics API.

No command; components auto-call /metrics endpoint.

> Expected: Requests hit malicious pod.

### Step 2: Capture Logs

**Context**: Review output from reproduction or external server logs for redirects.

**Command** ([[tools/kubectl]]):

```bash
kubectl logs -n kube-system malicious-metrics
```

> Shows redirect traffic; expected output: Logs with Host: 20.85.59.5 and Authorization: Bearer <token>.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Steal Application Access Token]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/kubectl]]

## Tags

- ssrf
- token-leak
- logs
