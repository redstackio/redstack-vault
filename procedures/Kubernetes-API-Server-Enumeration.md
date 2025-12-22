---
id: 344572c8-ee6e-4443-9bdc-526a0f3b6181
name: Kubernetes-API-Server-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:01.459294+00:00'
updated_at: '2023-04-10T20:34:06.178815+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Network Service Scanning]]'
  - '[[Active Scanning]]'
sub_techniques: []
tags:
  - '[[tags/kubernetes]]'
  - '[[tags/api-enumeration]]'
  - '[[tags/reconnaissance]]'
commands:
  - '[[commands/curl-check-kubernetes-api-health]]'
  - '[[commands/curl-get-kubernetes-api-swagger]]'
  - '[[commands/curl-get-kubernetes-api-version]]'
platforms:
  - Kubernetes
  - Linux
tools: []
validated: true
---

# Kubernetes-API-Server-Enumeration

## Summary

This procedure enumerates key endpoints of the Kubernetes API server to gather information about the cluster's structure, version, and health. It uses simple HTTP requests to probe the API server, helping attackers identify exposed services, versions for potential exploits, and overall cluster status, or allowing administrators to verify exposure and configurations.

## Description

The Kubernetes API server is the central management entity in a Kubernetes cluster, exposing a RESTful API for cluster interactions. Enumeration involves querying standard endpoints like /healthz for status, /swaggerapi for API documentation, and /api/v1 for core resources such as nodes and namespaces. This technique reveals cluster details without authentication if the API is exposed, aiding in reconnaissance for misconfigurations like anonymous access or outdated versions vulnerable to known exploits. In offensive scenarios, it maps the attack surface; defensively, it supports auditing for unauthorized exposure.

## Requirements

1. Network access to the Kubernetes API server (typically port 6443).
2. curl or equivalent HTTP client installed on the attacking machine.
3. Knowledge of the API server's IP address or hostname.
4. No authentication required for anonymous endpoints, but RBAC may restrict deeper access.

## Defense

- Restrict API server access using network policies, firewalls, and etcd encryption to limit exposure to trusted networks.
- Implement RBAC and Pod Security Policies to deny anonymous access and monitor API calls via audit logs.
- Regularly scan for exposed API servers using tools like kube-bench and enable API server flags like --anonymous-auth=false.
- Monitor logs for anomalous requests to /healthz, /swaggerapi, or /api/v1 endpoints.

## Objectives

1. Confirm the API server's availability and health to validate the target.
2. Retrieve API documentation to understand available resources and potential attack paths.
3. Gather version and core resource information to identify vulnerabilities or cluster layout.
4. Detect misconfigurations like public exposure without authentication.

## Instructions

### Step 1: Check API Server Health

**Context**: Verify if the Kubernetes API server is responsive and healthy. This step confirms the endpoint is reachable and returns a success status, indicating the server is operational without deeper access.

**Command** ([[commands/curl-check-kubernetes-api-health]]):
```bash
curl -k https://<TARGET_IP>:6443/healthz
```

> This command sends an unauthenticated GET request to the /healthz endpoint, which checks the server's liveness. The -k flag ignores TLS certificate validation, common for self-signed certs in Kubernetes setups. If successful, it helps confirm the target before further enumeration.

### Step 2: Retrieve API Swagger Documentation

**Context**: Fetch the OpenAPI specification to map all available API endpoints, paths, and operations. This reveals the full scope of cluster resources like pods, services, and secrets that could be targeted.

**Command** ([[commands/curl-get-kubernetes-api-swagger]]):
```bash
curl -k https://<TARGET_IP>:6443/swaggerapi
```

> The response contains JSON defining the API schema, including versions and resource types. Analyze this for endpoints like /apis/apps/v1/namespaces/{namespace}/deployments to identify exploitable features.

### Step 3: Query Core API Version and Resources

**Context**: Probe the v1 API endpoint to extract basic cluster information, such as supported API versions, nodes, and namespaces. This step provides initial insights into the cluster's scale and configuration.

**Command** ([[commands/curl-get-kubernetes-api-version]]):
```bash
curl -k https://<TARGET_IP>:6443/api/v1
```

> Without authentication, this may return limited data or an error, but success indicates anonymous read access. Look for details on nodes, pods, or namespaces in the response to guide further attacks.
