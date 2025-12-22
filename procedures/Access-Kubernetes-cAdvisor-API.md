---
id: 39065df7-d668-4046-a4ad-02fb9ef0977b
name: Access-Kubernetes-cAdvisor-API
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:01.432438+00:00'
updated_at: '2023-04-10T20:34:05.832062+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[System Information Discovery]]'
sub_techniques: []
tags:
  - '[[tags/API addresses that you should know]]'
  - '[[tags/cAdvisor]]'
  - '[[tags/Kubernetes]]'
  - reconnaissance
  - discovery
commands:
  - '[[commands/curl-access-cadvisor-api]]'
platforms:
  - Kubernetes
tools: []
validated: true
---

# Access-Kubernetes-cAdvisor-API

## Summary

This procedure demonstrates how to access the cAdvisor API endpoint on a Kubernetes node to retrieve container resource usage data, such as CPU, memory, and filesystem metrics. By querying this API, an attacker with network access to the node can gain insights into running containers, identify resource-intensive workloads, and spot potential targets for further exploitation within the cluster.

## Description

cAdvisor (Container Advisor) is a Kubernetes component that monitors resource usage and performance characteristics of running containers. It exposes an HTTP API on port 4194 by default, often without authentication in misconfigured clusters. This procedure involves sending an unauthenticated request to the API endpoint to fetch aggregated container statistics. The technique is useful during reconnaissance phases to map the cluster's container landscape, detect sensitive services, or identify privilege escalation opportunities based on resource patterns. It assumes the attacker has identified a Kubernetes node's IP address, typically through prior network scanning or enumeration. Successful access reveals JSON-formatted data on subcontainers, including names, images, and usage metrics, aiding in targeted attacks.

## Requirements

1. Network access to the Kubernetes node's IP address on port 4194.
2. The cAdvisor API must be exposed and unauthenticated (common in default setups).
3. Tools like curl installed on the attacker's machine.
4. Knowledge of the target node's IP, obtained via prior discovery (e.g., nmap scanning for port 4194).

## Defense

Defensive measures and detection strategies:

- Restrict access to cAdvisor endpoints using network policies, firewalls, or Kubernetes NetworkPolicies to limit exposure to internal traffic only.
- Enable mutual TLS (mTLS) or API authentication (e.g., via kubeconfig or service accounts) to prevent unauthorized queries.
- Monitor API access logs in Kubernetes control plane and node-level traffic for anomalous requests to port 4194 using tools like Falco or Prometheus.
- Regularly audit cluster configurations with tools like kube-bench to ensure monitoring ports are not publicly exposed.

## Objectives

1. Retrieve container resource usage data from the cAdvisor API to map the Kubernetes environment.
2. Identify running containers, their resource consumption, and potential high-value targets.
3. Validate API accessibility for further cluster reconnaissance or exploitation planning.

## Instructions

### Step 1: Identify the Target Node IP

**Context**: Before accessing the API, determine the IP address of a Kubernetes worker node running cAdvisor. This can be done via network scanning or querying the cluster if partial access is available. The goal is to target a node where containers of interest are hosted.

Use a tool like nmap to scan for open port 4194 if the IP range is known.

> Note: This step assumes prior reconnaissance; replace with actual scanning commands if needed.

### Step 2: Execute API Request Using Curl

**Context**: Send an HTTP GET request to the cAdvisor root endpoint (/metrics or /) to fetch resource data. The -k flag bypasses SSL certificate validation, which is common for self-signed or invalid certs in Kubernetes setups. This step retrieves raw metrics without authentication.

**Command** ([[commands/curl-access-cadvisor-api]]):
```bash
curl -k https://$_NODE_IP:4194/
```

> This command queries the API and returns JSON data on container stats. The endpoint / provides overall subcontainer information, while /metrics offers Prometheus-formatted data. Expect a response with fields like subcontainers (array of container objects), each containing name, aliases, state, cpu_usage, memory_usage, and filesystem details.

### Step 3: Parse and Analyze the Output

**Context**: Review the JSON response to extract actionable intelligence, such as container names, images, and resource spikes indicating database or application pods. Use jq for parsing if the output is verbose.

**Command** (extend with jq for filtering):
```bash
curl -k https://$_NODE_IP:4194/ | jq '.subcontainers[] | {name, cpu: .cpu_usage.total_usage_nano}'
```

> Filter for specific metrics to identify targets. Success is confirmed by receiving structured data without connection errors. If the API returns empty or errors, the endpoint may be protected or misconfigured.

## Expected Output

Successful execution produces JSON output similar to:

```json
{
  "subcontainers": [
    {
      "name": "/kubepods.slice/kubepods-burstable.slice/...",
      "aliases": [],
      "state": "running",
      "cpu_usage": {
        "total_usage_nano": 1234567890
      },
      "memory_usage": {
        "usage_bytes": 104857600,
        "working_set_bytes": 94371840
      }
    }
  ]
}
```

This indicates access was granted and data is retrievable, allowing further analysis of the cluster.
