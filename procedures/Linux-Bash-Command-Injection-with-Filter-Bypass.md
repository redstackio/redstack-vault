---
id: 4c55e92b-2208-4e03-a053-17c1d72d15f2
name: Linux-Bash-Command-Injection-with-Filter-Bypass
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:57.221624+00:00'
updated_at: '2023-04-06T03:55:57.244317+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques:
  - '[[sub-techniques/Unix-Shell|T1059.004 - Unix Shell]]'
tags:
  - '[[tags/Bypass-characters-filter]]'
  - '[[tags/Command-Injection]]'
  - '[[tags/Filter-Bypasses]]'
commands:
  - '[[commands/echo-home-first-character]]'
  - '[[commands/cat-etc-passwd-using-home-substring]]'
  - '[[commands/echo-dot-pipe-tr-translate]]'
  - '[[commands/tr-translate-heredoc-dot]]'
  - '[[commands/cat-etc-passwd-using-tr-command-substitution]]'
platforms:
  - Linux
tools: []
validated: true
---

# Linux-Bash-Command-Injection-with-Filter-Bypass

## Summary

This procedure demonstrates how to perform command injection in a Linux Bash environment by bypassing character filters that block common delimiters like slashes (/) and quotes. By using Bash parameter expansion and the tr command for character translation, an attacker can construct paths and execute arbitrary commands, such as reading sensitive files like /etc/passwd, without directly using filtered characters.

## Description

Command injection vulnerabilities occur when user input is passed unsanitized to system commands, allowing attackers to append or modify commands. In scenarios where filters block characters like /, ', ", or `, attackers can bypass them using Bash features: ${HOME:0:1} expands to the first character of $HOME (typically /), and tr can translate filtered characters to equivalents (e.g., mapping ! to " and - to 1 to produce / from .). This technique is useful in web applications or scripts that execute Bash commands with restricted input, enabling unauthorized file access or code execution. The target environment is a Linux system with Bash shell access, often via a vulnerable CGI script or misconfigured application. Expected outcomes include successful execution of injected commands and retrieval of system information.

## Requirements

1. Access to a Linux system with Bash shell (local or remote via vulnerable application).
2. The target application or script must execute user input as Bash commands without proper sanitization.
3. Knowledge of the filter rules (e.g., blocking / and quotes) to select appropriate bypass methods.
4. Basic Bash proficiency to construct and test injections.

## Defense

- Implement strict input validation and sanitization, whitelisting only allowed characters and rejecting suspicious patterns.
- Use parameterized execution or APIs that separate code from data, such as running commands via safe wrappers.
- Employ web application firewalls (WAFs) to detect injection patterns, including obfuscated variants.
- Run applications in least-privilege containers or with restricted shell environments (e.g., using rbash).
- Enable logging of command executions and monitor for anomalous file accesses like /etc/passwd.

## Objectives

1. Bypass character filters to construct forbidden paths and commands.
2. Execute arbitrary system commands to read sensitive files.
3. Demonstrate escalation from limited input to full command execution for unauthorized access.

## Instructions

### Step 1: Extract Root Directory Character Using Parameter Expansion

**Context**: Start by using Bash's parameter expansion on the $HOME variable to obtain the root directory slash (/) without directly typing it, assuming $HOME begins with /. This bypasses filters blocking literal / characters.

**Command** ([[commands/echo-home-first-character]]):
```bash
echo ${HOME:0:1}
```

> This command outputs the first character of $HOME, which is /. Verify this step succeeds before proceeding to path construction.

### Step 2: Read /etc/passwd Using Parameter Expansion

**Context**: Build the path to /etc/passwd by concatenating the extracted / with 'etc' and another /, then use cat to display the file contents. This tests the injection in a simple path without additional translations.

**Command** ([[commands/cat-etc-passwd-using-home-substring]]):
```bash
cat ${HOME:0:1}etc${HOME:0:1}passwd
```

> Successful output shows user entries from /etc/passwd, confirming path bypass works. If filtered, proceed to translation methods.

### Step 3: Translate Dot to Slash Using tr Command

**Context**: Use the tr command to map characters to produce / from a benign input like ., bypassing filters on / by translating ! to " and - to 1 (since . in ASCII context can be remapped). This provides an alternative to parameter expansion.

**Command** ([[commands/echo-dot-pipe-tr-translate]]):
```bash
echo . | tr '!-0' '"-1'
```

> The output should be /, validating the translation. This step isolates the tr bypass for reuse.

### Step 4: Alternative Translation with Heredoc Input

**Context**: Use tr with here-string input (<<<) for the same translation, offering a variation if pipe is filtered. This confirms the bypass method's flexibility.

**Command** ([[commands/tr-translate-heredoc-dot]]):
```bash
tr '!-0' '"-1' <<< .
```

> Output is /, similar to Step 3. Use this if the pipe version is blocked.

### Step 5: Read /etc/passwd Using tr Translation and Command Substitution

**Context**: Combine tr translations with command substitution $( ) to build the full path /etc/passwd dynamically, executing cat to read the file. This represents a full injection payload in a filtered environment.

**Command** ([[commands/cat-etc-passwd-using-tr-command-substitution]]):
```bash
cat $(echo . | tr '!-0' '"-1')etc$(echo . | tr '!-0' '"-1')passwd
```

> Output displays /etc/passwd contents, achieving the injection objective. In a real attack, replace cat with other commands like whoami or nc for reverse shells.
