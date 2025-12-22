---
id: 37bd8d19-02c5-4f58-9cc4-38907c8b19ba
name: curl-get-kubernetes-api-version
type: command
executor: bash
data: 'curl -k https://<TARGET_IP>:6443/api/v1'
output: null
created_at: '2023-04-06T03:56:01.451043+00:00'
updated_at: '2023-04-10T20:34:06.193303+00:00'
platforms:
  - Linux
  - Kubernetes
tags:
  - reconnaissance
  - api-enumeration
verified: true
validated: true
---

# curl-get-kubernetes-api-version

## Command

```bash
curl -k https://<TARGET_IP>:6443/api/v1
```

## Description

This command queries the core v1 API endpoint to retrieve information about supported versions and basic cluster resources like nodes and namespaces.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| <TARGET_IP> | IP address or hostname of the Kubernetes API server | Yes |
| -k | Ignore SSL/TLS certificate validation | Yes |
| :6443 | Default secure port for Kubernetes API server | Yes |
| /api/v1 | Core API version endpoint | Built-in |

## Examples

### Basic Usage

```bash
curl -k https://192.168.1.100:6443/api/v1
```

### With Follow Redirects

```bash
curl -k -L https://<TARGET_IP>:6443/api/v1
```

## Expected Output

If accessible, it returns details on API groups and resources:

```json
{
  "groupVersion": "v1",
  "versions": [
    {
      "groupVersion": "v1",
      "version": "v1"
    }
  ],
  "resources": [
    {
      "name": "nodes",
      "namespaced": false,
      "kind": "Node"
    },
    {
      "name": "namespaces",
      "namespaced": false,
      "kind": "Namespace"
    }
  ]
}
```

A 401/403 error shows authentication is required.

## Related

- [[procedures/Kubernetes-API-Server-Enumeration]]
- [[commands/curl-get-kubernetes-api-swagger]]
