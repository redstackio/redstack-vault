---
type: procedure
tactics:
  - '[[Privilege Escalation]]'
techniques:
  - '[[Escape to Host]]'
sub_techniques: []
tags:
  - container-escape
  - docker-pentest
  - breaking-out-of-containers
  - device-file
  - fdpasser
commands:
  - '[[commands/fdpasser-recv-bind-file-descriptor-in-container]]'
  - '[[commands/fdpasser-send-file-descriptor-from-host]]'
  - '[[commands/ls-list-host-file-permissions]]'
platforms:
  - Linux
  - Docker
tools:
  - '[[tools/fdpasser]]'
skill_level: advanced
impact_level: high
detection_risk: high
verified: true
validated: true
---

# Container-Escape-Using-Device-File

## Summary

This procedure outlines a technique to escape from a Docker container to the host system by leveraging the fdpasser tool to pass file descriptors between the container and host namespaces. By binding a received file descriptor to a local path inside the container and sending it from the host via the container's process namespace, an attacker with root access in the container can access or modify sensitive host files like /etc/shadow, effectively breaking container isolation.

## Description

Container escapes occur when isolation mechanisms fail, often due to misconfigurations such as privileged mode or shared Unix sockets. The fdpasser tool facilitates this by allowing the transmission of open file descriptors over Unix domain sockets, which can be made accessible across namespaces (e.g., via bind mounts). In this scenario, the attacker first prepares reception inside the container to target a host file, then from the host sends the descriptor of the bound file accessed through the container's root filesystem (/proc/<pid>/root). This can result in the host file gaining altered permissions (e.g., world-readable or setuid), enabling unauthorized access or privilege escalation on the host. This technique requires root in the container and host access for sending, typically in a post-exploitation phase after initial container compromise.

## Requirements

1. Root privileges inside the target container.
2. Command execution access on the host system (e.g., via SSH, another escape vector, or console access).
3. fdpasser binary available both inside the container and on the host.
4. A Unix domain socket accessible from both environments (e.g., bind-mounted /tmp/fdpasser.sock; configure as per tool documentation).
5. Ability to identify the container's process PID from the host (e.g., via `docker ps` or `pgrep`).

## Defense

- Avoid running containers in privileged mode and limit capabilities (e.g., drop CAP_SYS_ADMIN).
- Do not bind-mount host device files, /proc, or Unix sockets into untrusted containers.
- Enforce mandatory access controls like AppArmor, SELinux, or seccomp to block FD-passing syscalls (e.g., sendmsg/recvmsg).
- Monitor container and host for fdpasser execution, anomalous socket connections, or permission changes on critical files (e.g., via auditd or Falco).
- Use immutable container images and runtime security tools to prevent binary execution inside containers.

## Objectives

1. Bypass container isolation to access host system files directly.
2. Modify host file permissions or contents to enable further privilege escalation.
3. Achieve persistence or data exfiltration on the host by reading sensitive files like /etc/shadow.

## Instructions

### Step 1: Prepare the Environment and Tool

**Context**: Ensure the fdpasser tool is installed and ready on both the host and inside the container. Set up a shared Unix socket if not already configured (e.g., create /tmp/fdpasser.sock and bind-mount it into the container). This step is crucial for enabling FD passing across namespaces.

Refer to [[tools/fdpasser]] for compilation and setup. Copy the binary into the container if necessary (e.g., via `docker cp` from host).

### Step 2: Receive File Descriptor Inside the Container

**Context**: As root inside the container, execute the receive command to listen on the Unix socket and bind the incoming file descriptor to a local path (/moo). Specify the target host file (/etc/shadow) to focus the access attempt. This creates a bridge allowing the container to interact with the host resource.

**Command** ([[commands/fdpasser-recv-bind-file-descriptor-in-container]]):
```bash
./fdpasser recv /moo /etc/shadow
```

> This command opens the socket, receives the FD from the host, and binds it to /moo inside the container, effectively granting access to the host's /etc/shadow with potentially elevated permissions visible from the container. Expected output includes a confirmation like "File descriptor received successfully." You can then interact with /moo as if it were the host file (e.g., cat /moo to read shadow contents).

### Step 3: Send File Descriptor from the Host

**Context**: On the host, locate the PID of a process running inside the target container (e.g., using `docker inspect` or `pgrep` for a unique process like a sleep command). Then, open the bound path (/moo) via the container's namespace (/proc/<pid>/root/moo) and send its file descriptor back over the socket. This completes the pass, synchronizing access and potentially altering the host file's effective permissions.

**Command** ([[commands/fdpasser-send-file-descriptor-from-host]]):
```bash
./fdpasser send /proc/$(pgrep -f "sleep 1337")/root/moo
```

> Replace "sleep 1337" with the actual process pattern or use the direct PID (e.g., /proc/1234/root/moo). This transmits the FD, enabling the container's view to influence the host file. Expected output: "File descriptor sent successfully." If successful, the technique may propagate permission changes.

### Step 4: Verify Success by Checking Host File Permissions

**Context**: Back on the host, inspect the target file's permissions to confirm the escape. Successful execution often results in modified permissions (e.g., from -rw------- to -rwsrwsrwx), indicating the container was able to influence the host resource.

**Command** ([[commands/ls-list-host-file-permissions]]):
```bash
ls -la /etc/shadow
```

> Expected output for success:
```
-rwsrwsrwx 1 root shadow 1209 Oct 10  2019 /etc/shadow
```
The appearance of setuid (s) or world-writable (rw) bits confirms the escape, as the container has effectively escalated access to the host file.
