---
id: c0c41076-2444-4e3a-812f-1896140243e0
name: curl-get-kubernetes-api-swagger
type: command
executor: bash
data: 'curl -k https://<TARGET_IP>:6443/swaggerapi'
output: null
created_at: '2023-04-06T03:56:01.450931+00:00'
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

# curl-get-kubernetes-api-swagger

## Command

```bash
curl -k https://<TARGET_IP>:6443/swaggerapi
```

## Description

This command retrieves the OpenAPI (Swagger) specification from the Kubernetes API server, providing a comprehensive map of available endpoints and operations for cluster resources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| <TARGET_IP> | IP address or hostname of the Kubernetes API server | Yes |
| -k | Ignore SSL/TLS certificate validation | Yes |
| :6443 | Default secure port for Kubernetes API server | Yes |
| /swaggerapi | Swagger/OpenAPI endpoint | Built-in |

## Examples

### Basic Usage

```bash
curl -k https://192.168.1.100:6443/swaggerapi
```

### Save to File

```bash
curl -k https://<TARGET_IP>:6443/swaggerapi > api-swagger.json
```

## Expected Output

The response is a JSON document describing the API:

```json
{
  "swagger": "2.0",
  "info": {
    "title": "Kubernetes",
    "version": "v1.26.0"
  },
  "paths": {
    "/api/": {
      "get": {
        "description": "get available API versions",
        "operationId": "getAPIVersions"
      }
    }
  }
}
```

Errors like 403 indicate restricted access.

## Related

- [[procedures/Kubernetes-API-Server-Enumeration]]
- [[commands/curl-check-kubernetes-api-health]]
