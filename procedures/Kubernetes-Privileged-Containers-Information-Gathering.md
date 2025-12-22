---
id: 2a44eb9d-6221-4be7-af69-071bcee49486
name: Kubernetes-Privileged-Containers-Information-Gathering
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:01.178858+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[System Information Discovery]]'
sub_techniques: []
tags:
  - information-gathering
  - kubernetes
  - privileged-containers
commands:
  - '[[commands/ls-list-devices]]'
  - '[[commands/cat-read-kernel-messages]]'
platforms:
  - Kubernetes
  - Linux
tools: []
validated: true
---

# Kubernetes-Privileged-Containers-Information-Gathering

## Summary

This procedure demonstrates how to gather sensitive host node information by executing commands inside a privileged Kubernetes container. Privileged containers have elevated access to the host's filesystem and kernel, allowing attackers to enumerate devices and read kernel messages, which can reveal system configuration, hardware details, and recent kernel events for further exploitation.

## Description

In Kubernetes, privileged containers run with all host capabilities and can mount the host's root filesystem, providing direct access to /dev and kernel interfaces. This technique is useful during post-exploitation in a compromised cluster to perform discovery on the underlying nodes. By using kubectl exec to run commands like ls /dev and cat /dev/kmsg, an attacker can extract device information (e.g., disks, network interfaces) and kernel ring buffer logs, which may contain timestamps, errors, or security events. This information aids in identifying vulnerabilities, such as outdated kernel versions or misconfigurations. The procedure assumes the attacker has already gained access to run commands on a privileged pod, typically via initial pod compromise or RBAC abuse.

## Requirements

1. Kubectl access to the Kubernetes cluster with permissions to exec into pods.
2. Identification of a running privileged pod (e.g., via `kubectl get pods -o yaml | grep privileged: true`).
3. Network access to the cluster API server.
4. The target pod must be privileged, allowing host device access.

## Defense

- Disable privileged containers unless absolutely necessary by setting `securityContext.privileged: false` in pod specs.
- Monitor for suspicious activity within privileged containers using tools like Falco or Kubernetes audit logs for exec commands.
- Implement RBAC policies to restrict exec access to pods, using role bindings that deny exec on sensitive pods.
- Use Pod Security Standards or admission controllers to enforce non-privileged execution.

## Objectives

1. Enumerate host devices to understand the node's hardware and potential attack surfaces.
2. Extract kernel messages to identify system events, errors, or logs that reveal configurations.
3. Identify potential vulnerabilities in the host kernel or devices for lateral movement or escalation.

## Instructions

### Step 1: List Host Devices

**Context**: Execute a command inside the privileged container to list all files in the host's /dev directory. This reveals mounted devices, such as disks, USBs, and special files, providing insights into the node's storage and peripherals. Use kubectl exec to run the command remotely.

**Command** ([[commands/ls-list-devices]]):
```bash
kubectl exec -it <pod-name> -- ls /dev
```

> This runs `ls /dev` inside the container, which maps to the host's /dev due to privileged mode. Replace `<pod-name>` with the actual pod name (e.g., `nginx-abc123`). The command lists device nodes like /dev/sda, /dev/null, and /dev/zero.

### Step 2: Read Kernel Messages

**Context**: Use the privileged container to read the kernel ring buffer via /dev/kmsg, which contains recent kernel logs including boot messages, driver errors, and security notices. This can expose kernel version, loaded modules, or failure points for targeted exploits.

**Command** ([[commands/cat-read-kernel-messages]]):
```bash
kubectl exec -it <pod-name> -- cat /dev/kmsg
```

> This pipes the kernel messages to stdout. The output may be verbose; redirect to a file if needed (e.g., `kubectl exec ... > kernel_logs.txt`). Look for indicators like kernel version strings or error codes in the logs.
