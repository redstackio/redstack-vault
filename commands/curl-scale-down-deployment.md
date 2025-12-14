---
id: cmd-curl-scale-down
data: >-
  curl -X PUT
  127.0.0.1:8001/apis/apps/v1/namespaces/default/deployments/nginx/scale -H
  "Content-Type: application/json" -d @scaledown.json
tags:
  - kubernetes
  - api
  - scaling
type: command
output: HTTP 200 with scale status
executor: bash
platforms:
  - Kubernetes
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.542Z'
verified: false
validated: true
submitted: true
---
# curl -X PUT ... -d @scaledown.json

## Command

```bash
curl -X PUT 127.0.0.1:8001/apis/apps/v1/namespaces/default/deployments/nginx/scale -H "Content-Type: application/json" -d @scaledown.json
```

## Description

Scales the deployment down to 1 replica via API PUT.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -X PUT | HTTP method | Yes |
| endpoint | Scale subresource | Yes |
| -H | JSON header | Yes |
| -d @scaledown.json | Payload | Yes |

## Examples

### Basic Usage

```bash
curl -X PUT ... -d @scaledown.json
```

### Advanced Usage

```bash
curl -X PUT ... -d @scaledown.json --fail
```

## Expected Output

JSON with replicas: 1; exhaustion on repeats.

## Related

- [[commands/curl-scale-up-deployment]]
- [[procedures/create-kubernetes-scaling-script]]
