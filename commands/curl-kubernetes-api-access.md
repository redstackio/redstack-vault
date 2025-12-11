---
data: 'curl -k https://TARGET_IP:6443/api/v1/namespaces'
tags:
  - kubernetes
  - access
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 912bed90-4b1e-461a-9bbb-93e3cf7c0e73
created_at: '2025-12-11T06:10:10.584Z'
updated_at: '2025-12-11T06:10:10.584Z'
verified: false
validated: true
submitted: true
---
# curl-kubernetes-api-access

## Command

```bash
curl -k https://TARGET_IP:6443/api/v1/namespaces
```

## Description

This command tests unauthorized access to a Kubernetes API by listing namespaces, bypassing SSL verification with -k.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-k` | Insecure mode (ignore SSL errors) | Yes |
| `https://TARGET_IP:6443/api/v1/namespaces` | API endpoint to query | Yes |

## Examples

### Basic Usage

```bash
curl -k https://TARGET_IP:6443/api/v1/namespaces
```

### Advanced Usage

```bash
curl -k -H "Accept: application/json" https://TARGET_IP:6443/api/v1/pods
```

## Expected Output

JSON response listing namespaces if access is granted, e.g., {"kind":"NamespaceList", "items":[...]}

## Related

- [[procedures/Access-Unauthorized-Kubernetes-API]]
- [[commands/curl-create-kubernetes-job]]
