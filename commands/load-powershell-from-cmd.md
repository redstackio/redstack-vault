---
id: c5f83279-df55-4b78-93b1-46013160943e
name: load-powershell-from-cmd
type: command
executor: command_prompt
data: powershell
output: null
created_at: '2023-01-12T04:46:22.563476+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - powershell
  - execution
verified: true
validated: true
---

# load-powershell-from-cmd

## Command

```command_prompt
powershell
```

## Description

This command launches a new interactive PowerShell session from a Windows Command Prompt. When used after loading Invisi-Shell, it inherits the bypassed environment for stealthy script execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Launches default PowerShell; optional flags like -ExecutionPolicy Bypass can be added but are not required here. | N/A |

## Examples

### Basic Usage

```command_prompt
powershell
```

### With Policy Bypass

```command_prompt
powershell -ExecutionPolicy Bypass
```

## Expected Output

```
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Users\User> 
```

The prompt changes to PS, ready for commands. In a bypassed session, no logging events are generated.

## Related

- [[procedures/Bypass-PowerShell-Logging-with-Invisi-Shell]]
- [[tools/Invisi-Shell]]
