---
id: 3b504ce8-d9bb-4962-b2d8-c319984a4b51
name: Command-Injection-Filter-Bypass-with-PowerShell
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:57.395988+00:00'
updated_at: '2023-04-06T03:55:57.411955+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - '[[techniques/Command-and-Scripting-Interpreter/T1059.001|PowerShell]]'
sub_techniques: []
tags:
  - '[[tags/Bypass with $()]]'
  - '[[tags/Bypass with wildcards]]'
  - '[[tags/Command Injection]]'
  - '[[tags/Filter Bypasses]]'
commands: []
platforms:
  - Windows
tools: []
validated: true
---

# Command-Injection-Filter-Bypass-with-PowerShell

## Summary

This procedure demonstrates how to bypass command injection filters using PowerShell by leveraging wildcards and the $() subexpression operator to execute arbitrary commands, such as launching applications like Notepad or Calculator, even when certain characters, file paths, or executables are blocked by input sanitization rules.

## Description

Command injection vulnerabilities allow attackers to append and execute unintended system commands through unsanitized user inputs in web applications or scripts. Filters often block direct invocations of tools like 'powershell.exe' or specific paths, but this technique evades them by obfuscating paths with wildcards (* and ?) and using PowerShell's $() syntax to embed command execution within strings. This is particularly effective against web-based input fields or APIs that parse and execute system commands on Windows environments. The approach targets PowerShell as the interpreter, enabling further post-exploitation like file access or privilege escalation once initial execution succeeds.

## Requirements

1. A vulnerable application or input field that executes system commands without proper sanitization (e.g., a web form running `system()` or similar).
2. Target system running Windows with PowerShell installed (default on Windows 7+).
3. Attacker knowledge of blocked patterns (e.g., direct paths to notepad.exe or calc.exe).
4. Network access to submit inputs if targeting a remote web application.

## Defense

- Implement strict input validation and whitelisting to reject wildcards, special characters like $, (, ), and obfuscated paths.
- Use parameterized queries or safe APIs for command execution instead of direct string concatenation.
- Enable PowerShell logging (Module, Script Block, and Transcription) to monitor obfuscated invocations.
- Deploy web application firewalls (WAFs) tuned to detect injection patterns, including wildcard usage.
- Regularly audit application logs for anomalous command executions.

## Objectives

1. Bypass input filters blocking direct command execution to run arbitrary PowerShell commands.
2. Execute proof-of-concept payloads like launching GUI applications to confirm code execution.
3. Demonstrate potential for further exploitation, such as data exfiltration or lateral movement.

## Instructions

### Step 1: Identify Filter Patterns

**Context**: Analyze the application's input handling to understand blocked elements, such as direct paths to executables (e.g., C:\Windows\System32\notepad.exe) or the 'powershell' keyword. Test simple injections to map restrictions.

Submit test inputs like `notepad.exe` or `powershell -c calc` and observe rejection patterns. Use trial-and-error to confirm blocks on specific characters or strings.

### Step 2: Craft Obfuscated PowerShell Invocation for Notepad

**Context**: Use wildcards to match the path to notepad.exe (e.g., C:\*\*2\n??e*d.*?) where * matches multiple characters and ? matches single ones, bypassing path filters. The $() syntax embeds the execution within a PowerShell string.

**Code** ([[codes/PowerShell-Command-Injection-Bypass-with-Wildcards]]):

```powershell
powershell C:\*\*2\n??e*d.*? # notepad
```

> This command obfuscates the path to notepad.exe (typically C:\Windows\System32\notepad.exe) using wildcards: *\*2 matches 'Windows\', \n??e*d.*? matches 'notepad.exe'. Submit this as input to the vulnerable field. Expected behavior: Notepad launches on the target system if the filter is bypassed.

### Step 3: Craft Obfuscated PowerShell Invocation for Calculator

**Context**: Similarly, obfuscate the path to calc.exe (C:\*\*32\c*?c.e?e) to launch Calculator, confirming repeated bypass success and testing variations.

**Code** ([[codes/PowerShell-Command-Injection-Bypass-with-Wildcards]]):

```powershell
@^p^o^w^e^r^shell c:\*\*32\c*?c.e?e # calc
```

> This uses caret (^) escaping for 'powershell' to avoid keyword filters, followed by wildcards for the calc.exe path: *\*32 matches 'Windows\System32\', \c*?c.e?e matches 'calc.exe'. Submit to trigger Calculator execution. Expected behavior: Calculator window appears, validating the injection.
