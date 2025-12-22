---
type: code
language: bash
verified: true
tags:
  - chaining
  - command-injection
  - payload
platforms:
  - Linux
validated: true
---

# bash-multi-line-command-chain

## Code

```bash
original_cmd_by_server
ls
```

## Description

This Bash code snippet shows multi-line command chaining by separating commands with newlines, allowing sequential execution in environments that preserve line breaks in injected input. It enables longer payloads for complex operations in command injection attacks.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| original_cmd_by_server | The original server-executed command | ping 127.0.0.1 |
| ls | Injected command for listing or other actions | whoami |

## Usage

Use in injection points that support multi-line input, such as textarea fields in web apps. Execute the original command first, then chain additional steps like file enumeration or data exfiltration. Ideal for red team exercises simulating persistent access via chained recon and persistence commands.

## Detection

- Input validation logs showing multi-line submissions with shell metacharacters.
- Shell history or audit logs (e.g., bash_history) revealing sequential anomalous commands.
- Behavioral analytics flagging unusual command sequences in process trees.

## Related

- [[procedures/Command-Injection-Chaining-Commands]]
