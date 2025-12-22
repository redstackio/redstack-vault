---
id: proc-monitor-redirects-001
tags:
  - ssrf
  - token-leak
  - monitoring
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
  - '[[Automated Collection]]'
updated_at: '2025-12-14T03:46:08.946Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Automated Collection]]'
---
# Monitor-and-Capture-Redirected-Requests

## Summary

Monitors logs from the hijacked pod to capture incoming requests redirected via SSRF, including bearer tokens from control plane components like kube-controller-manager and azurepolicyaddon.

## Description

Once hijacked, the malicious server logs all requests, revealing sensitive data as clients blindly follow 30X redirects without validation. This procedure involves tailing pod logs and analyzing for tokens, headers, and origins (e.g., IPs like 34.122.28.173). Applicable in GKE/AKS where control plane traffic is internal but redirects externalize it.

## Requirements

1. Hijacker pod running in kube-system
2. kubectl access for log retrieval
3. Attacker endpoint configured in server for redirect target

## Defense

Defensive measures and detection strategies:

- Disable redirect following in Kubernetes clients (e.g., via client-go config)
- Implement webhook validation for API responses
- Correlate logs for unexpected external traffic from cluster IPs

## Objectives

1. Capture leaked bearer tokens and headers
2. Verify SSRF impact on sensitive data
3. Log requests for further analysis or exfiltration

## Instructions

### Step 1: Tail Pod Logs

**Context**: Stream logs from the malicious pod to observe real-time requests.

Use [[tools/kubectl]]:

```bash
kubectl logs -f <hijacker-pod-name> -n kube-system
```

> Streams logs; look for entries from components like cpmonitor with Authorization: Bearer headers.

### Step 2: Trigger Additional Traffic

**Context**: Force more requests to generate logs.

Run cluster health checks or scale resources to provoke API calls to metrics-server.

> Increases log volume; expect redirects to attacker server.

### Step 3: Analyze Captured Data

**Context**: Review logs for sensitive info.

No command; grep output.txt for 'Bearer' or external IPs.

> Identifies tokens; validate by decoding JWTs for cluster secrets.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Automated Collection]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/kubectl]]

## Tags

- ssrf
- token-leak
- monitoring
