---
id: cmd-kubectl-create-yaml
data: kubectl create -f sc-poc.yaml
tags:
  - kubernetes
  - resource-creation
type: command
output: storageclass/poc-ssrf created
executor: bash
platforms:
  - Kubernetes
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:54.832Z'
verified: false
validated: true
submitted: true
---
---

# kubectl-create-yaml

## Command

```bash
kubectl create -f sc-poc.yaml
```

## Description

Creates Kubernetes resources from a YAML file, used here to apply malicious StorageClass and PVC configurations for SSRF triggering.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-f` | Path to the YAML file containing resource definitions | Yes |

## Examples

### Basic Usage

```bash
kubectl create -f sc-poc.yaml
```

### Advanced Usage

```bash
kubectl create -f pvc-poc.yaml --namespace=default
```

## Expected Output

"storageclass/poc-ssrf created" or similar confirmation; resources appear in `kubectl get` listings.

## Related

- [[commands/kubectl-describe-pvc]]
- [[procedures/Create-Malicious-StorageClass-for-SSRF]]

---
