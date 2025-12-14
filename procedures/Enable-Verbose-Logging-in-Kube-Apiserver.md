---
id: proc-k8s-enable-logging-001
tags:
  - logging
  - kubernetes
type: procedure
tools:
  - '[[tools/kubectl]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Kubernetes
  - Linux
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Disable or Modify Tools]]'
updated_at: '2025-12-14T04:08:55.706Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Disable or Modify Tools]]'
---
# Enable-Verbose-Logging-in-Kube-Apiserver

## Summary

Modify the kube-apiserver manifest to enable detailed logging, allowing capture of full HTTP response bodies during SSRF exploitation.

## Description

At high klog verbosity (v=10), client-go logs entire responses from webhook requests, including redirects to internal services. This is key for leaking metadata in cloud setups. Edit the static pod manifest directly.

## Requirements

1. Cluster-admin access to edit manifests
2. Access to /etc/kubernetes/manifests/ on control plane node
3. Restart tolerance for apiserver

## Defense

- Restrict manifest edits via RBAC
- Monitor log level changes and unusual verbosity settings
- Use centralized logging to detect sensitive data exposure

## Objectives

1. Add logging flags to apiserver command
2. Ensure logs are directed to accessible files
3. Prepare for response body capture

## Instructions

### Step 1: Edit Manifest

**Context**: Append flags to enable logging without stderr.

**Command** (Manual Edit):
No direct command; use vi or sed:
```bash
vi /etc/kubernetes/manifests/kube-apiserver.yaml
```

> Add to spec.containers[0].command: `--log-dir=/var/log --logtostderr=false`. Save and exit; pod restarts automatically.

### Step 2: Verify Logging

**Context**: Check if flags applied.

**Command** ([[commands/check-apiserver-logs]]):
```bash
kubectl logs -n kube-system kube-apiserver-$(hostname)
```

> Output shows log paths and no stderr warnings.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Disable or Modify Tools]] Disable or Modify Tools (Logging)

### Sub-Techniques


## Commands Used

- [[commands/check-apiserver-logs]]

## Tools Used

- [[tools/kubectl]]

## Tags

- logging
- apiserver
- verbosity
