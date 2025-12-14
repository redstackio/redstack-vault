---
id: proc-uuid-1
tags:
  - kubernetes
  - setup
  - deployment
  - minikube
type: procedure
tools:
  - '[[tools/Minikube]]'
  - '[[tools/Docker]]'
  - '[[tools/kubectl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/install-minikube]]'
  - '[[commands/enable-minikube-addons]]'
  - '[[commands/docker-build-auth-service]]'
  - '[[commands/docker-build-protected-service]]'
  - '[[commands/docker-build-public-service]]'
  - '[[commands/minikube-load-auth-image]]'
  - '[[commands/minikube-load-protected-image]]'
  - '[[commands/minikube-load-public-image]]'
  - '[[commands/kubectl-apply-app]]'
verified: false
platforms:
  - Kubernetes
  - Docker
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:31:19.486Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Setup-Minikube-and-Deploy-Vulnerable-Kubernetes-Config

## Summary

This procedure sets up a local Minikube Kubernetes cluster, builds Docker images for auth, protected, and public services, and deploys a vulnerable NGINX Ingress configuration with external authentication to simulate the environment for auth bypass testing.

## Description

The setup replicates a Kubernetes environment where NGINX Ingress uses an external auth service (auth-service on port 8080) annotated with nginx.ingress.kubernetes.io/auth-url. The configuration includes a public service (no auth), a protected service (requires X-Api-Key), and the ingress vulnerable to path traversal due to improper URL normalization of encoded '../' (%2F). This is based on testing in Minikube to reproduce the HackerOne-reported issue. Prerequisites include downloading k8s-ingress-auth-bypass.zip containing app.yaml and service directories.

## Requirements

1. Host system with Docker 20.10.8 installed (Windows 10 Pro compatible)
2. Download of k8s-ingress-auth-bypass.zip and extraction
3. Admin privileges for Minikube installation
4. kubectl configured for Minikube

## Defense

Defensive measures and detection strategies:

- Use updated NGINX Ingress versions with proper URL normalization
- Implement auth service validation that decodes and normalizes paths fully
- Monitor ingress logs for encoded traversal patterns (%2F in paths)
- Enable Kubernetes network policies to restrict service access

## Objectives

1. Create a reproducible local Kubernetes environment for vulnerability testing
2. Deploy services and ingress mimicking production auth setup
3. Ensure baseline functionality before exploitation

## Instructions

### Step 1: Install and Start Minikube

**Context**: Install Minikube v1.23.2 to create a local Kubernetes cluster with Kubernetes v1.22.2.

**Command** ([[commands/install-minikube]]):
```bash
# Platform-specific installation (e.g., Chocolatey on Windows: choco install minikube; or brew on macOS)
minikube start --kubernetes-version=v1.22.2
```

> This initializes the cluster using Docker as the driver. Expected output: Cluster running with API server accessible.

### Step 2: Enable Ingress Addons

**Context**: Activate NGINX Ingress controller and DNS for local testing.

**Command** ([[commands/enable-minikube-addons]]):
```bash
minikube addons enable ingress
minikube addons enable ingress-dns
```

> Enables the vulnerable controller (v1.0.0-beta.3 by default). Expected output: Addons enabled confirmation.

### Step 3: Build Docker Images

**Context**: Compile images for services using provided Dockerfiles (Flask-based for auth).

**Command** ([[commands/docker-build-auth-service]]):
```bash
cd auth-service; docker build -t auth-service:0.0.4 .
```

> Builds auth-service image. Repeat for protected and public with respective commands.

### Step 4: Load Images to Minikube

**Context**: Make images available in the cluster's Docker daemon.

**Command** ([[commands/minikube-load-auth-image]]):
```bash
minikube image load auth-service:0.0.4
```

> Loads the image. Expected output: Image pushed successfully. Repeat for other images.

### Step 5: Deploy Configuration

**Context**: Apply manifests to create deployments, services, and ingress.

**Command** ([[commands/kubectl-apply-app]]):
```bash
kubectl apply -f app.yaml
```

> Deploys everything. Expected output: Resources created (deployments, services, ingress).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter

### Sub-Techniques

- None

## Commands Used

- [[commands/install-minikube]]
- [[commands/enable-minikube-addons]]
- [[commands/docker-build-auth-service]]
- [[commands/kubectl-apply-app]]

## Tools Used

- [[tools/Minikube]]
- [[tools/Docker]]
- [[tools/kubectl]]

## Tags

- [[kubernetes]]
- [[setup]]
- [[deployment]]
