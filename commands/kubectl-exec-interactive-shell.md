---
id: 4b154013-95b8-434b-a9c7-0a85ffbd4039
name: kubectl-exec-interactive-shell
type: command
executor: bash
data: kubectl exec -it $_POD_NAME -n $_NAMESPACE -- sh
output: null
created_at: '2023-04-06T03:56:01.280289+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Kubernetes
tags:
  - exec
  - shell
  - lateral-movement
verified: true
validated: true
---

# kubectl-exec-interactive-shell

## Command

```bash
kubectl exec -it $_POD_NAME -n $_NAMESPACE -- sh
```

## Description

This command executes an interactive shell (sh) in the specified Kubernetes pod's container, allowing command execution within the pod's environment for privilege escalation or lateral movement.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-it` | Interactive mode with TTY allocation | Yes |
| `$_POD_NAME` | Name of the target pod (e.g., app-pod-abc123) | Yes |
| `-n $_NAMESPACE` | Target namespace (e.g., default) | Yes |
| `-- sh` | Command to run inside the pod (sh for shell) | Yes |

## Examples

### Basic Usage

```bash
kubectl exec -it mypod -n default -- sh
```

### Advanced Usage

```bash
kubectl exec -it mypod -n default -- /bin/bash
```

## Expected Output

An interactive shell prompt inside the pod:

/ # 

From here, execute commands like 'whoami' or 'ls'.

## Related

- [[procedures/Kubernetes-RBAC-Pod-Exec-Privilege-Escalation]]
- [[commands/kubectl-get-pods]]
