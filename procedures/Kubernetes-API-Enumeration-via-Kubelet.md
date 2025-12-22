---
id: 061199cf-7813-4b7a-9ffa-c32673ba0bab
name: Kubernetes-API-Enumeration-via-Kubelet
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:01.549081+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/System Service Discovery|T1007 - System Service Discovery]]'
sub_techniques: []
tags:
  - Kubernetes
  - kubelet
  - API enumeration
  - discovery
commands:
  - '[[commands/curl-kubelet-root-endpoint]]'
  - '[[commands/curl-kubelet-pods-endpoint]]'
platforms:
  - Kubernetes
  - Linux
tools:
  - '[[tools/cURL]]'
validated: true
---

# Kubernetes-API-Enumeration-via-Kubelet

## Summary

This procedure uses the kubelet API to enumerate key details about a Kubernetes cluster, including node information and running pods. By accessing exposed kubelet endpoints without authentication, an attacker can discover the cluster's API server addresses, pod metadata, container images, and application configurations, providing a foothold for further reconnaissance or lateral movement in containerized environments.

## Description

The kubelet is the primary node agent in Kubernetes, responsible for managing pods and containers on worker nodes. It exposes an API on port 10250 (secure) or 10255 (insecure/read-only) that can be queried for cluster state information. If the kubelet API is misconfigured with anonymous access enabled, attackers with network reachability can query endpoints like the root path for node details and /pods for a list of running workloads. This technique maps to system service discovery as it reveals internal service configurations and running processes in the cluster. It is particularly effective against clusters in cloud environments where nodes may have public IPs or be accessible via VPC peering. Success enables mapping the attack surface for subsequent exploits like pod escape or secret extraction.

## Requirements

1. Network access to the target Kubernetes node's IP on port 10255 (insecure kubelet API).
2. The kubelet must have anonymous authentication enabled (common misconfiguration).
3. Curl or equivalent HTTP client installed on the attacker's machine.
4. Knowledge of the node's IP address (obtainable via prior network scanning).

## Defense

- Disable the insecure kubelet port (10255) and enforce TLS on 10250 with authentication (e.g., via --anonymous-auth=false and --tls-cert-file).
- Implement network policies or firewalls to restrict kubelet API access to only the control plane components.
- Enable Kubernetes audit logging and monitor for unauthorized API queries using tools like Falco or Prometheus.
- Regularly scan for exposed kubelet services using tools like kube-hunter or Trivy.

## Objectives

1. Retrieve node-level information from the kubelet root endpoint to identify API server addresses and cluster versions.
2. Enumerate running pods to discover application names, namespaces, images, and potential sensitive workloads.
3. Gather metadata for planning targeted attacks, such as identifying privileged pods or exposed services.

## Instructions

### Step 1: Query Kubelet Root Endpoint

**Context**: Start by accessing the kubelet root endpoint to obtain high-level node information, including the Kubernetes version, kubelet status, and references to the API server. This step reveals the cluster's API address if proxying is enabled and provides context for the node's role in the cluster.

**Command** ([[commands/curl-kubelet-root-endpoint]]):
```bash
curl -k https://$_NODE_IP:10255
```

> This command performs an unauthenticated GET request to the kubelet root, bypassing SSL verification with -k due to self-signed certificates. It returns JSON data about the node, which may include the API server's endpoint under allocated resources or conditions.

**Expected Output**:
```
{
  "kind": "Node",
  "apiVersion": "v1",
  "metadata": {
    "name": "node-1",
    "...": "..."
  },
  "status": {
    "conditions": [...],
    "nodeInfo": {
      "kubeletVersion": "v1.25.0",
      "...": "..."
    }
  }
}
```

### Step 2: Enumerate Pods via Kubelet API

**Context**: Follow up by querying the /pods endpoint to list all pods on the node. This exposes sensitive details like pod names, namespaces, container images, ports, and volumes, allowing attackers to identify high-value targets such as databases or configmaps with secrets.

**Command** ([[commands/curl-kubelet-pods-endpoint]]):
```bash
curl -k https://$_NODE_IP:10255/pods
```

> This command targets the pods resource path, again bypassing SSL. The response is a JSON array of pods, which can be parsed to extract API server interactions or service endpoints. If the second original endpoint used HTTP, switch to it only if HTTPS fails, but HTTPS is recommended for consistency.

**Expected Output**:
```
{
  "kind": "PodList",
  "apiVersion": "v1",
  "items": [
    {
      "metadata": {
        "name": "app-pod-abc123",
        "namespace": "default",
        "...": "..."
      },
      "spec": {
        "containers": [
          {
            "name": "nginx",
            "image": "nginx:1.21",
            "ports": [
              {
                "containerPort": 80
              }
            ]
          }
        ]
      }
    }
  ]
}
```
