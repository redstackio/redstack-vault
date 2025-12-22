---
data: cmd.exe /c whoami
tags:
  - execution
  - rce
type: command
output: Current user identity
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.160Z'
id: 6bee84e4-aa34-4428-9993-0a6adabb913c
verified: false
validated: true
submitted: true
---
# cmd-c-whoami

## Command

```cmd
cmd.exe /c whoami
```

## Description

Runs 'whoami' in non-interactive mode using cmd.exe /c, terminating after execution; ideal for webshell contexts to avoid hanging processes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /c | Carry out the command and terminate | Yes |
| whoami | The command to execute | Yes |

## Examples

### Basic Usage

```cmd
cmd.exe /c whoami
```

### Advanced Usage

```cmd
cmd.exe /c "whoami /all"
```

## Expected Output

User details including SID and privileges.

## Related

- [[Related Procedure: Execute-Commands-via-Uploaded-Webshell]]
