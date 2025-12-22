---
id: ddc5baeb-b72b-4577-a70c-5f893f3b8605
name: Command-Injection-to-Read-Etc-Passwd
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:57.103744+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter/Command-Line-Interface|T1059.003
    - Windows Command Shell]]
tags:
  - command-injection
  - exploits
  - rce
commands:
  - '[[commands/cat-display-etc-passwd]]'
platforms:
  - Linux
  - Web
tools: []
validated: true
---

# Command-Injection-to-Read-Etc-Passwd

## Summary

This procedure demonstrates how to exploit a command injection vulnerability in a web application to execute the `cat /etc/passwd` command on the underlying Linux server, allowing an attacker to read sensitive user account information from the /etc/passwd file. It is commonly used in web penetration testing to identify and exploit input validation flaws that permit arbitrary command execution.

## Description

Command injection vulnerabilities occur when a web application passes untrusted user input directly to a system shell command without proper sanitization, enabling attackers to append or inject additional commands. In this scenario, the application executes a backend command (e.g., a ping or file operation) based on user input, and by injecting shell metacharacters like backticks (`) or command substitution ($( )), the attacker can chain the `cat /etc/passwd` command to retrieve the file contents. The /etc/passwd file contains user account details, including usernames, UIDs, home directories, and shells, which can aid in further enumeration or privilege escalation. This technique targets Linux-based web servers and is effective against applications written in languages like PHP, Python, or Node.js that invoke system calls. Success depends on the application's input handling and the server's shell environment.

## Requirements

1. Access to a web application with a known or suspected command injection vulnerability, typically via a user input field (e.g., search box, ping tool, or file viewer).
2. Network connectivity to the target application over HTTP/HTTPS.
3. Basic knowledge of shell metacharacters and Linux commands.
4. Tools like a web browser or proxy (e.g., Burp Suite) for intercepting and modifying requests.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization, whitelisting allowed characters and rejecting shell metacharacters like `, $, ;, |, &&.
- Use parameterized APIs or safe library functions (e.g., Python's subprocess.run with shell=False) instead of direct system calls with user input.
- Deploy a Web Application Firewall (WAF) to detect and block common injection patterns, such as concatenated commands.
- Enable application logging for all system command executions and monitor for anomalous outputs, like unexpected file contents in responses.
- Run web applications in isolated environments (e.g., containers) with minimal privileges to limit the impact of successful injections.

## Objectives

1. Identify a vulnerable input point in the web application that executes system commands.
2. Inject a payload to execute `cat /etc/passwd` and retrieve the file contents.
3. Analyze the output for user account information to support further attacks like enumeration or lateral movement.

## Instructions

### Step 1: Identify the Vulnerable Input

**Context**: Locate an input field in the application that passes data to a system command, such as a diagnostic tool or search feature. Test for injection by appending simple payloads like `; id` to see if command output appears in the response.

**Command** ([[commands/cat-display-etc-passwd]]):

Use this command as the base for injection testing.

> This step verifies the vulnerability. If the response includes output from `id` (e.g., uid=33(www-data)), proceed to injection.

### Step 2: Craft and Inject the Payload

**Context**: Construct the injection using shell metacharacters to execute the additional command alongside the original one. Backticks or $() will substitute the output of `cat /etc/passwd` into the response.

**Code** ([[codes/Bash-Command-Injection-Payload-for-Cat-Etc-Passwd]]):

Embed the payload in the vulnerable input field, replacing `original_cmd_by_server` with the application's expected command (e.g., `ping`).

> Submit the payload via the web form or API request. The server will execute the injected command, and the /etc/passwd contents should appear in the application's output, such as a concatenated response string.

### Step 3: Verify and Analyze Output

**Context**: Confirm the injection success by checking for the expected file contents in the response, then parse for useful information like root or service account details.

**Command** ([[commands/cat-display-etc-passwd]]):

The injected command will produce output similar to:

```bash
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
```

> Look for indicators like multiple user entries or unexpected file paths. If no output appears, try variations like encoding the payload (e.g., base64) or using different metacharacters.
