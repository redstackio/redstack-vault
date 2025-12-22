---
id: 0bb61fff-7ae2-4e5e-b298-584a23d8ed39
name: new-smbshare-create-share
type: command
executor: powershell
data: New-SmbShare -Name "$_NAME" -Path "$_PATH" -FullAccess "$_USERNAME"
output: >-
  PS C:\ > New-SmbShare -Name "Shared Files" -Path "C:\Users\Bob\Desktop\shared"
  -FullAccess Bob"


  Name         ScopeName Path                         Description

  ----         --------- ----                         -----------

  Shared Files *         C:\Users\Bob\Desktop\test
created_at: '2020-03-27T22:21:14.917913+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - smb
  - powershell
  - exfiltration
verified: true
validated: true
---

# new-smbshare-create-share

## Command

```powershell
New-SmbShare -Name "$_NAME" -Path "$_PATH" -FullAccess "$_USERNAME"
```

## Description

This PowerShell command creates a new SMB file share on a Windows system, specifying the share name, the local path to the folder being shared, and granting full access (read/write/delete) to a designated user account. It is useful in post-exploitation for enabling remote file access over the network.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_NAME | The name of the SMB share as seen by remote clients (e.g., "ExfilShare") | Yes |
| $_PATH | The full local filesystem path to the directory or file to share (e.g., "C:\Temp\Data") | Yes |
| $_USERNAME | The username (local or domain) to grant full access permissions to (e.g., "DOMAIN\\attacker") | Yes |
| -FullAccess | Built-in parameter that sets full control permissions for the specified user | Built-in |

## Examples

### Basic Usage

```powershell
New-SmbShare -Name "TempShare" -Path "C:\Temp" -FullAccess "Bob"
```

This creates a share named "TempShare" pointing to C:\Temp with full access for user "Bob".

### Advanced Usage

```powershell
New-SmbShare -Name "ExfilShare" -Path "C:\Users\Victim\Documents" -FullAccess "DOMAIN\\attacker" -Description "Temporary share for data transfer"
```

Includes a description for the share and uses a domain user.

## Expected Output

When successful, the command outputs a table summarizing the created share:

```
Name         ScopeName Path                                  Description
----         --------- ----                                  -----------
Shared Files *         C:\Users\Bob\Desktop\shared        
```

If the share name is already in use, it will error: "The request is not supported (Exception from HRESULT: 0x80070032)". Use Remove-SmbShare first to delete existing shares.

## Related

- [[procedures/Create-Windows-SMB-Share-with-PowerShell]] (procedure that uses this command)
- [[Get-SmbShare]] (related command to list shares)
