---
type: command
executor: powershell
data: >-
  New-PSDrive -Name "$_NAME" -PSProvider FileSystem -Credential $Cred -Root
  \\$_TARGET_IP\$_SHARE
tags:
  - file-transfer
  - network
platforms:
  - Windows
verified: true
validated: true
---

# new-psdrive-mount-smb-share

## Command

```powershell
New-PSDrive -Name "$_NAME" -PSProvider FileSystem -Credential $Cred -Root \\$_TARGET_IP\$_SHARE
```

## Description

This command mounts a remote SMB share as a local PowerShell drive (PSDrive) using provided credentials, allowing authenticated access to files on the target Windows server. It requires a pre-defined $Cred PSCredential object and is commonly used for lateral movement or exfiltration in Windows environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_NAME | The drive letter or alias for the mounted share (e.g., "Z" or "RemoteShare") | Yes |
| -PSProvider | Specifies the FileSystem provider for file operations | Yes (built-in) |
| -Credential | The PSCredential object ($Cred) containing username and password | Yes |
| -Root | The UNC path to the SMB share (e.g., \\IP\sharename) | Yes |
| $_TARGET_IP | IP address or hostname of the target server within the -Root path | Yes (part of path) |
| $_SHARE | Name of the target share within the -Root path | Yes (part of path) |

## Examples

### Basic Usage

```powershell
New-PSDrive -Name "Z" -PSProvider FileSystem -Credential $Cred -Root "\\192.168.1.100\Documents"
```

### Advanced Usage

```powershell
New-PSDrive -Name "RemoteFiles" -PSProvider FileSystem -Credential $Cred -Root "\\server.domain.com\Public$" -Persist
```

(The -Persist flag makes the drive persistent across sessions, if elevated privileges allow.)

## Expected Output

A summary table of the new PSDrive upon successful mount:

```
Name           Used (GB)     Free (GB) Provider      Root                                               CurrentLocation
----           ---------     --------- --------      ----                                               ---------------
Z              0.00          0.00      FileSystem    \\192.168.1.100\Documents
```

If unsuccessful, an error like "Access is denied" or "The network path was not found" appears.

## Related

- [[procedures/Mount-Windows-SMB-Share-with-PowerShell-Authenticated]]
- [[codes/PowerShell-Create-PSCredential]]
