---
id: f5c950bc-bd83-4b3a-b300-65b73b8d7b0e
name: wmic-remote-process-create
type: command
executor: cmd
data: >-
  wmic /node:$_TARGET_HOST /user:$_DOMAIN\\$_USERNAME /password:$_PASSWORD
  process call create "$_PROCESS_PATH"
output: null
created_at: '2023-04-06T03:56:31.252966+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - wmi
  - remote-execution
verified: true
validated: true
---

# wmic-remote-process-create

## Command

```cmd
wmic /node:$_TARGET_HOST /user:$_DOMAIN\\$_USERNAME /password:$_PASSWORD process call create "$_PROCESS_PATH"
```

## Description

This command uses WMIC to remotely create and start a process on a Windows target via the WMI protocol. It is ideal for initial remote execution testing or delivering payloads in lateral movement scenarios. Specify the target host, credentials, and the full path to the executable to run.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_HOST | IP address, hostname, or domain name of the remote machine (e.g., 192.168.1.100 or target.domain.com) | Yes |
| $_DOMAIN | Domain name for the credentials (e.g., DOMAIN) | Yes |
| $_USERNAME | Username for authentication (e.g., administrator) | Yes |
| $_PASSWORD | Password for the user account | Yes |
| $_PROCESS_PATH | Full path to the executable on the target (e.g., "C:\\Windows\\System32\\calc.exe") | Yes |
| /node | Specifies the remote target | Built-in |
| /user | Specifies the username for authentication | Built-in |
| /password | Specifies the password (use securely; consider /securepassword for obfuscation) | Built-in |
| process call create | WMI method to create a new process | Built-in |

## Examples

### Basic Usage

Launch Calculator on a remote host:

```cmd
wmic /node:192.168.1.100 /user:DOMAIN\admin /password:Pass123 process call create "C:\Windows\System32\calc.exe"
```

### Advanced Usage

Execute a command shell and redirect output to a file:

```cmd
wmic /node:target.domain.com /user:DOMAIN\user /password:password process call create "cmd.exe /c whoami > C:\temp\output.txt"
```

### Query Variation for Verification

List processes to test connectivity:

```cmd
wmic /node:$_TARGET_HOST /user:$_DOMAIN\$_USERNAME /password:$_PASSWORD process list brief
```

## Expected Output

Successful execution returns output similar to:

```
Execute (\\target.domain.com\root\cimv2:Win32_Process.Handle="1234")? 
Method execution successful.
Out Parameters:
	instance of __PARAMETERS
{
	ReturnValue = 0;
	ProcessId = 1234;
};
```

A ReturnValue of 0 indicates success, with ProcessId showing the spawned process ID. Errors (e.g., ReturnValue 2 or 9) indicate access denied or invalid node.

## Related

- [[procedures/WMI-Remote-Process-Creation-via-WMIC]] (procedure that uses this command)
- [[techniques/Windows Management Instrumentation|T1047]] (MITRE technique)
