---
type: command
executor: bash
data: curl -L $_TARGET_URL/version
output: null
platforms:
  - Linux
  - Kubernetes
tags:
  - ssrf
  - discovery
  - etcd
verified: true
validated: true
---

# curl-get-etcd-version

## Command

```bash
curl -L $_TARGET_URL/version
```

## Description

This command queries an ETCD instance for its version information, useful in SSRF scenarios to identify the database version and potential vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Base URL of the ETCD server (e.g., http://127.0.0.1:2379) | Yes |
| -L | Follow HTTP redirects | No (but recommended) |

## Examples

### Basic Usage

```bash
curl -L http://127.0.0.1:2379/version
```

### Advanced Usage

```bash
curl -L -H "User-Agent: Mozilla/5.0" http://127.0.0.1:2379/version
```

## Expected Output

Successful execution returns JSON like:

```json
{"etcdserver":"3.4.0","etcdcluster":"3.4.0"}
```

This indicates the ETCD server and cluster versions.

## Related

- [[procedures/Cloud-Instance-and-Kubernetes-ETCD-Enumeration-via-SSRF]]
- [[commands/curl-get-etcd-recursive-keys]]
