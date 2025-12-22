---
id: bd432f06-a85b-4567-b574-0119448a30a4
name: WinRS-Open-CMD-on-Remote-Windows-Machine-With-Credentials
type: command
executor: powershell
data: 'winrs -r:$_COMPUTER_NAME -u:$_DOMAIN\\$_USERNAME -p:$_PASSWORD cmd'
output: null
created_at: '2023-01-12T19:33:20.916458+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - WinRS
  - remote-execution
  - credentials
verified: true
validated: true
---

# WinRS-Open-CMD-on-Remote-Windows-Machine-With-Credentials

## Command

```powershell
winrs -r:$_COMPUTER_NAME -u:$_DOMAIN\$_USERNAME -p:$_PASSWORD cmd
```

## Description

This command opens a remote CMD session using WinRS with explicit username and password credentials, suitable for non-domain or restricted access scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -r:$_COMPUTER_NAME | Target computer name or IP | Yes |
| -u:$_DOMAIN\$_USERNAME | Domain or local username (e.g., .\user for local) | Yes |
| -p:$_PASSWORD | Password for the user | Yes |
| cmd | Specifies the remote command shell | Yes |

## Examples

### Basic Usage

```powershell
winrs -r:TARGET-PC -u:.\Administrator -p:Pass123 cmd
```
(For local admin access.)

### Advanced Usage

```powershell
winrs -r:TARGET-PC -u:DOMAIN\user -p:Pass123 -remote:HTTPS cmd
```
(With domain creds and HTTPS.)

## Expected Output

Connects to remote CMD on success:

```
The request will be sent over HTTP.
Successful connection established.

Microsoft Windows [Version 10.0.19041.1]
(c) Microsoft Corporation. All rights reserved.

C:\Windows\system32> 
```
Failure shows "The user name or password is incorrect."

## Related

- [[commands/WinRS-Open-CMD-on-Remote-Windows-Machine]]
- [[procedures/Remote-Access-to-Windows-Machine-Using-Credentials]]
