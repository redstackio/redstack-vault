---
tags:
  - ssl-tls-misconfig
  - mitm
  - smtp
  - anonymous-ciphers
  - postfix
type: attack_chain
tools:
  - '[[tools/testssl-sh]]'
  - '[[tools/openssl-s-client]]'
  - '[[tools/nmap]]'
  - '[[tools/sslyze]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Scan-SSL-TLS-Cipher-Support-with-Testssl]]'
  - '[[procedures/Test-Anonymous-Cipher-Handshake-with-OpenSSL]]'
  - '[[procedures/Verify-SMTP-Port-Availability-with-Nmap]]'
  - '[[procedures/Analyze-SMTP-Cipher-Suites-with-Sslyze]]'
step_count: 4
techniques:
  - '[[Adversary-in-the-Middle]]'
  - '[[LLMNR-NBT-NS Poisoning and SMB Relay]]'
  - '[[Hardware]]'
updated_at: '2025-12-14T17:31:11.073Z'
description: >-
  Demonstrates discovery and exploitation of anonymous cipher support in SMTP
  services, allowing unauthenticated SSL/TLS handshakes that enable
  man-in-the-middle interception of email communications.
id: 99f4bea4-8e30-4a96-ad5f-e292b5483260
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
  - '[[LLMNR-NBT-NS Poisoning and SMB Relay]]'
  - '[[Hardware]]'
---
# SMTP SSL/TLS Misconfiguration Enabling Anonymous Ciphers for MITM Attacks

Multi-stage attack chain demonstrating the discovery and verification of anonymous cipher support in the SMTP service on apps.owncloud.com, which allows attackers to perform man-in-the-middle attacks by impersonating the server without authentication, potentially intercepting sensitive email communications.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Scan for Cipher Support] --> B[Test Anonymous Handshake]
    B --> C[Verify Port Availability]
    C --> D[Analyze Supported Ciphers]
    D --> E[MITM Interception Possible]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/testssl-sh]]
- [[tools/openssl-s-client]]
- [[tools/nmap]]
- [[tools/sslyze]]

### Target Environment

- Linux-based SMTP server (e.g., Postfix on Ubuntu)
- Open ports: 587 (SMTP submission with STARTTLS), 465 (SMTPS)
- Network access to the target domain (apps.owncloud.com) or IP (e.g., 188.138.69.67)

### Initial Access Requirements

- No credentials required due to anonymous cipher support
- Public network access to SMTP ports
- No prior access needed; remote scanning suffices

## Detailed Attack Procedures

### Step 1: Scan for SSL/TLS Cipher Support
procedure: [[procedures/Scan-SSL-TLS-Cipher-Support-with-Testssl]]

**Objective**: Identify supported SSL/TLS protocols, ciphers, and potential misconfigurations on the target, focusing on SMTP ports.

**Instructions**: Run the testssl.sh scan on the target domain to detect anonymous cipher support and other weaknesses.

Use [[commands/testssl-scan-target]]:

```bash
OPENSSL=/usr/local/Cellar/openssl/1.0.2d_1/bin/openssl bash testssl.sh apps.owncloud.com
```

**Expected Output**: Report showing supported protocols (e.g., TLS 1.0/1.1/1.2), ciphers (e.g., anonymous DH/ECDH), and vulnerabilities like support for weak ciphers on ports 587/465.

**Success Indicators**:
- Detection of anonymous ciphers (ADH, AECDH)
- Confirmation of SMTP port exposure

### Step 2: Test Anonymous Cipher Handshake
procedure: [[procedures/Test-Anonymous-Cipher-Handshake-with-OpenSSL]]

**Objective**: Verify if the SMTP server accepts unauthenticated SSL/TLS handshakes using anonymous ciphers, enabling impersonation.

**Instructions**: Attempt connections to SMTP ports using only anonymous ciphers to simulate MITM without authentication.

Execute [[commands/openssl-anonymous-connect-port465]]:

```bash
openssl s_client -connect apps.owncloud.com:465 -cipher aNULL
```

Then [[commands/openssl-anonymous-connect-port587]]:

```bash
openssl s_client -connect 50.30.33.235:587 -cipher aNULL
```

**Expected Output**: Successful handshake with no peer certificate verification, e.g., "New, TLSv1/SSLv3, Cipher is AECDH-AES256-SHA" and ESMTP banner.

**Success Indicators**:
- Handshake completes without authentication errors
- No certificate presented or trusted

### Step 3: Verify SMTP Port Availability
procedure: [[procedures/Verify-SMTP-Port-Availability-with-Nmap]]

**Objective**: Confirm that the SMTP submission port is open and responsive for further testing.

**Instructions**: Scan the target IP for the specific SMTP port to ensure service availability.

Run [[commands/nmap-scan-port587]]:

```bash
nmap 50.30.33.235 -p 587
```

**Expected Output**: Port state reported as "open" for submission service.

**Success Indicators**:
- Port 587/tcp open submission
- Service responsive to scans

### Step 4: Analyze SMTP Cipher Suites
procedure: [[procedures/Analyze-SMTP-Cipher-Suites-with-Sslyze]]

**Objective**: Perform a detailed analysis of supported cipher suites on the SMTP service using STARTTLS to confirm anonymous ciphers.

**Instructions**: Use sslyze to scan the SMTP port with STARTTLS enabled, listing all ciphers and vulnerabilities.

Execute [[commands/sslyze-analyze-smtp]]:

```bash
./sslyze.py --regular apps.owncloud.com:587 --starttls=smtp
```

**Expected Output**: List of ciphers including anonymous ones (e.g., AECDH-AES256-SHA, ADH-AES256-SHA), self-signed certificate details, and other issues like renegotiation support.

**Success Indicators**:
- Anonymous ciphers listed as supported
- Confirmation of untrusted self-signed cert (CN: loft11082.serverprofi24.de)

## Attack Chain Summary

### Key Achievements

1. Discovered anonymous DH/ECDH cipher support on SMTP ports 587/465
2. Verified successful unauthenticated handshakes via OpenSSL
3. Confirmed port openness and detailed cipher analysis
4. Enabled potential MITM for email interception, though limited by self-signed cert

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle
- [[LLMNR-NBT-NS Poisoning and SMB Relay]] Application Layer Protocol
- [[Hardware]] Gather Victim Host Information: Identify Business Context (via scanning)

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection

---

*Last updated: 2023-10-01T00:00:00Z*
