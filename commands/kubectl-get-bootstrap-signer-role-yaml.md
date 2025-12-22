---
id: 759487c8-76cb-4fba-8bfe-924f1a58564d
name: kubectl-get-bootstrap-signer-role-yaml
type: command
executor: bash
data: 'kubectl get role system:controller:bootstrap-signer -n kube-system -o yaml'
output: null
created_at: '2023-04-06T03:56:01.250956+00:00'
updated_at: '2023-04-10T20:34:03.127967+00:00'
platforms:
  - Kubernetes
tags:
  - rbac
  - kubernetes
verified: true
validated: true
---

# kubectl-get-bootstrap-signer-role-yaml

## Command

```bash
kubectl get role system:controller:bootstrap-signer -n kube-system -o yaml
```

## Description

This command retrieves the YAML configuration of the system:controller:bootstrap-signer Role in the kube-system namespace. It is used to inspect RBAC permissions, verifying if the role allows actions like pod creation, which is essential before attempting to deploy malicious resources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `role` | The name of the Role resource (system:controller:bootstrap-signer) | Yes |
| `-n kube-system` | Specifies the namespace (kube-system) | Yes |
| `-o yaml` | Outputs the resource in YAML format for detailed inspection | Yes |

## Examples

### Basic Usage

```bash
kubectl get role system:controller:bootstrap-signer -n kube-system -o yaml
```

### Advanced Usage

To pipe to a file for offline review:

```bash
kubectl get role system:controller:bootstrap-signer -n kube-system -o yaml > bootstrap-role.yaml
```

## Expected Output

A YAML document describing the Role, including metadata and rules array with allowed verbs (e.g., create, get) on resources like pods. Example snippet:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: system:controller:bootstrap-signer
  namespace: kube-system
rules:
- apiGroups: ["\"]  
  resources: ["pods"]
  verbs: ["create", "get"]
```

If the role does not exist or access is denied, output will show an error like "Error from server (NotFound): roles.rbac.authorization.k8s.io \"system:controller:bootstrap-signer\" not found".

## Related

- [[procedures/Abuse-Kubernetes-Bootstrap-Signer-RBAC-to-Deploy-Malicious-Pod]]
