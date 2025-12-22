---
tags:
  - mitm
  - anonymous-ciphers
  - smtp
type: procedure
tools:
  - '[[tools/openssl-s-client]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/openssl-anonymous-connect-port465]]'
  - '[[commands/openssl-anonymous-connect-port587]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[LLMNR-NBT-NS Poisoning and SMB Relay]]'
updated_at: '2025-12-14T17:31:11.063Z'
sub_techniques: []
id: dd8f2105-6159-4ca2-aaeb-9961e065f15c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[LLMNR-NBT-NS Poisoning and SMB Relay]]'
---
# Test-Anonymous-Cipher-Handshake-with-OpenSSL

## Summary

This procedure tests SMTP servers for acceptance of anonymous ciphers by attempting SSL/TLS handshakes without authentication, confirming vulnerability to MITM impersonation on ports like 465 and 587.

## Description

Targeted at apps.owncloud.com, successful handshakes with aNULL ciphers showed no authentication required, using self-signed certs that weaken trust. This exploits Postfix misconfigurations allowing ADH/AECDH, enabling email interception. Requires OpenSSL installed and network access.

## Requirements

1. OpenSSL binary available
2. Target IP/domain and ports accessible (e.g., 188.138.69.67:587)
3. No credentials; tests public exposure

## Defense

Defensive measures and detection strategies:

- Configure server to exclude anonymous ciphers (e.g., tls_exclude_ciphers = aNULL)
- Log and alert on failed or anomalous handshakes
- Use HSTS or certificate transparency for email services

## Objectives

1. Verify unauthenticated handshake success
2. Simulate MITM by establishing anonymous connection
3. Document cipher used for proof-of-concept

## Instructions

### Step 1: Test Port 465 (SMTPS)

**Context**: Connect to implicit TLS port using anonymous ciphers to check handshake.

**Command** ([[commands/openssl-anonymous-connect-port465]]):
```bash
openssl s_client -connect apps.owncloud.com:465 -cipher aNULL
```

> Establishes connection; success if "CONNECTED" and cipher like AECDH-AES256-SHA without cert errors, showing ESMTP banner.

### Step 2: Test Port 587 (STARTTLS)

**Context**: Attempt connection on submission port with anonymous restriction.

**Command** ([[commands/openssl-anonymous-connect-port587]]):
```bash
openssl s_client -connect 50.30.33.235:587 -cipher aNULL
```

> Similar to Step 1; expect handshake success or failure based on config.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[LLMNR-NBT-NS Poisoning and SMB Relay]] Adversary-in-the-Middle: Application Layer Protocol

### Sub-Techniques

- None

## Commands Used

- [[commands/openssl-anonymous-connect-port465]]
- [[commands/openssl-anonymous-connect-port587]]

## Tools Used

- [[tools/openssl-s-client]]

## Tags

- [[mitm]]
- [[anonymous-ciphers]]
- [[smtp]]
