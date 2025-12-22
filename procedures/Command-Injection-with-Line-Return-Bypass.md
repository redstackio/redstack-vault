---
id: 5bd56b39-1cc4-49de-88a6-83f6adf39caf
name: Command-Injection-with-Line-Return-Bypass
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:57.134465+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques: []
tags:
  - '[[tags/Bypass-with-Line-Return]]'
  - '[[tags/Command-Injection]]'
  - '[[tags/Filter-Bypasses]]'
commands:
  - '[[commands/cat-view-etc-passwd]]'
platforms:
  - Linux
  - Web
tools: []
validated: true
---

# Command-Injection-with-Line-Return-Bypass

## Summary

This procedure demonstrates how to perform command injection attacks by bypassing input validation filters using URL-encoded line return characters (%0A). It allows attackers to execute arbitrary shell commands on a vulnerable web application or API endpoint, such as reading sensitive files or creating files on the target system, typically in a Linux environment.

## Description

Command injection vulnerabilities occur when user input is passed directly to system shell commands without proper sanitization. Filters may block common injection payloads like semicolons (;) or pipes (|), but inserting a line return (%0A in URL encoding) can split the input, allowing the original command to execute followed by the injected one. This technique is effective against web applications that decode URL-encoded input before processing. The target is usually a Linux-based server where commands like 'cat' can access files. Success enables remote code execution (RCE), data exfiltration, or persistence. Prerequisites include identifying a vulnerable input field (e.g., via fuzzing with tools like Burp Suite) and understanding the backend OS.

## Requirements

1. Access to a vulnerable web application endpoint that accepts user input and executes it in a shell (e.g., ping or whoami utilities).
2. Knowledge of the target system's OS (Linux assumed here) and basic shell commands.
3. A proxy tool like Burp Suite for intercepting and modifying HTTP requests.
4. URL encoding capability to insert %0A for line returns.

## Defense

- Implement strict input validation and sanitization, whitelisting allowed characters and rejecting any control characters like %0A.
- Use parameterized APIs or safe execution wrappers (e.g., Python's subprocess with shell=False) to avoid direct shell invocation.
- Employ web application firewalls (WAFs) to detect and block encoded injection patterns.
- Limit process privileges and monitor for anomalous file access or command executions via logging (e.g., auditd on Linux).

## Objectives

1. Bypass input filters to inject and execute arbitrary shell commands.
2. Read sensitive files like /etc/passwd to enumerate users.
3. Demonstrate persistence by creating and verifying files on the target system.
4. Achieve remote code execution leading to data exfiltration or further compromise.

## Instructions

### Step 1: Inject Payload to View Password File

**Context**: Identify a vulnerable input field (e.g., a search or ping form) and craft a payload that appends a line return after a benign input, followed by the command to read /etc/passwd. This splits the execution, bypassing filters that scan for direct injections.

**Code** ([[codes/url-encoded-line-return-bypass-to-cat-passwd]]):

```text
something%0Acat%20/etc/passwd
```

> Submit this URL-encoded payload via POST or GET to the vulnerable endpoint. The %0A acts as a newline, causing the server to execute 'something' on one line and 'cat /etc/passwd' on the next. Use [[commands/cat-view-etc-passwd]] as the base command being injected.

**Expected Output**: The response includes the contents of /etc/passwd, listing user accounts (e.g., root:x:0:0:root:/root:/bin/bash).

### Step 2: Inject Payload to Create and Read a Temporary File

**Context**: Extend the bypass to perform multi-command operations, such as creating a file with here-document syntax and then reading it. This verifies write access and demonstrates more complex injections. Decision point: If the first payload succeeds, proceed; otherwise, try alternative encodings like %0D%0A.

**Code** ([[codes/url-encoded-line-return-bypass-to-create-temp-file]]):

```text
;cat>/tmp/hi<<EOF%0ahello%0aEOF
;cat</tmp/hi
hello
```

> Intercept the request with a proxy, replace the input value with this payload, and submit. The semicolons chain commands, with %0A enabling the here-document. If write fails (permission denied), target a writable directory like /tmp.

**Expected Output**: Confirmation of file creation (no error), followed by the file contents 'hello' in the response.

## Expected Output

Successful injections return command outputs in the HTTP response body, such as file contents or execution results, without server errors.
