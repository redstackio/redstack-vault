---
id: proc-monitor-unavailability-001
tags:
  - monitoring
  - dos
  - api-server
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-k8s-version]]'
verified: false
platforms:
  - Kubernetes
  - GCP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:32:01.414Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Monitor-API-Server-Unavailability

## Summary

This procedure checks the Kubernetes API Server's responsiveness post-DoS trigger by querying the /version endpoint and reviewing GCP logs, confirming the control plane outage and GKE repair actions.

## Description

After concurrent secret creations, the API Server becomes unresponsive due to resource exhaustion. Curl to the secure /version endpoint (via kubectl proxy or direct) will hang, indicating DoS. GCP audit logs show internal server errors (500s) and control plane reprovisioning events in GKE. This validates the vulnerability's impact: temporary cluster unavailability until auto-repair.

## Requirements

1. Access to kubectl proxy or API endpoint URL
2. GCP console or gcloud for logs
3. Bastion VM for curl

## Defense

Defensive measures and detection strategies:

- Set up alerting on API Server error rates and memory metrics
- Use GKE's autorepair and autoupgrade features
- Review audit logs for patterns of concurrent large requests

## Objectives

1. Confirm API Server hang or crash
2. Observe error logs and recovery
3. Validate DoS success

## Instructions

### Step 1: Probe Version Endpoint

**Context**: Test basic API availability.

**Command** ([[commands/curl-k8s-version]]):
```bash
kubectl proxy & curl http://localhost:8001/version
# Or direct: curl -k https://<api-endpoint>/version
```

> Queries version; expected output: Hangs or times out during DoS.

### Step 2: Check Client Errors

**Context**: Observe kubectl command outputs.

**Command** ([[commands/kubectl-describe-cluster]]):
```bash
kubectl get nodes
```

> Fails; expected output: Connection timeout or unreachable.

### Step 3: Review GCP Logs

**Context**: Inspect audit and operations logs.

**Command** ([[commands/gcloud-logging-read]]):
```bash
gcloud logging read "resource.type=k8s_cluster AND jsonPayload.status=500" --project=gkek8s-178117 --limit=10
```

> Shows errors; expected output: Internal server errors, repair events.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used

- [[commands/curl-k8s-version]]
- [[commands/gcloud-logging-read]]
- [[commands/kubectl-describe-cluster]]

## Tools Used

- [[tools/curl]]

## Tags

- monitoring
- dos
- api-server
