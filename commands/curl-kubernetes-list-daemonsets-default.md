---
id: 82de18a3-911b-4352-96bf-e9501b922378
name: curl-kubernetes-list-daemonsets-default
type: command
executor: bash
data: >-
  curl -v -H "Authorization: Bearer $_JWT_TOKEN"
  https://$_API_SERVER/apis/extensions/v1beta1/namespaces/default/daemonsets
output: null
created_at: '2023-04-06T03:56:01.386360+00:00'
updated_at: '2023-04-10T20:34:01.659280+00:00'
platforms:
  - Kubernetes
tags:
  - discovery
  - kubernetes
verified: true
validated: true
---

# curl-kubernetes-list-daemonsets-default

## Command

```bash
curl -v -H "Authorization: Bearer $_JWT_TOKEN" https://$_API_SERVER/apis/extensions/v1beta1/namespaces/default/daemonsets
```

## Description

Lists daemonsets to identify node-wide pods for cluster reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_JWT_TOKEN | Bearer token | Yes |
| $_API_SERVER | API server URL | Yes |
| -v | Verbose | No |
| -H | Header | Yes |

## Examples

### Basic Usage

```bash
curl -v -H "Authorization: Bearer $_JWT_TOKEN" https://$_API_SERVER/apis/extensions/v1beta1/namespaces/default/daemonsets
```

## Expected Output

JSON daemonsets:

```json
{
  "kind": "DaemonSetList",
  "items": [
    {
      "metadata": {
        "name": "fluentd"
      }
    }
  ]
}
```

Success via 200 response.

## Related

- [[procedures/Kubernetes-Endpoint-Enumeration]]
- [[commands/curl-kubernetes-list-deployments-default]]
