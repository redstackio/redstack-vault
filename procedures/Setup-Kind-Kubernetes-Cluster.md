---
id: proc-001
tags:
  - kubernetes
  - setup
  - kind
type: procedure
tools:
  - '[[tools/kind]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/kind-create-cluster-with-config]]'
verified: false
platforms:
  - Kubernetes
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:23:49.953Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Setup-Kind-Kubernetes-Cluster

## Summary

This procedure provisions a local Kubernetes cluster using Kind (Kubernetes in Docker) configured specifically for testing NGINX Ingress vulnerabilities, including a labeled control-plane node and exposed ports for HTTP/HTTPS traffic.

## Description

Kind is used to create a lightweight, local Kubernetes environment that mimics a production setup. The configuration enables the ingress controller by labeling the node and mapping ports 80 and 443. This is the foundational step for reproducing the RCE exploit in a controlled environment. Prerequisites include Docker running on the host machine.

## Requirements

1. Docker installed and running on Linux/macOS/Windows.
2. Kind binary installed (via go install or binaries).
3. Local access to create YAML config files.
4. No prior cluster access needed; this sets up a new one.

## Defense

Defensive measures and detection strategies:

- Monitor for unauthorized Kind/Docker container creations in CI/CD or dev environments.
- Use cluster admission controllers to restrict local cluster provisioning in production-like setups.
- Log Docker daemon for suspicious image pulls related to Kind.

## Objectives

1. Establish a testable Kubernetes environment.
2. Expose necessary ports for ingress simulation.
3. Prepare for ingress controller deployment.
4. Validate cluster readiness for exploit steps.

## Instructions

### Step 1: Create Cluster Configuration

**Context**: Define lab.yaml with control-plane node labeled ingress-ready=true and extraPortMappings for ports 80/443 to enable ingress access.

**Command** ([[commands/kind-create-cluster-with-config]]):
No direct command here; manually create lab.yaml:

```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
  kubeadmConfigPatches:
  - |
    kind: InitConfiguration
    nodeRegistration:
      kubeletExtraArgs:
        node-labels: "ingress-ready=true"
  extraPortMappings:
  - containerPort: 80
    hostPort: 80
    protocol: TCP
  - containerPort: 443
    hostPort: 443
    protocol: TCP
```

> This YAML configures the cluster. Save as lab.yaml.

### Step 2: Provision the Cluster

**Context**: Use Kind to create the cluster from the config, which takes a few minutes to bootstrap.

**Command** ([[commands/kind-create-cluster-with-config]]):

```bash
kind create cluster --config lab.yaml
```

> Expected output includes pulling images, creating nodes, and "Cluster created" message. Verify with `kubectl cluster-info`.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/kind-create-cluster-with-config]]

## Tools Used

- [[tools/kind]]

## Tags

- kubernetes
- setup
- kind
