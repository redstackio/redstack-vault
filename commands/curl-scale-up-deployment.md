---
id: cmd-curl-scale-up
data: >-
  curl -X PUT
  127.0.0.1:8001/apis/apps/v1/namespaces/default/deployments/nginx/scale -H
  "Content-Type: application/json" -d @scale.json
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
updated_at: '2025-12-14T17:26:30.546Z'
verified: false
validated: true
submitted: true
---
# curl -X PUT ... -d @scale.json

## Command

```bash
curl -X PUT 127.0.0.1:8001/apis/apps/v1/namespaces/default/deployments/nginx/scale -H "Content-Type: application/json" -d @scale.json
```

## Description

Sends a PUT request to scale the nginx deployment to 999 replicas via proxied API.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -X PUT | HTTP method | Yes |
| 127.0.0.1:8001/.../scale | API endpoint | Yes |
| -H "Content-Type: application/json" | Header for JSON | Yes |
| -d @scale.json | Payload file | Yes |

## Examples

### Basic Usage

```bash
curl -X PUT ... -d @scale.json
```

### Advanced Usage

```bash
curl -X PUT ... -d @scale.json -v
```

## Expected Output

JSON response with updated replicas: 999; repeated calls cause delays.

## Related

- [[commands/curl-scale-down-deployment]]
- [[procedures/create-kubernetes-scaling-script]]
