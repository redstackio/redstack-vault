---
id: generate-uuid-2
name: curl-etcd-version
type: command
executor: bash
data: 'curl -k https://$_TARGET_IP:2379/version'
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Kubernetes
tags:
  - etcd
  - version
  - enumeration
verified: true
validated: true
---

# curl-etcd-version

## Command

```bash
curl -k https://$_TARGET_IP:2379/version
```

## Description

This command retrieves the version information from the etcd API endpoint, providing details on the etcd server, cluster, and build. It helps assess the target's etcd implementation for compatibility or vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address of the etcd node | Yes |
| -k | Skip SSL certificate checks | Yes (for testing) |

## Examples

### Basic Usage

```bash
curl -k https://10.0.0.1:2379/version
```

### Advanced Usage

```bash
curl -k https://10.0.0.1:2379/version | jq
```
(Pipes to jq for formatted JSON output)

## Expected Output

JSON with version details:
```
{"etcdserver":"3.5.0","etcdcluster":"3.5.0"}
```

## Related

- [[procedures/Kubernetes-Etcd-API-Enumeration]]
- [[commands/curl-etcd-endpoint-check]]
