---
id: b85425d2-3a0d-420d-a93a-637ecd55c8c0
name: curl-kubelet-root-endpoint
type: command
executor: bash
data: 'curl -k https://$_NODE_IP:10255'
output: null
created_at: '2023-04-06T03:56:01.543950+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Kubernetes
tags:
  - discovery
  - kubelet
  - curl
verified: true
validated: true
---

# curl-kubelet-root-endpoint

## Command

```bash
curl -k https://$_NODE_IP:10255
```

## Description

This command sends an unauthenticated HTTPS GET request to the kubelet root endpoint on a Kubernetes node to retrieve node status and configuration details, including potential API server references.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_NODE_IP | IP address of the target Kubernetes node | Yes |
| -k | Insecure mode: skip SSL certificate verification (common for self-signed certs) | Yes |
| :10255 | Insecure kubelet API port | Built-in |

## Examples

### Basic Usage

```bash
curl -k https://192.168.1.100:10255
```

### With Silent Output

```bash
curl -k -s https://$_NODE_IP:10255 | jq .
```

## Expected Output

JSON object describing the node:
```
{
  "kind": "Node",
  "status": {
    "nodeInfo": {
      "kubeletVersion": "v1.25.0"
    }
  }
}
```

## Related

- [[procedures/Kubernetes-API-Enumeration-via-Kubelet]]
- [[commands/curl-kubelet-pods-endpoint]]
