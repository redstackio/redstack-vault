---
id: f8c86c33-b7b3-4399-960c-6affe066c0f8-part1
name: load-powerview-encoded-command
type: command
executor: powershell
data: powershell -EncodedCommand $encodedCommand
output: null
created_at: '2023-04-06T03:56:23.962672+00:00'
updated_at: '2023-04-10T20:37:00.767168+00:00'
platforms:
  - Windows
tags:
  - powershell
  - powerview
  - execution
verified: true
validated: true
---

# load-powerview-encoded-command

## Command

```powershell
powershell -EncodedCommand $encodedCommand
```

## Description

Launches a new PowerShell process to execute an encoded command string, commonly used to import modules like PowerView without direct file access restrictions. Useful for initial tool loading in restricted environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$encodedCommand` | Base64-encoded PowerShell payload (e.g., for importing a module) | Yes |
| `-EncodedCommand` | Specifies the encoded string to execute | Built-in |

## Examples

### Basic Usage

```powershell
powershell -EncodedCommand $encodedCommand
```

### Advanced Usage

Encode and load: First generate with `powershell -c "[Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes('Import-Module ./PowerView.ps1'))"`, then execute.

## Expected Output

PowerShell session starts and executes the decoded command silently if successful; no output if import succeeds, or error if decoding fails (e.g., 'Invalid base-64 string').

## Related

- [[procedures/Bypass-PowerShell-Execution-Policy-for-PowerView]]
- [[commands/load-powerview-bypass-policy]]
