---
id: cda165a9-28fc-47a0-9d32-eec598181075
name: Change Password in a Writable /etc/passwd
type: procedure
verified: true
submitted: false
created_at: '2019-10-10T00:49:03.893825+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/File System Permissions Weakness|T1044 - File System
    Permissions Weakness]]
sub_techniques: []
tags:
  - '[[tags/misconfiguration]]'
  - '[[tags/Setup]]'
commands:
  - '[[commands/openssl-generate-sha512-crypt-hash]]'
platforms:
  - Linux
tools: []
validated: true
---

# Change Password in a Writable /etc/passwd

## Summary

When /etc/passwd is writable due to misconfiguration, an attacker can change a user's password by directly inserting a password hash into the file. This technique leverages legacy priority of /etc/passwd over /etc/shadow, allowing persistence or privilege escalation by targeting high-privilege accounts like root. It is particularly effective in environments where file permissions are overly permissive.

## Description

In Linux systems, the /etc/passwd file stores user account information, including password hashes in older or misconfigured setups. Normally, passwords are managed in /etc/shadow for security, but if /etc/passwd is writable (e.g., permissions 666 or owned by a low-privilege group), an attacker with write access can modify it to set a new password hash for any user. This overrides shadow entries and grants immediate access upon login. The procedure involves generating a SHA512-crypt hash using OpenSSL and editing the file entry. This is a post-exploitation technique for maintaining access or escalating privileges, assuming initial foothold via another vector like weak credentials or RCE.

## Requirements

1. Write access to /etc/passwd (check with `ls -l /etc/passwd`; should be writable by current user or group).
2. Knowledge of the target user's current entry in /etc/passwd (view with `grep user /etc/passwd`).
3. OpenSSL installed on the target system (common on Linux distributions).
4. Desired plaintext password to hash.
5. Backup of original /etc/passwd to avoid locking out legitimate users (optional but recommended for testing).

## Defense

- Enforce strict file permissions on /etc/passwd (644, owned by root:root) and monitor changes with tools like auditd or file integrity monitoring (e.g., Tripwire, AIDE).
- Use centralized authentication like LDAP or SSSD to avoid local file dependencies.
- Enable shadow password suite fully and disable legacy /etc/passwd password storage.
- Log and alert on modifications to critical files via SELinux/AppArmor or SIEM integration.

## Objectives

1. Generate a secure SHA512-crypt hash for the new password to insert into /etc/passwd.
2. Modify the target user's entry to include the new hash, enabling login with the chosen password.
3. Verify the change allows authentication without disrupting system functionality.

## Instructions

### Step 1: Identify the Target User and Verify Writable Access

**Context**: Select a user account to modify, such as root for privilege escalation. Confirm write permissions to ensure the modification will succeed without sudo escalation.

Run the following to view the current entry and check permissions:

```bash
grep root /etc/passwd
ls -l /etc/passwd
```

> This step identifies the exact line to edit (e.g., `root:x:0:0:root:/root:/bin/bash`) and confirms writability (look for `rw` in group/other permissions).

### Step 2: Generate SHA512-Crypt Password Hash

**Context**: Create a salted SHA512 hash of the desired password using OpenSSL. This hash will replace the 'x' placeholder in the password field, ensuring compatibility with modern Linux auth systems.

**Command** ([[commands/openssl-generate-sha512-crypt-hash]]):
```bash
openssl passwd -6 -salt $_SALT $_PASSWORD
```

> Choose a random salt (8 characters, alphanumeric) for security. For example, with salt '12345678' and password 'secretpass', the output is a hash like `$6$12345678$DgaVYkZjVTY58m0juyhsvwGEjwMI9RB5U0U63JEP2as7KF/gNTboh3MC6aE8CjcVHmb1Er9RWwbRQmaHhBUfs/`. This step produces the hash needed for insertion.

### Step 3: Edit /etc/passwd with the New Hash

**Context**: Backup the original file, then replace the 'x' in the password field with the generated hash. Use a text editor like vi or sed for the modification. Reference the original and modified entry examples below.

First, backup:

```bash
cp /etc/passwd /etc/passwd.bak
```

Then edit (using vi as example):

```bash
vi /etc/passwd
```

Replace the line from:

[[codes/original-etc-passwd-root-entry]]

To:

[[codes/modified-etc-passwd-root-entry-with-sha512-hash]]

> Save and exit. If using sed for automation: `sed -i 's/^root:x/root:$6$12345678$DgaVYkZjVTY58m0juyhsvwGEjwMI9RB5U0U63JEP2as7KF/gNTboh3MC6aE8CjcVHmb1Er9RWwbRQmaHhBUfs//g' /etc/passwd` (adjust hash). This step completes the password change.

### Step 4: Verify the Change

**Context**: Test the new password by attempting login or using su to switch users, confirming the hash works without errors.

```bash
su root
# Enter 'secretpass' when prompted
```

> Success is indicated by successful authentication and shell access. If it fails, revert from backup and check hash format.
