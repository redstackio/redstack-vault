---
id: proc-uuid-002
name: Prepare-Client-Certificate-and-Key
tags:
  - certificate
  - private-key
  - preparation
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands: []
verified: false
platforms:
  - Linux
  - Windows
  - macOS
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Private Keys]]'
updated_at: '2025-12-14T17:30:58.732Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Private Keys]]'
---
# Prepare-Client-Certificate-and-Key

## Summary

This procedure involves obtaining or generating a client certificate and private key valid for authenticating to the target site, which will be used in the curl command to demonstrate reuse.

## Description

Client certificates are used for mTLS authentication. In the attack, the victim's cert/key are provided to curl, allowing reuse on redirects. Generate self-signed or use real ones from the target CA. This step assumes access to cert tools like OpenSSL.

## Requirements

1. OpenSSL or similar for cert generation
2. Access to target's CA if not self-signed
3. Secure storage for private key

## Defense

Defensive measures and detection strategies:

- Rotate certificates regularly
- Use hardware security modules (HSM) for key storage
- Audit cert usage logs for unexpected domains

## Objectives

1. Create valid client.crt and client.key
2. Ensure compatibility with target server's CA
3. Prepare files for curl usage

## Instructions

### Step 1: Generate Private Key

**Context**: Create the private key for the certificate.

```bash
openssl genrsa -out client.key 2048
```

> Generates a 2048-bit RSA key. Expected output: client.key file created.

### Step 2: Generate Certificate Signing Request (CSR)

**Context**: Create CSR for signing.

```bash
openssl req -new -key client.key -out client.csr -subj "/CN=victim-client"
```

> Submits details for the cert. Expected output: client.csr file.

### Step 3: Sign the Certificate

**Context**: Use CA to sign the CSR.

```bash
openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt -days 365
```

> Signs with CA. Expected output: client.crt valid for 1 year.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Private Keys]] Private Keys

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- certificate
- private-key
- preparation
