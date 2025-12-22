---
id: a6311525-15fc-4836-aa89-80bfb805ffd2
name: Linux-Add-Root-User-Persistence
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:17.910876+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - '[[techniques/Account Manipulation|T1098 - Account Manipulation]]'
  - '[[techniques/Create Account|T1136 - Create Account]]'
sub_techniques: []
tags:
  - '[[tags/linux-persistence]]'
  - '[[tags/create-account]]'
  - '[[tags/root-user]]'
commands:
  - '[[commands/useradd-create-root-user]]'
  - '[[commands/passwd-set-password-interactive]]'
  - '[[commands/passwd-set-password-stdin]]'
platforms:
  - Linux
tools: []
validated: true
---

# Linux-Add-Root-User-Persistence

## Summary

This procedure creates a new user account with root-level privileges (UID 0) on a Linux system and sets its password, establishing persistence even if original credentials are revoked. It is typically used post-compromise to maintain long-term access to the target system for data exfiltration, lateral movement, or further exploitation.

## Description

In a post-exploitation scenario on a Linux host, attackers with administrative access can create a backdoor account by adding a new user with root UID and GID, effectively duplicating root privileges. This technique leverages standard system utilities like useradd and passwd to avoid detection from custom tools. The new account allows login via SSH, console, or other means, bypassing changes to the primary root password or account locks. This is particularly effective in environments where user creation is not heavily monitored, providing a stealthy persistence mechanism mapped to MITRE ATT&CK techniques for account creation and manipulation.

## Requirements

1. Administrative (root or sudo) privileges on the target Linux system.
2. Access to a terminal or shell on the compromised host.
3. Basic knowledge of Linux user management commands.

## Defense

- Limit administrative privileges to necessary users and implement principle of least privilege.
- Monitor for new user account creations and modifications using tools like auditd or centralized logging (e.g., alert on useradd executions or /etc/passwd changes).
- Enable multi-factor authentication (MFA) for all accounts, including root-equivalent users, and regularly audit user lists with commands like getent passwd | grep uid=0.

## Objectives

1. Create a new user account with root-level privileges (UID 0 and GID 0).
2. Set a secure password for the new account to enable future logins.
3. Establish persistence by providing an alternative root access path that survives credential changes.

## Instructions

### Step 1: Create New Root User Account

**Context**: This step uses the useradd command to create a new user with UID 0 and GID 0, granting it full root privileges without modifying the existing root account.

**Command** ([[commands/useradd-create-root-user]]):
```bash
sudo useradd -ou 0 -g 0 $_USERNAME
```

> The -o flag allows a non-unique UID, and -g 0 assigns the root group. Replace $_USERNAME with a stealthy name (e.g., a legitimate-looking username). Expected output is no error message, confirming the user is added; verify with `id $_USERNAME` showing uid=0(root).

### Step 2: Set Password Interactively

**Context**: Optionally, set the password interactively for security, prompting for input to avoid logging plaintext passwords in command history.

**Command** ([[commands/passwd-set-password-interactive]]):
```bash
sudo passwd $_USERNAME
```

> Enter the desired password when prompted (twice for confirmation). This avoids piping sensitive data. Expected output is "password updated successfully"; test by switching user with `su - $_USERNAME`.

### Step 3: Set Password via Standard Input (Automated)

**Context**: For scripted or non-interactive execution, pipe the password directly to passwd using echo and --stdin, useful in automated persistence deployment but riskier due to potential logging.

**Command** ([[commands/passwd-set-password-stdin]]):
```bash
echo "$_PASSWORD" | sudo passwd --stdin $_USERNAME
```

> Replace $_PASSWORD with a strong, unique value. This method is faster for batch operations. Expected output is "password updated successfully"; avoid using in environments with command logging enabled, as it may expose the password in history or process lists.
