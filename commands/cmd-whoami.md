---
data: cmd.exe /c whoami
tags:
  - discovery
  - windows
type: command
executor: cmd
platforms:
  - Windows
id: 51236e48-3359-4340-a798-f72d591848ae
created_at: '2025-12-13T09:00:33.846Z'
updated_at: '2025-12-13T09:00:33.846Z'
verified: false
validated: true
submitted: true
---
# cmd-whoami

## Command

```bash
cmd.exe /c whoami
```

## Description

Executes the whoami command to retrieve the current user's identity on a Windows system.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/c` | Carries out the command specified by string and then terminates | Yes |

## Examples

### Basic Usage

```bash
cmd.exe /c whoami
```

## Expected Output

The username of the current server process.

## Related

- [[procedures/Achieve-RCE-via-Arbitrary-ASP-File-Upload]]
