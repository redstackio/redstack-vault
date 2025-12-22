---
id: 1ef0f721-9848-4f45-b0c7-f732224a08b4
name: Linux-List-Capabilities-of-Executables
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:18.865869+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Defense Evasion]]'
  - '[[Privilege Escalation]]'
techniques:
  - '[[Abuse Elevation Control Mechanism]]'
  - '[[Process Injection]]'
sub_techniques: []
tags:
  - capabilities
  - linux-privilege-escalation
  - list-capabilities
commands:
  - '[[commands/getcap-list-capabilities-recursively]]'
platforms:
  - Linux
tools: []
validated: true
---

# Linux-List-Capabilities-of-Executables

## Summary

This procedure demonstrates how to list Linux file capabilities on executables to identify potential privilege escalation opportunities. Capabilities provide fine-grained privileges to processes without requiring full root access, and enumerating them reveals binaries that can be abused for elevated permissions in privilege escalation attacks.

## Description

On Linux systems, capabilities are a per-process privilege mechanism that replaces traditional setuid binaries for certain operations, such as binding to privileged ports or performing raw network I/O. They are stored as extended file attributes and can be queried using the `getcap` utility from the libcap package. This technique is commonly used during privilege escalation assessments to discover binaries with capabilities like `cap_net_raw` (for ping-like operations) or `cap_dac_override` (for bypassing file permissions). Attackers can then abuse these by injecting code into processes that inherit the capabilities or exploiting misconfigurations. The procedure targets common directories like `/usr/bin` and is applicable in post-exploitation scenarios where shell access is obtained. Success allows identification of vectors for techniques like abusing elevation controls or process injection, potentially leading to root access and data exfiltration.

## Requirements

1. Shell access to a Linux target system (local user privileges suffice, as `getcap` does not require elevated permissions).
2. `getcap` command available (part of libcap2-bin package; typically pre-installed on most distributions).
3. Read access to the target directories (e.g., `/usr/bin`, `/bin`).

## Defense

- Regularly audit and remove unnecessary capabilities from binaries using `setcap` to revoke them.
- Monitor system calls and process executions involving capabilities via auditd or sysdig for anomalous usage.
- Implement least-privilege principles by reviewing extended attributes with `getfattr` and restricting modifications to trusted administrators.

## Objectives

1. Enumerate capabilities on system executables to identify privilege escalation vectors.
2. Understand capability flags (e.g., `+ep` for effective and permitted) and their implications for abuse.
3. Verify output to spot high-value binaries like `ping` or `dumpcap` with network or override capabilities.

## Instructions

### Step 1: Enumerate Capabilities Recursively in a Directory

**Context**: Begin by targeting a directory containing executables, such as `/usr/bin`, to recursively list all files with capabilities. This step reveals binaries that inherit special privileges, which can be abused for escalation without full setuid root execution. The `-r` flag ensures recursive scanning, and output formats as `filename = cap_name+flags`.

**Command** ([[commands/getcap-list-capabilities-recursively]]):
```bash
ggetcap -r $_DIRECTORY
```

> The `getcap` command queries extended attributes for capabilities. Replace `$_DIRECTORY` with a path like `/usr/bin`. If no capabilities are present, output will be empty; otherwise, it lists files with associated privileges. This step is non-destructive and runs quickly on standard systems.

**Expected Output**:
```
/usr/bin/fping                = cap_net_raw+ep
/usr/bin/dumpcap              = cap_dac_override,cap_net_admin,cap_net_raw+eip
/usr/bin/gnome-keyring-daemon = cap_ipc_lock+ep
/usr/bin/rlogin               = cap_net_bind_service+ep
/usr/bin/ping                 = cap_net_raw+ep
/usr/bin/rsh                  = cap_net_bind_service+ep
/usr/bin/rcp                  = cap_net_bind_service+ep
```

**Success Indicators**:
- Output lists one or more binaries with capabilities (e.g., `cap_net_raw` indicates raw socket access).
- No permission errors; command completes without warnings.
