---
type: procedure
description: >-
  Extracts the Kubernetes service account token from a compromised pod to gain
  unauthorized access to the cluster API.
verified: true
submitted: false
created_at: '2023-04-06T03:56:17.381970+00:00'
updated_at: '2023-04-06T03:56:17.398594+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - >-
    [[techniques/Steal Application Access Token|T1528 - Steal Application Access
    Token]]
sub_techniques: []
tags:
  - '[[tags/container-kubernetes-pentest]]'
  - '[[tags/obtaining-service-account-token]]'
commands:
  - '[[commands/cat-kubernetes-service-account-token]]'
platforms:
  - Kubernetes
  - Linux
tools: []
validated: true
---

# Kubernetes-Service-Account-Token-Theft

## Summary

This procedure demonstrates how to extract a Kubernetes service account token from within a compromised pod. These tokens authenticate pods to the Kubernetes API server and can be abused to perform unauthorized actions such as listing secrets, deploying pods, or escalating privileges across the cluster.

## Description

Kubernetes service accounts provide identity for pods to interact with the API server. Tokens for these accounts are automatically mounted as read-only secrets at `/var/run/secrets/kubernetes.io/serviceaccount/token` in every pod bound to a service account (default is 'default'). An attacker with shell access in a pod can read this file to obtain a JSON Web Token (JWT) that impersonates the service account's permissions. This token can then be used externally via tools like `kubectl` or direct API calls, potentially leading to full cluster compromise if the service account has elevated roles. This technique is common in container escape or lateral movement scenarios within Kubernetes environments.

## Requirements

1. Shell access within a running pod (e.g., via initial container compromise or RCE).
2. The pod must be bound to a service account (most are by default).
3. Basic knowledge of Kubernetes filesystem paths.
4. No additional tools required beyond standard shell utilities like `cat`.

## Defense

- Use Pod Security Policies or Admission Controllers to restrict pod filesystem access and automate token rotation.
- Implement least-privilege RBAC: Avoid broad cluster-wide permissions for default service accounts.
- Enable audit logging on the API server to detect anomalous token usage.
- Use workload identity federation (e.g., with OIDC) instead of long-lived tokens.
- Scan for and bound service accounts to specific pods, disabling automounting where possible.

## Objectives

1. Extract the service account token from the pod's mounted secret.
2. Validate the token's usability for API interactions.
3. Enable further cluster enumeration or exploitation using the stolen token.

## Instructions

### Step 1: Confirm Pod Environment

**Context**: Verify you are executing within a Kubernetes pod and identify the service account in use. This ensures the token path is available and confirms the context.

Run the following to check the pod's metadata:

```bash
cat /proc/1/cgroup | grep pod
```

> This command inspects the container's cgroup to confirm it's running in a pod. If output contains 'kubepods', proceed.

### Step 2: Locate and Read the Service Account Token

**Context**: The token is mounted at a standard path. Reading it directly provides the JWT for API authentication.

**Command** ([[commands/cat-kubernetes-service-account-token]]):
```bash
cat /var/run/secrets/kubernetes.io/serviceaccount/token
```

> This reads the token file. The output is a long JWT string starting with 'eyJ...'. Copy this for later use. If the file doesn't exist, the pod may have automount disabled—check with `ls /var/run/secrets/`.

### Step 3: Validate Token Permissions

**Context**: Test the token to understand its scope, such as listing pods or secrets, to gauge impact.

Export the token as an environment variable and use curl to query the API (assuming API server endpoint is known, e.g., via `/var/run/secrets/kubernetes.io/serviceaccount/ca.crt` and host):

```bash
TOKEN=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)
curl -k -H "Authorization: Bearer $TOKEN" https://kubernetes.default.svc/api/v1/pods
```

> Expected: JSON response listing pods if permissions allow. Errors like 403 indicate limited access; 401 means invalid token.

## Expected Output

Successful execution yields the JWT token and API responses confirming access. For example, the token read will be a base64-encoded string, and validation will return cluster resource lists based on the service account's RBAC role.
