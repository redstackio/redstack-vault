---
id: 16a6468d-fb87-44cd-b4a3-75a50ebf50c5
name: curl-check-kubernetes-api-health
type: command
executor: bash
data: 'curl -k https://<TARGET_IP>:6443/healthz'
output: null
created_at: '2023-04-06T03:56:01.450991+00:00'
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

# curl-check-kubernetes-api-health

## Command

```bash
curl -k https://<TARGET_IP>:6443/healthz
```

## Description

This command checks the health status of the Kubernetes API server by querying the /healthz endpoint. It is used during initial reconnaissance to confirm the API server is running and accessible without authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| <TARGET_IP> | IP address or hostname of the Kubernetes API server | Yes |
| -k | Ignore SSL/TLS certificate validation (for self-signed certs) | Yes |
| :6443 | Default secure port for Kubernetes API server | Yes |
| /healthz | Health check endpoint | Built-in |

## Examples

### Basic Usage

```bash
curl -k https://192.168.1.100:6443/healthz
```

### With Verbose Output

```bash
curl -k -v https://<TARGET_IP>:6443/healthz
```

## Expected Output

On success, the server returns 'ok' indicating healthy status:

```
ok
```

A 404 or connection error suggests the endpoint is not exposed or firewalled.

## Related

- [[procedures/Kubernetes-API-Server-Enumeration]]
- [[commands/curl-get-kubernetes-api-swagger]]
