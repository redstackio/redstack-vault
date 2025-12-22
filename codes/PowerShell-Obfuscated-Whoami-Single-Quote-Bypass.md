---
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:55:57.255819+00:00'
updated_at: '2023-04-06T03:55:57.259251+00:00'
platforms:
  - Windows
tags:
  - obfuscation
  - bypass
  - command-injection
validated: true
---

# PowerShell-Obfuscated-Whoami-Single-Quote-Bypass

## Code

```powershell
w'h'o'am'i
```

## Description

This code snippet is an obfuscated string representing the 'whoami' command, achieved by inserting single quotes between each character. It bypasses simplistic filters that blacklist direct command names like 'whoami' while remaining executable in PowerShell contexts, such as when passed to Invoke-Expression. Use this in command injection scenarios to perform reconnaissance without triggering keyword-based defenses.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is a static obfuscated string with no variables. | N/A |

## Usage

Inject this string into a vulnerable input field where the backend uses PowerShell to evaluate user input (e.g., via a web form parameter: cmd=w'h'o'am'i). Pair it with a command like Invoke-Expression for execution. Ideal for initial foothold in red team operations targeting Windows web apps with poor input sanitization.

## Detection

- PowerShell execution logs showing strings with interspersed single quotes.
- Anomalous 'whoami' outputs in application logs or responses.
- WAF alerts on unusual quoting patterns in request payloads.
- Enable Module Logging and Script Block Logging in PowerShell to capture obfuscated invocations.

## Related

- [[procedures/Command-Injection-with-Filter-Bypass-using-Single-Quote]]
- [[powershell-execute-obfuscated-whoami]]
