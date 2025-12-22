---
id: 57981424-7fc1-491f-be52-b2270bfda865
name: map-sysinternals-smb
type: command
executor: cmd
data: 'net use Z: \\live.sysinternals.com\tools'
output: null
created_at: '2023-04-06T03:56:27.177044+00:00'
updated_at: '2023-04-10T20:37:14.787792+00:00'
platforms:
  - Windows
tags:
  - smb
  - mount
verified: true
validated: true
---

# map-sysinternals-smb

## Command

```cmd
net use Z: \\live.sysinternals.com\tools
```

## Description

Maps the public Sysinternals tools SMB share to drive Z: for direct access to executables like procdump.exe.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Z: | Drive letter to assign | Yes |
| \\live.sysinternals.com\tools | SMB share path | Yes |

## Examples

### Basic Usage

```cmd
net use Z: \\live.sysinternals.com\tools
```

Unmount later with 'net use Z: /delete'.

## Expected Output

```
The command completed successfully.
```

## Related

- [[procedures/windows-lsass-mini-dump-for-mimikatz]]
