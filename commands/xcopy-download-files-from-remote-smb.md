---
id: c562c864-1009-4a0a-8e6a-70525df7d968
name: xcopy-download-files-from-remote-smb
type: command
executor: cmd
data: xcopy \\$_REMOTE_IP\\$_SHARE\\$_FILENAME .
output: |
  C:\>xcopy \\10.10.10.100\files\secrets .
  \\10.10.10.100\files\secrets
  1 File(s) copied
created_at: '2019-11-25T23:00:09.678942+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - file-transfer
  - smb
verified: true
validated: true
---

# xcopy-download-files-from-remote-smb

## Command

```cmd
xcopy \\$_REMOTE_IP\\$_SHARE\\$_FILENAME .
```

## Description

This command uses xcopy to download a specific file from a remote SMB share to the current local directory. It is useful for transferring files during lateral movement or data exfiltration over SMB shares without requiring additional tools.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_REMOTE_IP | IP address of the remote host hosting the SMB share | Yes |
| $_SHARE | Name of the SMB share on the remote host | Yes |
| $_FILENAME | Name of the file to download from the share | Yes |
| . | Destination directory (current directory) | Yes |

## Examples

### Basic Usage

Download a file named 'secrets.txt' from the 'files' share on a remote host:

```cmd
xcopy \\192.168.1.100\\files\\secrets.txt .
```

### Advanced Usage

Download an entire directory from the remote share, including subdirectories (/s flag) and overwriting existing files (/y flag):

```cmd
xcopy \\$_REMOTE_IP\\$_SHARE\\*.* . /s /y
```

## Expected Output

When successful, xcopy will display the source path and confirm the number of files copied:

```
C:\>xcopy \\10.10.10.100\files\secrets .
\\10.10.10.100\files\secrets
1 File(s) copied
```

If the share is inaccessible, an error like "Invalid path" or access denied will appear.

## Related

- [[tools/xcopy]]
- [[procedures/smb-file-transfer-via-xcopy]]
