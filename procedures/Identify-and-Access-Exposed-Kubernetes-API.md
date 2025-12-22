---
tags:
  - initial-access
  - kubernetes
  - misconfiguration
type: procedure
tools:
  - '[[tools/binaryedge.io]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Kubernetes
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: b3534913-657c-4dc7-996e-379d83c8bc7a
created_at: '2025-12-10T05:44:16.288Z'
updated_at: '2025-12-10T05:44:16.288Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Identify and Access Exposed Kubernetes API

## Summary

This procedure focuses on confirming the identity of an exposed Kubernetes API and gaining initial unauthorized access by querying basic cluster resources.

## Description

Once an exposed API is identified, attackers attempt to access it without credentials to verify the misconfiguration. This targets Kubernetes environments where the API server is publicly reachable. Outcomes include confirmation of access and preparation for escalation.

## Requirements

1. Identified target API endpoint
2. Kubernetes CLI tool (kubectl) installed
3. Network access to the API port

## Defense

Defensive measures and detection strategies:

- Enable RBAC and authentication on Kubernetes API
- Use API gateway or proxy with auth enforcement

## Objectives

1. Verify API exposure and lack of auth
2. Query cluster resources
3. Establish initial foothold

## Instructions

### Step 1: Configure kubectl for Target

**Context**: Set up kubectl to point to the exposed API.

Execute:

```bash
kubectl config set-cluster target --server=https://target-api:6443 --insecure-skip-tls-verify
kubectl config use-context target
```

> This configures access without TLS verification.

### Step 2: Query Resources

**Context**: Attempt to list pods to confirm access.

Use #kubectl-get-pods:

```bash
kubectl get pods --all-namespaces
```

> Successful output lists pods, indicating unauthorized access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- #kubectl-get-pods

## Tools Used

- #kubectl-get-pods

## Tags

- [[Initial Access]]
- #kubernetes
