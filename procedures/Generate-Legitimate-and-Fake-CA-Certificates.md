---
tags:
  - openssl
  - certificates
  - ca-spoofing
type: procedure
tools:
  - '[[tools/openssl]]'
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/openssl-genrsa-legit-ca]]'
  - '[[commands/openssl-req-legit-ca]]'
  - '[[commands/openssl-genrsa-fake-ca]]'
  - '[[commands/openssl-req-fake-ca]]'
  - '[[commands/openssl-genrsa-server]]'
  - '[[commands/openssl-req-server-csr]]'
  - '[[commands/openssl-x509-sign-server]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[SAML Tokens]]'
updated_at: '2025-12-14T17:24:19.160Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: ea1ba29c-f6d0-4765-89d3-179e86ce8b15
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[SAML Tokens]]'
---
# Generate-Legitimate-and-Fake-CA-Certificates

## Summary

This procedure uses OpenSSL to generate private keys, self-signed CA certificates for legitimate and fake authorities, and a server certificate signed by the legitimate CA, setting up the trust anchors for the TOCTOU attack.

## Description

On a Linux system, create 2048-bit RSA keys and self-signed certificates valid for 365 days using SHA256. The server CSR is signed with the legit CA to mimic a trusted setup, while the fake CA enables post-validation spoofing. This is essential for demonstrating the race condition where the CA bundle changes after initial handshake.

## Requirements

1. OpenSSL installed
2. Write permissions for key and cert files
3. Basic knowledge of PKI concepts

## Defense

Defensive measures and detection strategies:

- Use hardware security modules (HSMs) for CA key protection
- Monitor for unauthorized certificate generation via file integrity monitoring
- Implement certificate pinning in applications to prevent CA swaps

## Objectives

1. Create trusted and spoofed CA certificates
2. Generate signed server certificate
3. Prepare files for symlink-based TOCTOU

## Instructions

### Step 1: Generate Legit CA Key

**Context**: Create private key for legitimate CA.

**Command** ([[commands/openssl-genrsa-legit-ca]]):
```bash
openssl genrsa -out legit_ca.key 2048
```

> Outputs 2048-bit RSA key to legit_ca.key.

### Step 2: Create Legit CA Cert

**Context**: Self-sign the legit CA certificate.

**Command** ([[commands/openssl-req-legit-ca]]):
```bash
openssl req -x509 -new -nodes -key legit_ca.key -sha256 -days 365 -out legit_ca.crt -subj "/CN=Legit CA"
```

> Creates self-signed cert with subject CN=Legit CA.

### Step 3: Generate Fake CA Key

**Context**: Create private key for fake CA.

**Command** ([[commands/openssl-genrsa-fake-ca]]):
```bash
openssl genrsa -out fake_ca.key 2048
```

> Outputs 2048-bit RSA key to fake_ca.key.

### Step 4: Create Fake CA Cert

**Context**: Self-sign the fake CA certificate.

**Command** ([[commands/openssl-req-fake-ca]]):
```bash
openssl req -x509 -new -nodes -key fake_ca.key -sha256 -days 365 -out fake_ca.crt -subj "/CN=Fake CA"
```

> Creates self-signed cert with subject CN=Fake CA.

### Step 5: Generate Server Key

**Context**: Create private key for server.

**Command** ([[commands/openssl-genrsa-server]]):
```bash
openssl genrsa -out server.key 2048
```

> Outputs 2048-bit RSA key to server.key.

### Step 6: Create Server CSR

**Context**: Generate signing request for server cert.

**Command** ([[commands/openssl-req-server-csr]]):
```bash
openssl req -new -key server.key -out server.csr -subj "/CN=localhost"
```

> Creates CSR with subject CN=localhost.

### Step 7: Sign Server Cert

**Context**: Sign CSR with legit CA.

**Command** ([[commands/openssl-x509-sign-server]]):
```bash
openssl x509 -req -in server.csr -CA legit_ca.crt -CAkey legit_ca.key -CAcreateserial -out server.crt -days 365 -sha256
```

> Signs and outputs server.crt valid for 365 days.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[SAML Tokens]] Certificate Authority Spoofing

### Sub-Techniques


## Commands Used

- [[commands/openssl-genrsa-legit-ca]]
- [[commands/openssl-req-legit-ca]]
- [[commands/openssl-genrsa-fake-ca]]
- [[commands/openssl-req-fake-ca]]
- [[commands/openssl-genrsa-server]]
- [[commands/openssl-req-server-csr]]
- [[commands/openssl-x509-sign-server]]

## Tools Used

- [[tools/openssl]]

## Tags

- openssl
- certificates
- ca-spoofing
