---
tags:
  - hostnetwork
  - pod-deployment
  - kubernetes
type: procedure
tools:
  - '[[tools/kubectl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/kubectl-apply-hostnetwork-pod]]'
verified: false
platforms:
  - Kubernetes
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Deploy Container]]'
updated_at: '2025-12-14T17:28:44.908Z'
sub_techniques: []
id: 51256e78-b89f-4dae-9f97-9bfcb97f611d
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Deploy Container]]'
---
# Deploy-Malicious-Pod-with-HostNetwork

## Summary

Deploys a pod configured with hostNetwork=true to share the host's network namespace, granting access to raw sockets via default CAP_NET_RAW capability for subsequent MITM attacks.

## Description

By setting hostNetwork: true, the pod bypasses container network isolation and operates in the host's namespace, allowing tools like Scapy to sniff and inject packets on the host's interfaces, including traffic to the metadata service at 169.254.169.254. This is exploitable in clusters without capability restrictions. The pod uses ubuntu:latest with an infinite sleep to keep it running.

## Requirements

1. kubectl configured for the target cluster
2. Permissions to create pods
3. No PodSecurityPolicy blocking hostNetwork

## Defense

Defensive measures and detection strategies:

- Enforce PodSecurityStandards to deny hostNetwork
- Audit pod specs for hostNetwork usage
- Use admission controllers to validate capabilities

## Objectives

1. Gain host-level network access from within a container
2. Enable raw packet manipulation for MITM
3. Maintain pod persistence for exploit execution

## Instructions

### Step 1: Apply Pod Manifest

**Context**: Create the pod that enables host network sharing.

**Command** ([[commands/kubectl-apply-hostnetwork-pod]]):
```bash
kubectl apply -f - <<'EOF'
apiVersion: v1
kind: Pod
metadata:
  name: ubuntu-node
spec:
  hostNetwork: true
  containers:
  - name: ubuntu
    image: ubuntu:latest
    command: [ "/bin/sleep", "inf" ]
EOF
```

> Deploys the pod. Expected output: pod/ubuntu-node created.

### Step 2: Verify Pod Status

**Context**: Ensure the pod is running and scheduled.

**Command** ([[commands/kubectl-get-pods]]):
```bash
kubectl get pods
```

> Lists pods. Expected output: ubuntu-node Running.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Deploy Container]] Deploy Container

### Sub-Techniques

- None

## Commands Used

- [[commands/kubectl-apply-hostnetwork-pod]]
- [[commands/kubectl-get-pods]]

## Tools Used

- [[tools/kubectl]]

## Tags

- pod
- network-namespace
- exploitation
