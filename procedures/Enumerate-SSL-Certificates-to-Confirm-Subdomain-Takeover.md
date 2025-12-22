---
id: proc-uuid-003
name: Enumerate-SSL-Certificates-to-Confirm-Subdomain-Takeover
tags:
  - ssl-enumeration
  - subdomain-takeover
  - certificate-mismatch
type: procedure
tools:
  - '[[tools/SSLEnum]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:31.186Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Enumerate-SSL-Certificates-to-Confirm-Subdomain-Takeover

## Summary

This procedure enumerates SSL/TLS certificates for a target subdomain to detect mismatches in subject names, confirming dangling status and takeover potential when the certificate aligns with an unrelated domain.

## Description

Dangling subdomains often retain certificates from previously associated services. By pulling certificate details, attackers can verify if the subdomain resolves to an unrelated certificate (e.g., CN *.test.tugo.com for liveplan.com), indicating the original resource is gone and the subdomain is claimable. This step uses specialized tools to analyze certificate chains, alternative names, and validity, providing evidence for exploitation.

## Requirements

1. HTTPS-accessible subdomain (e.g., https://max1.liveplan.com)
2. SSLEnum tool installed and configured
3. Timestamp awareness for certificate retrieval (e.g., 7/8/2021)

## Defense

Defensive measures and detection strategies:

- Revoke certificates on resource decommissioning
- Monitor certificate transparency logs for mismatches
- Use wildcard certificates cautiously and audit regularly

## Objectives

1. Retrieve certificate details including CN and SANs
2. Identify dangling indicators like unrelated domain matches
3. Validate takeover feasibility for privilege escalation

## Instructions

### Step 1: Run SSLEnum on Target

**Context**: Fetch and parse the SSL certificate to extract key fields.

**Command** (using [[tools/SSLEnum]]):
```bash
go run main.go -d max1.liveplan.com
```

> Output includes CN *.test.tugo.com, SANs *.dev.tugo.com and *.uat.tugo.com, with dangling: true on 7/8/2021 at 1:40PM, confirming mismatch.

### Step 2: Analyze for Takeover

**Context**: Manually review output for unrelated issuers or names.

No command; parse results to check if certificate subjects do not include the target subdomain.

> Success if alternative names point to external domains like tugo.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/SSLEnum]]

## Tags

- [[ssl-enumeration]]
- [[subdomain-takeover]]
