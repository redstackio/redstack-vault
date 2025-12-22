---
type: procedure
description: >-
  Execute arbitrary commands on a target system by injecting obfuscated inputs
  that bypass filters blocking blacklisted words using single quotes.
verified: true
submitted: false
created_at: '2023-04-06T03:55:57.257560+00:00'
updated_at: '2023-04-06T03:55:57.271520+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques:
  - '[[sub-techniques/PowerShell|T1059.001 - PowerShell]]'
tags:
  - '[[tags/Bypass Blacklisted words]]'
  - '[[tags/Bypass with single quote]]'
  - '[[tags/Command Injection]]'
  - '[[tags/Filter Bypasses]]'
commands:
  - '[[commands/powershell-execute-obfuscated-whoami]]'
platforms:
  - Windows
tools: []
validated: true
---

# Command-Injection-with-Filter-Bypass-using-Single-Quote

## Summary

Command injection with filter bypass using single quotes allows an attacker to execute arbitrary commands on a target system by injecting malicious inputs into a command-line interface. This technique obfuscates blacklisted commands (e.g., 'whoami') by inserting single quotes between characters, such as 'w'h'o'am'i', to evade filters that block direct execution of sensitive commands. It is commonly used in web applications or scripts that dynamically execute user input via PowerShell's Invoke-Expression, enabling unauthorized access, privilege escalation, or data exfiltration.

## Description

Command injection vulnerabilities occur when an application passes unsanitized user input to system shell functions like Invoke-Expression in PowerShell. Filters may blacklist common reconnaissance commands like 'whoami' to prevent detection, but attackers can bypass these by obfuscating the input with single quotes, which escape the filter's pattern matching while preserving executability. This procedure targets Windows environments where PowerShell is the execution context, assuming the vulnerable application concatenates user input directly into a PowerShell command. Success results in arbitrary code execution, potentially leading to shell access or further compromise. Use this in controlled red team exercises or penetration tests to demonstrate input validation weaknesses.

## Requirements

1. Access to a web application or interface with a command injection vulnerability that uses PowerShell for execution (e.g., via a parameter in a POST request).
2. Knowledge of the blacklisted words or patterns in the filter (e.g., direct 'whoami' is blocked).
3. A proxy tool like Burp Suite for intercepting and modifying requests (optional but recommended for testing).
4. Target system running Windows with PowerShell enabled.

## Defense

Defensive measures and detection strategies:

- Sanitize user inputs by removing or encoding special characters like single quotes before passing to shell functions.
- Implement a whitelist approach instead of a blacklist for input validation, allowing only expected commands.
- Monitor system logs for suspicious activities, such as unusual PowerShell invocations or obfuscated command patterns.
- Enable PowerShell constrained language mode and script block logging to detect anomalous executions.
- Use web application firewalls (WAFs) to inspect and block injection attempts based on payload signatures.

## Objectives

1. Execute arbitrary commands on the target system despite active filters.
2. Bypass the filter that blocks blacklisted words using single quote obfuscation.
3. Gain unauthorized access, escalate privileges, or exfiltrate sensitive data via the injected command.

## Instructions

### Step 1: Identify the Vulnerable Input Point

**Context**: Locate the application endpoint or form field where user input is executed via PowerShell (e.g., a search parameter that runs system commands). Test for injection by appending simple payloads like '; whoami' and observing if it executes without the filter blocking.

**Why**: Confirms the vulnerability exists and identifies the execution context (PowerShell).

If the direct command is blocked, proceed to obfuscation.

**Expected Output**: Error messages or partial execution indicating filter presence, or successful output if unfiltered.

### Step 2: Obfuscate the Command Using Single Quotes

**Context**: Use the obfuscated command string from [[codes/PowerShell-Obfuscated-Whoami-Single-Quote-Bypass]] to bypass the filter. This inserts single quotes between letters, evading keyword-based blacklists while PowerShell interprets it as 'whoami'.

**Why**: Single quotes break pattern matching in simplistic filters without altering the command's semantics in PowerShell.

Reference the code snippet and prepare it for injection.

**Expected Output**: The obfuscated string ready for use, e.g., w'h'o'am'i.

### Step 3: Inject and Execute the Obfuscated Command

**Context**: Inject the obfuscated payload into the vulnerable parameter. For example, in a URL or POST body: ?cmd=w'h'o'am'i or using Invoke-Expression in the backend.

**Command** ([[commands/powershell-execute-obfuscated-whoami]]):
```powershell
Invoke-Expression "w'h'o'am'i"
```

> This command executes the obfuscated string via PowerShell's Invoke-Expression, running 'whoami' despite filters. Submit it through the vulnerable input (e.g., via curl or browser). If the app wraps input in Invoke-Expression, the payload alone suffices.

**Why**: Directly triggers command execution on the target, verifying bypass success.

**Expected Output**: Output of the 'whoami' command, such as 'nt authority\iusr' or the current user context, indicating successful injection.

**Success Indicators**:
- Command output appears in the application response or logs.
- No filter rejection errors (e.g., 'blacklisted word detected').
- Ability to chain with other commands (e.g., replace with 'net user' for escalation testing).
