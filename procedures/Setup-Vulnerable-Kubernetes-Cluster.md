---
id: proc-k8s-setup-vuln-cluster-001
tags:
  - kubernetes
  - setup
type: procedure
tools:
  - '[[tools/minikube]]'
  - '[[tools/kubectl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/start-minikube-vulnerable]]'
verified: false
platforms:
  - Kubernetes
  - Linux
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:09:00.746Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-Vulnerable-Kubernetes-Cluster

## Summary

This procedure sets up a local Kubernetes cluster using minikube at version 1.18.6 to reproduce the SSRF vulnerability in kube-apiserver admission webhooks.

## Description

In cloud environments like GKE, AKS, EKS, the kube-apiserver processes admission webhooks without validating external URLs, allowing SSRF. This step simulates a vulnerable cluster locally. Prerequisites include Docker installed and sufficient host resources (2GB RAM, 2 CPUs).

## Requirements

1. Minikube and kubectl installed
2. Docker runtime on host
3. No VM driver for direct execution

## Defense

- Use managed clusters with auto-upgrades to patch versions
- Monitor for minikube or unusual cluster startups in logs

## Objectives

1. Initialize a vulnerable Kubernetes v1.18.6 cluster
2. Verify cluster readiness for exploitation
3. Prepare environment for webhook deployment

## Instructions

### Step 1: Start Minikube Cluster

**Context**: Launch the cluster with vulnerable version and none driver to match production simulation.

**Command** ([[commands/start-minikube-vulnerable]]):
```bash
minikube start --vm-driver=none --kubernetes-version='v1.18.6'
```

> This command downloads and starts the cluster, updating kubeconfig. Expected output: Cluster running, API server accessible.

### Step 2: Verify Cluster

**Context**: Confirm the setup.

**Command** ([[commands/verify-kubectl]]):
```bash
kubectl cluster-info
kubectl version
```

> Output shows server version 1.18.6 and cluster details.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/start-minikube-vulnerable]]
- [[commands/verify-kubectl]]

## Tools Used

- [[tools/minikube]]
- [[tools/kubectl]]

## Tags

- kubernetes
- setup
- vulnerable-cluster
