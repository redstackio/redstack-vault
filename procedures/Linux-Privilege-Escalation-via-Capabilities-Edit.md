---
id: 232df366-d649-4335-8783-bff6d52967ae
name: Linux-Privilege-Escalation-via-Capabilities-Edit
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:18.892896+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Abuse Elevation Control Mechanism|T1548 - Abuse Elevation
    Control Mechanism]]
sub_techniques: []
tags:
  - '[[tags/Capabilities]]'
  - '[[tags/Edit-capabilities]]'
  - '[[tags/Linux-Privilege-Escalation]]'
commands:
  - '[[commands/setcap-add-cap_net_raw-p-to-ping-binary]]'
  - '[[commands/setcap-remove-capabilities-from-ping-binary]]'
platforms:
  - Linux
tools: []
validated: true
---

# Linux-Privilege-Escalation-via-Capabilities-Edit

## Summary

This procedure demonstrates how to escalate privileges on a Linux system by editing file capabilities using the setcap utility. By adding or removing specific capabilities like cap_net_raw to executables such as /bin/ping, an attacker with low-privileged access can grant themselves elevated permissions to perform actions typically restricted to root, such as sending raw network packets, enabling further post-exploitation activities.

## Description

Linux capabilities provide a fine-grained alternative to traditional setuid binaries for delegating privileges to processes without full root access. This technique involves using the setcap command to modify the capabilities of an existing binary, such as adding the cap_net_raw capability to ping, which allows a non-root user to perform raw socket operations. This can be abused for privilege escalation by enabling unauthorized network interactions or chaining with other exploits. The procedure assumes the attacker has write access to the binary or is operating in an environment where capability modifications are not restricted. It maps to scenarios where initial foothold access has been gained, and the goal is to expand control over the system. Expected outcomes include successful modification of capabilities, verifiable via getcap, leading to elevated functionality without full root compromise.

## Requirements

1. Low-privileged shell access on a Linux target system (e.g., via SSH or initial exploit).
2. setcap utility installed (part of libcap2-bin package on Debian-based systems).
3. Write permissions on the target binary (e.g., /bin/ping) or a custom executable in a writable directory.
4. Knowledge of Linux capabilities (e.g., cap_net_raw for raw network access).

## Defense

- Restrict setcap usage to root-only via file permissions and SELinux/AppArmor policies.
- Monitor system calls related to capability modifications using auditd (e.g., watch for setcap executions).
- Regularly audit file capabilities with getcap on critical binaries and alert on changes.
- Implement least privilege by avoiding unnecessary capabilities on executables and using containers for isolation.

## Objectives

1. Modify executable capabilities to grant elevated permissions to a low-privileged user.
2. Verify the capability changes and demonstrate escalated functionality (e.g., raw packet sending).
3. Enable further post-exploitation by expanding access without full root privileges.

## Instructions

### Step 1: Verify Current Capabilities

**Context**: Before modifying, check the existing capabilities on the target binary to understand the baseline and ensure the change is necessary. This helps confirm if cap_net_raw is already present or can be added.

Use [[commands/getcap-check-file-capabilities]] (note: this is a supporting command; implement via getcap /bin/ping) to inspect:

```bash
gitcap /bin/ping
```

> The getcap command lists capabilities. Expected output might show /bin/ping = cap_net_raw+p if already set, or no output if none. This step confirms the binary's state and identifies if escalation is feasible.

### Step 2: Remove Existing Capabilities

**Context**: If the binary has unwanted or conflicting capabilities, remove them first to start clean. This prevents permission errors during addition and ensures precise control.

Execute [[commands/setcap-remove-capabilities-from-ping-binary]]:

```bash
/usr/bin/setcap -r /bin/ping
```

> The -r flag removes all capabilities from the specified file. On success, no output is produced; verify with getcap showing no capabilities. Failure might output "failed to set capabilities" if permissions are insufficient.

### Step 3: Add Specific Capability for Escalation

**Context**: Add the cap_net_raw+p capability to enable raw network operations, allowing ping (or similar) to function with elevated privileges as a non-root user. The +p makes it inheritable for child processes.

Execute [[commands/setcap-add-cap_net_raw-p-to-ping-binary]]:

```bash
/usr/bin/setcap cap_net_raw+p /bin/ping
```

> This grants the ability to use raw sockets. Success is silent; verify by running ping as non-root and checking getcap output: /bin/ping = cap_net_raw+p. This enables privilege escalation for network-based attacks.

### Step 4: Test Escalated Functionality

**Context**: Validate the escalation by executing the modified binary to perform an action that requires the new capability, confirming the privilege gain.

Run ping on a target:

```bash
ping -c 1 8.8.8.8
```

> As a non-root user, this should now succeed without errors related to raw sockets. Look for successful ICMP responses in output, indicating the capability is active and escalation achieved.
