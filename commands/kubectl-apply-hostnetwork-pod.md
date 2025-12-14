---
data: |-
  kubectl apply -f - <<'EOF'
  apiVersion: v1
  kind: Pod
  metadata:
    name: ubuntu-node
  spec:
    hostNetwork: true
    containers:
    - name: ubuntu
      image: ubuntu:latest
      command: [ "/bin/sleep", "inf" ]
  EOF
tags:
  - pod
  - deployment
type: command
output: null
executor: bash
platforms:
  - Kubernetes
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.895Z'
id: 96ad540b-6830-4dcc-9eaa-a5a6f4b99ac0
verified: false
validated: true
submitted: true
---
# kubectl-apply-hostnetwork-pod

## Command

```bash
kubectl apply -f - <<'EOF'
apiVersion: v1
kind: Pod
metadata:
  name: ubuntu-node
spec:
  hostNetwork: true
  containers:
  - name: ubuntu
    image: ubuntu:latest
    command: [ "/bin/sleep", "inf" ]
EOF
```

## Description

Applies a Kubernetes pod manifest to deploy a container sharing the host's network namespace.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -f - | Inline YAML manifest | Yes |
| hostNetwork: true | Enables host network | Yes |
| image | Container image | Yes |

## Examples

### Basic Usage

```bash
kubectl apply -f pod.yaml
```

### Advanced Usage

```bash
kubectl apply -f - <<EOF ... (manifest)
```

## Expected Output

pod/ubuntu-node created

## Related

- [[procedures/Deploy-Malicious-Pod-with-HostNetwork]]
