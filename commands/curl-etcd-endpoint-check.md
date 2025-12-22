---
id: generate-uuid-1
name: curl-etcd-endpoint-check
type: command
executor: bash
data: 'curl -k https://$_TARGET_IP:2379'
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Kubernetes
tags:
  - etcd
  - enumeration
verified: true
validated: true
---

# curl-etcd-endpoint-check

## Command

```bash
curl -k https://$_TARGET_IP:2379
```

## Description

This command performs a basic health check on the etcd API endpoint by sending an unauthenticated GET request to the root path, bypassing TLS certificate validation. It is used to verify if the etcd service is exposed and responsive on the target IP and default port.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address of the Kubernetes master or etcd node | Yes |
| -k | Insecure mode: skip SSL certificate verification | Yes (for self-signed certs) |

## Examples

### Basic Usage

```bash
curl -k https://192.168.1.100:2379
```

### Advanced Usage

```bash
curl -k -v https://192.168.1.100:2379
```
(Adds verbose output for debugging connections)

## Expected Output

Successful response (JSON indicating health):
```
{}
```
Or error if inaccessible:
```
curl: (7) Failed to connect to 192.168.1.100 port 2379: Connection refused
```

## Related

- [[procedures/Kubernetes-Etcd-API-Enumeration]]
- [[commands/curl-etcd-version]]
