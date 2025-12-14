---
tags:
  - ssl-tls
  - recon
  - smtp
type: procedure
tools:
  - '[[tools/testssl-sh]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/testssl-scan-target]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:31:11.069Z'
sub_techniques: []
id: 2b4790da-ab6c-450e-9c80-77993ea65431
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Scan-SSL-TLS-Cipher-Support-with-Testssl

## Summary

This procedure uses testssl.sh to scan a target domain for SSL/TLS configurations, identifying supported protocols, ciphers, and vulnerabilities, particularly anonymous ciphers on SMTP services that enable MITM attacks.

## Description

In the context of testing apps.owncloud.com, this scan revealed support for anonymous DH and ECDH ciphers on ports 587 and 465, allowing unauthenticated connections. The tool tests protocols like TLS 1.0-1.2, cipher suites, and issues like BREACH vulnerability due to gzip compression. Prerequisites include network access to the target and a compatible OpenSSL binary.

## Requirements

1. Network connectivity to the target domain (e.g., apps.owncloud.com)
2. Installed testssl.sh and specified OpenSSL path
3. Basic Linux environment for execution

## Defense

Defensive measures and detection strategies:

- Disable anonymous ciphers in server config (e.g., Postfix smtpd_tls_exclude_ciphers)
- Monitor for anomalous SSL scans using tools like Fail2Ban or IDS signatures for testssl.sh patterns
- Enforce certificate pinning and trusted CAs to prevent MITM

## Objectives

1. Identify weak or anonymous cipher support in SSL/TLS
2. Detect misconfigurations on SMTP ports for potential interception
3. Gather evidence for vulnerability reporting

## Instructions

### Step 1: Prepare and Run Testssl Scan

**Context**: Set the OpenSSL path and execute the scan on the target to analyze HTTPS and implied SMTP configurations.

**Command** ([[commands/testssl-scan-target]]):
```bash
OPENSSL=/usr/local/Cellar/openssl/1.0.2d_1/bin/openssl bash testssl.sh apps.owncloud.com
```

> This command runs testssl.sh with a custom OpenSSL binary, scanning default port 443 but reporting on other services like SMTP. Expected output includes cipher lists (e.g., ADH-AES256-SHA supported), protocol versions, and vulnerabilities.

### Step 2: Review Scan Results

**Context**: Analyze the output for anonymous ciphers and port-specific issues.

**Command** (No execution; parse output):

> Look for sections on "Anonymous NULL encryption" or cipher grades; success if anonymous ciphers are offered on ports 587/465.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Identify Business Context

### Sub-Techniques

- None

## Commands Used

- [[commands/testssl-scan-target]]

## Tools Used

- [[tools/testssl-sh]]

## Tags

- [[ssl-tls]]
- [[recon]]
- [[smtp]]
