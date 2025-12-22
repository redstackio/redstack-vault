---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: compile-efs-potato-cs-dotnet-4x-default
type: command
executor: cmd
data: csc EfsPotato.cs
output: null
created_at: '2023-04-06T03:56:30.239739+00:00'
updated_at: '2023-04-10T20:37:54.225284+00:00'
platforms:
  - Windows
tags:
  - compilation
  - dotnet
  - privilege-escalation
verified: true
validated: true
---

# compile-efs-potato-cs-dotnet-4x-default

## Command

```cmd
csc EfsPotato.cs
```

## Description

Compiles the EfsPotato.cs source file using the default .NET 4.x compiler (csc.exe) to produce a 64-bit EfsPotato.exe binary. Use this on modern Windows systems with .NET 4.x installed for privilege escalation tool preparation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| EfsPotato.cs | Path to the C# source file | Yes |

## Examples

### Basic Usage

```cmd
csc EfsPotato.cs
```

### With Output Redirect

```cmd
csc EfsPotato.cs > compile.log 2>&1
```

## Expected Output

No output if successful; the EfsPotato.exe file is created in the current directory. Errors appear as CSxxxx messages if source issues or missing dependencies.

## Related

- [[commands/compile-efs-potato-cs-dotnet-4x-x86]]
- [[procedures/efs-potato-privilege-escalation]]
