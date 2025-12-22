---
id: cfafc087-ed2b-4f63-a579-2f65f52d76e1
name: curl-kubelet-pods-endpoint
type: command
executor: bash
data: 'curl -k https://$_IP_ADDRESS:10250/pods'
output: null
created_at: '2023-04-06T03:56:01.511075+00:00'
updated_at: '2023-04-10T20:34:01.313707+00:00'
platforms:
  - Linux
  - Kubernetes
tags:
  - discovery
  - kubernetes
  - kubelet
  - pods
verified: true
validated: true
---

# curl-kubelet-pods-endpoint

## Command

```bash
curl -k https://$_IP_ADDRESS:10250/pods
```

## Description

This command enumerates all pods running on a Kubernetes worker node via the Kubelet API, listing details like names, statuses, and containers. Use for discovering applications and potential entry points.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_IP_ADDRESS | IP address of the target Kubernetes worker node | Yes |
| -k | Ignore SSL certificate errors | Yes |

## Examples

### Basic Usage

```bash
curl -k https://192.168.1.100:10250/pods
```

### With JSON Formatting (if jq available)

```bash
curl -k https://192.168.1.100:10250/pods | jq '.'
```

## Expected Output

JSON array of pod objects:
```
{
  "kind": "PodList",
  "items": [
    {
      "metadata": {
        "name": "app-pod-1",
        "namespace": "default"
      },
      "status": {
        "phase": "Running"
      }
    }
  ]
}
```

## Related

- [[procedures/Kubelet-API-Enumeration-via-Curl]]
- [[commands/curl-kubelet-metrics-endpoint]]
