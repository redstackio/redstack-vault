---
type: procedure
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
  - '[[sub-techniques/Credentials In Files|T1552.001 - Credentials In Files]]'
tags:
  - '[[tags/Find sensitive files]]'
  - '[[tags/Linux - Privilege Escalation]]'
  - '[[tags/Looting for passwords]]'
commands:
  - '[[commands/locate-search-password-files]]'
platforms:
  - Linux
skill_level: beginner
impact_level: high
detection_risk: low
verified: true
validated: true
---

# Linux-Password-Looting

## Summary

Linux Password Looting involves systematically searching a compromised Linux system for files containing sensitive credentials, such as passwords stored in configuration files, history logs, or unsecured locations. This procedure uses built-in tools like the 'locate' command to quickly identify potential password-related files, followed by manual inspection to extract usable credentials for privilege escalation or lateral movement.

## Description

On a compromised Linux host, attackers often target common storage locations for credentials, including system files like /etc/shadow, user history files (~/.bash_history), SSH keys (~/.ssh/), and application configs that may embed plaintext passwords. The 'locate' command leverages a pre-built database to perform fast filename-based searches, making it efficient for initial reconnaissance without alerting host-based monitoring. Once files are identified, they can be inspected with tools like cat, grep, or strings to reveal credentials. This technique is particularly effective in environments with weak file permissions or legacy configurations. Success depends on the locate database being up-to-date; if not, alternatives like find can be used. Mapped to MITRE ATT&CK as part of Credential Access via unsecured files, this can lead to further compromise if passwords are reused or weak.

## Requirements

1. Shell access to the target Linux system (local or remote via SSH/reverse shell).
2. The 'locate' command available (part of mlocate package, usually pre-installed on most distributions).
3. Updated locate database (run 'updatedb' as root if necessary; may require elevated privileges).
4. Basic text processing tools like grep, cat, and awk for inspecting found files.

## Defense

- Enforce strict file permissions on sensitive locations (e.g., chmod 600 ~/.ssh/id_rsa, 640 /etc/shadow).
- Use tools like AppArmor or SELinux to restrict access to credential stores.
- Regularly rotate passwords and avoid storing them in plaintext files; use credential managers like HashiCorp Vault.
- Monitor for anomalous file access via auditd or sysdig, and enable full filesystem auditing.
- Periodically update and secure the mlocate database to prevent its abuse.

## Objectives

1. Identify files on the system that may contain passwords or credentials based on filenames.
2. Inspect and extract any readable credentials from located files.
3. Validate extracted credentials for reuse in privilege escalation or other attacks.

## Instructions

### Step 1: Update the Locate Database

**Context**: The 'locate' command relies on a database of file names and paths. If the database is outdated (e.g., after recent file changes), searches may miss relevant files. Updating ensures comprehensive results, but note this requires root privileges and may generate logs.

If you have sudo access, execute the update command. Otherwise, proceed to search with the current database and fall back to 'find' if needed.

**Command** ([[commands/locate-search-password-files]]):
```bash
sudo updatedb
```

> This rebuilds the database by indexing the filesystem. It may take several minutes on large systems. Expected output is minimal (progress indicators if verbose), and success is confirmed by no errors.

### Step 2: Search for Password-Related Files

**Context**: Use 'locate' to query for files containing 'password' in the name, which often flags configs, modules, or scripts with embedded credentials. Pipe to 'more' or 'less' for paginated viewing if the output is lengthy. This step uncovers potential targets like PAM configs or grub modules without directly reading contents.

**Command** ([[commands/locate-search-password-files]]):
```bash
locate password | more
```

> The command scans the database for matching paths. Expected output is a list of file paths, such as /etc/pam.d/common-password or /boot/grub/password.mod. Review the list for user-accessible files (e.g., avoid /etc/shadow if no root).

### Step 3: Inspect and Extract from Key Files

**Context**: From the located files, prioritize inspection of readable ones. Common extractions include grep for 'pass' patterns in configs or cat for history files. If a file contains hashes (e.g., from /etc/shadow), note them for offline cracking; plaintext is immediately usable.

For example, check a found PAM file:
```bash
grep -i password /etc/pam.d/common-password
```

Or view bash history for typed commands:
```bash
cat ~/.bash_history | grep -i pass
```

> Expected output varies: plaintext passwords in configs, command snippets in history, or error if permission denied. Success if credentials are revealed; document them for validation (e.g., test with su or ssh).
