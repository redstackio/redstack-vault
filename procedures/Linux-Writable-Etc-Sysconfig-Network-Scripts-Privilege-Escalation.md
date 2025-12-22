---
id: bde66c0e-b1d4-4c22-b296-de55267f37f0
name: Linux-Writable-Etc-Sysconfig-Network-Scripts-Privilege-Escalation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:19.195678+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Abuse Elevation Control Mechanism|T1548 - Abuse Elevation
    Control Mechanism]]
  - '[[techniques/Setuid and Setgid|T1166 - Setuid and Setgid]]'
sub_techniques: []
tags:
  - '[[tags/Linux - Privilege Escalation]]'
  - '[[tags/Writable /etc/sysconfig/network-scripts/ (Centos/Redhat)]]'
  - '[[tags/Writable files]]'
commands:
  - '[[commands/ls-check-directory-permissions]]'
  - '[[commands/cat-write-ifcfg-file]]'
  - '[[commands/ifup-trigger-interface]]'
platforms:
  - Linux
tools: []
validated: true
---

# Linux-Writable-Etc-Sysconfig-Network-Scripts-Privilege-Escalation

## Summary

This procedure exploits writable permissions on the /etc/sysconfig/network-scripts/ directory in CentOS or RedHat-based Linux systems to inject arbitrary commands into network interface configuration files. These files are sourced and executed with root privileges during network interface activation (e.g., via ifup or system boot), enabling privilege escalation from a low-privileged user to root.

## Description

On CentOS and RedHat systems, the /etc/sysconfig/network-scripts/ directory contains ifcfg-* files that define network interface configurations. These files are sourced by the ifup script, which runs as root. If the directory is world-writable (e.g., due to misconfiguration), an attacker with low-privileged access can create or modify an ifcfg-* file to inject commands into variable assignments or custom fields like EXEC. When the interface is brought up, the sourced file executes the injected commands as root. This technique is effective in post-exploitation scenarios where initial foothold is gained but escalation is needed. It provides persistence if the file remains and the system reboots, or immediate escalation if triggered via ifup.

## Requirements

1. Low-privileged shell access to the target system.
2. Write access to /etc/sysconfig/network-scripts/ directory (verify with ls -ld).
3. Target running CentOS or RedHat (RHEL) distribution.
4. Network interface management tools like ifup/ifdown available (standard on these distros).

## Defense

Defensive measures and detection strategies:

- Restrict write access to the /etc/sysconfig/network-scripts/ directory to root only (chmod 755 or lower).
- Monitor the directory for unauthorized changes using file integrity monitoring tools like AIDE or auditd.
- Implement the principle of least privilege to limit low-privileged users' access to system directories.
- Log and alert on ifup executions and file modifications in /etc/sysconfig/.

## Objectives

1. Verify and exploit writable permissions to inject a malicious configuration file.
2. Trigger execution of the injected commands to gain root privileges.
3. Achieve arbitrary command execution as root for further post-exploitation.

## Instructions

### Step 1: Verify Directory Writability

**Context**: Confirm that the /etc/sysconfig/network-scripts/ directory is writable by the current user, which is a prerequisite for injecting the malicious configuration.

**Command** ([[commands/ls-check-directory-permissions]]):
```bash
ls -ld /etc/sysconfig/network-scripts/
```

> This command lists the directory permissions. Look for 'w' in the group or other permissions indicating writability (e.g., drwxrwxrwt). If not writable, this procedure cannot proceed.

### Step 2: Create Malicious ifcfg Configuration File

**Context**: Write a specially crafted ifcfg file using the provided code snippet. The file injects a command like /bin/id into the NAME field (exploiting space injection during sourcing) and uses EXEC to reference a payload, allowing root execution when sourced by ifup.

**Command** ([[commands/cat-write-ifcfg-file]]):
```bash
cat > /etc/sysconfig/network-scripts/ifcfg-1337 << 'EOF'
```

> Follow this by pasting the content from [[codes/Ifcfg-Network-Script-Privilege-Escalation-Config]]. This creates the file ifcfg-1337 with the injected commands. Verify creation with ls /etc/sysconfig/network-scripts/ifcfg-1337.

### Step 3: Trigger Interface Activation to Execute Payload

**Context**: Bring up the fake interface defined in the ifcfg file to cause ifup to source it and execute the injected commands as root.

**Command** ([[commands/ifup-trigger-interface]]):
```bash
ifup ifcfg-1337
```

> This sources the malicious file as root. If successful, the injected commands (e.g., /bin/id) will run, demonstrating escalation. For persistence, the file will execute on reboot; for immediate effect, this step triggers it without reboot.
