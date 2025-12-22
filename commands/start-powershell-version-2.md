---
type: command
executor: powershell
data: powershell -version 2
platforms:
  - Windows
tags:
  - bypass
  - powershell
verified: true
validated: true
---

# start-powershell-version-2

## Command

```powershell
powershell -version 2
```

## Description

This command launches a new instance of PowerShell specifically using version 2, which can help evade security features in newer PowerShell versions such as logging and execution restrictions. Use it when operating in environments with PowerShell v2 still enabled to reduce detection risk during script execution or command invocation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-version 2` | Specifies PowerShell version 2 for the new session; limits features to those available in v2 | Yes |

## Examples

### Basic Usage

```powershell
powershell -version 2
```

This starts an interactive v2 shell. From there, you can execute commands or load scripts.

### Advanced Usage

```powershell
powershell -version 2 -Command "Get-Process"
```

Runs a single command in v2 mode without entering an interactive session. Replace the command as needed.

## Expected Output

Upon successful execution, you receive a PowerShell v2 prompt similar to:

```
Windows PowerShell
Copyright (C) 2009 Microsoft Corporation. All rights reserved.

PS C:\Users\User> $host.Version

Major  Minor  Build  Revision
-----  -----  -----  --------
2      0      -1     -1

PS C:\Users\User>
```

The version confirmation shows Major: 2, indicating the downgrade succeeded. If v2 is not installed, an error like "The term 'powershell' is not recognized" or version-specific failure appears.

## Related

- [[procedures/Downgrade-PowerShell-to-Version-2]]
