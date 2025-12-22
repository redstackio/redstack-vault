---
id: 6f6fc630-a1b9-4124-b4b1-081fb0e106e2
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:17.245600+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Privilege Escalation]]'
techniques:
  - '[[Escape to Host]]'
sub_techniques: []
tags:
  - container-escape
  - docker
  - kernel-module
  - procfs
commands:
  - '[[commands/cd-to-proc-escape-directory]]'
  - '[[commands/echo-hide-to-kernel-module]]'
  - '[[commands/echo-protect-to-kernel-module]]'
  - '[[commands/grep-pattern-in-proc-output]]'
platforms:
  - Linux
tools: []
skill_level: advanced
impact_level: high
detection_risk: high
validated: true
---

# Escape-Docker-Container-via-Kernel-Module-Procfs

## Summary

This procedure exploits a vulnerable kernel module within a Docker container to escape to the host system by manipulating procfs files. It assumes a malicious or vulnerable kernel module has already been loaded, allowing the attacker to hide and protect the module while extracting output, leading to arbitrary code execution on the host.

## Description

In containerized environments like Docker, attackers with initial access to a container can exploit kernel modules if the host kernel allows loading without proper restrictions. This technique targets the /proc filesystem interface provided by a vulnerable kernel module (e.g., one exposing an 'escape' directory). By navigating to /proc/escape and writing to control files like 'hide' and 'protect', the attacker conceals the module from detection and prevents unloading. Subsequently, output from the module (e.g., via /proc/output) can be queried to facilitate host access, such as spawning a shell or escalating privileges. This is particularly effective in misconfigured multi-tenant setups where AppArmor or seccomp profiles are not enforced. The procedure maps to MITRE ATT&CK technique T1611 (Escape to Host) under the Privilege Escalation tactic.

## Requirements

1. Initial access to a running Docker container with sufficient privileges to interact with /proc (typically root or high-priv user inside container).
2. A vulnerable kernel module already loaded on the host, exposing /proc/escape (e.g., via prior privilege escalation or misconfiguration).
3. Knowledge of the kernel module's interface, including control files like 'hide', 'protect', and output paths.
4. No external tools required; uses built-in shell commands.

## Defense

- Enforce strict kernel module loading policies using secure boot, module signing, or disabling modprobe in containers.
- Monitor procfs access and anomalous writes to /proc files via auditd or container runtime logs (e.g., Docker daemon).
- Use container security tools like AppArmor, SELinux, or seccomp to restrict syscalls related to module loading and procfs manipulation.
- Regularly scan for and remove unauthorized kernel modules on the host.

## Objectives

1. Hide the malicious kernel module from host enumeration tools like lsmod.
2. Protect the module from unloading to maintain persistence.
3. Extract module output to confirm escape and gain host shell access.
4. Achieve full host compromise from container breakout.

## Instructions

### Step 1: Navigate to the Escape Proc Directory

**Context**: Change the working directory to the procfs interface exposed by the vulnerable kernel module. This positions the shell to interact with control files for hiding and protecting the module.

**Command** ([[commands/cd-to-proc-escape-directory]]):
```bash
cd /proc/escape
```

> This command switches to the /proc/escape directory. If the directory does not exist, the module is not loaded or accessible, indicating failure (verify module loading prerequisites).

### Step 2: Hide the Kernel Module

**Context**: Write to the 'hide' control file to conceal the module from standard host queries (e.g., lsmod or /proc/modules), evading detection during the escape.

**Command** ([[commands/echo-hide-to-kernel-module]]):
```bash
echo 1 > hide
```

> Success is indicated by no error output; the module will no longer appear in loaded module lists on the host. If permission denied, escalate privileges inside the container.

### Step 3: Protect the Kernel Module from Unloading

**Context**: Write to the 'protect' control file to lock the module in memory, preventing automatic or manual unloading that could disrupt the escape.

**Command** ([[commands/echo-protect-to-kernel-module]]):
```bash
echo 1 > protect
```

> No output on success; the module is now persistent. Verify by attempting to unload (if possible) or checking host logs for unload failures.

### Step 4: Extract Module Output for Escape Confirmation

**Context**: Query the module's output file to retrieve any escaped data, such as host shell commands or credentials, confirming the breakout.

**Command** ([[commands/grep-pattern-in-proc-output]]):
```bash
grep -E 'pattern' /proc/output
```

> Replace 'pattern' with a specific regex for expected output (e.g., 'shell' for host access indicators). This filters relevant escape results; if no matches, the module may not have triggered the escape yet.
