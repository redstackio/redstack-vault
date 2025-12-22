---
id: f7609fcc-b527-460c-bda9-b752d70cc3e1
name: Kubernetes-Service-Account-Permissions-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:01.150511+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Cloud Service Discovery]]'
sub_techniques: []
tags:
  - information-gathering
  - kubernetes
  - service-account-permissions
commands:
  - '[[commands/kubectl-auth-can-i-list]]'
  - '[[commands/kubectl-auth-can-i-list-namespace-kube-system]]'
platforms:
  - Kubernetes
tools: []
validated: true
---

# Kubernetes-Service-Account-Permissions-Enumeration

## Summary

This procedure enumerates the permissions granted to the default service account in a Kubernetes cluster, helping identify potential paths for privilege escalation or lateral movement. By querying the Kubernetes API server, it reveals read access to secrets and config maps by default, as well as any additional privileges assigned by administrators.

## Description

In Kubernetes, service accounts are used by pods to authenticate to the API server. By default, all service accounts in a namespace have read access to secrets and config maps within that namespace. However, cluster administrators may grant broader permissions, such as access to the kube-system namespace or cluster-wide resources. This procedure uses kubectl and direct API queries to perform a self-subject rules review, listing all allowed actions, resources, and verbs for the current service account. This is particularly useful in compromised pods to map out exploitable permissions for further attacks like pod escape or cluster domination. The technique aligns with cloud service discovery by probing internal API permissions without external tools.

## Requirements

1. Access to a running pod in the Kubernetes cluster with the default service account.
2. kubectl installed and configured with cluster access, or environment variables set for direct API calls (e.g., KUBERNETES_SERVICE_HOST, TOKEN).
3. Authenticated session to the Kubernetes API server via service account token.

## Defense

- Enforce strict Role-Based Access Control (RBAC) policies, granting only necessary permissions to service accounts.
- Monitor API server logs for unauthorized self-subject rules review queries or unusual authorization checks.
- Use network policies to restrict pod-to-API-server traffic and audit service account token usage.

## Objectives

1. List all permissions available to the default service account in the current namespace.
2. Identify access to sensitive namespaces like kube-system for potential lateral movement.
3. Discover cluster-wide privileges that could enable privilege escalation.

## Instructions

### Step 1: List General Service Account Permissions

**Context**: This step queries the Kubernetes API for all actions the default service account can perform in the current namespace, providing an overview of local permissions like reading secrets or config maps.

**Command** ([[commands/kubectl-auth-can-i-list]]):
```bash
kubectl auth can-i --list
```

> This command performs a self-subject access review, outputting a table of resources, non-resource URLs, and allowed verbs. It helps identify if the service account has elevated rights beyond defaults.

### Step 2: Check Permissions in Kube-System Namespace

**Context**: The kube-system namespace contains critical cluster components. This step verifies if the service account can perform actions there, which could allow enumeration of system pods or secrets for lateral movement.

**Command** ([[commands/kubectl-auth-can-i-list-namespace-kube-system]]):
```bash
kubectl auth can-i --list --namespace=kube-system
```

> Similar to Step 1, but scoped to kube-system. Look for verbs like 'list', 'get', or 'create' on resources such as pods, secrets, or deployments, indicating potential compromise vectors.

### Step 3: Perform Detailed Self-Subject Rules Review via API

**Context**: For a comprehensive view including both namespace-scoped and cluster-scoped rules, directly query the authorization API endpoint. This reveals non-namespaced permissions like clusterroles that could enable broader attacks.

**Code** ([[codes/Kubernetes-SelfSubjectRulesReview-Curl-Query]]):
```bash
NAMESPACE=$(cat "/var/run/secrets/kubernetes.io/serviceaccount/namespace")
MASTER_URL="https://${KUBERNETES_SERVICE_HOST}:${KUBERNETES_SERVICE_PORT}"
TOKEN=$(cat "/var/run/secrets/kubernetes.io/serviceaccount/token")
curl "${MASTER_URL}/apis/authorization.k8s.io/v1/selfsubjectrulesreviews" \
  --cacert "/var/run/secrets/kubernetes.io/serviceaccount/ca.crt" \
  --header "Authorization: Bearer ${TOKEN}" \
  --header "Content-Type: application/json" \
  --data '{"kind":"SelfSubjectRulesReview","apiVersion":"authorization.k8s.io/v1","spec":{"namespace":"'${NAMESPACE}'"}}'
```

> This curl request sends a JSON payload to the API server, returning a detailed JSON response with rules grouped by API groups, resources, and verbs. Parse the output to identify high-privilege actions like 'create' on 'pods' in any namespace.
