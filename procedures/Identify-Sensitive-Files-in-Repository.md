---
tags:
  - information-disclosure
  - credentials
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/kubectl-exec-vault-secret]]'
verified: false
platforms:
  - Kubernetes
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Software]]'
updated_at: '2025-12-14T17:24:55.696Z'
sub_techniques: []
id: 9a6b1625-19b6-41c1-9251-0440b72facca
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
---
# Identify-Sensitive-Files-in-Repository

## Summary

This procedure focuses on pinpointing files within a public GitHub repository that contain hardcoded sensitive data, such as test credentials for secret management systems, to understand deployment practices.

## Description

Attackers target deployment scripts in open-source repos to find unredacted credentials. In this case, a Rake file in Sifchain's sifnode repo exposes a kubectl command for HashiCorp Vault, including test username and password. This reveals staging environment details and potential reuse in production contexts. The approach is manual browsing, with outcomes including credential harvesting for lateral movement simulations.

## Requirements

1. Access to the specific repository URL
2. Ability to view raw file contents on GitHub
3. Familiarity with Kubernetes and Vault commands

## Defense

Defensive measures and detection strategies:

- Use secret scanning tools on commit hooks to prevent hardcoded secrets
- Rotate any exposed test credentials immediately
- Limit public access to deployment scripts by using private repos for sensitive code

## Objectives

1. Locate scripts with embedded commands and secrets
2. Extract credentials and paths for Vault or similar systems
3. Map internal deployment namespaces and pod names

## Instructions

### Step 1: Locate the Target File

**Context**: Navigate to the specific commit and file path to inspect contents.

**Command** (Browser):
View https://github.com/Sifchain/sifnode/blob/30f0c45720b964342f3011c124c79c66c4c01a6b/deploy/rake/cluster.rake

> Expected output: Raw Ruby Rake code with embedded kubectl command.

### Step 2: Analyze the Embedded Command

**Context**: Identify and parse the hardcoded kubectl command for secrets.

**Command** ([[commands/kubectl-exec-vault-secret]]):
```bash
kubectl exec --kubeconfig=./kubeconfig -n vault -it vault-0 -- vault kv put kv-v2/staging/test username=test123 password=foobar123
```

> This command executes inside a Vault pod to store test secrets. Expected output: Exposure of username=test123 and password=foobar123, plus paths like kv-v2/staging/test.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Software]] Gather Victim Org Information: Code Repositories

### Sub-Techniques


## Commands Used

- [[commands/kubectl-exec-vault-secret]]

## Tools Used


## Tags

- [[information-disclosure]]
- [[Credentials]]
