---
id: c1208877-1b69-4dbb-bd23-3541be592851
name: Kubernetes-Endpoint-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:01.397235+00:00'
updated_at: '2023-04-10T20:34:01.643819+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Remote System Discovery|T1018 - Remote System Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Interesting endpoints to reach]]'
  - '[[tags/Kubernetes]]'
commands:
  - '[[commands/curl-kubernetes-list-pods-default]]'
  - '[[commands/curl-kubernetes-list-secrets-default]]'
  - '[[commands/curl-kubernetes-list-deployments-default]]'
  - '[[commands/curl-kubernetes-list-daemonsets-default]]'
platforms:
  - Kubernetes
tools: []
validated: true
---

# Kubernetes-Endpoint-Enumeration

## Summary

This procedure enumerates key resources in a Kubernetes cluster's default namespace, including pods, secrets, deployments, and daemonsets, using authenticated API calls via curl. It allows an attacker with valid credentials to map the cluster's structure, identify running services, and discover sensitive configurations for further exploitation such as lateral movement or privilege escalation.

## Description

Kubernetes clusters expose an API server that manages resources like pods (running containers), secrets (sensitive data like credentials), deployments (pod management configurations), and daemonsets (pods running on every node). With a valid JWT token obtained from service account credentials or user authentication, an attacker can query these endpoints to gather intelligence on the environment. This discovery technique is useful in cloud-native environments to understand workload distribution, potential weak points in configurations, and exposed secrets that could lead to broader compromise. The procedure assumes direct network access to the API server, typically over HTTPS on port 6443, and focuses on the default namespace to start reconnaissance without broader permissions.

## Requirements

1. Valid JWT token for Kubernetes API authentication (e.g., from a service account token or kubeconfig).
2. Network access to the Kubernetes API server (usually HTTPS on port 6443).
3. Curl or equivalent HTTP client installed on the attacker's machine.
4. Knowledge of the API server endpoint (master IP and port).

## Defense

- Implement Role-Based Access Control (RBAC) to restrict API access to least privilege, denying list operations on sensitive resources like secrets.
- Enforce network policies to limit traffic to the API server, using tools like Calico or Cilium for pod-to-API isolation.
- Enable API server auditing and encryption in transit (mTLS) to log and protect authentication requests.
- Use tools like Kubernetes Audit Logs or Falco to monitor anomalous API queries from unauthorized sources.

## Objectives

1. Enumerate pods, secrets, deployments, and daemonsets in the default namespace.
2. Gather details on running services, stored credentials, and cluster configurations.
3. Identify attack vectors such as misconfigured secrets or over-privileged deployments for escalation.

## Instructions

### Step 1: List Pods in Default Namespace

**Context**: This step retrieves a list of all pods in the default namespace, revealing running containers, their statuses, and associated metadata to map active workloads.

**Command** ([[commands/curl-kubernetes-list-pods-default]]):
```bash
curl -v -H "Authorization: Bearer $_JWT_TOKEN" https://$_API_SERVER/api/v1/namespaces/default/pods/
```

> This command authenticates with the JWT token and queries the core API v1 endpoint for pods. Replace $_JWT_TOKEN with the actual bearer token and $_API_SERVER with the API server URL (e.g., kubernetes.default.svc:443). The verbose (-v) flag shows request/response details for troubleshooting. Success is indicated by a 200 OK response with JSON containing pod objects; errors like 403 Forbidden suggest insufficient RBAC permissions.

### Step 2: List Secrets in Default Namespace

**Context**: Secrets often store credentials or keys; listing them exposes potential plaintext or encoded sensitive data that can be further retrieved or cracked.

**Command** ([[commands/curl-kubernetes-list-secrets-default]]):
```bash
curl -v -H "Authorization: Bearer $_JWT_TOKEN" https://$_API_SERVER/api/v1/namespaces/default/secrets/
```

> Query the secrets endpoint to list all stored secrets. Use the same authentication as above. Expected output is JSON with secret names and types (e.g., Opaque, kubernetes.io/tls). If secrets are base64-encoded, follow up by fetching individual ones with /secrets/{name}. A successful response lists resources without authentication failures.

### Step 3: List Deployments in Default Namespace

**Context**: Deployments manage replica sets and pod scaling; enumerating them reveals application architectures, versions, and labels for targeting specific services.

**Command** ([[commands/curl-kubernetes-list-deployments-default]]):
```bash
curl -v -H "Authorization: Bearer $_JWT_TOKEN" https://$_API_SERVER/apis/extensions/v1beta1/namespaces/default/deployments
```

> This uses the extensions API (note: in newer Kubernetes versions, use apps/v1/deployments for compatibility). The response includes deployment specs like replicas and selectors. Verify success by checking for JSON array of deployment objects; deprecated API warnings may appear but do not indicate failure.

### Step 4: List DaemonSets in Default Namespace

**Context**: DaemonSets ensure pods run on all nodes (e.g., logging agents); listing them identifies node-level services that could be exploited for persistence or lateral movement across the cluster.

**Command** ([[commands/curl-kubernetes-list-daemonsets-default]]):
```bash
curl -v -H "Authorization: Bearer $_JWT_TOKEN" https://$_API_SERVER/apis/extensions/v1beta1/namespaces/default/daemonsets
```

> Similar to deployments, query the extensions API for daemonsets. Output shows node selectors and pod templates. Success is a 200 response with daemonset details; use this to pinpoint cluster-wide agents for further probing.
