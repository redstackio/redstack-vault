---
tags:
  - certificate
  - https
  - openssl
type: procedure
tools:
  - '[[tools/OpenSSL]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/openssl-generate-cert]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:26:22.108Z'
sub_techniques: []
id: e8481640-385b-492f-a5f8-f65071f504dc
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Generate-Self-Signed-Certificate-for-HTTPS-Server

## Summary

This procedure generates a self-signed RSA 4096-bit certificate and private key pair using OpenSSL for use in an HTTPS server during curl vulnerability reproduction, valid for 1 day without passphrase.

## Description

For the CVE-2025-9086 reproduction, a self-signed cert is needed for the HTTPS server on port 9443 to set secure cookies. The command uses x509 for self-signing, SHA256 hashing, and a generic subject DN. This avoids real CA involvement and focuses on local testing. Expected outcome: cert.pem and key.pem files ready for Python HTTPS server.

## Requirements

1. OpenSSL installed
2. Write permissions in current directory
3. Basic knowledge of cert generation

## Defense

Defensive measures and detection strategies:

- Use proper CA-signed certs in production
- Monitor for self-signed cert usage in traffic
- Implement HSTS to prevent MITM

## Objectives

1. Create valid cert/key for local HTTPS
2. Enable secure cookie setting in test
3. Ensure compatibility with curl --insecure

## Instructions

### Step 1: Generate Certificate and Key

**Context**: Run OpenSSL to create self-signed cert and key.

**Command** ([[commands/openssl-generate-cert]]):
```bash
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 1 -nodes -subj "/C=XX/ST=StateName/L=CityName/O=CompanyName/OU=CompanySectionName/CN=CommonNameOrHostname"
```

> Generates files; output shows writing to files, no passphrase prompt due to -nodes.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used

- [[commands/openssl-generate-cert]]

## Tools Used

- [[tools/OpenSSL]]

## Tags

- certificate
- https
- openssl
