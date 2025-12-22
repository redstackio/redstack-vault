---
id: 94a01250-9615-4407-b201-44cb2017500b
name: Kubernetes-RBAC-List-Secrets
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:01.204271+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques: []
tags:
  - Kubernetes
  - RBAC
  - Secrets
  - Credential Access
commands:
  - '[[commands/curl-kubernetes-list-secrets]]'
platforms:
  - Kubernetes
tools: []
validated: true
---

# Kubernetes-RBAC-List-Secrets

## Summary

This procedure details how an attacker with valid RBAC permissions can enumerate and retrieve Kubernetes secrets from the kube-system namespace via the cluster's API server. Using a JWT token for authentication, the procedure leverages direct API calls to list sensitive data such as API keys, passwords, and certificates stored in secrets, enabling further credential access or lateral movement within the cluster.

## Description

In a Kubernetes environment, secrets are used to store sensitive information like tokens, passwords, and keys. If an attacker has obtained a service account token or user JWT with 'list' permissions on secrets (via RBAC misconfiguration), they can query the API server to dump these secrets. This targets the kube-system namespace, which often contains critical cluster-wide credentials. The technique relies on the Kubernetes API's RESTful interface and assumes the attacker has network access to the master node. Success exposes plaintext or encoded credentials that can be decoded for use in privilege escalation or data exfiltration. This is particularly effective in environments with overly permissive RBAC roles.

## Requirements

1. Valid JWT token with RBAC permissions to list secrets (e.g., via a bound service account).
2. Network access to the Kubernetes API server (master IP and port, typically 6443).
3. curl tool installed on the attacker's machine.
4. Knowledge of the target namespace (here, kube-system).

## Defense

- Implement principle of least privilege in RBAC: Restrict 'list' and 'get' verbs on secrets to only necessary roles.
- Use network policies and API server authentication to limit access to the control plane.
- Enable audit logging on the API server to monitor secret access attempts.
- Rotate secrets regularly and use external secret managers like HashiCorp Vault.
- Deploy tools like Falco or Kubernetes Audit to detect anomalous API calls.

## Objectives

1. Authenticate to the Kubernetes API server using a valid JWT token.
2. Retrieve a list of all secrets in the kube-system namespace.
3. Identify and extract sensitive credential data from the listed secrets for further exploitation.

## Instructions

### Step 1: Authenticate and List Secrets

**Context**: This step uses the Kubernetes API to send an authenticated GET request to enumerate all secrets in the specified namespace. The JWT token provides the necessary RBAC authorization. Replace placeholders with actual values before execution. This reveals secret names and metadata, which can then be followed up with individual 'get' requests to dump contents.

**Command** ([[commands/curl-kubernetes-list-secrets]]):
```bash
curl -v -H "Authorization: Bearer $_JWT_TOKEN" https://$_MASTER_IP:$_PORT/api/v1/namespaces/kube-system/secrets/
```

> This command performs a verbose GET request to the /api/v1/namespaces/kube-system/secrets/ endpoint. The Authorization header passes the JWT for bearer token authentication. If successful, it returns a JSON array of secret objects including names, types, and data keys. Errors may indicate insufficient permissions (403) or invalid token (401). Verify the output for secret names like 'kubeconfig' or 'registry-pull-secret' that may contain exploitable credentials.
