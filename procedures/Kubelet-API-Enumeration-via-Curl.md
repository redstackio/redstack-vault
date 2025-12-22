---
id: b1e526ca-9d9c-4521-857c-76df4681381c
name: Kubelet-API-Enumeration-via-Curl
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:01.520451+00:00'
updated_at: '2023-04-10T20:34:01.297998+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Remote System Discovery|T1018 - Remote System Discovery]]'
sub_techniques: []
tags:
  - '[[tags/API addresses that you should know]]'
  - '[[tags/Kubelet API]]'
  - '[[tags/Kubernetes]]'
commands:
  - '[[commands/curl-kubelet-root-endpoint]]'
  - '[[commands/curl-kubelet-metrics-endpoint]]'
  - '[[commands/curl-kubelet-pods-endpoint]]'
platforms:
  - Kubernetes
  - Linux
tools: []
validated: true
---

# Kubelet-API-Enumeration-via-Curl

## Summary

This procedure enumerates key information from the Kubelet API on Kubernetes worker nodes by querying its root, metrics, and pods endpoints using curl. It allows discovery of node status, resource metrics, and running pods, which can reveal potential targets for lateral movement or exploitation within the cluster.

## Description

The Kubelet is the primary node agent running on each worker node in a Kubernetes cluster, responsible for managing pod lifecycles and reporting node status to the control plane. The Kubelet API, exposed on port 10250 by default, provides endpoints for introspection. An attacker with network access to worker nodes can query these unauthenticated or weakly protected endpoints to gather intelligence on the cluster's composition, resource usage, and running workloads. This technique is useful during reconnaissance phases to map the environment and identify sensitive pods or services for further attacks. Note that while some endpoints may require authentication in hardened setups, many default configurations leave them accessible.

## Requirements

1. Network access to the Kubernetes cluster's worker nodes (ability to reach port 10250/TCP).
2. curl tool installed on the attacking machine (available on most Linux distributions).
3. Knowledge of at least one worker node IP address (can be obtained via prior reconnaissance like nmap scanning for port 10250).

## Defense

Defensive measures and detection strategies:

- Disable the Kubelet API's read-only access if not required for cluster operations, or bind it only to localhost.
- Implement RBAC policies to restrict API access and require authentication tokens for all endpoints.
- Monitor Kubelet API logs and network traffic for unauthorized requests to port 10250, using tools like Falco or Kubernetes audit logs.
- Use network segmentation to isolate worker nodes from untrusted networks.

## Objectives

1. Enumerate basic node and API information from the Kubelet root endpoint.
2. Retrieve metrics to assess resource usage and node health.
3. List running pods to identify potential targets for exploitation.
4. Gather intelligence for subsequent cluster compromise steps.

## Instructions

### Step 1: Query the Kubelet Root Endpoint

**Context**: This step accesses the root of the Kubelet API to retrieve general node information and confirm API availability. It helps verify the endpoint is reachable and exposes basic configuration details.

**Command** ([[commands/curl-kubelet-root-endpoint]]):
```bash
curl -k https://<IP_ADDRESS>:10250
```

> The -k flag ignores SSL certificate validation, common for self-signed certs in Kubernetes. Replace <IP_ADDRESS> with the target worker node's IP. This command probes the API's root, which may return a JSON response with node details or an authentication error if protected.

### Step 2: Retrieve Metrics from the Kubelet

**Context**: Querying the metrics endpoint provides Prometheus-formatted data on CPU, memory, and other resource usage for the node and its pods. This reveals workload patterns and potential resource-intensive targets.

**Command** ([[commands/curl-kubelet-metrics-endpoint]]):
```bash
curl -k https://<IP_ADDRESS>:10250/metrics
```

> Expected to return a text-based metrics dump. If the endpoint is unauthenticated, you'll see lines like # HELP kubelet_running_pods Number of pods currently running on the node. Use this data to identify high-value pods.

### Step 3: Enumerate Pods on the Node

**Context**: This step lists all pods managed by the Kubelet on the target node, including names, namespaces, and statuses. It exposes the cluster's application landscape for targeting sensitive services.

**Command** ([[commands/curl-kubelet-pods-endpoint]]):
```bash
curl -k https://<IP_ADDRESS>:10250/pods
```

> The response is typically JSON listing pod objects. Parse it to find pod IPs, container images, and volumes, which can guide further attacks like pod escape or lateral movement.

If any step fails due to authentication, consider token extraction from prior access (e.g., via kubectl) or check for anonymous access policies.
