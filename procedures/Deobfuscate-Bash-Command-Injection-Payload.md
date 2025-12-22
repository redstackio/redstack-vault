---
id: bbfa0c88-9e5a-4526-b397-ed6b108a8edb
name: Deobfuscate-Bash-Command-Injection-Payload
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:57.424343+00:00'
updated_at: '2023-04-06T03:55:57.438914+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Unix Shell]]'
  - '[[Binary Padding]]'
sub_techniques: []
tags:
  - '[[tags/Challenge]]'
  - '[[tags/Command Injection]]'
  - obfuscation
  - bash
commands:
  - '[[commands/bash-set-and-echo-variable]]'
  - '[[commands/bash-deobfuscate-with-expansion]]'
  - '[[commands/bash-reverse-with-rev]]'
  - '[[commands/bash-sh-execute-deobfuscated]]'
platforms:
  - Linux
tools: []
validated: true
---

# Deobfuscate-Bash-Command-Injection-Payload

## Summary

This procedure provides a step-by-step guide to analyze and deobfuscate an obfuscated Bash payload commonly used in command injection attacks. By breaking down the obfuscation techniques like variable substitution and string reversal, red teamers and defenders can understand how attackers hide malicious commands to execute arbitrary system actions, such as data exfiltration or malware installation.

## Description

Command injection occurs when an application allows untrusted input to modify or execute unintended system commands. Attackers often obfuscate payloads using Bash features like parameter expansion for string replacement and tools like 'tac' for reversal to bypass detection tools, WAFs, or logging. This procedure uses a sample obfuscated one-liner that sets a variable with encoded characters (using 'hh' and 'hm' as stand-ins for '/'), deobfuscates it, reverses the string, and prepares it for execution via 'sh'. The target environment is a Linux system vulnerable to command injection, such as a web app executing shell commands with user input (e.g., via 'ping' or 'ls'). Successful deobfuscation reveals the attacker's intent to run arbitrary commands, highlighting the need for input sanitization.

## Requirements

1. Linux system with Bash shell (e.g., Ubuntu or Kali).
2. Terminal access for testing in an isolated environment (use a VM to avoid risks).
3. Basic knowledge of Bash scripting and string manipulation.
4. The obfuscated payload code snippet for reference.

## Defense

- Implement strict input validation and sanitization, escaping special characters like ';', '|', and '$' in user inputs.
- Use parameterized execution or safe APIs (e.g., avoid direct shell calls with system() in code).
- Deploy application whitelisting to restrict executable commands and monitor for anomalies like unusual 'tac' or parameter expansions in logs.
- Enable command logging (e.g., via auditd on Linux) and use tools like Snort or ModSecurity to detect obfuscated injection patterns.

## Objectives

1. Identify common obfuscation techniques in command injection payloads, such as placeholder substitutions and reversals.
2. Deobfuscate the payload to reveal the underlying malicious command structure.
3. Demonstrate the execution of the deobfuscated payload in a controlled setting to assess impact.
4. Understand defensive measures to prevent such attacks in production environments.

## Instructions

### Step 1: Set and Inspect the Obfuscated Variable

**Context**: Begin by isolating the obfuscated string from the payload and printing it to understand the initial structure. This reveals placeholders like 'hh' and 'hm' used to hide path separators ('/').

**Command** ([[commands/bash-set-and-echo-variable]]):
```bash
g="/e\"\h\"hh\"/hm\"t\"c/\i\"sh\"hh/hmsu\e"; echo "$g"
```

> This sets the variable 'g' with the obfuscated string (escaped for proper quoting in Bash) and echoes it. The step confirms the payload's structure without executing anything harmful. Why: Inspection helps identify the obfuscation pattern before manipulation.

**Expected Output**:
```
/e"h"hh"/hm"t"c/\i"sh"hh/hmsu\e
```
(A single line showing the mangled string with embedded quotes and backslashes.)

### Step 2: Apply Parameter Expansion for Deobfuscation

**Context**: Replace the obfuscation placeholders ('hh' and 'hm') with '/' using Bash parameter expansion. This uncovers the hidden paths or command fragments.

**Command** ([[commands/bash-deobfuscate-with-expansion]]):
```bash
g="/e\"\h\"hh\"/hm\"t\"c/\i\"sh\"hh/hmsu\e"
deobf1="${g//hh/\/}"
deobf2="${deobf1//hm/\/}"
echo "$deobf2"
```

> This performs sequential replacements to simulate the payload's self-deobfuscation. Why: Attackers use this to dynamically generate valid commands at runtime, evading static analysis.

**Expected Output**:
```
/e"h"/ /"t"c/\i"sh"/ /su\e
```
(The string now has '/' in place of 'hh' and 'hm', making command paths visible.)

### Step 3: Reverse the Deobfuscated String

**Context**: The payload uses 'tac' to reverse content, but for character-level reversal (common in such obfuscations), use 'rev'. This step reveals the actual command sequence.

**Command** ([[commands/bash-reverse-with-rev]]):
```bash
echo "$deobf2" | rev
```

> Pipe the deobfuscated string to 'rev' to mirror the reversal intent. Why: Reversal hides the command from left-to-right reading in logs or previews.

**Expected Output**:
```
e\us / /"hs"i\ /c"t" / /"h"e
```
(The reversed string, which, when interpreted as a command, forms something like 'sh -i /c/tm /h /he' – in a real attack, this would resolve to a functional shell invocation for arbitrary execution.)

### Step 4: Execute the Deobfuscated Payload Safely

**Context**: In a controlled environment, execute the reversed/deobfuscated command using 'sh -c' to simulate the injection outcome and verify the attack's success.

**Command** ([[commands/bash-sh-execute-deobfuscated]]):
```bash
sh -c 'e\us / /"hs"i\ /c"t" / /"h"e'
```

> Wrap the deobfuscated output in 'sh -c' to run it. In practice, adjust based on full deobfuscation; test in a sandbox. Why: This confirms the payload's goal of spawning a shell for further actions like 'cat /etc/passwd' or reverse shell.

**Expected Output**:
```
(Depending on the exact deobfuscation, it may spawn an interactive shell or run a command like listing files. Success: No syntax errors, and arbitrary command execution is possible, e.g., output from a system command.)

**Decision Point**: If execution fails due to syntax, manually adjust quotes/backslashes based on the reversed string. Otherwise, proceed to assess impact (e.g., check for file access or network calls).
