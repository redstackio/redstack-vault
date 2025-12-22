---
type: procedure
tactics:
  - '[[Execution]]'
techniques:
  - '[[Command-Line Interface]]'
sub_techniques:
  - '[[Windows Command Shell]]'
tags:
  - bypass-blacklisted-words
  - bypass-with-double-quote
  - command-injection
  - filter-bypasses
commands: []
tools: []
platforms:
  - Windows
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Command-Injection-with-Double-Quote-Bypass

## Summary

This procedure demonstrates how to perform command injection on a Windows system by bypassing input filters that block blacklisted words, such as command names, using double quotes to encapsulate parts of the command. It allows execution of arbitrary commands like 'whoami' by fragmenting the input to evade simple keyword-based filtering, leading to potential system compromise.

## Description

Command injection vulnerabilities occur when user input is passed unsanitized to system shell commands, enabling attackers to append or modify commands. In this case, the target application filters out blacklisted terms (e.g., 'whoami') but fails to handle fragmented inputs wrapped in double quotes. By inserting a payload like `w"h"o"am"i`, the filter sees individual quoted segments as harmless, but the shell interprets it as the full command 'whoami'. This technique targets Windows environments using Command Prompt or PowerShell execution. It is effective against web applications, APIs, or services that invoke system commands based on user input, potentially allowing reconnaissance, privilege escalation, or further exploitation. Prerequisites include identifying a vulnerable input point, such as a search field or ping utility in a web app.

## Requirements

1. Access to a vulnerable application or service that executes user input via Windows Command Shell or PowerShell without proper sanitization.
2. Knowledge of blacklisted words in the filter (e.g., common commands like 'whoami', 'net user').
3. Network access to the target if it's a remote web application.
4. Basic understanding of Windows command syntax and shell interpretation.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization, rejecting any input containing shell metacharacters or quotes.
- Use parameterized execution or whitelisting for allowed commands instead of direct shell invocation.
- Deploy a Web Application Firewall (WAF) configured to detect fragmented command patterns and quote-based obfuscation.
- Enable command logging on Windows systems (e.g., via Sysmon or PowerShell transcription) to monitor for anomalous executions.
- Conduct regular code reviews and use tools like static analysis scanners to identify injection points.

## Objectives

1. Bypass keyword-based filters to inject and execute arbitrary commands on the target system.
2. Perform initial reconnaissance, such as identifying the current user context with 'whoami'.
3. Establish a foundation for further post-exploitation activities like data exfiltration or persistence.

## Instructions

### Step 1: Identify the Vulnerable Input Point

**Context**: Locate an input field in the target application that passes data directly to a Windows shell command, such as a 'ping' test or system diagnostic feature. Test for injection by appending simple payloads like '; whoami' to see if it executes.

**Why**: This confirms the vulnerability exists and identifies the filter's behavior, such as blocking full commands but allowing partial inputs.

**Expected Output**: Error messages or partial execution indicating shell access, but blocked on blacklisted terms.

### Step 2: Craft the Bypassed Payload

**Context**: Fragment the blacklisted command using double quotes to split it into non-blacklisted segments. For 'whoami', create `w"h"o"am"i` so the filter processes each quoted letter separately.

**Why**: Double quotes in Windows shells are interpreted literally but allow the command to reassemble during execution, evading regex-based filters that match whole words.

Use the following code snippet for the payload: [[codes/PowerShell-Whoami-Double-Quote-Bypass]]

**Expected Output**: The payload string ready for injection, e.g., `w"h"o"am"i`.

### Step 3: Inject and Execute the Payload

**Context**: Submit the crafted payload into the vulnerable input field, often concatenated with existing commands (e.g., in a ping input: `8.8.8.8; w"h"o"am"i`). If the application uses PowerShell, ensure the input is evaluated via Invoke-Expression or similar.

**Why**: This triggers the shell to execute the reassembled command, bypassing the filter and running the intended reconnaissance.

For direct testing in a PowerShell console (to validate the bypass logic before injection):

```powershell
Invoke-Expression 'w"h"o"am"i'
```

If the target is a web app, use a tool like Burp Suite to send the POST/GET request with the payload in the parameter.

**Expected Output**: Output from the command, such as the current username (e.g., 'domain\user'), confirming successful execution.

### Step 4: Verify and Escalate

**Context**: Check the response for command output. If successful, chain with additional bypassed commands (e.g., for 'net user': `n"e"t user`).

**Why**: Validates the bypass works and allows progression to more impactful actions like listing users or escalating privileges.

**Decision Point**: If the output shows a low-privilege user, proceed to privilege escalation techniques; if errors occur, adjust quote escaping (e.g., try single quotes or additional fragmentation).

**Expected Output**: Successful command results without filter blocks; errors indicate need for payload refinement.

**Success Indicators**:
- Command output appears in the application response or logs.
- No filter rejection messages for the fragmented payload.
- Ability to execute multiple bypassed commands sequentially.
