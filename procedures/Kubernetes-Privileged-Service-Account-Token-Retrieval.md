---
id: 119b7472-713c-4b1c-bdd7-54dd5d705ad0
name: Kubernetes-Privileged-Service-Account-Token-Retrieval
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:01.363869+00:00'
updated_at: '2023-04-10T20:33:59.606906+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - '[[techniques/Account Manipulation|T1098 - Account Manipulation]]'
sub_techniques: []
tags:
  - '[[tags/Kubernetes]]'
  - '[[tags/Privileged Service Account Token]]'
commands:
  - '[[commands/cat-kubernetes-service-account-token]]'
  - '[[commands/curl-retrieve-default-namespace-secrets]]'
platforms:
  - Kubernetes
tools: []
validated: true
---

# Kubernetes-Privileged-Service-Account-Token-Retrieval

## Summary

This procedure demonstrates how to retrieve a privileged Kubernetes service account token from within a compromised pod and use it to authenticate with the Kubernetes API to access sensitive resources like namespace secrets. It targets the default service account token mounted in pods, enabling an attacker with pod access to escalate privileges and perform unauthorized actions in the cluster.

## Description

Kubernetes service accounts provide an identity for processes running in pods to interact with the Kubernetes API server. Each pod automatically mounts a service account token at /run/secrets/kubernetes.io/serviceaccount/token, which can be used for API authentication. If the service account has elevated (privileged) permissions, such as cluster-admin roles, this token grants broad access to cluster resources. An attacker who has gained initial access to a pod—via container escape, misconfigured RBAC, or vulnerable applications—can read this token and impersonate the service account to list or manipulate secrets, deployments, or other objects. This technique is particularly dangerous in multi-tenant clusters where default service accounts may inherit excessive permissions. The procedure assumes the attacker is executing commands inside the pod's container and has network access to the API server.

## Requirements

1. Shell access to a running pod in the Kubernetes cluster (e.g., via kubectl exec or container breakout).
2. The pod must be associated with a service account that has API access (default in most setups).
3. Network connectivity from the pod to the Kubernetes API server (typically via the service cluster IP).
4. Basic tools like cat and curl available in the container (common in most base images).

## Defense

- Implement strict RBAC policies to limit service account permissions; avoid using cluster-admin roles for default accounts.
- Use Pod Security Standards or admission controllers to prevent unnecessary token mounts or restrict pod access.
- Enable API server audit logging to monitor token usage and anomalous requests from pod IPs.
- Regularly rotate service account tokens and use short-lived certificates where possible.
- Deploy network policies to isolate pods and limit outbound traffic to the API server.

## Objectives

1. Extract the service account token from the pod's mounted secret volume.
2. Authenticate with the Kubernetes API using the token to verify privileges.
3. Retrieve sensitive data, such as secrets in the default namespace, to demonstrate elevated access.

## Instructions

### Step 1: Retrieve the Service Account Token

**Context**: Access the mounted token file within the pod's filesystem to obtain the JWT token for the service account. This token is automatically provided by Kubernetes and grants the pod's identity for API calls.

**Command** ([[commands/cat-kubernetes-service-account-token]]):
```bash
cat /run/secrets/kubernetes.io/serviceaccount/token
```

> This command reads the token file and outputs the raw JWT string. Copy this token for use in subsequent API requests. If the file does not exist, the pod may not have a service account mounted—check pod spec with `kubectl describe pod` from outside.

### Step 2: Use Token to Query Namespace Secrets

**Context**: Authenticate to the Kubernetes API server using the retrieved token to list secrets in the default namespace. This verifies the token's validity and demonstrates potential for data exfiltration or further abuse if the account is privileged.

**Command** ([[commands/curl-retrieve-default-namespace-secrets]]):
```bash
curl -k -v -H "Authorization: Bearer $_JWT_TOKEN" https://$_MASTER_IP:$_PORT/api/v1/namespaces/default/secrets/
```

> Replace placeholders with actual values: $_JWT_TOKEN from Step 1, $_MASTER_IP as the API server IP (often 10.96.0.1 in-cluster), and $_PORT as 443 or the secure port. The -k flag ignores SSL verification for self-signed certs; -v provides verbose output for debugging. Success is indicated by a JSON response listing secrets; errors like 401 suggest insufficient privileges or invalid token.
