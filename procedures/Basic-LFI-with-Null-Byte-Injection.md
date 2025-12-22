---
id: 2f1d95af-c677-4d14-a4f6-0b4a1d6915af
name: Basic-LFI-with-Null-Byte-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:58.040475+00:00'
updated_at: '2023-04-10T20:22:13.110206+00:00'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Basic LFI]]'
  - '[[tags/File Inclusion]]'
  - '[[tags/Null byte]]'
  - lfi
  - php
  - file-disclosure
commands:
  - '[[commands/curl-basic-lfi-null-byte]]'
platforms:
  - Web
  - Linux
tools: []
skill_level: beginner
impact_level: medium
detection_risk: low
validated: true
---

# Basic-LFI-with-Null-Byte-Injection

## Summary

This procedure outlines how to exploit a Local File Inclusion (LFI) vulnerability in PHP applications (versions below 5.3.4) by injecting a null byte (%00) into the file path parameter. This tricks the application into terminating the string early, allowing access to sensitive files outside the intended directory, such as /etc/passwd or configuration files, enabling information disclosure and potential further compromise.

## Description

Local File Inclusion vulnerabilities occur when user-supplied input is used to include files without proper validation, allowing attackers to read arbitrary files on the server. In older PHP versions (<5.3.4), null bytes act as string terminators in certain contexts, like file functions (e.g., include() or file_get_contents()). By appending a null byte after a path traversal sequence (e.g., ../../../../etc/passwd%00), the application reads the desired file while ignoring any subsequent filtering or extension checks. This technique is useful in web penetration testing to disclose system files, credentials, or source code. It targets public-facing web apps and requires no authentication, but success depends on the application's input handling and PHP configuration (e.g., allow_url_include off, but file inclusion enabled).

## Requirements

1. Network access to a vulnerable web application (e.g., HTTP/HTTPS endpoint).
2. Identification of the LFI parameter (e.g., ?page= or ?file= in the URL).
3. Confirmation of PHP version <5.3.4 (can be checked via error messages or tools like phpversion()).
4. A tool like curl or a web browser for sending requests; Burp Suite recommended for interception and manipulation.
5. Basic knowledge of path traversal payloads and the target server's file structure (e.g., Linux paths like /etc/passwd).

## Defense

Defensive measures and detection strategies:

- Upgrade PHP to version 5.3.4 or later, where null byte handling was fixed in string operations.
- Implement strict input validation: whitelist allowed file paths, reject traversal sequences (../), and sanitize user input using basename() or realpath().
- Use access controls like chroot jails or containerization to limit file system access; disable dangerous functions (include(), require()) via php.ini.
- Monitor web server logs for suspicious requests containing %00, ../ sequences, or attempts to access /etc/, /proc/, or config files; use WAF rules to block LFI patterns.
- Enable PHP error logging and security headers to prevent information leakage.

## Objectives

1. Exploit LFI to read sensitive system files on the target server.
2. Disclose configuration files, user credentials, or application source code.
3. Gather information for further attacks, such as credential reuse or privilege escalation within the organization.

## Instructions

### Step 1: Identify the Vulnerable Parameter and Test Basic LFI

**Context**: Locate the file inclusion parameter and verify basic path traversal works without null byte, to confirm LFI susceptibility. This step ensures the application includes files based on user input.

Look for endpoints like index.php?page=home and test traversal by appending ../ sequences to reach known files.

**Command** ([[commands/curl-basic-lfi-null-byte]]):

Use a modified curl command to test a basic traversal first (adjust payload for your target).

```bash
curl "http://$_TARGET_URL/index.php?page=../../../etc/passwd"
```

> This sends a request attempting to include /etc/passwd. If successful, you'll see user account listings; if filtered (e.g., by .php extension check), proceed to null byte injection. Expected output: Partial or full file contents if vulnerable, or an error/page not found.

### Step 2: Inject Null Byte to Bypass Filters

**Context**: If basic traversal fails due to extension checks (e.g., application appends .php and rejects non-PHP files), inject a null byte (%00 URL-encoded) to terminate the string early, tricking the include function into reading the target file.

Construct the payload as: traversal_path + target_file + %00 + (optional fake extension like .php to bypass some filters).

**Command** ([[commands/curl-basic-lfi-null-byte]]):

```bash
curl "http://$_TARGET_URL/index.php?page=../../../etc/passwd%00"
```

> This terminates the path at /etc/passwd, ignoring any appended .php. Expected output: Full contents of /etc/passwd, such as root:x:0:0:root... If successful, try other files like /etc/shadow (if readable) or application configs (e.g., ../../../../var/www/config.php%00).

### Step 3: Verify and Escalate Disclosure

**Context**: Confirm the exploit works by targeting multiple files and checking for sensitive data. This step validates success and explores for higher-value information.

If /etc/passwd works, test for web root files (e.g., index.php source) or logs. Use tools like Burp to iterate payloads quickly.

Adapt the command for different files:

```bash
curl "http://$_TARGET_URL/index.php?page=../../../var/www/html/index.php%00"
```

> Expected output: Source code of index.php if accessible. Success criteria: Readable file contents without application errors; look for credentials, API keys, or database configs. If blocked, try absolute paths or encode payloads further (%2e%2e%2f for ../).
