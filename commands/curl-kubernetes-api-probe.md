---
data: 'curl -k https://<target-ip>:6443/version'
tags:
  - recon
  - api
type: command
output: '{"major":"1","minor":"20"}'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.630Z'
id: d4d6ded4-fa82-4c4a-8143-83bde058bc6c
verified: false
validated: true
submitted: true
---
# curl-kubernetes-api-probe

## Command

```bash
curl -k https://<target-ip>:6443/version
```

## Description

Probes an exposed Kubernetes API endpoint to retrieve version information, confirming accessibility without authentication. Use -k to ignore self-signed certs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-k` | Insecure mode, skip cert verification | Yes |
| `https://<target-ip>:6443/version` | API endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -k https://192.168.1.100:6443/version
```

### Advanced Usage

```bash
curl -k -H "Accept: application/json" https://<target-ip>:6443/api/v1/namespaces
```

## Expected Output

JSON object with Kubernetes version details, e.g., {"major":"1","minor":"20","gitVersion":"v1.20.0"}.

## Related

- [[commands/kubectl-create-job-rce]]
- [[procedures/Access-Exposed-Kubernetes-Endpoint]]
