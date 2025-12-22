---
type: code
language: yaml
verified: true
created_at: '2023-04-06T03:56:01.225240+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Kubernetes
tags:
  - rbac
  - yaml
  - configuration
validated: true
---

# RBAC-Wildcard-Rules-YAML

## Code

```yaml
resources:
- '*'
verbs:
- '*'
```

## Description

This YAML snippet defines RBAC rules granting access to all resources ('*') with all possible verbs ('*'), such as get, create, delete, and update. It is intended for insertion into a Kubernetes ClusterRole or Role definition under the 'rules' section to enable full cluster permissions for privilege escalation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This snippet has no variables; customize the surrounding YAML (e.g., metadata.name, subjects) as needed. | N/A |

## Usage

Embed this snippet in a full ClusterRole YAML file within the 'rules' array, then apply using [[commands/kubectl-apply-rbac-wildcard]]. For example, in a privilege escalation scenario after gaining initial API access, create a binding to your service account to achieve cluster-wide control. Used in procedures like [[procedures/Modify-Kubernetes-RBAC-for-Wildcard-Access]].

## Detection

- Audit logs showing creation/update of ClusterRoles with '*' patterns.
- Anomalous 'can-i' checks or permission queries post-application.
- RBAC validation tools like kubectl describe clusterrole detecting wildcard rules.

## Related

- [[procedures/Modify-Kubernetes-RBAC-for-Wildcard-Access]]
- [[tools/kubectl]]
