---
id: proc-run-repro-script-001
tags:
  - ssrf
  - reproduction
  - gke
type: procedure
tools:
  - '[[tools/kubectl]]'
  - '[[tools/Docker]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/run-reproduction-script-gke]]'
  - '[[commands/cleanup-reproduction-environment-gke]]'
verified: false
platforms:
  - Kubernetes
  - Cloud (GKE)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Application Access Token]]'
updated_at: '2025-12-14T03:46:08.948Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
---
# Run-Reproduction-Script-to-Observe-Redirects

## Summary

Executes a reproduction script to automate hijacker deployment, trigger control plane requests, and capture SSRF redirects in a GKE or AKS environment, demonstrating token leakage.

## Description

The run.sh script handles scaling, deployment, and logging for managed Kubernetes. Setting USE_GKE=1 configures for Google Kubernetes Engine, including node pool adjustments. It deploys the hijacker, waits for traffic, and logs to output.txt. Use CLEANUP=1 variant for teardown. Requires script access and cluster context.

## Requirements

1. run.sh script in local directory
2. kubectl and Docker access to cluster
3. GKE/AKS cluster with metrics-server enabled

## Defense

Defensive measures and detection strategies:

- Log and alert on pod scaling in kube-system
- Network policies to block external redirects from API servers
- SIEM monitoring for anomalous external requests from control plane IPs

## Objectives

1. Automate SSRF reproduction
2. Capture evidence of redirects and leaks
3. Test in managed environments like GKE

## Instructions

### Step 1: Execute Reproduction Script

**Context**: Run the script to deploy and observe initial redirects.

Execute [[commands/run-reproduction-script-gke]]:

```bash
USE_GKE=1 ./run.sh
```

> Deploys hijacker, triggers requests; output.txt shows logs from components like kube-controller-manager.

### Step 2: Review Captured Logs

**Context**: Analyze output for SSRF evidence.

No command; inspect output.txt for 30X responses and incoming requests.

> Expect entries with bearer tokens and headers from internal IPs.

### Step 3: Cleanup if Needed

**Context**: Tear down to restore environment.

Execute [[commands/cleanup-reproduction-environment-gke]]:

```bash
USE_GKE=1 CLEANUP=1 ./run.sh
```

> Removes pod and scales up metrics-server.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Steal Application Access Token]]

### Sub-Techniques


## Commands Used

- [[commands/run-reproduction-script-gke]]
- [[commands/cleanup-reproduction-environment-gke]]

## Tools Used

- [[tools/kubectl]]
- [[tools/Docker]]

## Tags

- ssrf
- reproduction
- gke
