---
id: 184df40e-a2f6-4778-99c2-20591177ad87
name: kubectl-auth-can-i-list
type: command
executor: bash
data: kubectl auth can-i --list
output: null
created_at: '2023-04-06T03:56:01.145290+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Kubernetes
tags:
  - authorization
  - discovery
verified: true
validated: true
---

# kubectl-auth-can-i-list

## Command

```bash
kubectl auth can-i --list
```

## Description

This command checks the authorization permissions for the current user or service account against the Kubernetes API server, listing all allowed actions in the current namespace. It is useful for enumerating service account capabilities during discovery phases.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--list` | Output a detailed list of all permissions in table format | Yes |

## Examples

### Basic Usage

```bash
kubectl auth can-i --list
```

### Usage with Context

Run this inside a pod to see default service account permissions.

## Expected Output

```
Resources                                     Non-Resource URLs   Resource Names   Verbs
---------                                     -----------------   --------------   -----
selfsubjectaccessreviews.authorization.k8s.io []                 []                [create]
selfsubjectrulesreviews.authorization.k8s.io  []                 []                [create]
secrets                                       []                 []                [get list watch]
configmaps                                    []                 []                [get list watch]

# And potentially more based on RBAC.
```

A table showing resources, verbs, and scopes. Success is indicated by the presence of allowed verbs on key resources like secrets.

## Related

- [[procedures/Kubernetes-Service-Account-Permissions-Enumeration]]
