---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques:
  - '[[sub-techniques/Unix-Shell|T1059.004 - Unix Shell]]'
tags:
  - '[[tags/Bypass with backslash newline]]'
  - '[[tags/Command Injection]]'
  - '[[tags/Filter Bypasses]]'
commands:
  - '[[commands/display-contents-of-etc-passwd]]'
platforms:
  - Linux
  - Web
tools: []
validated: true
---

# Command-Injection-Filter-Bypass-with-Backslash-Newline

## Summary

This procedure demonstrates how to bypass input filters in a vulnerable web application to achieve command injection on a Linux target by using backslash-newline sequences to obfuscate malicious commands. It allows execution of arbitrary system commands, such as reading sensitive files like /etc/passwd, by splitting the payload across lines to evade keyword-based detection.

## Description

Command injection vulnerabilities occur when user input is passed unsanitized to system shells, enabling attackers to append or modify commands. Filters often block common commands like 'cat' or paths like '/etc/passwd' by scanning for exact strings. The backslash-newline bypass exploits line continuation in shells (e.g., bash), where a backslash (\) followed by a newline allows splitting the command without altering its execution. This technique is useful in web applications with partial WAF protections or custom input validation. The target environment is typically a Linux-based web server with a vulnerable CGI, PHP, or similar script. Success grants file read access, potentially leading to further enumeration or privilege escalation. Note: This maps to Unix shell execution, not Windows, despite original mapping.

## Requirements

1. Access to a web application with a command injection vulnerability (e.g., via a parameter that executes system commands like ping or whoami).
2. Knowledge of the target's shell (assumed bash or compatible Unix shell).
3. Tools for testing injections, such as a browser or [[tools/Burp-Suite]] for intercepting requests.
4. Basic understanding of URL encoding for web delivery.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization, avoiding direct shell execution (use APIs like subprocess with lists in Python).
- Deploy WAF rules to detect anomalous payloads, including backslash-newline patterns and common command fragments.
- Enable application logging for all executed commands and monitor for unexpected file accesses (e.g., /etc/passwd via auditd or SELinux).
- Use least-privilege principles for web server processes to limit impact of injected commands.

## Objectives

1. Bypass input filters designed to block command injection payloads.
2. Execute arbitrary commands on the target Linux system to read sensitive files.
3. Demonstrate URL-encoded variations for web-based delivery.
4. Verify successful injection through expected file contents in the response.

## Instructions

### Step 1: Craft and Inject Backslash-Newline Payload

**Context**: Identify the injection point (e.g., a 'host' parameter in a ping form). Split the target command 'cat /etc/passwd' using backslash-newline to evade filters scanning for full strings. Submit this as input to the vulnerable endpoint.

**Code** ([[codes/backslash-newline-bypass-payload-for-cat-etc-passwd]]):

```bash
cat /et\
c/pa\
sswd
```

> This payload, when injected, is interpreted by the shell as 'cat /etc/passwd' due to line continuation. Submit it via POST/GET to the vulnerable parameter. The backslash escapes the newline, allowing multi-line input in single fields.

**Expected Output**: The application response includes the contents of /etc/passwd, such as user entries starting with 'root:x:0:0:root:/root:/usr/bin/zsh'.

### Step 2: Verify Execution with Basic Command

**Context**: Confirm the injection works by executing a simple command like 'cat /etc/passwd' directly (if unfiltered) or as a baseline. Use this to validate the environment before applying bypasses.

**Command** ([[commands/display-contents-of-etc-passwd]]):

```bash
cat /etc/passwd
```

> If the basic command succeeds without bypass, the vulnerability is unfiltered. Otherwise, proceed to obfuscated versions. This step ensures the target path exists and the shell has read access.

**Expected Output**: List of user accounts, e.g., 'root:x:0:0:root:/root:/usr/bin/zsh\ndaemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin'.

### Step 3: Apply URL-Encoded Backslash-Newline for Web Delivery

**Context**: For HTTP parameters, encode the payload to handle spaces, slashes, and newlines. This prevents URL parsing issues while preserving the shell interpretation.

**Code** ([[codes/url-encoded-backslash-newline-bypass-payload-for-cat-etc-passwd]]):

```bash
cat%20/et%5C%0Ac/pa%5C%0Asswd
```

> URL encoding translates ' ' to %20, '/' to %2F (if needed), '\' to %5C, and newline to %0A. Inject this encoded string into the web form or request. The server decodes it before shell execution, triggering the bypass.

**Expected Output**: Same as Step 1, with /etc/passwd contents reflected in the HTTP response body.
