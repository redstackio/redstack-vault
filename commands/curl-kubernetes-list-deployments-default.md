---
id: b40beea3-5d7a-415a-bc5d-0c98509b4b2e
name: curl-kubernetes-list-deployments-default
type: command
executor: bash
data: >-
  curl -v -H "Authorization: Bearer $_JWT_TOKEN"
  https://$_API_SERVER/apis/extensions/v1beta1/namespaces/default/deployments
output: null
created_at: '2023-04-06T03:56:01.386182+00:00'
updated_at: '2023-04-10T20:34:01.659280+00:00'
platforms:
  - Kubernetes
tags:
  - discovery
  - kubernetes
verified: true
validated: true
---

# curl-kubernetes-list-deployments-default

## Command

```bash
curl -v -H "Authorization: Bearer $_JWT_TOKEN" https://$_API_SERVER/apis/extensions/v1beta1/namespaces/default/deployments
```

## Description

Retrieves deployments in the default namespace to understand application scaling and configurations.

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
curl -v -H "Authorization: Bearer $_JWT_TOKEN" https://$_API_SERVER/apis/extensions/v1beta1/namespaces/default/deployments
```

## Expected Output

JSON deployments:

```json
{
  "kind": "DeploymentList",
  "items": [
    {
      "metadata": {
        "name": "web-app"
      },
      "spec": {
        "replicas": 3
      }
    }
  ]
}
```

200 OK confirms success.

## Related

- [[procedures/Kubernetes-Endpoint-Enumeration]]
- [[commands/curl-kubernetes-list-daemonsets-default]]
