---
id: a00dfda4-f08a-4543-b0ca-164f841730f8
name: launch-interactive-ftp-session
type: command
executor: bash
data: ftp $_TARGET_IP
output: |-
  root@kali:~# ftp 10.10.10.10
  Connected to 10.10.10.10.
  220 Microsoft FTP Service
  Name (10.10.10.10:root): anonymous
  331 Anonymous access allowed, send identity (e-mail name) as password.
  Password:
  230 User logged in.
  Remote system type is Windows_NT.
  ftp>
created_at: '2019-09-11T22:47:55.931243+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - Windows
tags:
  - file-transfer
  - network
verified: true
validated: true
---

# Launch-Interactive-FTP-Session

## Command

```bash
ftp $_TARGET_IP
```

## Description

This command initiates an interactive FTP client session to connect to a remote FTP server at the specified IP address or hostname. It is used to establish a session for file browsing, uploading, and downloading in network-based operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | The IP address or hostname of the FTP server (e.g., 10.10.10.10 or ftp.example.com) | Yes |

## Examples

### Basic Usage

```bash
ftp 10.10.10.10
```

Connects to the FTP server at 10.10.10.10 and prompts for username/password.

### Advanced Usage

```bash
ftp ftp.example.com
```

Connects using a hostname instead of IP; supports IPv4/IPv6.

## Expected Output

```
root@kali:~# ftp 10.10.10.10
Connected to 10.10.10.10.
220 Microsoft FTP Service
Name (10.10.10.10:root): anonymous
331 Anonymous access allowed, send identity (e-mail name) as password.
Password:
230 User logged in.
Remote system type is Windows_NT.
ftp>
```

The output shows connection success, server greeting, login prompts, and the interactive 'ftp>' prompt upon successful authentication.

## Related

- [[procedures/Browse-FTP-Site-with-Interactive-Session]]
