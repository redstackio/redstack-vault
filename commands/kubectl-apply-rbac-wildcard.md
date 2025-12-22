---
type: command
executor: bash
data: kubectl apply -f $_YAML_FILE
output: null
created_at: '2023-04-06T03:56:01.225330+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Kubernetes
tags:
  - rbac
  - kubectl
verified: true
validated: true
---

# kubectl-apply-rbac-wildcard

## Command

```bash
kubectl apply -f $_YAML_FILE
```

## Description

This command applies a Kubernetes YAML manifest file containing RBAC configurations, such as ClusterRoles and ClusterRoleBindings, to grant escalated permissions. Use it to deploy wildcard access rules after preparing the YAML file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -f, --filename | Path to the YAML file containing RBAC definitions (e.g., wildcard-clusterrole.yaml) | Yes |
| $_YAML_FILE | Placeholder for the YAML file path | Yes |

## Examples

### Basic Usage

```bash
kubectl apply -f wildcard-clusterrole.yaml
```

### Advanced Usage (with validation)

```bash
kubectl apply --dry-run=server -f wildcard-clusterrole.yaml
```

## Expected Output

When successful, kubectl confirms the creation or update of resources:
```
clusterrole.rbac.authorization.k8s.io/wildcard-clusterrole configured
clusterrolebinding.rbac.authorization.k8s.io/wildcard-binding configured
```

Errors may indicate insufficient permissions, such as:
```
Error from server (Forbidden): ...
```

## Related

- [[procedures/Modify-Kubernetes-RBAC-for-Wildcard-Access]]
- [[tools/kubectl]]
