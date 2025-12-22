---
id: cmd-curl-version-001
data: curl .../version
tags:
  - monitoring
  - api
type: command
output: '{"major":"1","minor":"17"} (normal); hangs during DoS'
executor: bash
platforms:
  - Linux
  - Kubernetes
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.383Z'
verified: false
validated: true
submitted: true
---
# curl-k8s-version

## Command

```bash
curl -k https://<k8s-api-endpoint>/version
```

## Description

Queries the Kubernetes API Server /version endpoint to check availability; hangs during DoS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/version` | API path | Yes |
| `-k` | Insecure TLS (if self-signed) | No |

## Examples

### Basic Usage

```bash
curl https://kubernetes.default.svc/version
```

### Advanced Usage

Via proxy: `kubectl proxy & curl http://localhost:8001/version`

## Expected Output

JSON with version info; indefinite hang on unavailability.

## Related

- [[Related Procedure: Monitor-API-Server-Unavailability]]
