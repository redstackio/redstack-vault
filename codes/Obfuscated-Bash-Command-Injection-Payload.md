---
id: 336e75a7-1dc7-40b5-954d-f1874025416c
name: Obfuscated-Bash-Command-Injection-Payload
type: code
language: bash
verified: true
created_at: '2023-04-06T03:55:57.422096+00:00'
updated_at: '2023-04-06T03:55:57.426004+00:00'
platforms:
  - Linux
tags:
  - command-injection
  - obfuscation
  - payload
validated: true
---

# Obfuscated-Bash-Command-Injection-Payload

## Code

```bash
g="/e"\h"hh"/hm"t"c/\i"sh"hh/hmsu\e;tac$@<${g//hh??hm/}
```

## Description

This obfuscated Bash one-liner is a payload for command injection attacks. It sets a variable 'g' with a mangled string using placeholders and quotes to hide the structure, then uses parameter expansion to modify it (replacing patterns like 'hh??hm'), and pipes to 'tac' for reversal before potential execution. The intent is to dynamically generate and run arbitrary commands (e.g., spawning a shell) while evading pattern-based detection in logs or filters.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `$@` | Positional parameters passed to 'tac' for options | (e.g., -s for separator) |

(No user-substitutable variables like IP/port; self-contained for injection.)

## Usage

Inject this payload into vulnerable inputs that execute shell commands, such as a web form running 'ping $input' or 'ls $input'. For example: `ping `payload``. In a red team scenario, deliver via XSS or direct input to gain RCE. Always test in isolated environments to avoid unintended execution.

## Detection

- Monitor shell logs for suspicious variable assignments, parameter expansions (${...//...}), or 'tac' invocations in non-standard contexts.
- Use regex in SIEM tools to flag strings with repeated placeholders like 'hh'/'hm' or unusual quote/escape patterns.
- Behavioral detection: Unusual processes spawned from web apps (e.g., 'sh' from Apache).
- Tools like OSSEC or Falco can alert on command injection signatures.

## Related

- [[procedures/Deobfuscate-Bash-Command-Injection-Payload]]
