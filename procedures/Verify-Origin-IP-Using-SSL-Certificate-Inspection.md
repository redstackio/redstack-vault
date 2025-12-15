---
id: proc-003
tags:
  - ssl-inspection
  - certificate-verification
  - origin-ip
type: procedure
tools:
  - '[[tools/openssl]]'
  - '[[tools/perl]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/openssl-inspect-ssl-certificate-for-dns-names]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Software]]'
updated_at: '2025-12-14T17:29:57.323Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
---
# Verify-Origin-IP-Using-SSL-Certificate-Inspection

## Summary

This procedure verifies if a suspected origin IP belongs to the target domain by connecting via TLS and extracting DNS names from the SSL certificate using openssl and perl.

## Description

To confirm backend server ownership, attackers inspect the TLS certificate presented by the IP. In this case, connecting to the DoD application's origin IP retrieves a certificate whose Subject Alternative Names (SAN) include the target domain, validating it as the internal server. This bypasses Akamai's edge. Prerequisites: openssl and perl installed, known candidate IP from DNS recon.

## Requirements

1. openssl and perl installed
2. Suspected origin IP (e.g., ██████)
3. Port 443 access

## Defense

Defensive measures and detection strategies:

- Use certificate pinning to prevent inspection bypasses
- Monitor for anomalous TLS connections to internal IPs
- Implement HSTS and strict transport security

## Objectives

1. Extract certificate DNS names
2. Confirm IP-domain association
3. Validate bypass candidate

## Instructions

### Step 1: Connect and Parse Certificate

**Context**: This step establishes a TLS connection to the IP, fetches the certificate, and parses SAN fields for domain matches.

**Command** ([[commands/openssl-inspect-ssl-certificate-for-dns-names]]):
```bash
true | openssl s_client -connect ██████:443 2>/dev/null | openssl x509 -noout -text | perl -l -0777 -ne '@names=/\bDNS:([^\s,]+)/g; print join("\n", sort @names);'
```

> The openssl s_client connects to port 443, pipes to x509 for text output, and perl regex extracts DNS: entries from SAN. Suppress errors with 2>/dev/null; true ensures pipe flow.

**Expected Output**: Sorted list of DNS names, e.g., █████████, confirming the target domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Software]] Software

### Sub-Techniques

- None

## Commands Used

- [[commands/openssl-inspect-ssl-certificate-for-dns-names]]

## Tools Used

- [[tools/openssl]]
- [[tools/perl]]

## Tags

- [[ssl-inspection]]
- [[certificate-verification]]
- [[origin-ip]]
