---
data: >-
  kubectl exec --kubeconfig=./kubeconfig -n vault -it vault-0 -- vault kv put
  kv-v2/staging/test username=test123 password=foobar123
tags:
  - vault
  - secrets
type: command
output: Key "kv-v2/staging/test" written!
executor: bash
platforms:
  - Kubernetes
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:55.680Z'
id: 816356f0-2e61-4fa1-a723-5c983b23dea9
verified: false
validated: true
submitted: true
---
# kubectl-exec-vault-secret

## Command

```bash
kubectl exec --kubeconfig=./kubeconfig -n vault -it vault-0 -- vault kv put kv-v2/staging/test username=test123 password=foobar123
```

## Description

This command executes inside a Kubernetes pod named vault-0 in the vault namespace to store key-value secrets in HashiCorp Vault's kv-v2 engine at path staging/test. It uses hardcoded test credentials, which were exposed in a public script, highlighting information disclosure risks in deployment automation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--kubeconfig=./kubeconfig` | Path to Kubernetes configuration file for cluster access | Yes |
| `-n vault` | Target namespace for the pod | Yes |
| `-it` | Interactive flags for terminal execution | Yes |
| `vault-0` | Name of the Vault pod to exec into | Yes |
| `vault kv put` | Vault CLI subcommand to write key-value data | Yes |
| `kv-v2/staging/test` | Secret path in Vault | Yes |
| `username=test123` | Key-value pair for username | Yes |
| `password=foobar123` | Key-value pair for password | Yes |

## Examples

### Basic Usage

```bash
kubectl exec --kubeconfig=./kubeconfig -n vault -it vault-0 -- vault kv put kv-v2/staging/test username=test123 password=foobar123
```

### Advanced Usage

In a deployment script, wrap with error handling:

```bash
kubectl exec --kubeconfig=./kubeconfig -n vault -it vault-0 -- vault kv put kv-v2/staging/test username=test123 password=foobar123 || echo "Failed to write secret"
```

## Expected Output

Success message from Vault: "Key \"kv-v2/staging/test\" written!" indicating the secret was stored successfully. On failure, Vault errors like authentication issues.

## Related

- [[Related Procedure: Identify-Sensitive-Files-in-Repository]]
