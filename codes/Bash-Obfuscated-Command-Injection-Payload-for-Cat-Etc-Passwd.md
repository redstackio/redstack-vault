---
type: code
language: bash
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tags:
  - command-injection
  - filter-bypass
  - payload
platforms:
  - Linux
validated: true
---

# Bash-Obfuscated-Command-Injection-Payload-for-Cat-Etc-Passwd

## Code

```bash
/???/??t /???/p??s??

test=/ehhh/hmtc/pahhh/hmsswd
cat ${test//hhh\/hm/}
cat ${test//hh??hm/}
```

## Description

This bash code snippet provides an obfuscated payload for command injection bypass. It starts with a wildcard-obfuscated direct attempt to 'cat /etc/passwd' (/???/??t for /bin/cat, /???/p??s?? for /etc/passwd). Then, it assigns an obfuscated path to the 'test' variable and uses two parameter expansions to replace patterns like 'hhh/hm' and 'hh??hm' with '/', reconstructing and executing 'cat /etc/passwd'. This evades filters scanning for direct paths or keywords by delaying reconstruction until runtime.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| test | Obfuscated command string; customize for other commands (e.g., replace with mangled 'whoami') | /ehhh/hmtc/pahhh/hmsswd |

## Usage

Inject this multi-line payload into a command injection vulnerability using command separators like ';' or newlines (if allowed). For example, in a web parameter: '; [paste code here]'. Set up a listener if chaining to network commands. Used in red team engagements to test filter efficacy or during pentests to access sensitive data.

## Detection

- Application logs showing bash expansions (${...}) or unusual variable assignments.
- File access audits detecting 'cat' on /etc/passwd from web processes.
- WAF alerts on repeated characters (e.g., 'hhh') or wildcard patterns in inputs.
- Shell history or process monitoring revealing reconstructed commands.

## Related

- [[procedures/Command-Injection-Filter-Bypass-Using-Variable-Expansion]]
