---
id: tool-uuid-5
url: 'https://kubernetes.github.io/ingress-nginx/'
tags:
  - ingress
  - nginx
  - vulnerable
type: tool
verified: false
platforms:
  - Kubernetes
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.401Z'
validated: true
submitted: true
---
# NGINX-Ingress-Controller

**Status**: Unverified

## Overview

NGINX Ingress Controller manages external access to Kubernetes services, vulnerable component in this auth bypass.

## Description

Version k8s.gcr.io/ingress-nginx/controller:v1.0.0-beta.3 lacks proper URL normalization, allowing path traversal in external auth.

## Features

- Feature 1: HTTP routing and load balancing
- Feature 2: Annotation-based auth-url support
- Feature 3: Header forwarding (X-Original-Url)

## Installation

### Requirements

- Kubernetes cluster

### Install Commands

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.0.0-beta.3/deploy/static/provider/cloud/deploy.yaml
```

## Basic Usage

```bash
kubectl get ingress
```

### Common Options

| Option | Description |
|--------|-------------|
| Annotations | auth-url config |

## Examples

### Example 1: Basic Usage

```bash
# Deploy via Minikube addon
minikube addons enable ingress
```

### Example 2: Advanced Usage

```bash
# With auth annotation in ingress yaml
ingress.yaml: annotations: nginx.ingress.kubernetes.io/auth-url: "http://auth-service/verify"
```

## MITRE ATT&CK Mapping

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

- Pods: ingress-nginx-controller
- Logs: Encoded paths in access logs

## Related Procedures

- [[procedures/Exploit-Path-Traversal-for-Auth-Bypass]]

## Related Tools

- [[tools/Minikube]]

## References

- GitHub: https://kubernetes.github.io/ingress-nginx/
