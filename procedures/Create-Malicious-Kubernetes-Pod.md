---
tags:
  - kubernetes
  - pod-creation
type: procedure
tools:
  - '[[tools/kubectl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/kubectl-run-pod]]'
verified: false
platforms:
  - Kubernetes
  - Linux
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:26:56.641Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 6a6eb5bb-5783-4133-b6fe-ffd48929a02d
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Create-Malicious-Kubernetes-Pod

## Summary

This procedure deploys a simple pod in a Kubernetes cluster using kubectl and a lightweight image like busybox, providing a foothold for further exploitation such as disk DoS via bind-mounted files.

## Description

In a Kubernetes environment, attackers with cluster access can create pods to execute commands that interact with host resources. This step sets up a pod named 'rate' that mounts host files like /etc/hosts read-write, enabling subsequent disk exhaustion attacks. The pod runs in the default namespace without special privileges, exploiting the lack of resource limits.

## Requirements

1. kubectl installed and configured with cluster access
2. Permissions to create pods (e.g., via RBAC role)
3. Busybox image available in the registry

## Defense

Defensive measures and detection strategies:

- Implement Pod Security Policies to restrict pod creation
- Use NetworkPolicies to limit pod deployments
- Monitor kubectl API calls for unusual pod creations via audit logs

## Objectives

1. Gain container runtime access within the cluster
2. Establish baseline for bind-mount interactions
3. Prepare for resource exhaustion

## Instructions

### Step 1: Deploy the Pod

**Context**: Create a pod to serve as the attack vector.

**Command** ([[commands/kubectl-run-pod]]):
```bash
kubectl run rate --image=busybox
```

> This creates a pod named 'rate' using the busybox image, which provides basic Unix utilities. Expected output: "pod/rate-c848c5c8b-5b8vm created" (pod name may vary with hash).

### Step 2: Verify Pod Status

**Context**: Ensure the pod is running before proceeding.

**Command** (kubectl get pods):
```bash
kubectl get pods
```

> Lists pods; look for 'rate-<hash>' in Running state.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used

- [[commands/kubectl-run-pod]]

## Tools Used

- [[tools/kubectl]]

## Tags

- [[kubernetes]]
- [[pod-creation]]
