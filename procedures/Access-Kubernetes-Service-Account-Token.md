---
id: 11e6166b-19f4-4806-b4d6-f5ab9c57767f
type: procedure
name: Access-Kubernetes-Service-Account-Token
verified: true
submitted: false
created_at: '2023-04-06T03:56:01.003683+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Access Token Manipulation|T1134 - Access Token Manipulation]]'
sub_techniques: []
tags:
  - '[[tags/Container Environment]]'
  - '[[tags/Kubernetes]]'
  - '[[tags/Service Account]]'
commands:
  - '[[commands/extract-kubernetes-service-account-token]]'
  - '[[commands/query-kubernetes-api-with-token]]'
platforms:
  - Kubernetes
  - Linux
tools: []
validated: true
---

# Access-Kubernetes-Service-Account-Token

## Summary

This procedure demonstrates how to access and utilize the default service account token mounted in a Kubernetes pod to authenticate requests to the Kubernetes API server, enabling potential privilege escalation or lateral movement within the cluster.

## Description

In Kubernetes, each namespace has a default service account whose token is automatically mounted into pods at /var/run/secrets/kubernetes.io/serviceaccount/token. This token serves as a JSON Web Token (JWT) for authenticating API requests from the pod. An attacker with initial access to a compromised pod can extract this token and use it to impersonate the service account, querying cluster resources, creating pods, or escalating privileges if the service account has elevated RBAC permissions. This technique is common in container escape or lateral movement scenarios within cloud-native environments.

## Requirements

1. Shell access to a running container within a Kubernetes pod (e.g., via compromised application or initial access vector).
2. The pod must be running in a namespace with a default service account (standard configuration).
3. Network connectivity from the pod to the Kubernetes API server (typically via kubernetes.default.svc).
4. Basic tools like cat and curl available in the container (common in most Linux-based images).

## Defense

- Limit service account permissions using RBAC: Assign minimal roles to default service accounts and avoid cluster-wide bindings.
- Monitor API server access logs for anomalous requests from pod IPs or unusual user agents.
- Use network policies to restrict pod-to-API-server traffic and implement pod security standards to prevent token mounting.
- Regularly rotate service account tokens and enable token projection only when necessary.
- Deploy runtime security tools like Falco or Sysdig to alert on unauthorized token access attempts.

## Objectives

1. Extract the service account token from the pod's mounted secret.
2. Authenticate to the Kubernetes API server using the token.
3. Query cluster resources to assess privileges and identify further attack paths.

## Instructions

### Step 1: Extract the Service Account Token

**Context**: The token is mounted as a file in the pod's filesystem. Reading it provides the JWT needed for authentication. This step verifies access to the token and captures it for use.

**Command** ([[commands/extract-kubernetes-service-account-token]]):
```bash
cat /var/run/secrets/kubernetes.io/serviceaccount/token
```

> This command outputs the raw JWT token. Store it in a variable (e.g., TOKEN=$(cat ...)) or file for subsequent use. If the file does not exist, the pod may have custom security contexts disabling automounting—check pod spec with 'kubectl describe pod' if external access is available.

### Step 2: Authenticate and Query the API Server

**Context**: Use the extracted token to make an authenticated request to the API server. This tests the service account's permissions and reveals accessible resources, such as listing namespaces or pods, which can inform lateral movement.

**Command** ([[commands/query-kubernetes-api-with-token]]):
```bash
curl --insecure -H "Authorization: Bearer $_TOKEN" $_API_ENDPOINT
```

> Replace $_TOKEN with the extracted JWT and $_API_ENDPOINT with a valid API path (e.g., https://kubernetes.default.svc/api/v1/namespaces). The --insecure flag skips TLS verification, common in internal cluster communication. Successful output includes JSON with cluster data; errors indicate insufficient permissions or invalid token.
