---
data: kubectl apply -f go-redirect.yaml
tags:
  - kubernetes
  - deploy
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:38.924Z'
id: 30d30528-3d5b-44de-babc-c66ae65edf1e
verified: false
validated: true
submitted: true
---
# kubectl-apply

## Command

```bash
kubectl apply -f go-redirect.yaml
```

## Description

Applies a Kubernetes YAML manifest to deploy resources like the malicious pod for hijacking.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -f | Path to YAML file | Yes |

## Examples

### Deploy Pod

```bash
kubectl apply -f go-redirect.yaml
```

## Expected Output

pod/malicious-metrics created in kube-system namespace.

## Related

- [[tools/kubectl]]
- [[procedures/Deploy-Malicious-Pod-to-Hijack-Metrics-Server]]
