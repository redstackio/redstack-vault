---
id: ac-snapcraft-rce-escape
tags:
  - rce
  - container-escape
  - snapcraft
  - dynamic-linker-hijacking
  - x11
type: attack_chain
tools:
  - '[[tools/tar]]'
  - '[[tools/snap]]'
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Linux
  - Ubuntu
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Prepare-Malicious-Directory-for-Snap-RCE]]'
  - '[[procedures/Trigger-RCE-in-Snap-Application]]'
  - '[[procedures/Demonstrate-Snap-Container-Restrictions]]'
  - '[[procedures/Escape-Snap-Container-via-X11]]'
  - '[[procedures/Verify-Host-Access-After-Escape]]'
step_count: 5
techniques:
  - '[[Dynamic Linker Hijacking]]'
  - '[[Escape to Host]]'
updated_at: '2025-12-14T17:23:23.843Z'
description: >-
  Multi-stage attack exploiting Snapcraft's empty LD_LIBRARY_PATH in wrapper
  scripts to achieve RCE inside the snap container, followed by escape to host
  via X11 permissions for full user access.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Dynamic Linker Hijacking]]'
  - '[[Escape to Host]]'
---
# Snapcraft RCE via Dynamic Linker Hijacking and X11 Container Escape

Multi-stage attack chain exploiting a vulnerability in Snapcraft versions before 4.4.4, where generated bash wrapper scripts use empty variables for LD_LIBRARY_PATH, causing the dynamic linker to load libraries from the current working directory (cwd). An attacker places a malicious libc.so.6 in the cwd or a subdirectory like 'tls', achieving initial RCE inside the snap container limited to user home directory access (non-dotfiles). This escalates to full system access as the current user via X11 permissions for container escape. Applicable to snap-installed apps like Chromium, VLC, or Docker when run from an attacker-controlled directory.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare Malicious CWD] --> B[Trigger RCE in Snap] --> C[Confirm Container Limits]
    C --> D[Escape via X11]
    D --> E[Full Host Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/tar]]
- [[tools/snap]]
- [[tools/make_libc.py]]

### Target Environment

- Ubuntu Linux (tested on 18.04.4 LTS)
- Snapcraft version < 4.4.4
- Vulnerable snap app installed (e.g., Chromium, VLC, Docker)
- X11 display server running with snap X11 plug enabled

### Initial Access Requirements

- Local user access to the target system
- Ability to extract files and run snap apps from custom directories
- No elevated privileges needed initially; exploits user-level snap execution

## Detailed Attack Procedures

### Step 1: Prepare Malicious Directory
procedure: [[procedures/Prepare-Malicious-Directory-for-Snap-RCE]]

**Objective**: Extract the POC archive to set up a malicious current working directory with fake files and a 'tls' subdirectory containing the hijacked libc.so.6 library.

**Instructions**: Use [[commands/extract-snap-escape-poc]] to unpack the archive:

```bash
tar xfvz snap-escape
```

Then change to the directory with [[commands/change-to-malicious-directory]]:

```bash
cd snap-escape
```

Verify setup using [[commands/list-directory-contents]]:

```bash
ls
```

**Expected Output**: Files like 'amazing-movie.mp4', 'README.txt', and 'tls' directory listed.

**Success Indicators**:
- POC files extracted successfully
- Current directory contains malicious 'tls' subdirectory

### Step 2: Trigger RCE in Snap Application
procedure: [[procedures/Trigger-RCE-in-Snap-Application]]

**Objective**: Run the vulnerable snap app from the malicious cwd to load the fake libc.so.6 via dynamic linker hijacking, achieving initial code execution inside the container.

**Instructions**: Launch the snap app, e.g., Chromium, using [[commands/run-chromium-from-malicious-dir]]:

```bash
chromium
```

This triggers the payload in the malicious library.

**Expected Output**: Console message like 'Got code execution running as itszn inside snap container!'.

**Success Indicators**:
- RCE payload executes inside snap
- Ability to write to non-dotfiles in home directory confirmed

### Step 3: Demonstrate Snap Container Restrictions
procedure: [[procedures/Demonstrate-Snap-Container-Restrictions]]

**Objective**: Verify confinement limits, such as inability to modify dotfiles or access /etc, to highlight the initial scoped impact.

**Instructions**: Attempt to write to a dotfile using [[commands/attempt-dotfile-modification]]:

```bash
echo 'echo PWNED' >> /home/itszn/.bashrc
```

Try reading system files with [[commands/attempt-system-file-read]]:

```bash
cat /etc/issue
```

**Expected Output**: Permission denied errors due to snap confinement.

**Success Indicators**:
- Access to dotfiles and /etc blocked
- Confirms RCE is container-bound

### Step 4: Escape Snap Container via X11
procedure: [[procedures/Escape-Snap-Container-via-X11]]

**Objective**: Exploit X11 permissions granted to the snap to break out of the container and gain host-level access as the current user.

**Instructions**: Leverage the X11 plug in the snap configuration to pivot from container to host; no direct command, but triggered post-RCE via payload exploiting DISPLAY environment and XAUTHORITY access.

**Expected Output**: Payload escalates to host context, allowing previously denied operations.

**Success Indicators**:
- Transition from container to host environment
- X11 socket access enables escape

### Step 5: Verify Host Access After Escape
procedure: [[procedures/Verify-Host-Access-After-Escape]]

**Objective**: Confirm full user privileges on the host by accessing restricted files and modifying dotfiles.

**Instructions**: Read system info with [[commands/read-system-issue-post-escape]]:

```bash
cat /etc/issue
```

Modify dotfile using [[commands/modify-dotfile-post-escape]]:

```bash
echo 'echo PWNED' >> /home/itszn/.bashrc
```

Verify with [[commands/check-dotfile-modification]]:

```bash
tail -n 1 /home/itszn/.bashrc
```

**Expected Output**: Successful read of '/etc/issue' (e.g., 'Ubuntu 18.04.4 LTS') and 'echo PWNED' appended.

**Success Indicators**:
- Full access to /etc and dotfiles
- Persistent host-level compromise

## Attack Chain Summary

### Key Achievements

1. Achieved RCE inside snap via cwd library hijacking
2. Demonstrated snap confinement limits
3. Escaped container using X11 for host access
4. Gained full user privileges, enabling dotfile modification and system reads

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Dynamic Linker Hijacking]] Dynamic Linker Search Order Hijacking
- [[Escape to Host]] Escape to Host

### MITRE ATT&CK Tactics

- [[Execution]] Execution
- [[Privilege Escalation]] Privilege Escalation

---

*Last updated: 2023-10-01T00:00:00Z*
